# -*- coding: utf-8 -*-
import socket
import struct
from crypto import nWfpHMtglmECQdQYhOJEvgLDLAxncADh
from crypto import PVayTxzTsXuVHdaTbmvmjjKYIcPvDCfp
def VZMYYKflhhpoDVoMZpjdZXgOvFauOPCJ(sock, wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc, key):
    with open(wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc, 'wb') as f:
        lITlBDeIfXqYynyJbTqnIRbASFnvUgoF = struct.unpack("!I", sock.recv(4))[0]
        while lITlBDeIfXqYynyJbTqnIRbASFnvUgoF:
            JBIgvbqOXXVGAuoBCPmkbSCYowjjGPzc = sock.recv(lITlBDeIfXqYynyJbTqnIRbASFnvUgoF)
            f.write(PVayTxzTsXuVHdaTbmvmjjKYIcPvDCfp(JBIgvbqOXXVGAuoBCPmkbSCYowjjGPzc, key))
            lITlBDeIfXqYynyJbTqnIRbASFnvUgoF = struct.unpack("!I", sock.recv(4))[0]
def HzAjoiVYonBFgBOJBQkRmNoIKrnQyXOB(sock, wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc, key):
    with open(wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc, 'rb') as f:
        JBIgvbqOXXVGAuoBCPmkbSCYowjjGPzc = f.read(4096)
        while len(JBIgvbqOXXVGAuoBCPmkbSCYowjjGPzc):
            AFIoKFnYGLXVQPuqqfJQTJrYwsmcGrmq = nWfpHMtglmECQdQYhOJEvgLDLAxncADh(JBIgvbqOXXVGAuoBCPmkbSCYowjjGPzc, key)
            sock.send(struct.pack("!I", len(AFIoKFnYGLXVQPuqqfJQTJrYwsmcGrmq)))
            sock.send(AFIoKFnYGLXVQPuqqfJQTJrYwsmcGrmq)
            JBIgvbqOXXVGAuoBCPmkbSCYowjjGPzc = f.read(4096)
        sock.send('\x00\x00\x00\x00')
