# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def KfgGTgPuzocurWrNYsVgHYMbLmPIPMyF(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to KfgGTgPuzocurWrNYsVgHYMbLmPIPMyF file.'
    else:
        return 'Error: File not found.'
def KehMkcIWuqhhzGBYmDhABhFBbSUHTUGm(TnCnCsiQLaIdjlODStadLehhYvDLIORe):
    if not TnCnCsiQLaIdjlODStadLehhYvDLIORe.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM = TnCnCsiQLaIdjlODStadLehhYvDLIORe.split('/')[-1]
    if not zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM:
        zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(TnCnCsiQLaIdjlODStadLehhYvDLIORe, zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(zyPjVbORiUtMykNmPTGiQhVLHeNqfWTM)
