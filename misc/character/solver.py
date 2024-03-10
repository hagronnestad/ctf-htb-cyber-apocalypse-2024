from pwn import *

remote_ip = '94.237.51.96'
remote_port = 51605

conn = remote(remote_ip, remote_port)

char = ''
count = 0
flag = ''

while char != b'}':
    print(conn.recvuntil(b'Which character (index) of the flag do you want? Enter an index: '))
    indexstr = str(count).encode()
    print(indexstr)
    conn.sendline(indexstr)
    response = conn.recvline()
    parts = response.split(b':')
    char = parts[1].strip()
    print(response)
    flag += char.decode()
    count += 1

print('\n')
print('Flag is:', flag)
print('\n')

# Close the connection
conn.close()
