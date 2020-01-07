# -*- coding: utf-8 -*-
import socket
xQONpDMEWwdcyzsJfXAAyVNPnlhaJHjY = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888 ]
def MvZinykUruQJuVLuSfOSJrTlUqTbQNfH(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs = ''
    for WhMhEAwNvAgBYSXLYqiSKnSYegGyepgq in xQONpDMEWwdcyzsJfXAAyVNPnlhaJHjY:
        KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        HlApKzUAquWCmLOsWZSSEOdFcbwCFmHV = KEfKtinHjESFlEsKVSeKTfsUWJwRkCbx.connect_ex((ip, WhMhEAwNvAgBYSXLYqiSKnSYegGyepgq))
        socket.setdefaulttimeout(0.5)
        yIdqPvhytIwdRMVmagAsfYPVsNsxQKys = 'open' if not HlApKzUAquWCmLOsWZSSEOdFcbwCFmHV else 'closed'
        VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs += '{:>5}/tcp {:>7}\n'.format(WhMhEAwNvAgBYSXLYqiSKnSYegGyepgq, yIdqPvhytIwdRMVmagAsfYPVsNsxQKys)
    return VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs.rstrip()
