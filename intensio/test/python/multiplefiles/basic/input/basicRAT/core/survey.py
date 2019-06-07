# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import ctypes
import getpass
import os
import platform
import socket
import urllib
import uuid

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

def run(plat_type):
    # OS information
    sys_platform = platform.platform()
    processor    = platform.processor()
    architecture = platform.architecture()[0]

    # session information
    username = getpass.getuser()

    # network information
    hostname    = socket.gethostname()
    fqdn        = socket.getfqdn()
    internal_ip = socket.gethostbyname(hostname)
    raw_mac     = uuid.getnode()
    mac         = ':'.join(("%012X" % raw_mac)[i:i+2] for i in range(0, 12, 2))

    # get external ip address
    ex_ip_grab = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',
                   'ipecho.net/plain', 'myexternalip.com/raw' ]
    external_ip = ''
    for url in ex_ip_grab:
        try:
            external_ip = urllib.urlopen('http://'+url).read().rstrip()
        except IOError:
            pass
        if external_ip and (6 < len(external_ip) < 16):
            break

    # platform specific
    is_admin = False

    if plat_type.startswith('win'):
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0

    elif plat_type.startswith('linux') or platform.startswith('darwin'):
        is_admin = os.getuid() == 0

    admin_access = 'Yes' if is_admin else 'No'

    survey_results = '''
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
    '''.format(sys_platform, processor, architecture,
    hostname, fqdn, internal_ip, external_ip, mac, username, admin_access)

    return survey_results
