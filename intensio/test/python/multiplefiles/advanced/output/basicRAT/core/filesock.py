# -*- coding: utf-8 -*-
import socket
import struct
from crypto import OIJlEMhoCyDUUoWtgCXOrvRTyaRVyTSL
from crypto import OOSQgYvTvpdkmeNosFwYWGwcjCXuPycq
def FTRyFOjSwbeSTWbxSIEtCfgDgehOccog(sock, bVVukzWmJjgiNMqVVxzEwyILHxHiIYtw, key):
    with open(bVVukzWmJjgiNMqVVxzEwyILHxHiIYtw, 'wb') as f:
        QepCDtOhUBJNXzbwcBydJLNEoLNTqBNW = struct.unpack("!I", sock.recv(4))[0]
        while QepCDtOhUBJNXzbwcBydJLNEoLNTqBNW:
            obwDTWGFVWXUAXMdBApNtmmsxHHopvJl = sock.recv(QepCDtOhUBJNXzbwcBydJLNEoLNTqBNW)
            f.write(OOSQgYvTvpdkmeNosFwYWGwcjCXuPycq(obwDTWGFVWXUAXMdBApNtmmsxHHopvJl, key))
            QepCDtOhUBJNXzbwcBydJLNEoLNTqBNW = struct.unpack("!I", sock.recv(4))[0]
def pUEBZcbXEzrESIqDVRRBfvrEtwjpOcEu(sock, bVVukzWmJjgiNMqVVxzEwyILHxHiIYtw, key):
    with open(bVVukzWmJjgiNMqVVxzEwyILHxHiIYtw, 'rb') as f:
        obwDTWGFVWXUAXMdBApNtmmsxHHopvJl = f.read(4096)
        while len(obwDTWGFVWXUAXMdBApNtmmsxHHopvJl):
            wjgIpIPNMkeTwJbzLSACdhjBNtsudcRw = OIJlEMhoCyDUUoWtgCXOrvRTyaRVyTSL(obwDTWGFVWXUAXMdBApNtmmsxHHopvJl, key)
            sock.send(struct.pack("!I", len(wjgIpIPNMkeTwJbzLSACdhjBNtsudcRw)))
            sock.send(wjgIpIPNMkeTwJbzLSACdhjBNtsudcRw)
            obwDTWGFVWXUAXMdBApNtmmsxHHopvJl = f.read(4096)
        sock.send('\x00\x00\x00\x00')
