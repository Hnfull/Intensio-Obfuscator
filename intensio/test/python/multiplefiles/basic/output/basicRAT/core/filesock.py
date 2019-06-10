# -*- coding: utf-8 -*-
import socket
import struct
from crypto import rupicluuYAUuPXtZzzprBLFiIHrFbgdx
from crypto import sUdzqtLgbOHLwwhpgZAqnWQnkYcohXdZ
def sNdGHwfRcufgNuCsHbgAAzzPLlkgojAe(sock, XxPlchPxQLRKcdYmEIicQIuINeJVwooa, key):
    with open(XxPlchPxQLRKcdYmEIicQIuINeJVwooa, 'wb') as f:
        bUrBSsxqdDjYXzgJnUEEAyuytpumZjUD = struct.unpack("!I", sock.recv(4))[0]
        while bUrBSsxqdDjYXzgJnUEEAyuytpumZjUD:
            ELGQiDnmxWEsslqlSBSWoDiJsGWjlupQ = sock.recv(bUrBSsxqdDjYXzgJnUEEAyuytpumZjUD)
            f.write(sUdzqtLgbOHLwwhpgZAqnWQnkYcohXdZ(ELGQiDnmxWEsslqlSBSWoDiJsGWjlupQ, key))
            bUrBSsxqdDjYXzgJnUEEAyuytpumZjUD = struct.unpack("!I", sock.recv(4))[0]
def uwhiOqBSmedbvGGpKrsruHWAGHrUprFP(sock, XxPlchPxQLRKcdYmEIicQIuINeJVwooa, key):
    with open(XxPlchPxQLRKcdYmEIicQIuINeJVwooa, 'rb') as f:
        ELGQiDnmxWEsslqlSBSWoDiJsGWjlupQ = f.read(4096)
        while len(ELGQiDnmxWEsslqlSBSWoDiJsGWjlupQ):
            QxCEvpNeDCJqUGXGClaWuaowSeydgMTM = rupicluuYAUuPXtZzzprBLFiIHrFbgdx(ELGQiDnmxWEsslqlSBSWoDiJsGWjlupQ, key)
            sock.send(struct.pack("!I", len(QxCEvpNeDCJqUGXGClaWuaowSeydgMTM)))
            sock.send(QxCEvpNeDCJqUGXGClaWuaowSeydgMTM)
            ELGQiDnmxWEsslqlSBSWoDiJsGWjlupQ = f.read(4096)
        sock.send('\x00\x00\x00\x00')
