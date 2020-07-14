# -*- coding: utf-8 -*-
import socket
import struct
from crypto import tWFjgkigGlBgJzJuDPvNFxkOVaoVHkvq
from crypto import fKVDYrzdKZVcijwKGIciPJNJhgUGEXQd
def rmKLLEJCqgoJgOaymQmnoOotvYFjGJwt(sock, UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl, key):
    with open(UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl, 'wb') as f:
        KYUImcrJiPUjfQKtQfklTtycuICqXNuh = struct.unpack("!I", sock.recv(4))[0]
        while KYUImcrJiPUjfQKtQfklTtycuICqXNuh:
            awEejdcpwWhFYAGkieRMfqYBAgnjGzYU = sock.recv(KYUImcrJiPUjfQKtQfklTtycuICqXNuh)
            f.write(fKVDYrzdKZVcijwKGIciPJNJhgUGEXQd(awEejdcpwWhFYAGkieRMfqYBAgnjGzYU, key))
            KYUImcrJiPUjfQKtQfklTtycuICqXNuh = struct.unpack("!I", sock.recv(4))[0]
def gKBMfnwhSSxqoYgKzwEAFFmdZUXetvKm(sock, UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl, key):
    with open(UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl, 'rb') as f:
        awEejdcpwWhFYAGkieRMfqYBAgnjGzYU = f.read(4096)
        while len(awEejdcpwWhFYAGkieRMfqYBAgnjGzYU):
            XadHKpkQklBjaRoXDUvlQtFXFfMdzsVW = tWFjgkigGlBgJzJuDPvNFxkOVaoVHkvq(awEejdcpwWhFYAGkieRMfqYBAgnjGzYU, key)
            sock.send(struct.pack("!I", len(XadHKpkQklBjaRoXDUvlQtFXFfMdzsVW)))
            sock.send(XadHKpkQklBjaRoXDUvlQtFXFfMdzsVW)
            awEejdcpwWhFYAGkieRMfqYBAgnjGzYU = f.read(4096)
        sock.send('\x00\x00\x00\x00') 
