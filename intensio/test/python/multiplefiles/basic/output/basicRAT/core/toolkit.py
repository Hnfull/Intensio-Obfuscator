# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def RhnTmTNQqHkoWkxISbScOYnmfkMKbIBB(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to RhnTmTNQqHkoWkxISbScOYnmfkMKbIBB file.'
    else:
        return 'Error: File not found.'
def hBwkweoTQVWRFtCiQwUrBWIrKqSmTGBP(ZdbdDcxafJkxVIFzvgrdCYAolZNpzPnH):
    if not ZdbdDcxafJkxVIFzvgrdCYAolZNpzPnH.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    XxPlchPxQLRKcdYmEIicQIuINeJVwooa = ZdbdDcxafJkxVIFzvgrdCYAolZNpzPnH.split('/')[-1]
    if not XxPlchPxQLRKcdYmEIicQIuINeJVwooa:
        XxPlchPxQLRKcdYmEIicQIuINeJVwooa = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(ZdbdDcxafJkxVIFzvgrdCYAolZNpzPnH, XxPlchPxQLRKcdYmEIicQIuINeJVwooa)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(XxPlchPxQLRKcdYmEIicQIuINeJVwooa)
