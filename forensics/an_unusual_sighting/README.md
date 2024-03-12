# An Unusual Sighting

> As the preparations come to an end, and The Fray draws near each day, our newly established team has started work on refactoring the new CMS application for the competition. However, after some time we noticed that a lot of our work mysteriously has been disappearing! We managed to extract the SSH Logs and the Bash History from our dev server in question. The faction that manages to uncover the perpetrator will have a massive bonus come competition!
>
> Docker:
> `94.237.60.100:41306`
> 
> Files:
> - `forensics_an_unusual_sighting.zip`

**Writeup by:** Hein Andre Grønnestad

- [An Unusual Sighting](#an-unusual-sighting)
	- [Files](#files)
	- [Docker Service](#docker-service)
	- [Flag](#flag)


## Files

We take a look at the provided files.

```bash
$ ll
total 32
-rwxrwxrwx 1 hag hag  3284 Mar 12 18:38 forensics_an_unusual_sighting.zip
-rw-r--r-- 1 hag hag 25755 Mar 12 18:38 README.md

$ unzip forensics_an_unusual_sighting.zip
Archive:  forensics_an_unusual_sighting.zip
  inflating: bash_history.txt
  inflating: sshd.log
```


## Docker Service

The Docker service is actually some kind of command line interface. The service asks us questions and we answer them. All the questions are about the provided files.

```bash
$ nc 94.237.60.100 41306

+---------------------+---------------------------------------------------------------------------------------------------------------------+
|        Title        |                                                     Description                                                     |
+---------------------+---------------------------------------------------------------------------------------------------------------------+
| An unusual sighting |                        As the preparations come to an end, and The Fray draws near each day,                        |
|                     |             our newly established team has started work on refactoring the new CMS application for the competition. |
|                     |                  However, after some time we noticed that a lot of our work mysteriously has been disappearing!     |
|                     |                     We managed to extract the SSH Logs and the Bash History from our dev server in question.        |
|                     |               The faction that manages to uncover the perpetrator will have a massive bonus come the competition!   |
|                     |                                                                                                                     |
|                     |                                            Note: Operating Hours of Korp: 0900 - 1900                               |
+---------------------+---------------------------------------------------------------------------------------------------------------------+


Note 2: All timestamps are in the format they appear in the logs

What is the IP Address and Port of the SSH Server (IP:PORT)
>
```

It looks like we're supposed to answer questions about the provided files. We answer the first question:

```bash
What is the IP Address and Port of the SSH Server (IP:PORT)
> 100.107.36.130:2221
[+] Correct!


What time is the first successful Login
> 2024-02-13 11:29:50
[+] Correct!


What is the time of the unusual Login
> 2024-02-13 11:29:50
[-] Wrong Answer. #Woops :D


What is the time of the unusual Login
> 2024-02-19 04:00:14
[+] Correct!


What is the Fingerprint of the attacker's public key
> OPkBSs6okUKraq8pYo4XwwBg55QSo210F09FCe1-yj4
[+] Correct!


What is the first command the attacker executed after logging in
> whoami
[+] Correct!


What is the final command the attacker executed before logging out
> ./setup
[+] Correct!

[+] Here is the flag: HTB{B3sT_0f_luck_1n_th3_Fr4y!!}
```

## Flag

```
HTB{B3sT_0f_luck_1n_th3_Fr4y!!}
```
