from pwn import *

def set_address(address):
    # Convert to binary string, remove '0b', and pad with zeros
    binary_string = bin(address)[2:].zfill(11)

    # Replace every high bit with a 5 for 5 volts
    binary_string = binary_string.replace('1', '5')

    # Make comma separated list
    binary_string = ','.join(binary_string)

    # Split the list so we can manipulate it
    binary_list = binary_string.split(',')

    # Make sure A9 is always 12 volts
    binary_list[-10] = '12'

    # Rejoin the list
    binary_string = ','.join(binary_list)

    # Create final command
    binary_string = 'set_address_pins([' + binary_string + '])'
    #print(binary_string)
    conn.sendline(binary_string.encode())


remote_ip = '83.136.254.199'
remote_port = 46073

conn = remote(remote_ip, remote_port)

print(conn.recvuntil(b'> ').decode())
print(conn.recvuntil(b'> ').decode())

conn.sendline(b'set_ce_pin(0)') # active low

address = 0x7e0

flag = ''

while (address < 0x800):
    conn.sendline(b'set_oe_pin(5)') # active low
    conn.recvuntil(b'> ')
    conn.sendline(b'set_we_pin(5)') # active low
    conn.recvuntil(b'> ')
    set_address(address)
    conn.recvuntil(b'> ')
    conn.sendline(b'set_oe_pin(0)') # active low
    conn.recvuntil(b'> ')
    conn.sendline(b'read_byte()')
    read_byte_line = conn.recvline()
    print(read_byte_line)

    pattern = r'0x[0-9A-Fa-f]+'
    matches = re.findall(pattern, read_byte_line.decode())
    char = chr(int(matches[0], 16))
    flag += char

    address += 1

print(flag)

# Close the connection
conn.close()
