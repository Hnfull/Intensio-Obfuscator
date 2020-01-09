# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def YqJAJWVCKIQnzKVFYIFbwvGyLEHkdSzJ(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to YqJAJWVCKIQnzKVFYIFbwvGyLEHkdSzJ file.'
    else:
        return 'Error: File not found.'
def IqKsJvdgDmUmoQnjYBwqdobWQbQIsuSB(YVUdGVfPLuGahYVogiZwNjGiGgGkIegS):
    if not YVUdGVfPLuGahYVogiZwNjGiGgGkIegS.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    FncUDhpNFnbFvciPnXtmEumcvADoZbpd = YVUdGVfPLuGahYVogiZwNjGiGgGkIegS.split('/')[-1]
    if not FncUDhpNFnbFvciPnXtmEumcvADoZbpd:
        FncUDhpNFnbFvciPnXtmEumcvADoZbpd = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(YVUdGVfPLuGahYVogiZwNjGiGgGkIegS, FncUDhpNFnbFvciPnXtmEumcvADoZbpd)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(FncUDhpNFnbFvciPnXtmEumcvADoZbpd)
