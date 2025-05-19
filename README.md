# 25CE_final

## Simulation CSE with AES and 2FA

This project demonstrates client-side encryption using AES-256 in CBC mode, with 2FA integration for added security.  
It is intended for educational purposes and simulates how encryption and decryption can be managed on the client side.

### Included Files

- `encry.py` — Encrypts a file (`input.txt`) using AES-256-CBC with a random IV and a key from `key.txt`.
- `decry2fa.py` — Decrypts the encrypted file (`encrypted.bin`) using the same key and IV, with optional 2FA logic.
- `key.txt` — Stores the AES-256 key in hex format.

---

## How It Works

### Encryption

1. Place the plaintext you want to encrypt in `input.txt`.
2. Run `encry.py`:
   - The script reads the key from `key.txt` .
   - It generates a random IV for each encryption.
   - The IV is prepended to the ciphertext and saved as `encrypted.bin`.

### Decryption

1. Run `decry2fa.py`:
   - The script reads the key from `key.txt`.
   - It extracts the IV from the first 16 bytes of `encrypted.bin`.
   - It decrypts the ciphertext and writes the result to `decrypted.txt`.
   - Optionally, 2FA logic can be enabled for additional verification.

---

## Security Notes

- **Key Security:**  
  The AES key is stored in `key.txt` as a hex string. Anyone with access to this file can decrypt your data.  
  For real-world use, never share or expose your encryption keys.

> we use key.txt to maintain the key for the convinence, since it just a simulation

- **IV Handling:**  
  Each encryption uses a new random IV, which is stored at the beginning of the encrypted file for proper decryption.

- **2FA Integration:**  
  The decryption script includes a placeholder for 2FA (using `pyotp`). You can expand this to require a valid 2FA code before allowing decryption.

---

## Requirements

- Python 3.x
- `cryptography` library
- `pyotp` library (for 2FA, optional)

Install dependencies with:

```bash
pip install cryptography pyotp
```

---

## Attribution

Some parts of this project and documentation were generated or assisted by GitHub Copilot.
