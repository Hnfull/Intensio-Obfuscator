# -*- coding: utf-8 -*-
import socket
import struct
from crypto import atPheiSoAtFBPAPiSWphKMBoMpifCYtC
from crypto import JwCsVFlvwSXxzwZKpzKYaxboNPDvwiug
def KbuhTZtIvVSBvshIvIaoAxspIPzFrRTF(sock, EaleibjntEwBrEGEpOACJgDqRDRDdRnP, key):
    with open(EaleibjntEwBrEGEpOACJgDqRDRDdRnP, 'wb') as f:
        bsxpUGsuqUvPEeZYyipFSzhjZizFJybT = struct.unpack("!I", sock.recv(4))[0]
        while bsxpUGsuqUvPEeZYyipFSzhjZizFJybT:
            AYItGRPvIgkPHMVNQExgSHDqPqaMwOWs = sock.recv(bsxpUGsuqUvPEeZYyipFSzhjZizFJybT)
            f.write(JwCsVFlvwSXxzwZKpzKYaxboNPDvwiug(AYItGRPvIgkPHMVNQExgSHDqPqaMwOWs, key))
            bsxpUGsuqUvPEeZYyipFSzhjZizFJybT = struct.unpack("!I", sock.recv(4))[0]
def uNZFEeimqaxXIxuHxoqgUngTOwwhLTrZ(sock, EaleibjntEwBrEGEpOACJgDqRDRDdRnP, key):
    with open(EaleibjntEwBrEGEpOACJgDqRDRDdRnP, 'rb') as f:
        AYItGRPvIgkPHMVNQExgSHDqPqaMwOWs = f.read(4096)
        while len(AYItGRPvIgkPHMVNQExgSHDqPqaMwOWs):
            BnOLjgHzPdpgNeSiHHGMGrLiMVoeHVGp = atPheiSoAtFBPAPiSWphKMBoMpifCYtC(AYItGRPvIgkPHMVNQExgSHDqPqaMwOWs, key)
            sock.send(struct.pack("!I", len(BnOLjgHzPdpgNeSiHHGMGrLiMVoeHVGp)))
            sock.send(BnOLjgHzPdpgNeSiHHGMGrLiMVoeHVGp)
            AYItGRPvIgkPHMVNQExgSHDqPqaMwOWs = f.read(4096)
        sock.send('\x00\x00\x00\x00')
