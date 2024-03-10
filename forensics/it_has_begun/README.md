# It Has Begun

> The Fray is upon us, and the very first challenge has been released! Are you ready factions!? Considering this is just the beginning, if you cannot musted the teamwork needed this early, then your doom is likely inevitable.
> 
> Files:
> - [forensics_it_has_begun.zip](forensics_it_has_begun.zip)

**Writeup by:** Stig Rune Grønnestad

- [It Has Begun](#it-has-begun)
	- [Recon](#recon)
		- [Part of RSA key](#part-of-rsa-key)
		- [Random hash](#random-hash)
		- [Punycode?](#punycode)
	- [Flag](#flag)

## Recon

Looking at the attached file `script.sh` I found a few clues quickly, namely the `{BTH` and `NG5kX3kwdVJfR3IwdU5kISF9` cought my attention. The first string seemed to be a reversed part of the flag, and the second string seemed to be a base64 encoded string. I combined these two and for some reason thought I was missing a middle part which led me down a small rabbit hole.

I used CyberChef for the decoding and reversing.

### Part of RSA key
```
tS_u0y_ll1w{BTH

Reversed -> 

HTB{w1ll_y0u_St
```
https://gchq.github.io/CyberChef/#recipe=Reverse('Character')&input=dFNfdTB5X2xsMXd7QlRI

### Random hash
```
NG5kX3kwdVJfR3IwdU5kISF9

From Base64 ->

4nd_y0uR_Gr0uNd!!}
```
https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)&input=Tkc1a1gza3dkVkpmUjNJd2RVNWtJU0Y5

```
Combined:

HTB{w1ll_y0u_St4nd_y0uR_Gr0uNd!!}
```

### Punycode?

For some reason I got an error using the flag (copy-paste error or something), which led me down a small rabbit hole. Looking at the part of the URLs `0xda4` (decimal 3492) led me to believe I had to use punycode (RFC 3492) to get the flag. This was not the case, but it was a fun detour.

```
Punycode: A Bootstring encoding of Unicode for Internationalized Domain Names in Applications (IDNA)
RFC 3492
```

## Flag
The flag was simply:

`HTB{w1ll_y0u_St4nd_y0uR_Gr0uNd!!}`