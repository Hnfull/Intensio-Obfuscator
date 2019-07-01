# -*- coding: utf-8 -*-
import socket
GEWjXbeeKxmaTjNwkMVhkYRserXlsCIr = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888 ]
def UwJJCZSPlkHSnmZsJzoLdcCgHWoExiro(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv = ''
    for ZSJpsSjHtBSoaVmoZQKZRaSwOtvwBfby in GEWjXbeeKxmaTjNwkMVhkYRserXlsCIr:
        VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        vsYAsZMfGAodinpWnIQLxZyehzXjVKlr = VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.connect_ex((ip, ZSJpsSjHtBSoaVmoZQKZRaSwOtvwBfby))
        socket.setdefaulttimeout(0.5)
        qiawrtCpHsERSobFzVgBwpumthRXOqbP = 'open' if not vsYAsZMfGAodinpWnIQLxZyehzXjVKlr else 'closed'
        wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv += '{:>5}/tcp {:>7}\n'.format(ZSJpsSjHtBSoaVmoZQKZRaSwOtvwBfby, qiawrtCpHsERSobFzVgBwpumthRXOqbP)
    return wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv.rstrip()
