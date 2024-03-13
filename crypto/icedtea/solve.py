from Crypto.Util.Padding import unpad
from Crypto.Util.number import bytes_to_long as b2l, long_to_bytes as l2b

# Constants
BLOCK_SIZE = 64  # block size in bits
DELTA = 0x9e3779b9
KEY_HEX = '850c1413787c389e0b34437a6828a1b2'
CIPHERTEXT_HEX = 'b36c62d96d9daaa90634242e1e6c76556d020de35f7a3b248ed71351cc3f3da97d4d8fd0ebc5c06a655eb57f2b250dcb2b39c8b2000297f635ce4a44110ec66596c50624d6ab582b2fd92228a21ad9eece4729e589aba644393f57736a0b870308ff00d778214f238056b8cf5721a843'

# Helper functions
def _xor(a, b):
    return bytes(_a ^ _b for _a, _b in zip(a, b))

# Decryption function for a single block
def decrypt_block(ciphertext_block, key):
    # Split the key into parts
    K = [b2l(key[i:i+4]) for i in range(0, len(key), 4)]
    
    # Prepare block
    c = b2l(ciphertext_block)
    msk = (1 << (BLOCK_SIZE//2)) - 1
    m1 = c & msk
    m0 = c >> (BLOCK_SIZE//2)
    
    s = DELTA * 32
    for i in range(32):
        m1 -= ((m0 << 4) + K[2]) ^ (m0 + s) ^ ((m0 >> 5) + K[3])
        m1 &= msk
        m0 -= ((m1 << 4) + K[0]) ^ (m1 + s) ^ ((m1 >> 5) + K[1])
        m0 &= msk
        s -= DELTA
    
    return l2b(m0) + l2b(m1)

# Decrypt the entire ciphertext
def decrypt_ecb(ciphertext, key):
    blocks = [ciphertext[i:i+8] for i in range(0, len(ciphertext), 8)]
    decrypted_blocks = [decrypt_block(block, key) for block in blocks]
    decrypted = b''.join(decrypted_blocks)
    return unpad(decrypted, 8)  # Assuming block size for padding is 8 bytes

# Prepare key and ciphertext
key_bytes = bytes.fromhex(KEY_HEX)
ciphertext_bytes = bytes.fromhex(CIPHERTEXT_HEX)

# Decrypt
decrypted = decrypt_ecb(ciphertext_bytes, key_bytes)
print(decrypted)
