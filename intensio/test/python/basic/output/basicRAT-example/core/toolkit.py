# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def TVGWZMRKxoXpZYXviSTfzyVIwwSZWbme(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to TVGWZMRKxoXpZYXviSTfzyVIwwSZWbme file.'
    else:
        return 'Error: File not found.'
def gCaGLgrmWThFgtcraDJLXlyMiFiZhXtC(wZeKliJjXRYRdozBSSjHLXwmnkJyCXmR):
    if not wZeKliJjXRYRdozBSSjHLXwmnkJyCXmR.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz = wZeKliJjXRYRdozBSSjHLXwmnkJyCXmR.split('/')[-1]
    if not iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz:
        iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(wZeKliJjXRYRdozBSSjHLXwmnkJyCXmR, iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz)
