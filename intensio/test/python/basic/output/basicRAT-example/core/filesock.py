# -*- coding: utf-8 -*-
import socket
import struct
from crypto import LQOdRjWyVheTJCytAXEImYNlfGEClgVr
from crypto import xYJEIEJwYxrIrxmzUDOdGnbQaPoRNnfl
def HbceFmYOVWlodQwVoWSxMaMBMGxoEetP(sock, iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz, key):
    with open(iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz, 'wb') as f:
        txTFAUdkMFlMrPgxIXNmXDECGyzWXEtV = struct.unpack("!I", sock.recv(4))[0]
        while txTFAUdkMFlMrPgxIXNmXDECGyzWXEtV:
            QnytXfvdxMiEIifxQWXgJSaVFmfalJfv = sock.recv(txTFAUdkMFlMrPgxIXNmXDECGyzWXEtV)
            f.write(xYJEIEJwYxrIrxmzUDOdGnbQaPoRNnfl(QnytXfvdxMiEIifxQWXgJSaVFmfalJfv, key))
            txTFAUdkMFlMrPgxIXNmXDECGyzWXEtV = struct.unpack("!I", sock.recv(4))[0]
def asXVMcyVvbVzovqlkrejIEPWhlhIaWVQ(sock, iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz, key):
    with open(iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz, 'rb') as f:
        QnytXfvdxMiEIifxQWXgJSaVFmfalJfv = f.read(4096)
        while len(QnytXfvdxMiEIifxQWXgJSaVFmfalJfv):
            YGKUZlcAHJNDjoKPdvBbmTLcDWFlKhRc = LQOdRjWyVheTJCytAXEImYNlfGEClgVr(QnytXfvdxMiEIifxQWXgJSaVFmfalJfv, key)
            sock.send(struct.pack("!I", len(YGKUZlcAHJNDjoKPdvBbmTLcDWFlKhRc)))
            sock.send(YGKUZlcAHJNDjoKPdvBbmTLcDWFlKhRc)
            QnytXfvdxMiEIifxQWXgJSaVFmfalJfv = f.read(4096)
        sock.send('\x00\x00\x00\x00')
