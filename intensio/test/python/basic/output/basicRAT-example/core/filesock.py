# -*- coding: utf-8 -*-
import socket
import struct
from crypto import jPZzsDfeiZRgNjrNBIlaUBIRWcGSUACw
from crypto import vTYSKuIhNxlSaaGMqczXnvvdSEyfcCaz
def yjQlCEghfMxsJwdmoDLBqnesZhMFoTtH(sock, FncUDhpNFnbFvciPnXtmEumcvADoZbpd, key):
    with open(FncUDhpNFnbFvciPnXtmEumcvADoZbpd, 'wb') as f:
        wrfmfPofnjEPTQiegThajFOEXiBVoePW = struct.unpack("!I", sock.recv(4))[0]
        while wrfmfPofnjEPTQiegThajFOEXiBVoePW:
            pZhgXVQDbEjdsRHIDYqoliHgjlprVcFO = sock.recv(wrfmfPofnjEPTQiegThajFOEXiBVoePW)
            f.write(vTYSKuIhNxlSaaGMqczXnvvdSEyfcCaz(pZhgXVQDbEjdsRHIDYqoliHgjlprVcFO, key))
            wrfmfPofnjEPTQiegThajFOEXiBVoePW = struct.unpack("!I", sock.recv(4))[0]
def LsEvOAVQPRUrrNvbBUQcKlyeWdlSoWyi(sock, FncUDhpNFnbFvciPnXtmEumcvADoZbpd, key):
    with open(FncUDhpNFnbFvciPnXtmEumcvADoZbpd, 'rb') as f:
        pZhgXVQDbEjdsRHIDYqoliHgjlprVcFO = f.read(4096)
        while len(pZhgXVQDbEjdsRHIDYqoliHgjlprVcFO):
            pKzVbVxoXGexagJwIbDETVAHTqkBkABN = jPZzsDfeiZRgNjrNBIlaUBIRWcGSUACw(pZhgXVQDbEjdsRHIDYqoliHgjlprVcFO, key)
            sock.send(struct.pack("!I", len(pKzVbVxoXGexagJwIbDETVAHTqkBkABN)))
            sock.send(pKzVbVxoXGexagJwIbDETVAHTqkBkABN)
            pZhgXVQDbEjdsRHIDYqoliHgjlprVcFO = f.read(4096)
        sock.send('\x00\x00\x00\x00')
