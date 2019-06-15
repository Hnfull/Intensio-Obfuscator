# -*- coding: utf-8 -*-
import socket
uMYrgJWRDSuHOXPBYBxQfypLrqcShlOh = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888 ]
def qNmYcqkdDwIyTmsloXpVvavKuztOpfDt(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    YMGyjOPytDADCtQTHlvArJaBXhupfTQS = ''
    for xAjjXmPqxOqrzSvtOzBKwEqMKLHzWGeR in uMYrgJWRDSuHOXPBYBxQfypLrqcShlOh:
        CbHagqpBcIpeEWUyuBbobjCzudqKrPsR = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        huNvzEUyIZIZtvmfkMnatZTEOWeLcRsM = CbHagqpBcIpeEWUyuBbobjCzudqKrPsR.connect_ex((ip, xAjjXmPqxOqrzSvtOzBKwEqMKLHzWGeR))
        socket.setdefaulttimeout(0.5)
        IwyihucOXEbDmdmYUCCrHVfzfKinCHCY = 'open' if not huNvzEUyIZIZtvmfkMnatZTEOWeLcRsM else 'closed'
        YMGyjOPytDADCtQTHlvArJaBXhupfTQS += '{:>5}/tcp {:>7}\n'.format(xAjjXmPqxOqrzSvtOzBKwEqMKLHzWGeR, IwyihucOXEbDmdmYUCCrHVfzfKinCHCY)
    return YMGyjOPytDADCtQTHlvArJaBXhupfTQS.rstrip()
