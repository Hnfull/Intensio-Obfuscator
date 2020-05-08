# -*- coding: utf-8 -*-
import socket
import struct
from crypto import NWRhKgbNSvkvMUDnFuZRlBpUMUnJgApy
from crypto import LTqWdFNAWGRrOFnEzPNXLrpSVbprqLyx
def CjLXxPxHYyQurzSYeNzJAXdgNVMivrcn(sock, RJJtPMsJNduwmrIJzEAYvWHbExNuMYns, key):
    with open(RJJtPMsJNduwmrIJzEAYvWHbExNuMYns, 'wb') as f:
        xWUVJxLHQCvmYskbxETZBTcGdZfNCrNO = struct.unpack("!I", sock.recv(4))[0]
        while xWUVJxLHQCvmYskbxETZBTcGdZfNCrNO:
            SnBtPOkvdRMvWamyNZpMsMiXvJpQzibE = sock.recv(xWUVJxLHQCvmYskbxETZBTcGdZfNCrNO)
            f.write(LTqWdFNAWGRrOFnEzPNXLrpSVbprqLyx(SnBtPOkvdRMvWamyNZpMsMiXvJpQzibE, key))
            xWUVJxLHQCvmYskbxETZBTcGdZfNCrNO = struct.unpack("!I", sock.recv(4))[0]
def HOhRIwHVlAgUqVdUvEaVGenLqGggxwgI(sock, RJJtPMsJNduwmrIJzEAYvWHbExNuMYns, key):
    with open(RJJtPMsJNduwmrIJzEAYvWHbExNuMYns, 'rb') as f:
        SnBtPOkvdRMvWamyNZpMsMiXvJpQzibE = f.read(4096)
        while len(SnBtPOkvdRMvWamyNZpMsMiXvJpQzibE):
            qHSnTmzFUYExFtYCxxInuFrHJbrizihL = NWRhKgbNSvkvMUDnFuZRlBpUMUnJgApy(SnBtPOkvdRMvWamyNZpMsMiXvJpQzibE, key)
            sock.send(struct.pack("!I", len(qHSnTmzFUYExFtYCxxInuFrHJbrizihL)))
            sock.send(qHSnTmzFUYExFtYCxxInuFrHJbrizihL)
            SnBtPOkvdRMvWamyNZpMsMiXvJpQzibE = f.read(4096)
        sock.send('\x00\x00\x00\x00')
