# Stop Drop and Roll

> The Fray: The Video Game is one of the greatest hits of the last... well, we don't remember quite how long. Our "computers" these days can't run much more than that, and it has a tendency to get repetitive...
>
> Docker:
> - `nc 94.237.55.163 51669`

**Writeup by:** Stig Rune Grønnestad

## Playing the game

I anticipate based on the description that this is a simple game of sending the correct response to the server, and that it's going to get repetitive. Let's connect and see what happens.

```bash
└─$ nc 94.237.55.163 51669
===== THE FRAY: THE VIDEO GAME =====
Welcome!
This video game is very simple
You are a competitor in The Fray, running the GAUNTLET
I will give you one of three scenarios: GORGE, PHREAK or FIRE
You have to tell me if I need to STOP, DROP or ROLL
If I tell you there's a GORGE, you send back STOP
If I tell you there's a PHREAK, you send back DROP
If I tell you there's a FIRE, you send back ROLL
Sometimes, I will send back more than one! Like this:
GORGE, FIRE, PHREAK
In this case, you need to send back STOP-ROLL-DROP!
Are you ready? (y/n)
```

Yup, based on the output below I got tired already. Let's write a script to play the game for us.

```bash
Ok then! Let's go!
GORGE, FIRE, FIRE, FIRE
What do you do? STOP-ROLL-ROLL-ROLL
FIRE, PHREAK, PHREAK, GORGE, FIRE
What do you do? ROLL-DROP-DROP-STOP-ROLL
FIRE, PHREAK, GORGE, PHREAK, PHREAK
What do you do? ROLL-DROP-STOP-DROP-DROP
GORGE, PHREAK, GORGE, PHREAK
What do you do?
```

## Solve Script

[Solver](solver.py)

The python scripts reads character by character and responds to the server as soon as it has enough information to make a decision. It might not the most efficient way to solve this, and the output is a little weird, but it works.

After around 500 games the flag is revealed.

## Flag

HTB{1_wiLl_sT0p_dR0p_4nD_r0Ll_mY_w4Y_oUt!}