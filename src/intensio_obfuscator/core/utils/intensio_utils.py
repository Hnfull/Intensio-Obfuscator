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
            countLoop   = 0

            for i in line:
                if countLoop == maxIndex:
                    break
                else:
                    pass
                if i == "\"" or i == "\'":
                    if line[countLoop - 1] == "\\":
                        pass
                    else:      
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


    def VerifyMultipleLinesComments(self, line):
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
            if numberQuotes == 3:
                return True
            else:
                return False


    def RemoveDuplicatesValuesInList(self, listArg):
        removeDuplicateValues = list(dict.fromkeys(listArg))
        return removeDuplicateValues


    def CheckFileDir(self, output, detectFiles, blockDir, blockFile, dirOnly):
        filesName = []

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


class Reg:
    # -- All features -- #
    checkIfVarMultipleQuotes    = r"\s*[\w\.]+\s*\=\s*.*[\"|\']{3}"
    checkIfRegexMultipleQuotes  = r"\s*r{1}[\']{3}|\s*r{1}[\"]{3}"
    checkIfStdoutMultipleQuotes = r"\s*print{1}\s*\(?[\"|\']{3}|\s*sys\.write\.stdout{1}\s*\(?[\"|\']{3}"
    checkIfEndVarStdoutMultipleQuotes = r".*\"{3}|.*\'{3}"
    
    pythonFileHeader = r"^\s*\#\!.*python|^\s*\#\s*-\*-" 

    # -- Delete empty line feature -- #
    detectLineEmpty = r"^\s*$"

    # --  Delete comments feature only -- #
    hashCommentsAfterLine = r"^[^\#]+\#.*"
    hashCommentsBeginLine = r"^\s*\#.*"

    quotesCommentsMultipleLines     = r"^\s+[\"|\']{3}\s*|^[\"|\']{3}\s*"
    quotesCommentsOneLine           = r"^\s*[\"]{3}.*[\"]{3}\s*$|^\s*[\']{3}.*[\']{3}\s*$"
    quotesCommentsEndMultipleLines  = r"^\s+[\"|\']{3}\s*|^[\"|\']{3}\s*|.+[\"|\']{3}\s*$"

    # -- Replace string to string feature only -- #
    detectSpecialChars = r"\.|\:|\)|\(|\=|\[|\]|\{|\}|\,|\+|\s|\*|\-|\%|\/|\^|\'|\""
    detectSpecialCharsWihtoutQuotes = r"\.|\:|\)|\(|\=|\[|\]|\{|\}|\,|\+|\s|\*|\-|\%|\/|\^"
    
    # -- Replace string to string feature and Padding empty classes and functions feature -- #
    detectFunctions = r"def\s+(\w+)"
    detectClasses   = r"class\s+(\w+)"
    detectErrorVars = r"except(\s+\w+\s+as\s+)(\w)"
    detectLoopVars  = r"for\s+([\w\s\,]+)(\s+in\s+)"
    detectSimpleVars = r"(^[\s|a-zA-Z_]+[\,\s\w]{0,})+(\s*=\s*[\[|\{\(|\w+|\"|\'])"

    # -- Padding scripts feature only -- #
    addIndentScript = r".*\:{1}\s*$"
    noAddScript     = r"^\@|\s+\@|\s+return|\s*def\s+.+\s*\:{1}|^class\s+.+\s*\:{1}|.*[\{|\[|\(|\)|\]|\}|\,|\\|\^|\'|\"|0-9]\s*$|\s+yield.*|\s+raise.*|\s*\)+\s*for\s+\w+\s+in\s+"
    detectComma     = r".+\,{1}\s*$"
    detectOpenSymb  = r".+[\{|\[|\(]$|.+[\{|\[|\(]\s+$"

    # -- Padding empty classes feature only -- #
    checkClassInLine = r"\s*class\s+\w+"

    # -- Padding empty functions feature only -- #
    checkFunctionInLine = r"\s*def\s+\w+"

    # -- Delete .pyc files feature only -- #
    detectPycFiles = r".*\.pyc$"

    # -- Replace files name feature only -- #
    detectPythonImport = r"\s*from\s+|\s*import\s+"

    # -- Replace string to hex feature only -- #
    detectExecFunction  = r"exec\(\w+\)"
    detectMultipleQuotes = r"\'{3}|\"{3}"

    # -- Detect arg of program -- #
    detectMlenArg   = r"^lower$|^medium$|^high$"
    detectIndentArg = r"^[2|4|8]$"


class Colors: 
    # PROGRESS = "\033[94m" + "\033[1m" # blue + bold
    SUCCESS = "\033[92m"                # green
    SECTION = "\033[93m" + "\033[1m"    # yellow + bold
    ERROR   = "\x1b[1;37;41m"           # highlighted red
    DISABLE = "\033[0m"                 # disable colors


# --only for breaking a loop -- #
class BreakLoop (Exception):
    pass
