# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def rnwqXTByWxsicjfOSpWVLNleVrtRtZmw(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to rnwqXTByWxsicjfOSpWVLNleVrtRtZmw file.'
    else:
        return 'Error: File not found.'
def PlOfLCyrxgxNAxXDeIcCEPXCWCAHjkCM(fzXeczXGLhpJOfWdZElFRIoIeGiUwvoU):
    if not fzXeczXGLhpJOfWdZElFRIoIeGiUwvoU.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc = fzXeczXGLhpJOfWdZElFRIoIeGiUwvoU.split('/')[-1]
    if not wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc:
        wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(fzXeczXGLhpJOfWdZElFRIoIeGiUwvoU, wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc)
