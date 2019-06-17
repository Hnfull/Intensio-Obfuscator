# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def rfHmOENFcCMGJVUDkfWYqGIOFiiQeppp(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to rfHmOENFcCMGJVUDkfWYqGIOFiiQeppp file.'
    else:
        return 'Error: File not found.'
def fTBqkQoEyLkFGuxuVbMlcrBDwpWkCbRo(FyUlDJVqRLskqRmXepPYnzpUnKZihbdD):
    if not FyUlDJVqRLskqRmXepPYnzpUnKZihbdD.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd = FyUlDJVqRLskqRmXepPYnzpUnKZihbdD.split('/')[-1]
    if not ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd:
        ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(FyUlDJVqRLskqRmXepPYnzpUnKZihbdD, ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(ZPPOkbsCooupiQaFoXrvjbpkCzeUCtcd)
