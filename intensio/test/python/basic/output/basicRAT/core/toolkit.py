# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def LlROorMFrfkrVzxGoecinHGGiVJxsTUb(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to LlROorMFrfkrVzxGoecinHGGiVJxsTUb file.'
    else:
        return 'Error: File not found.'
def AMDsKcNbycBNHxPhqStxinNymdVWAXZv(aSKDoeoDPvsurgPhQYutVFRhigeWgwQe):
    if not aSKDoeoDPvsurgPhQYutVFRhigeWgwQe.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    EaleibjntEwBrEGEpOACJgDqRDRDdRnP = aSKDoeoDPvsurgPhQYutVFRhigeWgwQe.split('/')[-1]
    if not EaleibjntEwBrEGEpOACJgDqRDRDdRnP:
        EaleibjntEwBrEGEpOACJgDqRDRDdRnP = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(aSKDoeoDPvsurgPhQYutVFRhigeWgwQe, EaleibjntEwBrEGEpOACJgDqRDRDdRnP)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(EaleibjntEwBrEGEpOACJgDqRDRDdRnP)
