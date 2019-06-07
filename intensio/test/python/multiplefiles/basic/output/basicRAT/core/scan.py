# -*- coding: utf-8 -*-
import socket
jdjpvxAJKDYzoZCyhAcYOvltiaivTbqv = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888 ]
def GTNwDzYuHtAruxpPMVsjCisGlsWOQvoR(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO = ''
    for jumtownqyqZwmluxHsnMiRVGtzfFCykt in jdjpvxAJKDYzoZCyhAcYOvltiaivTbqv:
        WerXeVRoSuIOUzPqeUfRcYEiijTiROFb = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        oXhVhCSSOjtlOCjXibceugbxQjGOlbeQ = WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.connect_ex((ip, jumtownqyqZwmluxHsnMiRVGtzfFCykt))
        socket.setdefaulttimeout(0.5)
        EiSswZKVVCgLIrySRgbskdKfQGVFcNQV = 'open' if not oXhVhCSSOjtlOCjXibceugbxQjGOlbeQ else 'closed'
        WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO += '{:>5}/tcp {:>7}\n'.format(jumtownqyqZwmluxHsnMiRVGtzfFCykt, EiSswZKVVCgLIrySRgbskdKfQGVFcNQV)
    return WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO.rstrip()
