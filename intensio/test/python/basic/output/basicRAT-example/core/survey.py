# -*- coding: utf-8 -*-
import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid
def fRTWRMDwKMKaMMycbCQhFAtbEWeTzpNy(plat_type):
    ZLWFyQexObWDAVRgVOJuNGQAedCeFocT = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]
    oBrOxpWZDpabzaLkTAJesLGjPbBlFraK = getpass.getuser()
    uoirlwuHJEzzSfQmQybfeHjiQzoMBVIr    = socket.gethostname()
    zeWDOsIDNjfcOgoDtoXXwJAIcvanDOes        = socket.getfqdn()
    lmiVTKRFAoTwRlpedbOOJrmIRDOaQgUT = socket.gethostbyname(uoirlwuHJEzzSfQmQybfeHjiQzoMBVIr)
    mPhVbEQrhRtgorOCfJTSQasOGECJdpuM     = uuid.getnode()
    ZtEUSaviunQGzuUFvZAlKjoxXPcpqgyo         = ':'.join(("%012X" % mPhVbEQrhRtgorOCfJTSQasOGECJdpuM)[yUgtagPEWgZFwMNcuvyhbmhzBzVoIpvC:yUgtagPEWgZFwMNcuvyhbmhzBzVoIpvC+2] for yUgtagPEWgZFwMNcuvyhbmhzBzVoIpvC in range(0, 12, 2))
    IiaItVCmjDDlMxTgJAgMuMzOyIgjIbBu = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    OsDjBhrfbNqLuKrVSCwLTjvTugpKWiGJ = ''
    for NfoGrMlbvfpbjpDqKvyqgneTBRjEqipy in IiaItVCmjDDlMxTgJAgMuMzOyIgjIbBu:
        try:
            OsDjBhrfbNqLuKrVSCwLTjvTugpKWiGJ = urllib.urlopen('http://'+NfoGrMlbvfpbjpDqKvyqgneTBRjEqipy).read().rstrip()
        except IOError:
            pass
        if OsDjBhrfbNqLuKrVSCwLTjvTugpKWiGJ and (6 < len(OsDjBhrfbNqLuKrVSCwLTjvTugpKWiGJ) < 16):
            break
    uhfZDdczDpVwciBNRUKKQBRRJMADcVGe = False
    if plat_type.startswith('win'):
        uhfZDdczDpVwciBNRUKKQBRRJMADcVGe = ctypes.windll.shell32.IsUserAnAdmin() != 0
    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        uhfZDdczDpVwciBNRUKKQBRRJMADcVGe = os.getuid() == 0
    xsOwClbybXVQtKGYGvPInPMiscPpfWkZ = 'Yes' if uhfZDdczDpVwciBNRUKKQBRRJMADcVGe else 'No'
    xknplISuOFxzVrlhpVCqlAfQmvrfNmqg = '''
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
    '''.format(ZLWFyQexObWDAVRgVOJuNGQAedCeFocT, processor, architecture,
    uoirlwuHJEzzSfQmQybfeHjiQzoMBVIr, zeWDOsIDNjfcOgoDtoXXwJAIcvanDOes, lmiVTKRFAoTwRlpedbOOJrmIRDOaQgUT, OsDjBhrfbNqLuKrVSCwLTjvTugpKWiGJ, ZtEUSaviunQGzuUFvZAlKjoxXPcpqgyo, oBrOxpWZDpabzaLkTAJesLGjPbBlFraK, xsOwClbybXVQtKGYGvPInPMiscPpfWkZ)
    return xknplISuOFxzVrlhpVCqlAfQmvrfNmqg
