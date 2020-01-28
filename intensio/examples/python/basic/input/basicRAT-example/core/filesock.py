# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import socket
import struct

from crypto import AES_encrypt
from crypto import AES_decrypt

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

# recieve a file from a socket
def recvfile(sock, fname, key):
    with open(fname, 'wb') as f:
        datasize = struct.unpack("!I", sock.recv(4))[0]
        while datasize:
            res = sock.recv(datasize)
            f.write(AES_decrypt(res, key))
            datasize = struct.unpack("!I", sock.recv(4))[0]

# send a file over a socket
def sendfile(sock, fname, key):
    with open(fname, 'rb') as f:
        res = f.read(4096)
        while len(res):
            enc_res = AES_encrypt(res, key)
            sock.send(struct.pack("!I", len(enc_res)))
            sock.send(enc_res)
            res = f.read(4096)
        sock.send('\x00\x00\x00\x00') # EOF
