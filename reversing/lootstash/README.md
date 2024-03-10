# LootStash

> A giant stash of powerful weapons and gear have been dropped into the arena - but there's one item you have in mind. Can you filter through the stack to get to the one thing you really need?
> 
> Files:
> - [rev_lootstash.zip](rev_lootstash.zip)

**Writeup by:** Hein Andre Grønnestad

- [LootStash](#lootstash)
  - [Checking Provided Files](#checking-provided-files)
  - [Dynamic Analysis](#dynamic-analysis)
  - [Static Analysis](#static-analysis)
    - [`r2`](#r2)
    - [`strings`](#strings)
  - [Flag](#flag)


## Checking Provided Files

```bash
$ ll
total 24
-rw-r--r-- 1 hag hag 14161 Mar 10 23:32 README.md
-rwxrwxrwx 1 hag hag  8013 Mar 10 23:32 rev_lootstash.zip

$ unzip rev_lootstash.zip
Archive:  rev_lootstash.zip
   creating: rev_lootstash/
  inflating: rev_lootstash/stash

$ cd rev_lootstash/

$ ll
total 32
-rwxr-xr-x 1 hag hag 30704 Feb  7 21:45 stash

$ file stash
stash: ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=817b1311ae44bdc6ed8a9b563159616844e59c64, for GNU/Linux 3.2.0, not stripped
```


## Dynamic Analysis

```bash
$ ./stash
Diving into the stash - let's see what we can find.
.....
You got: 'Earthsong, Dawn of Visions'. Now run, before anyone tries to steal it!

$ ./stash
Diving into the stash - let's see what we can find.
.....
You got: 'Twitch, Vessel of the Forgotten'. Now run, before anyone tries to steal it!

$ ./stash
Diving into the stash - let's see what we can find.
.....
You got: 'Frostward, Annihilation of Mourning'. Now run, before anyone tries to steal it!
```


## Static Analysis

So according to `file` we have a `ELF 64-bit LSB pie executable, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, BuildID[sha1]=817b1311ae44bdc6ed8a9b563159616844e59c64, for GNU/Linux 3.2.0, not stripped` file.


### `r2`

```bash
$ r2 stash
Warning: run r2 with -e bin.cache=true to fix relocations in disassembly
[0x000020c0]> aaaaa
[x] Analyze all flags starting with sym. and entry0 (aa)
[x] Analyze function calls (aac)
[x] Analyze len bytes of instructions for references (aar)
[x] Finding and parsing C++ vtables (avrr)
[x] Type matching analysis for all functions (aaft)
[x] Propagate noreturn information (aanr)
[x] Finding function preludes
[x] Enable constraint types analysis for variables
[0x000020c0]> pdf @main
            ; DATA XREF from entry0 @ 0x20d4
┌ 221: int main (int argc, char **argv, char **envp);
│           ; var int64_t var_8h @ rbp-0x8
│           ; var signed int64_t var_4h @ rbp-0x4
│           0x000021a9      55             push rbp
│           0x000021aa      4889e5         mov rbp, rsp
│           0x000021ad      4883ec10       sub rsp, 0x10
│           0x000021b1      488b05a05600.  mov rax, qword [obj.stdout] ; obj.__TMC_END__
│                                                                      ; [0x7858:8]=0
│           0x000021b8      b900000000     mov ecx, 0                  ; size_t size
│           0x000021bd      ba02000000     mov edx, 2                  ; int mode
│           0x000021c2      be00000000     mov esi, 0                  ; char *buf
│           0x000021c7      4889c7         mov rdi, rax                ; FILE*stream
│           0x000021ca      e8b1feffff     call sym.imp.setvbuf        ; int setvbuf(FILE*stream, char *buf, int mode, size_t size)
│           0x000021cf      bf00000000     mov edi, 0                  ; time_t *timer
│           0x000021d4      e897feffff     call sym.imp.time           ; time_t time(time_t *timer)
│           0x000021d9      89c7           mov edi, eax                ; int seed
│           0x000021db      e880feffff     call sym.imp.srand          ; void srand(int seed)
│           0x000021e0      488d05712e00.  lea rax, str.Diving_into_the_stash___lets_see_what_we_can_find. ; 0x5058 ; "Diving into the stash - let's see what we can find."
│           0x000021e7      4889c7         mov rdi, rax                ; const char *s
│           0x000021ea      e851feffff     call sym.imp.puts           ; int puts(const char *s)
│           0x000021ef      c745fc000000.  mov dword [var_4h], 0
│       ┌─< 0x000021f6      eb18           jmp 0x2210
│       │   ; CODE XREF from main @ 0x2214
│      ┌──> 0x000021f8      bf2e000000     mov edi, 0x2e               ; '.' ; int c
│      ╎│   0x000021fd      e82efeffff     call sym.imp.putchar        ; int putchar(int c)
│      ╎│   0x00002202      bf01000000     mov edi, 1                  ; int s
│      ╎│   0x00002207      e884feffff     call sym.imp.sleep          ; int sleep(int s)
│      ╎│   0x0000220c      8345fc01       add dword [var_4h], 1
│      ╎│   ; CODE XREF from main @ 0x21f6
│      ╎└─> 0x00002210      837dfc04       cmp dword [var_4h], 4
│      └──< 0x00002214      7ee2           jle 0x21f8
│           0x00002216      e885feffff     call sym.imp.rand           ; int rand(void)
│           0x0000221b      4863c8         movsxd rcx, eax
│           0x0000221e      48ba81808080.  movabs rdx, 0x8080808080808081
│           0x00002228      4889c8         mov rax, rcx
│           0x0000222b      48f7e2         mul rdx
│           0x0000222e      48c1ea0a       shr rdx, 0xa
│           0x00002232      4889d0         mov rax, rdx
│           0x00002235      48c1e008       shl rax, 8
│           0x00002239      4829d0         sub rax, rdx
│           0x0000223c      48c1e003       shl rax, 3
│           0x00002240      4829c1         sub rcx, rax
│           0x00002243      4889ca         mov rdx, rcx
│           0x00002246      4889d0         mov rax, rdx
│           0x00002249      48c1e803       shr rax, 3
│           0x0000224d      8945f8         mov dword [var_8h], eax
│           0x00002250      8b45f8         mov eax, dword [var_8h]
│           0x00002253      4898           cdqe
│           0x00002255      488d14c50000.  lea rdx, [rax*8]
│           0x0000225d      488d05fc4d00.  lea rax, obj.gear           ; 0x7060
│           0x00002264      488b0402       mov rax, qword [rdx + rax]
│           0x00002268      4889c6         mov rsi, rax
│           0x0000226b      488d051e2e00.  lea rax, str._nYou_got:__s._Now_run__before_anyone_tries_to_steal_it__n ; 0x5090 ; "\nYou got: '%s'. Now run, before anyone tries to steal it!\n"
│           0x00002272      4889c7         mov rdi, rax                ; const char *format
│           0x00002275      b800000000     mov eax, 0
│           0x0000227a      e8d1fdffff     call sym.imp.printf         ; int printf(const char *format)
│           0x0000227f      b800000000     mov eax, 0
│           0x00002284      c9             leave
└           0x00002285      c3             ret
[0x000020c0]>
```


### `strings`

Let's run `strings` on the binary to see if we can find the list of strings being output by the binary.

```bash
$ strings stash
/lib64/ld-linux-x86-64.so.2
V1YahD
setvbuf
sleep
puts
putchar
time
stdout
__libc_start_main
srand
__cxa_finalize
printf
libc.so.6
GLIBC_2.34
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
PTE1
u+UH
Ebony, Core of Perdition
Phantomdream, Trinket of the Corrupted
Earthsong, Dawn of Visions
Torment, Beacon of Twilight's End
Moonshard, Baton of the Wind
Mirage, Bead of Secrets
Inertia, Sphere of Nightmares
Spellkeeper, Glory of Pride
Mirage, Stone of the Wind
Ghost, Baton of Suffering
Scar, Idol of Horrors
Phantomsong, Focus of Fallen Souls
Netherlight, Touch of Woe
Scarlet, Visage of Summoning
Massacre, Seal of the Shadows
Dementia, Fan of Eternal Justice
Scarlet, Insignia of Hatred
Silence, Destruction of Diligence
Dreamsong, Globe of Perdition
Fury, Allegiance of Grieving Widows
Pursuit, Allegiance of the Forest
Moonlight, Cry of Shifting Sands
Doombinder, Edge of Twilight's End
Draughtbane, Bond of Hate
Blazefury, Sculptor of Grace
Clemence, Breaker of Cunning
Celestia, Slayer of Illumination
Nexus, Jewel of Pride's Fall
Dusksong, Whisper of the Covenant
Splinter, Aspect of the Forsaken
Tranquillity, Eye of Terror
Dreamwhisper, Betrayer of the Breaking Storm
Delusion, Idol of the Moon
Soulsliver, Fan of Fools
Fluke, Sculptor of Widows

# ...abbreviated
```

So we have a list of strings that are being output by the binary. We can see that the binary is outputting a random string from a list of strings. We can also see that the binary is using `srand` and `rand` to generate a random number, and then using that number to index into the list of strings to get a random string to output.

Let's just quickly check if the big list of strings contains anything that looks like a flag.

```bash
$ strings stash | grep HTB
HTB{n33dl3_1n_a_l00t_stack}
```

There it is! 🚩 That was easier than expected!


## Flag

`HTB{n33dl3_1n_a_l00t_stack}`
