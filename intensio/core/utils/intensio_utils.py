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


    def Platform(self, getOS, getPathType):
        if getOS == True:
            if self.platform == "win32":
                return "win32"
            else:
                return "unix"
        elif getPathType == True:
            if self.platform == "win32":
                return "\\"
            else:
                return "/"


    def DictMerge(self, dict1, dict2):
        merge = {**dict1, **dict2}
        return merge


    def DetectIntoSimpleQuotes(self, line, maxIndexLine=None):
            if maxIndexLine == None:
                maxIndex = len(line)
            else:
                maxIndex = maxIndexLine

            countQuotes = 0
            countLoop = 0

            for i in line:
                if countLoop == maxIndex:
                    break
                else:
                    pass

                if i == "\"" or i == "\'":      
                    countQuotes += 1
                countLoop += 1

            if countQuotes == 0:
                return False
            elif (countQuotes % 2) == 0:
                return False
            else:
                return True


    def DetectMultipleLinesQuotes(self, line):
        countQuotes = 0
        simpleQuotes = 0
        doubleQuotes = 0
        numberQuotes = 0

        for i in line:
            if i == "\"" or i == "\'":
                if i == "\'":
                    simpleQuotes += 1
                if i == "\"":
                    doubleQuotes += 1
        
        if simpleQuotes >= doubleQuotes:
            numberQuotes = simpleQuotes
        else:
            numberQuotes = doubleQuotes

        if numberQuotes == 0:
            return False
        elif (numberQuotes % 2) == 0:
            return False
        else:
            return True


    def CheckFileDir(self, output, detectFiles, blockDir, blockFile, dirOnly):
        filesName       = []

        if dirOnly == False:
            recursFiles = [
                            file for file in glob.glob("{0}{1}**{1}*.{2}".format(
                                                                                output, 
                                                                                Utils.Platform(self, getOS=False, getPathType=True), 
                                                                                detectFiles), 
                                                                                recursive=True
                                                                        )
            ]
        else:
            recursFiles = [
                            file for file in glob.glob("{0}{1}**{1}".format(
                                                                            output, 
                                                                            Utils.Platform(self, getOS=False, getPathType=True), 
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
    # PROGRESS = "\033[94m" + "\033[1m" # blue + bold
    SUCCESS = "\033[92m"                # green
    SECTION = "\033[93m" + "\033[1m"    # yellow + bold
    ERROR   = "\x1b[1;37;41m"           # highlighted red
    DISABLE = "\033[0m"                 # disable colors


# --only for breaking a loop -- #
class BreakLoop (Exception):
    pass
