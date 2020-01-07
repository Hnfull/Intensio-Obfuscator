# -*- coding: utf-8 -*-
def bytestring_to_int(bytes):
    i = 0
    while bytes:
        i = i << 8
        i += ord(bytes[-1])
        bytes = bytes[:-1]
    return i
def int_to_bytestring(i):
    bs = ''
    while i:
        bs += chr(i & 0xff)
        i = i >> 8
    return bs
