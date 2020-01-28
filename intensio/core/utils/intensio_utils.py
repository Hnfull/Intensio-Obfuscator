# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import sys
import glob
import os

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Utils:

    def __init__(self):
        self.platform = sys.platform


    def Platform(self):
        if self.platform == "win32":
            return "\\"
        else:
            return "/"


    def DictMerge(self, dict1, dict2):
        merge = {**dict1, **dict2}
        return merge


    def CheckFileDir(self, output, detectFiles, blockDir, blockFile, dirOnly):
        filesName       = []

        if dirOnly == False:
            recursFiles = [
                            file for file in glob.glob("{0}{1}**{1}*.{2}".format(
                                                                                output, 
                                                                                Utils.Platform(self), 
                                                                                detectFiles), 
                                                                                recursive=True
                                                                        )
            ]
        else:
            recursFiles = [
                            file for file in glob.glob("{0}{1}**{1}".format(
                                                                            output, 
                                                                            Utils.Platform(self), 
                                                                            ), 
                                                                            recursive=True
                                                                    )
            ]

        for file in recursFiles:
            if blockFile == False:
                if blockDir in file:
                    continue
                else:
                    if os.path.getsize(file) > 0:
                        filesName.append(file)
                    else:
                        continue
            else:
                if blockDir in file or blockFile in file:
                    continue
                else:
                    if os.path.getsize(file) > 0:
                        filesName.append(file)
                    else:
                        continue

        return filesName[:]


class Colors:

    PROGRESS = "\033[94m" + "\033[1m"   # blue + bold
    SUCCESS = "\033[92m"                # green
    SECTION = "\033[93m" + "\033[1m"    # yellow + bold
    ERROR   = "\x1b[1;37;41m"           # highlighted red
    DISABLE = "\033[0m"                 # disable color