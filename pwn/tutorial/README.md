# Tutorial

> Before we start, practice time!
> 
> Files:
> - [pwn_tutorial.zip](pwn_tutorial.zip)

**Writeup by:** Stig Rune Grønnestad

- [Tutorial](#tutorial)
	- [Recon](#recon)
		- [test.c](#testc)
		- [Connecting to the docker](#connecting-to-the-docker)
		- [Helper Code](#helper-code)
		- [Question #1](#question-1)
		- [Question #2](#question-2)
		- [Question #3](#question-3)
		- [Question #4](#question-4)
		- [Question #5](#question-5)
		- [Question #6](#question-6)
		- [Question #7](#question-7)
	- [Flag](#flag)

## Recon

We are given a zip file `pwn_tutorial.zip` with the following contents:

- README.txt
- test
- test.c

```bash
└─$ file test
test: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=53c21665e88c2f76a35aeaeb24acac843cce0b61, for GNU/Linux 3.2.0, not stripped
```

### test.c

```c
#include <stdio.h>
#include <limits.h>

int add(int x, int y) { return x + y; }

void main(){
	int n1, n2;
	printf("INT_MAX value: %d\n\nEnter 2 numbers: ", INT_MAX);
	scanf("%d %d", &n1, &n2);
	printf(n1 < 0 || n2 < 0 ? "\n[-] Negative values detected! Exiting..\n" : "\nThe sum of %d and %d is %d\n\n", n1, n2, add(n1, n2));
}
```

### Connecting to the docker

```bash
└─$ nc 94.237.51.233 53080
This is a simple questionnaire to get started with the basics.

◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉
◉                                                                                           ◉
◉  C/C++ provides two macros named INT_MAX and INT_MIN that represent the integer limits.   ◉
◉                                                                                           ◉
◉  INT_MAX = 2147483647                  (for 32-bit Integers)                              ◉
◉  INT_MAX = 9,223,372,036,854,775,807   (for 64-bit Integers)                              ◉
◉                                                                                           ◉
◉  INT_MIN = –2147483648                 (for 32-bit Integers)                              ◉
◉  INT_MIN = –9,223,372,036,854,775,808  (for 64-bit Integers)                              ◉
◉                                                                                           ◉
◉  When this limit is passed, C will proceed with an 'unusual' behavior. For example, if we ◉
◉  add INT_MAX + 1, the result will NOT be 2147483648 as expected, but something else.      ◉
◉                                                                                           ◉
◉  The result will be a negative number and not just a random negative number, but INT_MIN. ◉
◉                                                                                           ◉
◉  This 'odd' behavior, is called Integer Overflow.                                         ◉
◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉◉
```

We are given 7 questions to answer. I used the information we were given as well as an online C compiler to answer the questions.

### Helper Code

I used the following code (this is for question 7) to answer the questions.

```c
#include <stdio.h>

#define INT_MAX 2147483647

int main()
{
    int result = INT_MAX+1337;
    printf("Result: %d\n", result);
    return 0;
}
```

### Question #1
```bash
[*] Question number 0x1:

Is it possible to get a negative result when adding 2 positive numbers in C? (y/n)

>> y

♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
♠                   ♠
♠      Correct      ♠
♠                   ♠
♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
```

### Question #2
```bash
[*] Question number 0x2:

What's the MAX 32-bit Integer value in C?

>> 2147483647

♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
♠                   ♠
♠      Correct      ♠
♠                   ♠
♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
```

### Question #3
```bash
[*] Question number 0x3:

What number would you get if you add INT_MAX and 1?

>> -2147483648

♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
♠                   ♠
♠      Correct      ♠
♠                   ♠
♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
```

### Question #4
```bash
[*] Question number 0x4:

What number would you get if you add INT_MAX and INT_MAX?

>> -2

♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
♠                   ♠
♠      Correct      ♠
♠                   ♠
♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
```

### Question #5
```bash
[*] Question number 0x5:

What's the name of this bug? (e.g. buffer overflow)

>> integer overflow

♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
♠                   ♠
♠      Correct      ♠
♠                   ♠
♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
```

### Question #6
```bash
[*] Question number 0x6:

What's the MIN 32-bit Integer value in C?

>> -2147483648

♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
♠                   ♠
♠      Correct      ♠
♠                   ♠
♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠ ♠
```

### Question #7
```bash
[*] Question number 0x7:

What's the number you can add to INT_MAX to get the number -2147482312?

>> 1337

HTB{gg_3z_th4nk5_f0r_th3_tut0r14l}
```

When the final question was answered correctly, the flag was given.

## Flag

`HTB{gg_3z_th4nk5_f0r_th3_tut0r14l}`