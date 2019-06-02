# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

from Crypto import Random
from Crypto.Cipher import AES

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

KEY = 'bbc2d6c74c06f3403f425b7b107c2a07'
# generate your own key with...
# python -c "import binascii, os; print(binascii.hexlify(os.urandom(16)))"

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Utils:
    def __init__(self):
        pass

    def Pad(self, s):
        return s + b'\0' * (AES.block_size - len(s) % AES.block_size)


    def Encrypt(self, plaintext):
        plaintext = Utils.Pad(self, plaintext)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        return iv + cipher.encrypt(plaintext)


    def Decrypt(self, ciphertext):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(KEY, AES.MODE_CBC, iv)
        plaintext = cipher.decrypt(ciphertext[AES.block_size:])
        return plaintext.rstrip(b'\0')
