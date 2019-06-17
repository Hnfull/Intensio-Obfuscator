# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def aAnySaDTFrVXxqOhcXWKpuTwfUztFFJf(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to aAnySaDTFrVXxqOhcXWKpuTwfUztFFJf file.'
    else:
        return 'Error: File not found.'
def KtDZzQzMQDKhLyiTMPXCGJIpFCkIiomn(RfcDgMPxKpienDtEZyWQZHLByHiyQcXl):
    if not RfcDgMPxKpienDtEZyWQZHLByHiyQcXl.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg = RfcDgMPxKpienDtEZyWQZHLByHiyQcXl.split('/')[-1]
    if not BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg:
        BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(RfcDgMPxKpienDtEZyWQZHLByHiyQcXl, BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg)
