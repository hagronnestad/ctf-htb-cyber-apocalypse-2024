# Russian Roulette

> Welcome to The Fray. This is a warm-up to test if you have what it takes to tackle the challenges of the realm. Are you brave enough?
>
> Docker:
> - `nc 94.237.49.182 54163`
> - `nc 94.237.49.182 58579`
> Files:
> - `blockchain_russian_roulette.zip`

**Writeup by:** Hein Andre Grønnestad


- [Russian Roulette](#russian-roulette)
  - [Files](#files)



## Files

We take a look at the provided files.

```bash
$ ll
total 8
-rwxrwxrwx 1 hag hag 1091 Mar 12 20:47 blockchain_russian_roulette.zip
-rw-r--r-- 1 hag hag 2951 Mar 12 20:46 README.md

$ unzip blockchain_russian_roulette.zip
Archive:  blockchain_russian_roulette.zip
   creating: blockchain_russian_roulette/
  inflating: blockchain_russian_roulette/RussianRoulette.sol
  inflating: blockchain_russian_roulette/Setup.sol

$ ll
total 12
drwxr-xr-x 2 hag hag 4096 Mar  6 15:29 blockchain_russian_roulette
-rwxrwxrwx 1 hag hag 1091 Mar 12 20:47 blockchain_russian_roulette.zip
-rw-r--r-- 1 hag hag 2951 Mar 12 20:46 README.md

$ cd blockchain_russian_roulette/

$ ll
total 8
-rw-r--r-- 1 hag hag 359 Mar  6 15:29 RussianRoulette.sol
-rw-r--r-- 1 hag hag 342 Mar  6 15:29 Setup.sol
```


```bash
$ nc 94.237.49.182 58579
1 - Connection information
2 - Restart Instance
3 - Get flag
action? 1

Private key     :  0x37dc35f95b227104fdf157ae76c6b62fd39afa65bfe6acfa95a6acff3343c692
Address         :  0x98f1AF4b0334fB32CF226910ece24d6BdB41aC8b
Target contract :  0xf9de1941EDAC16D09Bf46Ecfe2b8837d05AC7248
Setup contract  :  0xB34a3E3B254F66550eB804ecB9eBfa776E6e2f20
```

```bash
$ python3 win.py
Successfully connected to the Ethereum node. Chain ID: 31337
Account balance: 5009.9986821 ETH
Transaction receipt: AttributeDict({'transactionHash': HexBytes('0x5823a0db6a19b5c8b8c95e5898cae1c4d29f9ea1cb3bb3948cb0b7ad21f4f96f'), 'transactionIndex': 0, 'blockHash': HexBytes('0x1cee49de0de88b9f6a96a5d9cc25f6cf2d347090d9e697d94c038a6de95af266'), 'blockNumber': 3, 'cumulativeGasUsed': 21064, 'gasUsed': 21064, 'effectiveGasPrice': 50000000000, 'from': '0x98f1AF4b0334fB32CF226910ece24d6BdB41aC8b', 'to': '0xf9de1941EDAC16D09Bf46Ecfe2b8837d05AC7248', 'contractAddress': None, 'logs': [], 'logsBloom': HexBytes('0x00000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000'), 'status': 1, 'type': 0, 'depositNonce': None})
```

```bash
$ nc 94.237.49.182 58579
1 - Connection information
2 - Restart Instance
3 - Get flag
action? 3
HTB{99%_0f_g4mbl3rs_quit_b4_bigwin}
```
