# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def unzip(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to unzip file.'
    else:
        return 'Error: File not found.'
def wget(url):
    if not url.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    fname = url.split('/')[-1]
    if not fname:
        fname = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(url, fname)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(fname)
