import os

# Generate a random 32-byte (256-bit) key
key = os.urandom(32)

# Save as hex string to key.txt
with open('key.txt', 'w') as f:
    f.write(key.hex())