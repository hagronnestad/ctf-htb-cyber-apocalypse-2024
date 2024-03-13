import time

p = 3714892429 # 0xdd6cc28d 	public (prime) modulus
g = 2212633605 # 0x83e21c05		public (primitive root) base
A = 3484137181 # 0xcfabb6dd	    public A
B = 3298958249 # 0xc4a21ba9	    public B
ciphertext = b'\x94\x99\x01\xd1\xad\x95\xe0\x13\xb3\xacZj{\x97|z\x1a(&\xe8\x01\xe4Y\x08\xc4\xbeN\xcd\xb2*\xe6{'

start_time = time.time()
found = False

for potential_b in range(p, 1, -1):
    if pow(g, potential_b, p) == B:
        found = True
        b = potential_b
        print(f"Found b: {b}")
        break
    
    if potential_b % 1000000 == 0:
        elapsed_time = time.time() - start_time
        print(f"Checked {potential_b} possibilities in {elapsed_time:.2f} seconds...")
        # Estimate remaining time based on current progress
        estimated_total_time = elapsed_time / potential_b * (p-1)
        estimated_remaining_time = estimated_total_time - elapsed_time
        print(f"Estimated remaining time: {estimated_remaining_time:.2f} seconds")

if found:
    # Once b is found, compute the shared secret C
    C = pow(A, b, p)
    print(f"Shared secret C: {C}")
else:
    print("b was not found within the search range.")