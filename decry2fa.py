import cryptography 
import os
import pyotp


def totp():
    '''
    check if the key is valid
    '''
    totp = pyotp.TOTP(key)
    return totp.verify(key)


'''
ask the key from user (the 6 key from 2 fa )
'''

flag_2fa = False
while flag_2fa == False:
    if len(key) == 6 and key.isdigit() and totp(flag_2fa):
        flag_2fa = True
    else:
        print("Please enter a valid 6 digit key")
        key = input("Key: ")



'''
aes decrypt
'''





'''
output decrypted file
'''