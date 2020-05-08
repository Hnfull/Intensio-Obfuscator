# -*- coding: utf-8 -*-
import socket
ycuSajaBjGeHsfYMFpMdBljhoNApuxoh = [ 
            21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
            514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888
]
def ZWGbjcQGpNPIRbBEIntiGRHypLrphsBH(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    CqLCFAGiFKpkaszSdjEiaizEkGPltyhw = ''
    for SNKtiLJIQqMCbBMmyfEurVwFeDorNnxo in ycuSajaBjGeHsfYMFpMdBljhoNApuxoh:
        KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        MHLubHXHCrSjxQtsTOTOAaDTaKyIabeg = KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.connect_ex((ip, SNKtiLJIQqMCbBMmyfEurVwFeDorNnxo))
        socket.setdefaulttimeout(0.5)
        FoguRKtWgnGafnCTCffcCYPrlYLkQrik = 'open' if not MHLubHXHCrSjxQtsTOTOAaDTaKyIabeg else 'closed'
        CqLCFAGiFKpkaszSdjEiaizEkGPltyhw += '{:>5}/tcp {:>7}\n'.format(SNKtiLJIQqMCbBMmyfEurVwFeDorNnxo, FoguRKtWgnGafnCTCffcCYPrlYLkQrik)
    return CqLCFAGiFKpkaszSdjEiaizEkGPltyhw.rstrip()
