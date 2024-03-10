import sys

flag = sys.argv[1]

# Uno Reverse!
flag = flag[::-1]

new_flag = ''

for i in range(0, len(flag), 3):
    new_flag += flag[i+1]
    new_flag += flag[i+2]
    new_flag += flag[i]

print(new_flag)
