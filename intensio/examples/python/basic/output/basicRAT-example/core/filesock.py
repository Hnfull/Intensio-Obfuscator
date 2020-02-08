# -*- coding: utf-8 -*-
import socket
import struct
from crypto import gcbCoqAgZztElhuzHlCRVsaXiDmrxjeQ
from crypto import zcqgzrNhhMMrepGKrXzOYcYeaRymVspf
def uBnCzheoKMvSEYNltgSkBmyfdIkCfmLO(sock, wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf, key):
    with open(wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf, 'wb') as f:
        yeqInXQCMFiMwlGmMNxgJTlDAkJjqaup = struct.unpack("!I", sock.recv(4))[0]
        while yeqInXQCMFiMwlGmMNxgJTlDAkJjqaup:
            LRjqPUJHyCvrJOgrtmlXcRUkUETBgjbS = sock.recv(yeqInXQCMFiMwlGmMNxgJTlDAkJjqaup)
            f.write(zcqgzrNhhMMrepGKrXzOYcYeaRymVspf(LRjqPUJHyCvrJOgrtmlXcRUkUETBgjbS, key))
            yeqInXQCMFiMwlGmMNxgJTlDAkJjqaup = struct.unpack("!I", sock.recv(4))[0]
def OLxWjqoEVTGyIdmtAzGMiyvWpgJuSYVT(sock, wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf, key):
    with open(wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf, 'rb') as f:
        LRjqPUJHyCvrJOgrtmlXcRUkUETBgjbS = f.read(4096)
        while len(LRjqPUJHyCvrJOgrtmlXcRUkUETBgjbS):
            ZxinEtYCgnFwwsSwsIYdPLylbDOfMjZn = gcbCoqAgZztElhuzHlCRVsaXiDmrxjeQ(LRjqPUJHyCvrJOgrtmlXcRUkUETBgjbS, key)
            sock.send(struct.pack("!I", len(ZxinEtYCgnFwwsSwsIYdPLylbDOfMjZn)))
            sock.send(ZxinEtYCgnFwwsSwsIYdPLylbDOfMjZn)
            LRjqPUJHyCvrJOgrtmlXcRUkUETBgjbS = f.read(4096)
        sock.send('\x00\x00\x00\x00')
