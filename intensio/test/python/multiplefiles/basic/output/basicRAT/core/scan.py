# -*- coding: utf-8 -*-
import socket
DwhxaNsheqwjClrqeuggmWMOiZFzcjdM = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888 ]
def kVoQssmhUOQyeWHSppGMduiAtsJGjVOP(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    jLhewPiHvUwpJiUUvJccqlnCSUWejxGe = ''
    for vEBzwhTSayoOAkGLIqGTHpBbfSDubFjm in DwhxaNsheqwjClrqeuggmWMOiZFzcjdM:
        DZqtnqwIIAtdcrVFFphUANAFRUgKenqA = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ojmpErPdDPKBWqlUVBtPsrmyLuHaAenX = DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.connect_ex((ip, vEBzwhTSayoOAkGLIqGTHpBbfSDubFjm))
        socket.setdefaulttimeout(0.5)
        vGKoWJLWOethKDcOuWRDHRwNrMrspohZ = 'open' if not ojmpErPdDPKBWqlUVBtPsrmyLuHaAenX else 'closed'
        jLhewPiHvUwpJiUUvJccqlnCSUWejxGe += '{:>5}/tcp {:>7}\n'.format(vEBzwhTSayoOAkGLIqGTHpBbfSDubFjm, vGKoWJLWOethKDcOuWRDHRwNrMrspohZ)
    return jLhewPiHvUwpJiUUvJccqlnCSUWejxGe.rstrip()
