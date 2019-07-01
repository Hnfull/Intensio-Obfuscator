# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import argparse

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#
class Args:

    def __init__(self):
        self.parser = argparse.ArgumentParser(
                                            prog="intensio_obfuscator.py"
                                            )
        self.parser.add_argument(
                                "-i", "--input",
                                help="source file or directory - if multiple files indicate a directory that contain all your files"
                                )
        self.parser.add_argument(
                                "-c", "--code",
                                choices=["python"],
                                default="python",
                                help="language used in source file or directory"
                                )
        self.parser.add_argument(
                                "-o", "--output",
                                help="output file or directory that will be obfuscated - if multiple file indicate a empty directory that will contain all your files"
                                )
        self.parser.add_argument(
                                "-m", "--mixerlevel",
                                choices=["lower", "medium", "high"],
                                default="medium",
                                help="length levels of the number of characters for output variables /classes/functions"
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
                                "-rc", "--rcommentaries",
                                action="store_true",
                                default=True,
                                help="activate the 'rcommentaries' obfuscation feature"
                                )
        self.parser.add_argument(
                                "-rp", "--rprint",
                                action="store_true",
                                default=False,
                                help="activate the 'rprint' obfuscation feature"
                                )
        self.parser.add_argument(
                                "-v", "--verbose",
                                action="store_true",
                                default=False,
                                help="improve verbosity"
                                )


    def GetArgHelp(self):
        return self.parser.print_help()

    
    def GetArgsValue(self):
        return self.parser.parse_args()
