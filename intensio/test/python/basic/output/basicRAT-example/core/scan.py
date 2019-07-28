# -*- coding: utf-8 -*-
import socket
HWXRGpmZWmswHmFskrlCXkwuUcVQcCHw = [
            21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
            514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888
]
def RFoEiiXZCSKDbavjQFTvIQdNPwqpFxYl(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD = ''
    for iROgVXHhEOVvgCxzLfIyfkpaQKVIRJkM in HWXRGpmZWmswHmFskrlCXkwuUcVQcCHw:
        AyZqbpGshExdUACZVcljMTjUuUSOeIyC = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        CdRlwYXEPPisULDeIlrFwanGtyMidoCn = AyZqbpGshExdUACZVcljMTjUuUSOeIyC.connect_ex((ip, iROgVXHhEOVvgCxzLfIyfkpaQKVIRJkM))
        socket.setdefaulttimeout(0.5)
        ZyFEGCfUcFCSHwpyTaMcQeGIYNMkPqRH = 'open' if not CdRlwYXEPPisULDeIlrFwanGtyMidoCn else 'closed'
        IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD += '{:>5}/tcp {:>7}\n'.format(iROgVXHhEOVvgCxzLfIyfkpaQKVIRJkM, ZyFEGCfUcFCSHwpyTaMcQeGIYNMkPqRH)
    return IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD.rstrip()
