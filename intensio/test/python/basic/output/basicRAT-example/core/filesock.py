# -*- coding: utf-8 -*-
import socket
import struct
from crypto import SKKkrmGLAJRDTUbwjJLaYtKBVMQbZzJS
from crypto import YRziRmEPPXlBbFMWPzvDXHZlVuNCrPBT
def WyerSerlsTFVDKVjjvmFBBWFhDZeEwrB(sock, GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb, key):
    with open(GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb, 'wb') as f:
        oUCArFtoAOMsNEMQfbBvLmbWRHZXoBxM = struct.unpack("!I", sock.recv(4))[0]
        while oUCArFtoAOMsNEMQfbBvLmbWRHZXoBxM:
            lpGVxvkkZIMgABNFjuQjvQTCcuTcQogC = sock.recv(oUCArFtoAOMsNEMQfbBvLmbWRHZXoBxM)
            f.write(YRziRmEPPXlBbFMWPzvDXHZlVuNCrPBT(lpGVxvkkZIMgABNFjuQjvQTCcuTcQogC, key))
            oUCArFtoAOMsNEMQfbBvLmbWRHZXoBxM = struct.unpack("!I", sock.recv(4))[0]
def mlagwFzeYdHITweNNECIpONaDpUVkCnW(sock, GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb, key):
    with open(GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb, 'rb') as f:
        lpGVxvkkZIMgABNFjuQjvQTCcuTcQogC = f.read(4096)
        while len(lpGVxvkkZIMgABNFjuQjvQTCcuTcQogC):
            CyyaRhBiJWukKxRsXbLBnDQNbkXfudWc = SKKkrmGLAJRDTUbwjJLaYtKBVMQbZzJS(lpGVxvkkZIMgABNFjuQjvQTCcuTcQogC, key)
            sock.send(struct.pack("!I", len(CyyaRhBiJWukKxRsXbLBnDQNbkXfudWc)))
            sock.send(CyyaRhBiJWukKxRsXbLBnDQNbkXfudWc)
            lpGVxvkkZIMgABNFjuQjvQTCcuTcQogC = f.read(4096)
        sock.send('\x00\x00\x00\x00')
