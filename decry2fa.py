import os
import pyotp
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def totp():
    '''
    check if the key is valid
    '''
    totp = pyotp.TOTP(key)
    return totp.verify(key)


def read_file(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

def write_file(filepath, data):
    with open(filepath, 'wb') as f:
        f.write(data)


'''
ask the key from user (the 6 key from 2 fa )
'''
"""
flag_2fa = False
while flag_2fa == False:
    if len(key) == 6 and key.isdigit() and totp(flag_2fa):
        flag_2fa = True
    else:
        print("Please enter a valid 6 digit key")
        key = input("Key: ")
"""


'''
aes decrypt
'''
def aes_decrypt(ciphertext, key, iv):
    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext





'''
output decrypted file
'''
if __name__ == "__main__":
    with open('key.txt', 'r') as f:
        key = f.read().strip()
    key = bytes.fromhex(key)
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")
    ciphertext = read_file('encrypted.bin')
    plaintext = aes_decrypt(ciphertext[16:], key, ciphertext[:16]) 
    write_file('decrypted.txt', plaintext)
