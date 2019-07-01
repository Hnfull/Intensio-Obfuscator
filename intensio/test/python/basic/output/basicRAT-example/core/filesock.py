# -*- coding: utf-8 -*-
import socket
import struct
from crypto import ZpfOVTDDOGytHjPnbATuBExgLHZMDMoS
from crypto import XYaDaLCpdDWbhHDijfqwaNYabStIUUmh
def WxGcwiPDYRLzbqatyPwfpKjEErHxBDJt(sock, CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE, key):
    with open(CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE, 'wb') as f:
        JClySHBJdvvyVLhzDCwcaogWfTndAmAL = struct.unpack("!I", sock.recv(4))[0]
        while JClySHBJdvvyVLhzDCwcaogWfTndAmAL:
            OdSgDwhUViOzBUiUXsWgQNSyUWJFEFte = sock.recv(JClySHBJdvvyVLhzDCwcaogWfTndAmAL)
            f.write(XYaDaLCpdDWbhHDijfqwaNYabStIUUmh(OdSgDwhUViOzBUiUXsWgQNSyUWJFEFte, key))
            JClySHBJdvvyVLhzDCwcaogWfTndAmAL = struct.unpack("!I", sock.recv(4))[0]
def kQpMdhVtDbXGIdiCoexmQnzVVIsSBSlE(sock, CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE, key):
    with open(CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE, 'rb') as f:
        OdSgDwhUViOzBUiUXsWgQNSyUWJFEFte = f.read(4096)
        while len(OdSgDwhUViOzBUiUXsWgQNSyUWJFEFte):
            qXSSDGARwfxGyLnmFgDfGruRhZrnfLhb = ZpfOVTDDOGytHjPnbATuBExgLHZMDMoS(OdSgDwhUViOzBUiUXsWgQNSyUWJFEFte, key)
            sock.send(struct.pack("!I", len(qXSSDGARwfxGyLnmFgDfGruRhZrnfLhb)))
            sock.send(qXSSDGARwfxGyLnmFgDfGruRhZrnfLhb)
            OdSgDwhUViOzBUiUXsWgQNSyUWJFEFte = f.read(4096)
        sock.send('\x00\x00\x00\x00')
