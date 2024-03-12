# BoxCutter

> You've received a supply of valuable food and medicine from a generous sponsor. There's just one problem - the box is made of solid steel! Luckily, there's a dumb automated defense robot which you may be able to trick into opening the box for you - it's programmed to only attack things with the correct label.
> 
> Files: [cutter](rev_boxcutter/rev_boxcutter/cutter)

**Writeup by:** Stig Rune Grønnestad

- [BoxCutter](#boxcutter)
	- [Recon](#recon)
	- [Solver](#solver)
	- [Flag](#flag)

## Recon

```bash
┌──(stig㉿STIG-DESKTOP)-[/mnt/c/dev/ctf-htb-cyber-apocalypse-2024/reversing/box_cutter/rev_boxcutter/rev_boxcutter]
└─$ file cutter
cutter: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=f76eb244685ad0c3b817caa99093531754fc84c8, for GNU/Linux 3.2.0, not stripped
```

We have a 64-bit ELF binary. Let's run it and see what it does.

```bash
└─$ ./cutter
[X] Error: Box Not Found
```

main function:
```c
undefined8 main(void)
{
  undefined8 local_28;
  undefined7 local_20;
  undefined uStack_19;
  undefined7 uStack_18;
  int local_10;
  uint local_c;
  
  local_28 = 0x540345434c75637f;
  local_20 = 0x45f4368505906;
  uStack_19 = 0x68;
  uStack_18 = 0x374a025b5b0354;

  for (local_c = 0; local_c < 0x17; local_c = local_c + 1) {
    *(byte *)((long)&local_28 + (long)(int)local_c) =
         *(byte *)((long)&local_28 + (long)(int)local_c) ^ 0x37;
  }

  local_10 = open((char *)&local_28,0);

  if (local_10 < 1) {
    puts("[X] Error: Box Not Found");
  }
  else {
    puts("[*] Box Opened Successfully");
    close(local_10);
  }

  return 0;
}
```

Basically we need to find the correct label for the box. If the file is opened successfully, the box is opened.

## Solver
The instructive part of this lesson is to treat the locals defined in main as a continuous array of bytes (like they are laid out on the stack), and xor each byte with 0x37. This will give us the correct label for the box.

[Solver](solver.py)

```bash
└─$ python3 solver.py
[+] Modified filename: HTB{tr4c1ng_th3_c4ll5}
```

## Flag
HTB{tr4c1ng_th3_c4ll5}