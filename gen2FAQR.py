import qrcode

url = "otpauth://totp/25CE_FinalDemo:liang.cs10%40nycu.edu.tw?secret=62JR3WMXFPZTYGLPAHLOA4OOKRQAOLKE&issuer=25CE_FinalDemo"

# Generate and save the QR code
img = qrcode.make(url)
img.save("2fa_qrcode.png")
print("QR code saved as 2fa_qrcode.png")