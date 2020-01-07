# -*- coding: utf-8 -*-
import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from common import int_to_bytestring, bytestring_to_int
FB_KEY = 'b14ce95fa4c33ac2803782d18341869f'
class PaddingError(Exception):
    pass
def pkcs7(s, bs=AES.block_size):
    i = (bs - (len(s) % bs))
    return s + (chr(i)*i)
def unpkcs7(s):
    i = s[-1]
    if s.endswith(i*ord(i)):
        return s[:-ord(i)]
    raise PaddingError("PKCS7 improper padding {}".format(repr(s[-32:])))
def diffiehellman(sock, server=True, bits=2048):
    p = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF;
    g = 2
    a = bytestring_to_int(os.urandom(32))
    xA = pow(g, a, p)
    if server:
        sock.send(int_to_bytestring(xA))
        b = bytestring_to_int(sock.recv(4096))
    else:
        b = bytestring_to_int(sock.recv(4096))
        sock.send(int_to_bytestring(xA))
    s = pow(b, a, p)
    return SHA256.new(int_to_bytestring(s)).digest()
def AES_encrypt(plaintext, KEY):
    plaintext = pkcs7(plaintext)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(plaintext)
def AES_decrypt(ciphertext, KEY):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return unpkcs7(plaintext)
