# -*- coding: utf-8 -*-
import socket
import struct
from crypto import OKSupbNTJNKeVNXuKbkkfKZkGSEpfkGZ
from crypto import PCIXrYBHgUfcWimMNwcVTszRyHYsbXNo
def ZtWixuDXDhaMQOEglQBRYVZQGcktUJMs(sock, ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd, key):
    with open(ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd, 'wb') as f:
        vAPgzCKekcbgYopsXtoRHHZDGFRVnksK = struct.unpack("!I", sock.recv(4))[0]
        while vAPgzCKekcbgYopsXtoRHHZDGFRVnksK:
            ffaUkAqHMlWyxurEkOziyHsJecvgNTSj = sock.recv(vAPgzCKekcbgYopsXtoRHHZDGFRVnksK)
            f.write(PCIXrYBHgUfcWimMNwcVTszRyHYsbXNo(ffaUkAqHMlWyxurEkOziyHsJecvgNTSj, key))
            vAPgzCKekcbgYopsXtoRHHZDGFRVnksK = struct.unpack("!I", sock.recv(4))[0]
def WFREbbdnIuOOJMStvqQujEfaBoFJDwWU(sock, ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd, key):
    with open(ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd, 'rb') as f:
        ffaUkAqHMlWyxurEkOziyHsJecvgNTSj = f.read(4096)
        while len(ffaUkAqHMlWyxurEkOziyHsJecvgNTSj):
            JOQqjbMmireQWqOVeWtCxopobyaiIxtz = OKSupbNTJNKeVNXuKbkkfKZkGSEpfkGZ(ffaUkAqHMlWyxurEkOziyHsJecvgNTSj, key)
            sock.send(struct.pack("!I", len(JOQqjbMmireQWqOVeWtCxopobyaiIxtz)))
            sock.send(JOQqjbMmireQWqOVeWtCxopobyaiIxtz)
            ffaUkAqHMlWyxurEkOziyHsJecvgNTSj = f.read(4096)
        sock.send('\x00\x00\x00\x00')
