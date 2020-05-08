# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def mBuXjpkzrIUZngwxvXemPAvEUwbDTnHC(plat_type):
    mVuiaVOKTkPjfiJmLGQsCejdCEZjUnDZ = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    rdNISIBtrjsFvRQYIVpJoWixJrpaFzlo = getpass.getuser()
    jWZOvBfgpddVJpSNZTlBSNDcixXjDqwD    = socket.gethostname()
    vwAXQbCQseEKIUsTjrkiVhUhTrsYlVKW        = socket.getfqdn()
    JDEibbwXPIJLxKEXOdgRcCGrXuTAINQc = socket.gethostbyname(jWZOvBfgpddVJpSNZTlBSNDcixXjDqwD)
    UyHpNXcdSuLSBNzKxkuCLMcwXAtyqAGj     = uuid.getnode()
    uOfeibsqqOEeFEBzJOblXmIxsEFSxbgy         = ':'.join(("%012X" % UyHpNXcdSuLSBNzKxkuCLMcwXAtyqAGj)[GCUjyZRZOtbOdqlCfwkIcZIwUsqyTIGd:GCUjyZRZOtbOdqlCfwkIcZIwUsqyTIGd+2] for GCUjyZRZOtbOdqlCfwkIcZIwUsqyTIGd in range(0, 12, 2))
    gKdhOuXDgEuoqKJvnvxynAKTyaBScPoa = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    ySkGEXJIBVkcndIYMuKYhCmDfpYWdNPP = ''
    for tnnIJSfiTScARZZsGmguYEWsbqrjJmIp in gKdhOuXDgEuoqKJvnvxynAKTyaBScPoa:
        try:
            ySkGEXJIBVkcndIYMuKYhCmDfpYWdNPP = urllib.urlopen('http://'+tnnIJSfiTScARZZsGmguYEWsbqrjJmIp).read().rstrip()
        except IOError:
            pass
        if ySkGEXJIBVkcndIYMuKYhCmDfpYWdNPP and (6 < len(ySkGEXJIBVkcndIYMuKYhCmDfpYWdNPP) < 16):
            break
    JVdNpUrcdzzsCpMCnxQVfKgOiuGchXET = False
    if plat_type.startswith('win'):
        JVdNpUrcdzzsCpMCnxQVfKgOiuGchXET = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        JVdNpUrcdzzsCpMCnxQVfKgOiuGchXET = os.getuid() == 0
    EIxiwTzzBiZTZEYJgHvQonmtGQbSyQZi = 'Yes' if JVdNpUrcdzzsCpMCnxQVfKgOiuGchXET else 'No'
    aElOVWxvboeSrTxUhWGYaAnZRFoJWoRw = '''
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
    '''.format(mVuiaVOKTkPjfiJmLGQsCejdCEZjUnDZ, processor, architecture,
    jWZOvBfgpddVJpSNZTlBSNDcixXjDqwD, vwAXQbCQseEKIUsTjrkiVhUhTrsYlVKW, JDEibbwXPIJLxKEXOdgRcCGrXuTAINQc, ySkGEXJIBVkcndIYMuKYhCmDfpYWdNPP, uOfeibsqqOEeFEBzJOblXmIxsEFSxbgy, rdNISIBtrjsFvRQYIVpJoWixJrpaFzlo, EIxiwTzzBiZTZEYJgHvQonmtGQbSyQZi)
    return aElOVWxvboeSrTxUhWGYaAnZRFoJWoRw
