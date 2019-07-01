# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def RbcepsCLJFdyLrfGPpeSTBlQPtvvVLEZ(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to RbcepsCLJFdyLrfGPpeSTBlQPtvvVLEZ file.'
    else:
        return 'Error: File not found.'
def rHHjbfnKBiRRdvWEKyKrcxfDJmjOAsAE(kZOAqfHfsupfmFHaHZnLDQEHpblqSUCA):
    if not kZOAqfHfsupfmFHaHZnLDQEHpblqSUCA.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE = kZOAqfHfsupfmFHaHZnLDQEHpblqSUCA.split('/')[-1]
    if not CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE:
        CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(kZOAqfHfsupfmFHaHZnLDQEHpblqSUCA, CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE)
