# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def azYcCKZXPAlsEILbtinhYEYbdmYFLcdm(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to azYcCKZXPAlsEILbtinhYEYbdmYFLcdm file.'
    else:
        return 'Error: File not found.'
def buyFmCSWGTBfvISGQIWFLtElgktcqpgK(sUaJfpOuQuvOLAxfuwahzntNPiPrbwxU):
    if not sUaJfpOuQuvOLAxfuwahzntNPiPrbwxU.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf = sUaJfpOuQuvOLAxfuwahzntNPiPrbwxU.split('/')[-1]
    if not wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf:
        wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(sUaJfpOuQuvOLAxfuwahzntNPiPrbwxU, wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(wqTNCoDdwbmUDUzLKwPqhjHcwrTXTbnf)
