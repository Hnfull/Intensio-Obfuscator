# -*- coding: utf-8 -*-
import socket
qMJttwSzSvHNeimvnDWIqxYvXDkxCfEk = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888 ]
def XIYCETtbzJrGxUAdNDRxrQdvVWmOeGVH(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV = ''
    for KaZhkkNQIEVRwMqpONxafexByNSuTpXs in qMJttwSzSvHNeimvnDWIqxYvXDkxCfEk:
        vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        fAqSmYdrvLveIGVfxAwdnKPQnbaEEfuB = vKjYJEdVkGFOUvjlozKKzKIFWxfRvDKr.connect_ex((ip, KaZhkkNQIEVRwMqpONxafexByNSuTpXs))
        socket.setdefaulttimeout(0.5)
        yfjSFbyNZiVrSoYOpEwTISLwXdTtpBpG = 'open' if not fAqSmYdrvLveIGVfxAwdnKPQnbaEEfuB else 'closed'
        DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV += '{:>5}/tcp {:>7}\n'.format(KaZhkkNQIEVRwMqpONxafexByNSuTpXs, yfjSFbyNZiVrSoYOpEwTISLwXdTtpBpG)
    return DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV.rstrip()
