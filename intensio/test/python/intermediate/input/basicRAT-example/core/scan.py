# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import socket

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

PORTS = [ 
            21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
            514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888
]

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

def single_host(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'

    results = ''

    for p in PORTS:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        c = s.connect_ex((ip, p))
        socket.setdefaulttimeout(0.5)

        state = 'open' if not c else 'closed'

        results += '{:>5}/tcp {:>7}\n'.format(p, state)

    return results.rstrip()
