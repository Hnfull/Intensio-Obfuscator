# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def ukJbTOkOxldunMGJEcZYdKLfaPaQYtMN(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to ukJbTOkOxldunMGJEcZYdKLfaPaQYtMN file.'
    else:
        return 'Error: File not found.'
def KDOPBQkyLfClRmcCUvOgwjlbjmpDAwWK(NfoGrMlbvfpbjpDqKvyqgneTBRjEqipy):
    if not NfoGrMlbvfpbjpDqKvyqgneTBRjEqipy.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    paCQjENnuYPVmljLLYILWWljITjDzepC = NfoGrMlbvfpbjpDqKvyqgneTBRjEqipy.split('/')[-1]
    if not paCQjENnuYPVmljLLYILWWljITjDzepC:
        paCQjENnuYPVmljLLYILWWljITjDzepC = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(NfoGrMlbvfpbjpDqKvyqgneTBRjEqipy, paCQjENnuYPVmljLLYILWWljITjDzepC)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(paCQjENnuYPVmljLLYILWWljITjDzepC)
