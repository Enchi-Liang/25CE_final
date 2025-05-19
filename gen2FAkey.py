import pyotp

# Generate a random base32 secret for TOTP
secret = "62JR3WMXFPZTYGLPAHLOA4OOKRQAOLKE"

# Save the secret to FA2key.txt
with open('FA2key.txt', 'w') as f:
    f.write(secret)

# Generate a provisioning URI for Google Authenticator
issuer_name = "25CE_FinalDemo"
account_name = "liang.cs10@nycu.edu.tw"  # Change to your email or username
uri = pyotp.totp.TOTP(secret).provisioning_uri(name=account_name, issuer_name=issuer_name)

print("Your 2FA secret (add to your authenticator app):", secret)
print("Scan this QR code in Google Authenticator app:")
print(uri)
