# -*- coding: utf-8 -*-
import socket
import struct
from crypto import ViGXFyDUMuRTyaLjdXDsFguYFLFKNZZW
from crypto import CeouyyhuFLsWInUrJoBdWRYPlFgaiRak
def yFFWnjJJUKgntESTvKXvkedPLbkUrxVc(sock, BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg, key):
    with open(BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg, 'wb') as f:
        XUduQHLtvwVQpPCxXwniqiUCUsJpZDCo = struct.unpack("!I", sock.recv(4))[0]
        while XUduQHLtvwVQpPCxXwniqiUCUsJpZDCo:
            EZNNHhROexgnNCKXCXEwJepwcJFNWNOZ = sock.recv(XUduQHLtvwVQpPCxXwniqiUCUsJpZDCo)
            f.write(CeouyyhuFLsWInUrJoBdWRYPlFgaiRak(EZNNHhROexgnNCKXCXEwJepwcJFNWNOZ, key))
            XUduQHLtvwVQpPCxXwniqiUCUsJpZDCo = struct.unpack("!I", sock.recv(4))[0]
def PeNHllDzashAnbpvjTvghjdRoEWXqpjx(sock, BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg, key):
    with open(BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg, 'rb') as f:
        EZNNHhROexgnNCKXCXEwJepwcJFNWNOZ = f.read(4096)
        while len(EZNNHhROexgnNCKXCXEwJepwcJFNWNOZ):
            ZspVoMThOtlIiwRRPOLIMZiTjdXQocZe = ViGXFyDUMuRTyaLjdXDsFguYFLFKNZZW(EZNNHhROexgnNCKXCXEwJepwcJFNWNOZ, key)
            sock.send(struct.pack("!I", len(ZspVoMThOtlIiwRRPOLIMZiTjdXQocZe)))
            sock.send(ZspVoMThOtlIiwRRPOLIMZiTjdXQocZe)
            EZNNHhROexgnNCKXCXEwJepwcJFNWNOZ = f.read(4096)
        sock.send('\x00\x00\x00\x00')
