# Delulu

> HALT! Recognition protocol initiated. Please present your face for scanning.
> 
> Files:
> - [delulu](challenge/delulu)
> - [flag.txt](challenge/flag.txt)
> - glibc

**Writeup by:** Stig Rune Grønnestad

- [Delulu](#delulu)
  - [Recon](#recon)
  - [Ghidra](#ghidra)

## Recon

We are given a binary and a flag file. Let's start by checking the file data and running the binary:

```bash
└─$ checksec delulu
[*] Checking for new versions of pwntools
    To disable this functionality, set the contents of /home/stig/.cache/.pwntools-cache-3.11/update to 'never' (old way).
    Or add the following lines to ~/.pwn.conf or ~/.config/pwn.conf (or /etc/pwn.conf system-wide):
        [update]
        interval=never
[*] A newer version of pwntools is available on pypi (4.11.1 --> 4.12.0).
    Update with: $ pip install -U pwntools
[*] '/mnt/c/dev/ctf-htb-cyber-apocalypse-2024/pwn/delulu/challenge/delulu'
    Arch:     amd64-64-little
    RELRO:    Full RELRO
    Stack:    Canary found
    NX:       NX enabled
    PIE:      PIE enabled
    RUNPATH:  b'./glibc/'
```

```bash
└─$ file delulu
delulu: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./glibc/ld-linux-x86-64.so.2, BuildID[sha1]=edae8c8bd5153e13fa60aa00f53071bb7b9a122f, for GNU/Linux 3.2.0, not stripped

└─$ ./delulu
      🟨🟨🟨
      🟨🟨🟨
      🟨🟨🟨
   🟨🟨🟨🟨🟨🟨
   🟨🟨🟨🟨🟨🟨
   🟨🟨🟨🟨🟨🟨
  🟨🟨🟨🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨🟨
🟨⬛️⬛️⬛️🟨⬛️⬛️⬛️🟨
🟨⬛️⬜️⬜️🟨⬛️⬜️⬜️🟨
🟨⬛️⬜️⬜️🟨⬛️⬜️⬜️🟨
🟨🟨🟨🟨🟨🟨🟨🟨🟨
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️⬛️
🟨🟨🟨⬛️⬛️⬛️🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨🟨
🟪🟪🟪🟪🟪🟪🟪🟪🟪
    🟪🟪🟪🟪🟪
🟨🟪🟪🟨🟨🟨🟪🟪🟨
🟨🟪🟪🟨🟨🟨🟪🟪🟨
🟨🟨🟪🟨🟨🟨🟪🟨🟨
🟨🟨🟪🟨🟨🟨🟪🟨🟨
🟨🟨🟪🟨🟨🟨🟪🟨🟨
🟨🟨🟪🟪🟨🟨🟪🟪🟨
🟨🟨🟨🟨🟨🟨🟨🟨🟨
  🟪🟪🟪🟪🟪🟪
    🟪🟪🟪🟪🟪🟪
  🟨🟨🟨🟨🟨🟨🟨🟨
  🟨🟨🟨🟨🟨🟨🟨🟨
  🟨🟨🟨🟨🟨🟨🟨🟨
  🟨🟨🟨🟨🟨🟨🟨🟨
  🟨🟨🟨🟨🟨🟨🟨🟨
      🟨🟨🟨🟨
🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨

The D-LuLu face identification robot will scan you shortly!

Try to deceive it by changing your ID.

>>
```

## Ghidra

Opening the binary in Ghidra, we can see that the binary is a program that reads input from the user.

`main`:
```c
undefined8 main(void)
{
	long in_FS_OFFSET;
	long local_48;
	long *local_40;
	undefined8 local_38;
	undefined8 local_30;
	undefined8 local_28;
	undefined8 local_20;
	long local_10;

	local_10 = *(long *)(in_FS_OFFSET + 0x28);
	local_48 = 0x1337babe;
	local_40 = &local_48;
	local_38 = 0;
	local_30 = 0;
	local_28 = 0;
	local_20 = 0;
	read(0,&local_38,0x1f);
	printf("\n[!] Checking.. ");
	printf((char *)&local_38);
	if (local_48 == 0x1337beef) {
		delulu();
	}
	else {
		error("ALERT ALERT ALERT ALERT\n");
	}
	if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
					/* WARNING: Subroutine does not return */
		__stack_chk_fail();
	}
	return 0;
}
```

This indicates that `0x1f` bytes are read from `0` (stdin) into the buffer `local_38`:
```c
read(0, &local_38, 0x1f)
```

Checking `local_48` for the value `0x1337beef`:
```c
	if (local_48 == 0x1337beef) {
		delulu();
	}
```

`0x1337BEEF` is `322420463` in decimal.

`delulu()` seems to be the next step. Let's see if it's possible to use buffer overflow on the stack.

`main`s stack:
```c
               *********************************
               *           FUNCTION            *
               *********************************
               undefined main()
       undefin   AL:1    <RETURN>
       undefin   Stack[  local_10              XREF[2 0010145f(
                                                     001014fc(
       undefin   Stack[  local_20              XREF[1 0010148d(
       undefin   Stack[  local_28              XREF[1 00101485(
       undefin   Stack[  local_30              XREF[1 0010147d(
       undefin   Stack[  local_38              XREF[3 00101475(
                                                     00101495(
                                                     001014bf(
       undefin   Stack[  local_40              XREF[1 00101471(
       undefin   Stack[  local_48              XREF[3 00101465(
                                                     0010146d(
                                                     001014d0(
               main                      XREF[4 Entry Point(*), 
                                                _start:00101198(*
                                                00102654, 
                                                00102778(*)  
```
