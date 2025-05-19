# Simulation CSE with AES and 2FA

25CE_final

This probject use aes and 2fa to simulate the client-side encryption
which contain 3 file:

- encry.py
- decry2fa.py
- key.txt

## AES File Encryption & Decryption

This project use simple scripts to encrypt and decrypt files using AES-256 in CBC mode.

### Usage

- **encrypt.py**  
  Encrypts `input.txt` using a fixed key form `key.txt` and random IV , and outputs `encrypted.bin`.  
  The IV is prepended to the ciphertext for use during decryption.

- **decry2fa.py**  
  Decrypts `encrypted.bin` using the same key form `key.txt` and the same IV, and outputs the result as `decrypted.txt`.

**Note:**  
Keep `key.txt` secure. Anyone with access to them can decrypt files

>we use key.txt to maintain the key for the convinence, since it just a simulation
