# -*- coding: utf-8 -*-
import socket
YCjKzWkANMqdaXiSLSpFrloaGYqLeDgS = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888 ]
def eAOPXLqeIRVTvCYSGAofEFfYvLiVtZNL(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    xmEHmdwPzUStwSwmNfSpKeYWgMQDiyLb = ''
    for wYEJqwDMunOyDEMToZxMnkddFvWYXsFD in YCjKzWkANMqdaXiSLSpFrloaGYqLeDgS:
        KLBoUVtzkpdvINqmcTAkJDqOArHeoAwi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        RaRAhKaXFuBUkWSffajyoUGreJvXWIJv = KLBoUVtzkpdvINqmcTAkJDqOArHeoAwi.connect_ex((ip, wYEJqwDMunOyDEMToZxMnkddFvWYXsFD))
        socket.setdefaulttimeout(0.5)
        KIZpojRgKeDRYKswCRAxNqncvoLQmFhV = 'open' if not RaRAhKaXFuBUkWSffajyoUGreJvXWIJv else 'closed'
        xmEHmdwPzUStwSwmNfSpKeYWgMQDiyLb += '{:>5}/tcp {:>7}\n'.format(wYEJqwDMunOyDEMToZxMnkddFvWYXsFD, KIZpojRgKeDRYKswCRAxNqncvoLQmFhV)
    return xmEHmdwPzUStwSwmNfSpKeYWgMQDiyLb.rstrip()
