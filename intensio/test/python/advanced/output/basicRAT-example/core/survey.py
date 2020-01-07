# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def rfNCAgnAnRylAPIRGWkGlkRoAehDvsQR(plat_type):
    AIEmbPNdrgXRVbytDCaQacZsxCbHxWLJ = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    RQpoxrgLFDFzRqSHvKZnKuRpJJfijqFD = getpass.getuser()
    MNYcRgdKkVRNYqGPfAWlAgksjrOOMbzc    = socket.gethostname()
    kFpRIbmETKtXhCXJCaUMKazPhQnQGGTx        = socket.getfqdn()
    CIiXSJnmePSjkNSTcsIYINfLJuzPdlIo = socket.gethostbyname(MNYcRgdKkVRNYqGPfAWlAgksjrOOMbzc)
    TkpoJlTTizpVSpiBDijFbtFgLvgdBSib     = uuid.getnode()
    PdWQPrVakLSteFCzfYMGsmxiAZMtCJaU         = ':'.join(("%012X" % TkpoJlTTizpVSpiBDijFbtFgLvgdBSib)[fcUvUWvdMWjQzCEAElsAtioTqFjArjjm:fcUvUWvdMWjQzCEAElsAtioTqFjArjjm+2] for fcUvUWvdMWjQzCEAElsAtioTqFjArjjm in range(0, 12, 2))
    jrgAhUzsQgEhhLYgxhpWtCZDxCGFMDKQ = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    nuyEokaadRVNQWNwnyjemUABlDAzvNBu = ''
    for TnCnCsiQLaIdjlODStadLehhYvDLIORe in jrgAhUzsQgEhhLYgxhpWtCZDxCGFMDKQ:
        try:
            nuyEokaadRVNQWNwnyjemUABlDAzvNBu = urllib.urlopen('http://'+TnCnCsiQLaIdjlODStadLehhYvDLIORe).read().rstrip()
        except IOError:
            pass
        if nuyEokaadRVNQWNwnyjemUABlDAzvNBu and (6 < len(nuyEokaadRVNQWNwnyjemUABlDAzvNBu) < 16):
            break
    OqkKdeQDoZTEkfkNZkSjScvbbIoDDxBL = False
    if plat_type.startswith('win'):
        OqkKdeQDoZTEkfkNZkSjScvbbIoDDxBL = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        OqkKdeQDoZTEkfkNZkSjScvbbIoDDxBL = os.getuid() == 0
    icUGcNlKaZRtdhItmPEboHNaTJyoYNGL = 'Yes' if OqkKdeQDoZTEkfkNZkSjScvbbIoDDxBL else 'No'
    LpvBLEqFVpsnZAHkgOxORDBKcGMRQACn = '''
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
    '''.format(AIEmbPNdrgXRVbytDCaQacZsxCbHxWLJ, processor, architecture,
    MNYcRgdKkVRNYqGPfAWlAgksjrOOMbzc, kFpRIbmETKtXhCXJCaUMKazPhQnQGGTx, CIiXSJnmePSjkNSTcsIYINfLJuzPdlIo, nuyEokaadRVNQWNwnyjemUABlDAzvNBu, PdWQPrVakLSteFCzfYMGsmxiAZMtCJaU, RQpoxrgLFDFzRqSHvKZnKuRpJJfijqFD, icUGcNlKaZRtdhItmPEboHNaTJyoYNGL)
    return LpvBLEqFVpsnZAHkgOxORDBKcGMRQACn
