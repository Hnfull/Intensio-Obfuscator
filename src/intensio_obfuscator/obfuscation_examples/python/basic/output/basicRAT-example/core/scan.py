# -*- coding: utf-8 -*-
import socket
GOvcnVKDLMrnefakXmwjdWvNTmvmBaiz = [ 
            21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
            514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888
]
def kXXXRVfuUYZNQGSSpKiUekvTkBCiaQQG(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl = ''
    for qfLIwRNXQkYEhoERneZekXhtNSjaWdNN in GOvcnVKDLMrnefakXmwjdWvNTmvmBaiz:
        hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        KEcIztUGTeqTubwElcPWynqNSRjuxAhL = hZQTGxmzGJgpoqWsNisEnfYpjCARWJwY.connect_ex((ip, qfLIwRNXQkYEhoERneZekXhtNSjaWdNN))
        socket.setdefaulttimeout(0.5)
        cNRnqsGJiIXQNXmzxYYnetBlzAgytCpA = 'open' if not KEcIztUGTeqTubwElcPWynqNSRjuxAhL else 'closed'
        IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl += '{:>5}/tcp {:>7}\n'.format(qfLIwRNXQkYEhoERneZekXhtNSjaWdNN, cNRnqsGJiIXQNXmzxYYnetBlzAgytCpA)
    return IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl.rstrip()
