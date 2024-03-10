# Makeshift

> Weak and starved, you struggle to plod on. Food is a commodity at this stage, but you can’t lose your alertness - to do so would spell death. You realise that to survive you will need a weapon, both to kill and to hunt, but the field is bare of stones. As you drop your body to the floor, something sharp sticks out of the undergrowth and into your thigh. As you grab a hold and pull it out, you realise it’s a long stick; not the finest of weapons, but once sharpened could be the difference between dying of hunger and dying with honour in combat.
>
> Files:
> - `crypto_makeshift.zip`

**Writeup by:** Hein Andre Grønnestad


- [Makeshift](#makeshift)
	- [Files](#files)
	- [Analysis](#analysis)
	- [`solve.py`](#solvepy)
	- [Flag](#flag)


## Files

We take a look at the provided files.

```bash
$ ll
total 32
-rwxrwxrwx 1 hag hag   652 Mar 10 18:47 crypto_makeshift.zip
-rw-r--r-- 1 hag hag 25581 Mar 10 18:47 README.md

$ unzip crypto_makeshift.zip
Archive:  crypto_makeshift.zip
   creating: challenge/
  inflating: challenge/source.py
 extracting: challenge/output.txt

$ ll
total 36
drwxr-xr-x 2 hag hag  4096 Jan 29 15:00 challenge
-rwxrwxrwx 1 hag hag   652 Mar 10 18:47 crypto_makeshift.zip
-rw-r--r-- 1 hag hag 25785 Mar 10 18:47 README.md

$ cd challenge/

$ ll
total 8
-rw-r--r-- 1 hag hag  34 Jan 29 14:48 output.txt
-rw-r--r-- 1 hag hag 184 Jan 29 14:46 source.py

$ cat output.txt
!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB

$ cat source.py
```
```python
from secret import FLAG

flag = FLAG[::-1]
new_flag = ''

for i in range(0, len(flag), 3):
    new_flag += flag[i+1]
    new_flag += flag[i+2]
    new_flag += flag[i]

print(new_flag)
```


## Analysis

We can see that `output.txt` contains the flag in some form.

We also see that the `source.py` Python program was most likely used to make the `output.txt` file. Knowing how the Python program works, we should be able to reverse the process and return the contents into a readable flag.

I think we can actually use the provided program to unobfuscate the flag. Because the operation in the program is reversable.


## `solve.py`

Full script: [`solve.py`](challenge/solve.py)

I modified the program a little bit to take the flag from the command line:

```python
import sys

flag = sys.argv[1]

# Uno Reverse!
flag = flag[::-1]

new_flag = ''

for i in range(0, len(flag), 3):
    new_flag += flag[i+1]
    new_flag += flag[i+2]
    new_flag += flag[i]

print(new_flag)
```

Let's try it:

```bash
$ python3 solve.py '!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB'
HTB{4_b3tTeR_w3apOn_i5_n3edeD!?!}
```

It works! And when we run it again on the actual flag we get the same obfuscated flag from `output.txt`.

```bash
$ python3 solve.py 'HTB{4_b3tTeR_w3apOn_i5_n3edeD!?!}'
!?}De!e3d_5n_nipaOw_3eTR3bt4{_THB
```

## Flag

`HTB{4_b3tTeR_w3apOn_i5_n3edeD!?!}`
