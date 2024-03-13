# Pursue The Tracks

> Luxx, leader of The Phreaks, immerses himself in the depths of his computer, tirelessly pursuing the secrets of a file he obtained accessing an opposing faction member workstation. With unwavering determination, he scours through data, putting together fragments of information trying to take some advantage on other factions. To get the flag, you need to answer the questions from the docker instance.
> 
> Files:
> - [z.mft](forensics_persue_the_tracks/z.mft)

**Writeup by:** Stig Rune Grønnestad

- [Pursue The Tracks](#pursue-the-tracks)
	- [Recon](#recon)
		- [file](#file)
		- [strings](#strings)
		- [Checking out the docker](#checking-out-the-docker)
	- [Extraction](#extraction)
		- [analyzeMFT.py](#analyzemftpy)
		- [MFTExplorer](#mftexplorer)
	- [Solving](#solving)
	- [Flag](#flag)

## Recon

### file
```bash
└─$ file z.mft
z.mft: data
```

### strings
```bash
└─$ strings z.mft
```

[strings.txt](strings.txt)

Not much to go on here, but the file is named `z.mft` which is a clue to the file system. It seems to relate to Master File Table (MFT) which is used for NTFS file systems. This is a good clue to start with.

### Checking out the docker

```bash
└─$ nc 94.237.54.153 44496

+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
|       Title       |                                                                    Description
      |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
| Pursue The Tracks |                                    Luxx, leader of The Phreaks, immerses himself in the depths of his computer,
      |
|                   |                      tirelessly pursuing the secrets of a file he obtained accessing an opposing faction member workstation.
      |
|                   | With unwavering determination, he scours through data, putting together fragments of information trying to take some advantage on other factions. |
|                   |                                    To get the flag, you need to answer the questions from the docker instance.
      |
+-------------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

Files are related to two years, which are those? (for example: 1993,1995)
>
```

We obviously need to extract some data from the `z.mft` file to answer the questions. 

## Extraction

### analyzeMFT.py

https://github.com/dkovar/analyzeMFT

```bash
└─$ python analyzeMFT.py -f z.mft -o z.csv
└─$ python analyzeMFT.py -d -f z.mft -o z.csv > z.txt
```

The files `z.csv` and `z.txt` was created. The txt file was generated with `-debug` flag on.

### MFTExplorer

After struggling with getting the actual file size to answer the last question, I found a tool called `MFTExplorer` which is a GUI tool for analyzing MFT files. It was able to give me the actual file size of the file in question. Check out Eric Zimmerman's tools here:

https://ericzimmerman.github.io/#!index.md

## Solving

I used the output from `analyzeMFT` in conjunction with `MFTExplorer` to answer the questions.

The first questions were easy enough, but I was struggling with the last question regarding the size of entry 40: `Final_Project_Proposal.pdf`. The size was finally revealed to be 57344 bytes using `MFTExplorer` (shown as `Actual Size: 0xE000`).

```bash

Files are related to two years, which are those? (for example: 1993,1995)
>2023,2024
[+] Correct!

There are some documents, which is the name of the first file written? (for example: randomname.pdf)
> Final_Annual_Report.xlsx
[+] Correct!

Which file was deleted? (for example: randomname.pdf)
> Marketing_Plan.xlsx
[+] Correct!

How many of them have been set in Hidden mode? (for example: 43)
> 1
[+] Correct!

Which is the filename of the important TXT file that was created? (for example: randomname.txt)
> credentials.txt
[+] Correct!

A file was also copied, which is the new filename? (for example: randomname.pdf)
> Financial_Statement_draft.xlsx
[+] Correct!

Which file was modified after creation? (for example: randomname.pdf)
> Project_Proposal.pdf
[+] Correct!

What is the name of the file located at record number 45? (for example: randomname.pdf)
> Annual_Report.xlsx
[+] Correct!

What is the size of the file located at record number 40? (for example: 1337)
>> 57344
[+] Correct!
```

## Flag

HTB{p4rs1ng_mft_1s_v3ry_1mp0rt4nt_s0m3t1m3s}