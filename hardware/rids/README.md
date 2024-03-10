# Rids

>Upon reaching the factory door, you physically open the RFID lock and find a flash memory chip inside. The chip's package has the word W25Q128 written on it. Your task is to uncover the secret encryption keys stored within so the team can generate valid credentials to gain access to the facility.
> 
> Files: `client.py`

**Writeup by:** Stig Rune Grønnestad

- [Rids](#rids)
	- [Recon](#recon)
		- [Datasheet](#datasheet)
	- [Exploitation](#exploitation)
	- [Flag](#flag)

## Recon

We are given a file `client.py` and a hint that the RFID lock has a flash memory chip with the word `W25Q128` written on it. This is a hint that the flash memory chip is a Winbond W25Q128. This is a common flash memory chip, and the datasheet can be found here:

https://www.winbond.com/hq/product/code-storage-flash-memory/serial-nor-flash/?__locale=en&partNo=W25Q128JV

### Datasheet

From the sample code we can see the following:

```python
jedec_id = exchange([0x9F], 3)
print(jedec_id)
```

According to the datasheet this corresponds to command "8.2.27 Read JEDEC ID (9Fh)".

Let's see if it's possible to communicate with the flash memory chip using the `client.py` file.

## Exploitation

Using the datasheet we can find the read command for the flash memory chip. The command is `0x03` and the datasheet states that the command is followed by a 24-bit address and then the data is read. The solution was to try to read from address 0 and increase the length until a completed flag was printed.

This code was used to read from the chip, the length was increased until a completed flag was printed.

The data was recieved as hex values and the flag was printed by converting the hex values to ascii.

```python
data = exchange([0x03], 128)
print(data)

for c in data:
    print(chr(c), end='')
    if c == 125:
        break;
```

## Flag

HTB{m3m02135_57023_53c2375_f02_3v32y0n3_70_533!@}