# -*- coding: utf-8 -*-
import datetime
import os
import urllib
import zipfile
def tAwBBLJuYUpjfKGKmoHiMchedOirrdBI(f):
    if os.path.isfile(f):
        try:
            with zipfile.ZipFile(f) as zf:
                zf.extractall('.')
                return 'File {} extracted.'.format(f)
        except zipfile.BadZipfile:
            return 'Error: Failed to tAwBBLJuYUpjfKGKmoHiMchedOirrdBI file.'
    else:
        return 'Error: File not found.'
def MvsxOckMDUuCxUTEMjPxoqmnxnPPluSc(DupvyQQFsTNzzMdqkTLlsfNBAjsKJLoI):
    if not DupvyQQFsTNzzMdqkTLlsfNBAjsKJLoI.startswith('http'):
        return 'Error: URL must begin with http:// or https:// .'
    eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci = DupvyQQFsTNzzMdqkTLlsfNBAjsKJLoI.split('/')[-1]
    if not eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci:
        eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))
    try:
        urllib.urlretrieve(DupvyQQFsTNzzMdqkTLlsfNBAjsKJLoI, eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci)
    except IOError:
        return 'Error: Download failed.'
    return 'File {} downloaded.'.format(eNbzIjEVvLYLmhmunDRWLfdfFIkdeGci)
