# Character

> Security through Induced Boredom is a personal favourite approach of mine. Not as exciting as something like The Fray, but I love making it as tedious as possible to see my secrets, so you can only get one character at a time!
>
> Docker:
> - `nc 94.237.51.96 51605`

**Writeup by:** Hein Andre Grønnestad


- [Character](#character)
  - [Service](#service)
  - [Solve Script](#solve-script)
  - [Running The Script](#running-the-script)
  - [Flag](#flag)


## Service

When connecting to the service we're presented with a question; `Which character (index) of the flag do you want?`. When the service is given an index it seems to return the flag character at that index. Seems like all we need is a simple script to do the enumeration for us.

```bash
$ nc 94.237.51.96 51605
Which character (index) of the flag do you want? Enter an index: 0
Character at Index 0: H
Which character (index) of the flag do you want? Enter an index: 1
Character at Index 1: T
Which character (index) of the flag do you want? Enter an index: 255
Index out of range!
Which character (index) of the flag do you want? Enter an index:
```


## Solve Script

Full script here: [`solver.py`](solver.py)

```python
from pwn import *

remote_ip = '94.237.51.96'
remote_port = 51605

conn = remote(remote_ip, remote_port)

char = ''
count = 0
flag = ''

while char != b'}':
    print(conn.recvuntil(b'Which character (index) of the flag do you want? Enter an index: '))
    indexstr = str(count).encode()
    print(indexstr)
    conn.sendline(indexstr)
    response = conn.recvline()
    parts = response.split(b':')
    char = parts[1].strip()
    print(response)
    flag += char.decode()
    count += 1

print('\n')
print('Flag is:', flag)
print('\n')

# Close the connection
conn.close()

```


## Running The Script

```bash
$ python3 solver.py
[+] Opening connection to 94.237.51.96 on port 51605: Done
b'Which character (index) of the flag do you want? Enter an index: '
b'0'
b'Character at Index 0: H\n'
b'Which character (index) of the flag do you want? Enter an index: '
b'1'
b'Character at Index 1: T\n'

# ...abbreviated

b'Which character (index) of the flag do you want? Enter an index: '
b'102'
b'Character at Index 102: !\n'
b'Which character (index) of the flag do you want? Enter an index: '
b'103'
b'Character at Index 103: }\n'


Flag is: HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0ng!!}


[*] Closed connection to 94.237.51.96 port 51605

```


## Flag

`HTB{tH15_1s_4_r3aLly_l0nG_fL4g_i_h0p3_f0r_y0Ur_s4k3_tH4t_y0U_sCr1pTEd_tH1s_oR_els3_iT_t0oK_qU1t3_l0ng!!}`
