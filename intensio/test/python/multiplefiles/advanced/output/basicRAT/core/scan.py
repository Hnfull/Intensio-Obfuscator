# -*- coding: utf-8 -*-
import socket
XXtGjKuvDEiBlVquLzWMgzcsySivLDpvYdBcGtAAfXoDLApSvkGVyavRjUaUSawheiHydDITkhFdnMdlkkcBahpCYOpgmqrdOuoMtLkwYZeFzhuTFIhRefjfzJHgapLY = [ 21, 22, 23, 25, 53, 80, 110, 111, 135, 139, 143, 179, 443, 445,
514, 993, 995, 1723, 3306, 3389, 5900, 8000, 8080, 8443, 8888 ]
def akGhgWAsrNerlMRUvIFHcflRklhewuUkzYqkvLBNozlsVOkjxFtRxDaktuwICXcGikXNeGvqeJqjuRduBIiziSZMlxTdCEvZNTJqcvgWekorQqrSvwepGqMtoGWnQWik(ip):
    try:
        socket.inet_aton(ip)
    except socket.error:
        return 'Error: Invalid IP address.'
    hIDFGYuVpbaIlxViLvqgIbIhkiJmTzZsHHwUmubDjlevLrijuHkpHdrTAmglOhTqJXVlswyPadMDgfWCCpSQeROrDWrqLxksbVwYUvrIscTLXbDjkbavjEXnKSIBtZOe = ''
    for gEEircvGZhRpwhbwyXIDrXNgmSKbLIKkcrzeoWRMPLligXdxgWNPVkjtRrdswHYKVsHNpPNdbgExIwluHeBXbLxIVVDoosLsTyREMaxHwERugpGFxdtUnvbDDtyAIDip in XXtGjKuvDEiBlVquLzWMgzcsySivLDpvYdBcGtAAfXoDLApSvkGVyavRjUaUSawheiHydDITkhFdnMdlkkcBahpCYOpgmqrdOuoMtLkwYZeFzhuTFIhRefjfzJHgapLY:
        lvzYufOIGLgYmTgPhpuVtPMleHAdfHtsSoNEIStJktyHOYEToPvxnOiTvbAMRhwcVvJeXVdfEOrVidAeHVmtnsPLVsaPsFfngCCvDcZUHveyaOmAbCUiMrJBtTUnPIfH = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        IgyQmaPRLNzlTvGjIxOKlTDYkafJHqLBHCfiHmdssGhuXujUeqVrntUkGyjhDRyEIVWXkCmNpbGVguJmaSQAeZgIOntcfNNFmGQYWKoEbtnJdKCFYCTjzHWQbNcTMKXF = lvzYufOIGLgYmTgPhpuVtPMleHAdfHtsSoNEIStJktyHOYEToPvxnOiTvbAMRhwcVvJeXVdfEOrVidAeHVmtnsPLVsaPsFfngCCvDcZUHveyaOmAbCUiMrJBtTUnPIfH.connect_ex((ip, gEEircvGZhRpwhbwyXIDrXNgmSKbLIKkcrzeoWRMPLligXdxgWNPVkjtRrdswHYKVsHNpPNdbgExIwluHeBXbLxIVVDoosLsTyREMaxHwERugpGFxdtUnvbDDtyAIDip))
        socket.setdefaulttimeout(0.5)
        VhUNUjLNJIMoBqcuABmziwqlFLtJQoPBBtQsdWTDPyylbkOszyLNEjPvztsNGkXlZZrHTLUtxhcEkUujJjciVJwTfjQpUMOJHyZZYXHPTNWvCpsDIiILSsgVhmlkZoze = 'open' if not IgyQmaPRLNzlTvGjIxOKlTDYkafJHqLBHCfiHmdssGhuXujUeqVrntUkGyjhDRyEIVWXkCmNpbGVguJmaSQAeZgIOntcfNNFmGQYWKoEbtnJdKCFYCTjzHWQbNcTMKXF else 'closed'
        hIDFGYuVpbaIlxViLvqgIbIhkiJmTzZsHHwUmubDjlevLrijuHkpHdrTAmglOhTqJXVlswyPadMDgfWCCpSQeROrDWrqLxksbVwYUvrIscTLXbDjkbavjEXnKSIBtZOe += '{:>5}/tcp {:>7}\n'.format(gEEircvGZhRpwhbwyXIDrXNgmSKbLIKkcrzeoWRMPLligXdxgWNPVkjtRrdswHYKVsHNpPNdbgExIwluHeBXbLxIVVDoosLsTyREMaxHwERugpGFxdtUnvbDDtyAIDip, VhUNUjLNJIMoBqcuABmziwqlFLtJQoPBBtQsdWTDPyylbkOszyLNEjPvztsNGkXlZZrHTLUtxhcEkUujJjciVJwTfjQpUMOJHyZZYXHPTNWvCpsDIiILSsgVhmlkZoze)
    return hIDFGYuVpbaIlxViLvqgIbIhkiJmTzZsHHwUmubDjlevLrijuHkpHdrTAmglOhTqJXVlswyPadMDgfWCCpSQeROrDWrqLxksbVwYUvrIscTLXbDjkbavjEXnKSIBtZOe.rstrip()
