# -*- coding: utf-8 -*-
import socket
import struct
from crypto import aNZTYevmZkLIbpnXMxKrkTKZcOnrEXIu
from crypto import CkoyYDxmdvqmpDqmiDQfNmYJEooZuJfR
def CJaDqhybJXLaLvKovpVOBoslaLrUFgCi(sock, eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci, key):
    with open(eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci, 'wb') as f:
        laPYLZTnbxhHkeKDMXWOcaLlBxTdoGck = struct.unpack("!I", sock.recv(4))[0]
        while laPYLZTnbxhHkeKDMXWOcaLlBxTdoGck:
            OJAzmUdAkXgQjXzfXujXmtIzuolVdzDI = sock.recv(laPYLZTnbxhHkeKDMXWOcaLlBxTdoGck)
            f.write(CkoyYDxmdvqmpDqmiDQfNmYJEooZuJfR(OJAzmUdAkXgQjXzfXujXmtIzuolVdzDI, key))
            laPYLZTnbxhHkeKDMXWOcaLlBxTdoGck = struct.unpack("!I", sock.recv(4))[0]
def fwTVfMnsGkhBgXZUJprRUDzBlsiQfVQB(sock, eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci, key):
    with open(eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci, 'rb') as f:
        OJAzmUdAkXgQjXzfXujXmtIzuolVdzDI = f.read(4096)
        while len(OJAzmUdAkXgQjXzfXujXmtIzuolVdzDI):
            fhDuNdFRaJQXGoBMEVlyYvueRJeDsxrt = aNZTYevmZkLIbpnXMxKrkTKZcOnrEXIu(OJAzmUdAkXgQjXzfXujXmtIzuolVdzDI, key)
            sock.send(struct.pack("!I", len(fhDuNdFRaJQXGoBMEVlyYvueRJeDsxrt)))
            sock.send(fhDuNdFRaJQXGoBMEVlyYvueRJeDsxrt)
            OJAzmUdAkXgQjXzfXujXmtIzuolVdzDI = f.read(4096)
        sock.send('\x00\x00\x00\x00')
