# Dynastic

> You find yourself trapped inside a sealed gas chamber, and suddenly, the air is pierced by the sound of a distorted voice played through a pre-recorded tape. Through this eerie transmission, you discover that within the next 15 minutes, this very chamber will be inundated with lethal hydrogen cyanide. As the tape’s message concludes, a sudden mechanical whirring fills the chamber, followed by the ominous ticking of a clock. You realise that each beat is one step closer to death. Darkness envelops you, your right hand restrained by handcuffs, and the exit door is locked. Your situation deteriorates as you realise that both the door and the handcuffs demand the same passcode to unlock. Panic is a luxury you cannot afford; swift action is imperative. As you explore your surroundings, your trembling fingers encounter a torch. Instantly, upon flipping the switch, the chamber is bathed in a dim glow, unveiling cryptic letters etched into the walls and a disturbing image of a Roman emperor drawn in blood. Decrypting the letters will provide you the key required to unlock the locks. Use the torch wisely as its battery is almost drained out!
>
> Files:
> - `crypto_dynastic.zip`

**Writeup by:** Hein Andre Grønnestad


- [Dynastic](#dynastic)
  - [Files](#files)
  - [`source.py`](#sourcepy)
  - [`solve.py`](#solvepy)
  - [Flag](#flag)


## Files

We take a look at the provided files.

```bash
$ ll
total 8
-rwxrwxrwx 1 hag hag  963 Mar 10 23:10 crypto_dynastic.zip
-rw-r--r-- 1 hag hag 1375 Mar 10 23:10 README.md

$ unzip crypto_dynastic.zip
Archive:  crypto_dynastic.zip
   creating: crypto_dynastic/
  inflating: crypto_dynastic/source.py
  inflating: crypto_dynastic/output.txt

$ ll
total 12
drwxr-xr-x 2 hag hag 4096 Mar  6 12:30 crypto_dynastic
-rwxrwxrwx 1 hag hag  963 Mar 10 23:10 crypto_dynastic.zip
-rw-r--r-- 1 hag hag 1375 Mar 10 23:10 README.md

$ cd crypto_dynastic/

$ ll
total 8
-rw-r--r-- 1 hag hag 140 Mar  6 12:30 output.txt
-rw-r--r-- 1 hag hag 555 Mar  6 12:30 source.py

$ cat output.txt
Make sure you wrap the decrypted text with the HTB flag format :-]
DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL
```


## `source.py`

```python
from secret import FLAG
from random import randint

def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

def encrypt(m):
    c = ''
    for i in range(len(m)):
        ch = m[i]
        if not ch.isalpha():
            ech = ch
        else:
            chi = to_identity_map(ch)
            ech = from_identity_map(chi + i)
        c += ech
    return c

with open('output.txt', 'w') as f:
    f.write('Make sure you wrap the decrypted text with the HTB flag format :-]\n')
    f.write(encrypt(FLAG))
```

Based on the `source.py` program I made a new program to "decrypt" the flag.


## `solve.py`

```python
def to_identity_map(a):
    return ord(a) - 0x41

def from_identity_map(a):
    return chr(a % 26 + 0x41)

def decrypt(c):
    m = ''
    for i in range(len(c)):
        ch = c[i]
        if not ch.isalpha():
            dch = ch
        else:
            chi = to_identity_map(ch)
            dch = from_identity_map(chi - i)
        m += dch
    return m

with open('solved.txt', 'w') as f:
    f.write('Make sure you wrap the decrypted text with the HTB flag format :-]\n')
    f.write(decrypt("DJF_CTA_SWYH_NPDKK_MBZ_QPHTIGPMZY_KRZSQE?!_ZL_CN_PGLIMCU_YU_KJODME_RYGZXL"))

```

```bash
$ python3 solve.py

$ ll
total 16
-rw-r--r-- 1 hag hag 140 Mar  6 12:30 output.txt
-rw-r--r-- 1 hag hag 140 Mar 10 23:19 solved.txt
-rw-r--r-- 1 hag hag 575 Mar 10 23:19 solve.py
-rw-r--r-- 1 hag hag 806 Mar 10 23:17 source.py

$ cat solved.txt
Make sure you wrap the decrypted text with the HTB flag format :-]
DID_YOU_KNOW_ABOUT_THE_TRITHEMIUS_CIPHER?!_IT_IS_SIMILAR_TO_CAESAR_CIPHER
```


## Flag

`HTB{DID_YOU_KNOW_ABOUT_THE_TRITHEMIUS_CIPHER?!_IT_IS_SIMILAR_TO_CAESAR_CIPHER}`
