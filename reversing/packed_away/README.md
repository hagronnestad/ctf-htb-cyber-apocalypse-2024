# PackedAway

> To escape the arena's latest trap, you'll need to get into a secure vault - and quick! There's a password prompt waiting for you in front of the door however - can you unpack the password quick and get to safety?
> 
> Files: [packed](rev_packedaway/rev_packedaway/packed)

**Writeup by:** Stig Rune Grønnestad

- [PackedAway](#packedaway)
	- [Recon](#recon)
		- [file](#file)
		- [strings](#strings)
		- [Unpack](#unpack)
	- [Flag](#flag)

## Recon

### file
```bash
└─$ file packed
packed: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), statically linked, no section header
```

### strings
```bash
└─$ strings packed
UPX!
-9ya
tdoP7yd
/lib64
nux-x86-
so.2
3/aC
g_app
cation_g[
et_type
_check_
tanc
signal
0d;a
unref
_ITM
gi2m
Cl-eTabl[_f
mkSr._*(
mk'gt{
x$buff
t"wid
28view
xwtK
#v7c
Jend
?fz&,quesd
'0ow
E6_7pWbx
ospac
mmk+G
Sfau^
cxa_f
t$&r
[P-2.0
c       6Ye;w
[`bssq
BC_034
5O=e
;XCv
PTE1
u+UH
Hr3t_0f_th3_p45}
ck3d
F#s3cj
5w0rdogreen
Window
wDeholder
chang%
g.gtk.example
,tivates
;*3$"?D
Vfvd
 &6F2
USQRH
W^YH
PROT_EXEC|PROT_WRITE failed.
_j<X
$Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 4.22 Copyright (C) 1996-2024 the UPX Team. All Rights Reserved. $
_RPWQM)
j"AZR^j
PZS^
/proc/self/exe
IuDSWH
s2V^
XAVAWPH
YT_j
AY^_
D$ [I
UPX!u
slIT$}
}aw993u
([]A\A]
I[8k
(L      "
tL      n
+xHf
p(E1[$1
fFj9
~*"|]
I5(Ag
@bQs
 k1(
=(I[u
A^A_)
m@S r6
ck5?
JAPC
JG=,1
SRVW
RY?WVj,4
GCC: (Debian 12.
0-14)
x$<;
wP4"
 Gx_
~"/!l
G ^/!
@.?!l
B.'=
L/`d
Scrt1.o
stuff.c
deregi
m_clones)do_g
balo
        tors9ux5omple)d.0
_`!_fin`array_entr`
me ummy2
NX7_)t*ma
activa
6FRA
ME_END
GLOBAL_OFFSET_TA
DYN#IC,GNU*Hm;
`3HDRW
icPi
0typ
check
cTMC
@Tgl
(ize@
|sig0:LM
a.wGw
Wview
]nt+
#[smo
A'db
UgmonIwx!a_wCV
Gosp
.m`Ih{
X(l5v
XJje
K]hrdl
l>ize8
        tgv
dY1T
Cay+
3que
sym,b
fK      dynb
la(
;d?@
UPX!
UPX!
```

UPX packed file, packed with version 4.22.

> $Info: This file is packed with the UPX executable packer http://upx.sf.net $
$Id: UPX 4.22 Copyright (C) 1996-2024 the UPX Team. All Rights Reserved. $

### Unpack
Let's see if it's possible to unpack the file.

```bash
└─$ upx -d packed
                       Ultimate Packer for eXecutables
                          Copyright (C) 1996 - 2024
UPX 4.2.2       Markus Oberhumer, Laszlo Molnar & John Reiser    Jan 3rd 2024

        File size         Ratio      Format      Name
   --------------------   ------   -----------   -----------
     22867 <-      8848   38.69%   linux/amd64   packed

Unpacked 1 file.
```

```bash
└─$ file packed
packed: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=d24a6e8eef367eb565e8bb90fe3ef9e9d0a71a43, for GNU/Linux 3.2.0, not stripped
```

I checked it with Ghidra before I tried `strings` again, and found the password in the strings output.

```bash
└─$ strings packed | grep HTB
HTB{unp4ck3dr3t_HH0f_th3_pH0f_th3_pH0f_th3_pH0f_th3_pH
HTB{
HTB{unp4ck3d_th3_s3cr3t_0f_th3_p455w0rd}
```

There it was.

## Flag

HTB{unp4ck3d_th3_s3cr3t_0f_th3_p455w0rd}