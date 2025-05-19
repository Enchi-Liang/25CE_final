import os
import pyotp
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

'''
read file 
'''
def read_file(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

'''
aes encrypt
'''
def aes_encrypt(data, key):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(data) + padder.finalize()
    ciphertext = encryptor.update(padded_data) + encryptor.finalize()
    return iv + ciphertext  # Prepend IV for later decryption


'''
output encrypted file
'''
def write_file(filepath, data):
    with open(filepath, 'wb') as f:
        f.write(data)

if __name__ == "__main__":
    with open('key.txt', 'r') as f:
        key = f.read().strip()
    key = bytes.fromhex(key)  
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")
    iv = os.urandom(16)  # Generate a random IV
    plaintext = read_file('input.txt')  
    encrypted = aes_encrypt(plaintext, key)
    write_file('encrypted.bin', encrypted)
