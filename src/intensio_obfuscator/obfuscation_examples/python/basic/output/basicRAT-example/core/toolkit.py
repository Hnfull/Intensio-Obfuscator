# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def BCKwnkdhaeEKirDhgeLvQLbhwrLlyeGW(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to unzip file.'
    else:
        return 'Error: File not found.'
def heKCnAtKSPPzAttcFMAgPDiEOYCKLulX(cUxqDMTIZwVlTWebtlAhvJRWpxkRxQBs):
    if not cUxqDMTIZwVlTWebtlAhvJRWpxkRxQBs.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl = cUxqDMTIZwVlTWebtlAhvJRWpxkRxQBs.split('/')[-1]
    if not UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl:
        UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(cUxqDMTIZwVlTWebtlAhvJRWpxkRxQBs, UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(UPjPUktdPamGxNAzLwFyJdyGcAbiuDAl)
