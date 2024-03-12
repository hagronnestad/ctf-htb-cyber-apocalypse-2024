# The locals are stored on the stack sequentially
# so let's treat them as such.
# local_28 = 0x540345434c75637f;
# local_20 = 0x45f4368505906;
# uStack_19 = 0x68;
# uStack_18 = 0x374a025b5b0354

initial_bytes = 0x540345434C75637F.to_bytes(8, 'little') + \
                0x45f4368505906.to_bytes(7, 'little') + \
                0x68.to_bytes(1, 'little') + \
                0x374a025b5b0354.to_bytes(7, 'little')

# Convert the initial bytes to a byte sequence
byte_sequence = bytearray(initial_bytes)

#   for (local_c = 0; local_c < 0x17; local_c = local_c + 1) {
#     *(byte *)((long)&local_28 + (long)(int)local_c) =
#          *(byte *)((long)&local_28 + (long)(int)local_c) ^ 0x37;
#   }
# Loop through the byte sequence and XOR each byte with 0x37
for i in range(23):  # 0x17 is 23 in decimal
    byte_sequence[i] ^= 0x37

# Convert the modified byte sequence to a string to see
# what we get.
modified_filename = byte_sequence.decode('utf-8')
print ("[+] Modified filename: " + modified_filename)