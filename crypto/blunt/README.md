# Blunt
> Valuing your life, you evade the other parties as much as you can, forsaking the piles of weaponry and the vantage points in favour of the depths of the jungle. As you jump through the trees and evade the traps lining the forest floor, a glint of metal catches your eye. Cautious, you creep around, careful not to trigger any sensors. Lying there is a knife - damaged and blunt, but a knife nonetheless. You’re not helpless any more.
> 
> Files: 
> [output.txt](crypto_blunt/challenge/output.txt) |
> [source.py](crypto_blunt/challenge/source.py)

**Writeup by:** Stig Rune Grønnestad

## Recon

We are given two files, `output.txt` and `source.py`. Let's see what they contain.

[source.py]
```python
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.number import getPrime, long_to_bytes
from hashlib import sha256
from secret import FLAG
import random

p = getPrime(32)
print(f'p = 0x{p:x}')

g = random.randint(1, p-1)
print(f'g = 0x{g:x}')

a = random.randint(1, p-1)
b = random.randint(1, p-1)

A, B = pow(g, a, p), pow(g, b, p)

print(f'A = 0x{A:x}')
print(f'B = 0x{B:x}')

C = pow(A, b, p)
assert C == pow(B, a, p)

# now use it as shared secret
hash = sha256()
hash.update(long_to_bytes(C))

key = hash.digest()[:16]
iv = b'\xc1V2\xe7\xed\xc7@8\xf9\\\xef\x80\xd7\x80L*'
cipher = AES.new(key, AES.MODE_CBC, iv)

encrypted = cipher.encrypt(pad(FLAG, 16))
print(f'ciphertext = {encrypted}')
```

[output.txt]
```bash
p = 0xdd6cc28d
g = 0x83e21c05
A = 0xcfabb6dd
B = 0xc4a21ba9
ciphertext = b'\x94\x99\x01\xd1\xad\x95\xe0\x13\xb3\xacZj{\x97|z\x1a(&\xe8\x01\xe4Y\x08\xc4\xbeN\xcd\xb2*\xe6{'
```

Googling "encryption p g A B" yields the Diffie-Hellman key exchange. The key exchange is used to establish a shared secret between two parties. The shared secret is then used to encrypt the message. The shared secret is calculated as `C = pow(A, b, p) = pow(B, a, p)`. The shared secret is then used as the key for the AES encryption.

https://en.wikipedia.org/wiki/Diffie–Hellman_key_exchange

