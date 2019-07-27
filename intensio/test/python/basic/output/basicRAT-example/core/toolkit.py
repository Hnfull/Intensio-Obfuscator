# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def ilIYRIhpPBvFVGhxFfVhANtrRkIfdoWp(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to ilIYRIhpPBvFVGhxFfVhANtrRkIfdoWp file.'
    else:
        return 'Error: File not found.'
def PxLarNPvrlTeRhjeFpMkbnGFraeCPfiQ(agiQWYdtFDyDNbELmUPwfeZwMrPuZFFh):
    if not agiQWYdtFDyDNbELmUPwfeZwMrPuZFFh.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb = agiQWYdtFDyDNbELmUPwfeZwMrPuZFFh.split('/')[-1]
    if not GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb:
        GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(agiQWYdtFDyDNbELmUPwfeZwMrPuZFFh, GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb)
