# -*- coding: utf-8 -*-
import socket
import struct
from crypto import tVDmDmjQtBrNujmFMifjLQBPSaCrtfRc
from crypto import XqHWrremwBFsMYrDDXfxsCwsOQaHkIuZ
def oObhPcBxCTMcssEIlptmwgzCPHPiFSKF(sock, zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM, key):
    with open(zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM, 'wb') as f:
        OMnHTKyrBVkvDkXOPTnVdMgYbwBHtFkN = struct.unpack("!I", sock.recv(4))[0]
        while OMnHTKyrBVkvDkXOPTnVdMgYbwBHtFkN:
            XyQxqRICkoiwTzriAANqPzzKIOLXyPdp = sock.recv(OMnHTKyrBVkvDkXOPTnVdMgYbwBHtFkN)
            f.write(XqHWrremwBFsMYrDDXfxsCwsOQaHkIuZ(XyQxqRICkoiwTzriAANqPzzKIOLXyPdp, key))
            OMnHTKyrBVkvDkXOPTnVdMgYbwBHtFkN = struct.unpack("!I", sock.recv(4))[0]
def zNAZkysAqusNrAkwvlbriurTqUjGQrDM(sock, zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM, key):
    with open(zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM, 'rb') as f:
        XyQxqRICkoiwTzriAANqPzzKIOLXyPdp = f.read(4096)
        while len(XyQxqRICkoiwTzriAANqPzzKIOLXyPdp):
            NkTgCBfOQcSbNiQaEqpZbbopzfCetLWt = tVDmDmjQtBrNujmFMifjLQBPSaCrtfRc(XyQxqRICkoiwTzriAANqPzzKIOLXyPdp, key)
            sock.send(struct.pack("!I", len(NkTgCBfOQcSbNiQaEqpZbbopzfCetLWt)))
            sock.send(NkTgCBfOQcSbNiQaEqpZbbopzfCetLWt)
            XyQxqRICkoiwTzriAANqPzzKIOLXyPdp = f.read(4096)
        sock.send('\x00\x00\x00\x00')
