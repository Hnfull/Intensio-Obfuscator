# -*- coding: utf-8 -*-
import socket
OVbfsErWjEGulsJIxHpHSYzISKXnKVgT = [ 
            21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
            514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888
]
def yShuNOqUqzALOCGCHoYOlDhwzZsDXaRP(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM = ''
    for EbeRdzCAZECWPggcgqfQTNGJQAHVkhaL in OVbfsErWjEGulsJIxHpHSYzISKXnKVgT:
        hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        YublEceJJOcxEjjMaUEGARYvmqzZuYbo = hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.connect_ex((ip, EbeRdzCAZECWPggcgqfQTNGJQAHVkhaL))
        socket.setdefaulttimeout(0.5)
        yYFPrPYJrvAJuvNOMithRgPDjVGBaGhG = 'open' if not YublEceJJOcxEjjMaUEGARYvmqzZuYbo else 'closed'
        UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM += '{:>5}/tcp {:>7}\n'.format(EbeRdzCAZECWPggcgqfQTNGJQAHVkhaL, yYFPrPYJrvAJuvNOMithRgPDjVGBaGhG)
    return UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM.rstrip()
