 # -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import argparse

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#
class Args:

    def __init__(self):
        self.parser = argparse.ArgumentParser(
                                            prog="intensio_obfuscator.py"
                                            )
        self.parser.add_argument(
                                "-f", "--onefile",
                                action="store_true",
                                default=False,
                                help="if only one file"
                                )
        self.parser.add_argument(
                                "-d", "--multiplefiles",
                                action="store_true",
                                default=False,
                                help="if multiple files (directory of project)"
                                )
        self.parser.add_argument(
                                "-i", "--input",
                                help="source file or directory - if multiple files indicate a directory that contain all your files"
                                )
        self.parser.add_argument(
                                "-c", "--code",
                                choices=["python"],
                                help="language used in source file or directory"
                                )
        self.parser.add_argument(
                                "-o", "--output",
                                help="output file or directory that will be obfuscated - if multiple file indicate a empty directory that will contain all your files"
                                )
        self.parser.add_argument(
                                "-m", "--mixer",
                                choices=["lower", "medium", "high"],
                                default="medium",
                                help="length level of variables mix output"
                                )
        self.parser.add_argument(
                                "-r", "--replace",
                                action="store_true",
                                default=False,
                                help="activate the 'replace' obfuscation feature"
                                )
        self.parser.add_argument(
                                "-p", "--padding",
                                action="store_true",
                                default=False,
                                help="activate the 'padding' obfuscation feature"
                                )
        self.parser.add_argument(
                                "-rm", "--remove",
                                action="store_true",
                                default=False,
                                help="activate the 'remove' obfuscation feature"
                                )
        self.parser.add_argument(
                                "-s", "--secret",
                                action="store_true",
                                default=False,
                                help="activate the 'secret' bullshit feature"
                                )

    def GetArgHelp(self):
        return self.parser.print_help()
    
    def GetArgsValue(self):
        return self.parser.parse_args()
