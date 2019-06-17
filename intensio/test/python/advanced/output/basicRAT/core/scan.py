# -*- coding: utf-8 -*-
import socket
GEQvebUOCvZgyUZLaOZbmoDtPAEluSHu = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888 ]
def MXharpYQHqoDolbKYeZNUbHCGorzssHg(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    XEkjNYcTbgvCEMvcoyVGQJSfnbMbZQjP = ''
    for PZwxtEhxIBMWmNPphOSinnBnZSiBAWjP in GEQvebUOCvZgyUZLaOZbmoDtPAEluSHu:
        NnAHEyzstOAhyDIxNvEBiZNNgIEkjaKT = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        tDKsbHzsrqscmFImbenCsRXqKwYJxXNG = NnAHEyzstOAhyDIxNvEBiZNNgIEkjaKT.connect_ex((ip, PZwxtEhxIBMWmNPphOSinnBnZSiBAWjP))
        socket.setdefaulttimeout(0.5)
        BwcRQJmLsUEVESwNqzSCSephmUVMpmxA = 'open' if not tDKsbHzsrqscmFImbenCsRXqKwYJxXNG else 'closed'
        XEkjNYcTbgvCEMvcoyVGQJSfnbMbZQjP += '{:>5}/tcp {:>7}\n'.format(PZwxtEhxIBMWmNPphOSinnBnZSiBAWjP, BwcRQJmLsUEVESwNqzSCSephmUVMpmxA)
    return XEkjNYcTbgvCEMvcoyVGQJSfnbMbZQjP.rstrip()
