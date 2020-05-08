# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def NOUxdzmQvSpxotaVTzRAjYSvXjAxlOVW(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to unzip file.'
    else:
        return 'Error: File not found.'
def MDtVRFxrOMzieeGphIeylKeAqJfuDFSb(tnnIJSfiTScARZZsGmguYEWsbqrjJmIp):
    if not tnnIJSfiTScARZZsGmguYEWsbqrjJmIp.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    RJJtPMsJNduwmrIJzEAYvWHbExNuMYns = tnnIJSfiTScARZZsGmguYEWsbqrjJmIp.split('/')[-1]
    if not RJJtPMsJNduwmrIJzEAYvWHbExNuMYns:
        RJJtPMsJNduwmrIJzEAYvWHbExNuMYns = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(tnnIJSfiTScARZZsGmguYEWsbqrjJmIp, RJJtPMsJNduwmrIJzEAYvWHbExNuMYns)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(RJJtPMsJNduwmrIJzEAYvWHbExNuMYns)
