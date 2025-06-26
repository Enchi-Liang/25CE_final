# 25CE_final

## Simulation CSE with AES and 2FA

This project demonstrates client-side encryption using AES-256 in CBC mode, combined with Two-Factor Authentication (2FA).
It is intended for educational purposes and simulates how encryption and decryption can be managed on the client side.

### 2025/6/26 update

113下 密碼工程 期末project.
成績:76/100 (含互評+助教評分?細節不清楚，佔學期總成績15%)
> 算合理的成績，畢竟做的挺簡陋、陽春(算一算大概不影響A+就放飛了)。


### Included Files

- `encry.py` — Encrypts a file (`input.txt`) using AES-256-CBC with a random IV and a key from `key.txt`.
- `decry2fa.py` — Decrypts the encrypted file (`encrypted.bin`) using the same key and IV, with optional 2FA logic.
- `genkey.py` — Generate random AES-256 key in hex format to `key.txt`.
- `gen2FAkey.py` —  Generates a TOTP 2FA secret, saves it to `FA2key.txt`, and prints a provisioning URL for Google Authenticator.
- `gen2FAQR.py` — Generates a QR code for the TOTP provisioning URL.
- `key.txt` — Stores the AES-256 key in hex format.
- `FA2key.txt` — Stores the 2FA key in hex format.
- `input.txt` — Stores the plaintext.

---

## Requirements

- Python 3.x
- `cryptography` library
- `pyotp` library (for 2FA, optional)
- `qrcode` library (for QR code generation)

Install dependencies with:

```bash
pip install cryptography pyotp qrcode[pil]
```

---

## How It Works

### Encryption

1. Place the plaintext you want to encrypt in `input.txt`.
2. Run `encry.py`:
   - The script reads the key from `key.txt` .
   - It generates a random IV for each encryption.
   - The IV is prepended to the ciphertext and saved as `encrypted.bin`.

### 2FA Setup

1. Run `gen2FAkey.py` to generate a new TOTP secret in `FA2key.txt` and print a provisioning URL.
    - > here is a fix secret in the file, just for convinence and demo.
1. (Optional) Run `gen2FAQR.py` to generate a QR code for the provisioning URL.
1. Add the secret to your authenticator app (e.g., Google Authenticator) by scanning the QR code or entering the secret manually.

### Decryption

1. Run `decry2fa.py`:
   - The script prompts for a 6-digit 2FA code from your authenticator app.
   - It reads the key from `key.txt` and the TOTP secret from `FA2key.txt`.
   - It extracts the IV from the first 16 bytes of `encrypted.bin`.
   - It decrypts the ciphertext and writes the result to `decrypted.txt`.
   - Decryption only proceeds if the 2FA code is valid.

---

## Security Notes

- **Key Security:**  
  The AES key is stored in `key.txt` as a hex string. Anyone with access to this file can decrypt your data.
  Also, The 2FA integration stored in `FA2key.txt` as a hex string. Anyone with access to this file can decrypt your data.
  For real-world use, never share or expose your encryption keys.

> we use `key.txt` , `FA2key.txt` to maintain the key for the convinence, since it just a simulation.
> Also, in this way can prevent the hack form the software.

- **IV Handling:**  
  Each encryption uses a new random IV, which is stored at the beginning of the encrypted file for proper decryption.

- **2FA Integration:**  
  The decryption script requires a valid 2FA code, adding an extra layer of security.

---

## Attribution

Some parts of this project were generated or assisted by GitHub Copilot.
