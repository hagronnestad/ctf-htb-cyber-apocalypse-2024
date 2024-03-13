# Iced TEA

> Locked within a cabin crafted entirely from ice, you're enveloped in a chilling silence. Your eyes land upon an old notebook, its pages adorned with thousands of cryptic mathematical symbols. Tasked with deciphering these enigmatic glyphs to secure your escape, you set to work, your fingers tracing each intricate curve and line with determination. As you delve deeper into the mysterious symbols, you notice that patterns appear in several pages and a glimmer of hope begins to emerge. Time is flying and the temperature is dropping, will you make it before you become one with the cabin?
>
> Files:
> - [`crypto_iced_tea.zip`](crypto_iced_tea.zip)

**Writeup by:** ChatGPT


## Files

```bash
$ unzip crypto_iced_tea.zip
Archive:  crypto_iced_tea.zip
   creating: crypto_iced_tea/
  inflating: crypto_iced_tea/source.py
  inflating: crypto_iced_tea/output.txt
```

- [`source.py`](crypto_iced_tea/source.py)
- [`output.txt`](crypto_iced_tea/output.txt)


## Challenge Overview

The challenge provided us with a Python script implementing a custom block cipher encryption algorithm, a hexadecimal key, and a ciphertext. Our goal was to decrypt the ciphertext to retrieve the flag.


### Given Data

- **Encryption Algorithm**: A Python script that defines a block cipher based on the Tiny Encryption Algorithm (TEA).
- **Key**: `850c1413787c389e0b34437a6828a1b2`
- **Ciphertext**: `b36c62d96d9daaa90634242e1e6c76556d020de35f7a3b248ed71351cc3f3da97d4d8fd0ebc5c06a655eb57f2b250dcb2b39c8b2000297f635ce4a44110ec66596c50624d6ab582b2fd92228a21ad9eece4729e589aba644393f57736a0b870308ff00d778214f238056b8cf5721a843`


## Solution Approach

1. **Understanding the Encryption Script**: The script uses a block cipher with either ECB or CBC mode. It employs a simplified version of the TEA encryption algorithm, iterating through 32 rounds of mixing the data with a key.

2. **Implementing the Decryption**: To decrypt the ciphertext, we needed to reverse the encryption steps. This involved:
    - Splitting the provided key and ciphertext into the appropriate formats.
    - Implementing a decryption function that precisely reverses the operations (additions and XORs) performed during encryption.
    - Handling the ECB mode for simplicity, as no IV was provided, indicating the use of ECB mode in this challenge.

3. **Decryption Process**: The decryption process involved splitting the ciphertext into blocks, decrypting each block by reversing the TEA algorithm's steps, and finally combining and unpadding the decrypted blocks to retrieve the plaintext.


## Decryption Code

A Python function was implemented to decrypt the ciphertext using the given key. It carefully reversed the encryption logic, including subtracting the `DELTA` constant in the opposite order of the encryption rounds and correctly handling the modular arithmetic to ensure accurate decryption.

Full code here: [solve.py](solve.py)

```bash
$ python3 solve.py
b'HTB{th1s_1s_th3_t1ny_3ncryp710n_4lg0r1thm_____y0u_m1ght_h4v3_4lr34dy_s7umbl3d_up0n_1t_1f_y0u_d0_r3v3rs1ng}'
```


## Flag

After running the decryption process, we successfully retrieved the flag:

```
HTB{th1s_1s_th3_t1ny_3ncryp710n_4lg0r1thm_____y0u_m1ght_h4v3_4lr34dy_s7umbl3d_up0n_1t_1f_y0u_d0_r3v3rs1ng}
```
