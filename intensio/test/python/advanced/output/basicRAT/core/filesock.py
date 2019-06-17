# -*- coding: utf-8 -*-
import socket
import struct
from crypto import yMJpVmADtfOFNuYBnBVUdcWvfJqpMgZu
from crypto import bWtlivskZCwkkAfMYrPiAvIokwvvoWcD
def OWpYpOpSPJpgHOwScrENXbxmAmIcFHCq(sock, JpJneYoLcVlbdMmeCofNRxOJuKxVLgyq, key):
    with open(JpJneYoLcVlbdMmeCofNRxOJuKxVLgyq, 'wb') as f:
        NaMHtvUnEmQGUsxKbBIYLXTtkNOIETsd = struct.unpack("!I", sock.recv(4))[0]
        while NaMHtvUnEmQGUsxKbBIYLXTtkNOIETsd:
            FxeyCWhPLTRwWiVvJEInJLIlhlTQfVwb = sock.recv(NaMHtvUnEmQGUsxKbBIYLXTtkNOIETsd)
            f.write(bWtlivskZCwkkAfMYrPiAvIokwvvoWcD(FxeyCWhPLTRwWiVvJEInJLIlhlTQfVwb, key))
            NaMHtvUnEmQGUsxKbBIYLXTtkNOIETsd = struct.unpack("!I", sock.recv(4))[0]
def jpcIoIirVbyQvKBDBSJylGVgqeBgwYWB(sock, JpJneYoLcVlbdMmeCofNRxOJuKxVLgyq, key):
    with open(JpJneYoLcVlbdMmeCofNRxOJuKxVLgyq, 'rb') as f:
        FxeyCWhPLTRwWiVvJEInJLIlhlTQfVwb = f.read(4096)
        while len(FxeyCWhPLTRwWiVvJEInJLIlhlTQfVwb):
            SgAKmSRLMvnWoeQUMnerkCbWQlgMCcYT = yMJpVmADtfOFNuYBnBVUdcWvfJqpMgZu(FxeyCWhPLTRwWiVvJEInJLIlhlTQfVwb, key)
            sock.send(struct.pack("!I", len(SgAKmSRLMvnWoeQUMnerkCbWQlgMCcYT)))
            sock.send(SgAKmSRLMvnWoeQUMnerkCbWQlgMCcYT)
            FxeyCWhPLTRwWiVvJEInJLIlhlTQfVwb = f.read(4096)
        sock.send('\x00\x00\x00\x00')
