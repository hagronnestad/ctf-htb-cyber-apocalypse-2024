# Writing on the Wall

> As you approach a password-protected door, a sense of uncertainty envelops you—no clues, no hints. Yet, just as confusion takes hold, your gaze locks onto cryptic markings adorning the nearby wall. Could this be the elusive password, waiting to unveil the door's secrets?
> 
> Files:
> - [flag.txt](pwn_writing_on_the_wall/challenge/flag.txt) | [writing_on_the_wall](pwn_writing_on_the_wall/challenge/writing_on_the_wall)

**Writeup by:** Stig Rune Grønnestad

- [Writing on the Wall](#writing-on-the-wall)
	- [Recon](#recon)
		- [file](#file)
		- [strings](#strings)
		- [Running](#running)
	- [main()](#main)

## Recon

### file
```bash
└─$ file writing_on_the_wall
writing_on_the_wall: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter ./glibc/ld-linux-x86-64.so.2, BuildID[sha1]=e1865b228b26ed7b4714423d70d822f6f188e63c, for GNU/Linux 3.2.0, not stripped
```

### strings
[strings.txt](strings.txt)

### Running
```bash
└─$ ./writing_on_the_wall

〰③ ╤ ℙ Å ⅀ ₷

The writing on the wall seems unreadable, can you figure it out?

>> yes

[-] You activated the alarm! Troops are coming your way, RUN!
```

## main()

Using ghidra to decompile.

```c
undefined8 main(void)
{
  int iVar1;
  long in_FS_OFFSET;
  char local_1e [6];
  undefined8 local_18;
  long local_10;
  
  local_10 = *(long *)(in_FS_OFFSET + 0x28);
  local_18 = 0x2073736170743377;
  read(0,local_1e,7);
  iVar1 = strcmp(local_1e,(char *)&local_18);
  if (iVar1 == 0) {
    open_door();
  }
  else {
    error("You activated the alarm! Troops are coming your way, RUN!\n");
  }
  if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
    __stack_chk_fail();
  }
  return 0;
}
```

The program reads 7 bytes from stdin and compares it to `0x2073736170743377` which is `w3tsp  `. If the input is correct, `open_door()` is called.

```c