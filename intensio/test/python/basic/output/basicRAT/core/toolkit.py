# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def ndihMjdnlCHUtgTkZGHzGlSVbSpuIbXc(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to ndihMjdnlCHUtgTkZGHzGlSVbSpuIbXc file.'
    else:
        return 'Error: File not found.'
def IgrlqpfRMwQwXaaXwAPDNAbOXZIrvCcw(HiJzpfxOqMnOohWJImURiUzCtymUmfjZ):
    if not HiJzpfxOqMnOohWJImURiUzCtymUmfjZ.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj = HiJzpfxOqMnOohWJImURiUzCtymUmfjZ.split('/')[-1]
    if not wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj:
        wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(HiJzpfxOqMnOohWJImURiUzCtymUmfjZ, wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj)
