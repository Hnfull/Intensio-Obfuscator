# -*- coding: utf-8 -*-

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

# Convert an interger into a series of bytes
# A lightweight replacement for struck.pack()
def bytestring_to_int(bytes):
    i = 0
    while bytes:
        i = i << 8
        i += ord(bytes[-1])
        bytes = bytes[:-1]
    return i

# Convert a series of bytes into an integer
# A lightweight replacement for struck.unpack()
def int_to_bytestring(i):
    bs = ''
    while i:
        bs += chr(i & 0xff)
        i = i >> 8
    return bs
