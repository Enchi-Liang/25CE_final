import os
import pyotp
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend

def totp(user_code, secret_path='FA2key.txt'):
    '''
    check if the key is valid
    '''
    if not os.path.exists(secret_path):
        print(f"TOTP secret file '{secret_path}' not found.")
        return False
    with open(secret_path, 'r') as f:
        secret = f.read().strip()
    totp = pyotp.TOTP(secret)
    return totp.verify(user_code)


def read_file(filepath):
    with open(filepath, 'rb') as f:
        return f.read()

def write_file(filepath, data):
    with open(filepath, 'wb') as f:
        f.write(data)


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
    while True:
        try:
            FA2_key_input = input("Enter your 6-digit 2FA code: ")
            if len(FA2_key_input) == 6 and FA2_key_input.isdigit() and totp(FA2_key_input):
                print("2FA code is valid.")
                break
            else:
                print("Invalid 2FA code. Please try again.")
        except Exception as e:
            print(f"Error during 2FA verification: {e}")

    with open('key.txt', 'r') as f:
        key = f.read().strip()
    key = bytes.fromhex(key)
    if len(key) != 32:
        raise ValueError("Key must be 32 bytes for AES-256")
    ciphertext = read_file('encrypted.bin')
    plaintext = aes_decrypt(ciphertext[16:], key, ciphertext[:16]) 
    write_file('decrypted.txt', plaintext)
