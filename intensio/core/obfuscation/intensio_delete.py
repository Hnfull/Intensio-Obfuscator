# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import re
import fileinput
import os
import sys
from progress.bar import Bar

from core.utils.intensio_utils import Utils, Reg

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Delete:

    def __init__(self):
        self.utils  = Utils()


    def LinesSpaces(self, outputArg, verboseArg):
        checkLinesSpace     = {}
        checkEmptyLine      = 0
        countRecursFiles    = 0
        numberLine          = 0

        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg, 
                                                detectFiles="py", 
                                                blockDir="__pycache__", 
                                                blockFile=False,
                                                dirOnly=False
        )

        for file in recursFiles:
            countRecursFiles += 1

        # -- Delete all empty lines -- #
        with Bar("Obfuscation ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                with fileinput.FileInput(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        if eachLine == "\n":
                            pass
                        else:
                            sys.stdout.write(eachLine)

                bar.next(1)
            bar.finish()

        with Bar("Check       ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                numberLine = 0
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        numberLine += 1
                        if eachLine == "\n":
                            checkLinesSpace[numberLine] = file
                            checkEmptyLine += 1

                bar.next(1)
            bar.finish()

        if checkEmptyLine == 0:
            return 0
        else:
            if verboseArg:
                print("\n[!] Empty line that not been deleted... :\n")
                for key, value in checkLinesSpace.items():
                    print("\n-> File : {}".format(value))
                    print("-> Line : {}".format(key))
            return 1


    def Comments(self, outputArg, verboseArg):
        getIndexList            = []
        checkDeleted            = {}
        countLineCommentOutput  = 0
        countLineCommentInput   = 0
        multipleLinesComments   = 0
        countRecursFiles        = 0
        numberLine              = 0
        noCommentsQuotes        = 0
        detectIntoSimpleQuotes  = None
            
        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg, 
                                                detectFiles="py", 
                                                blockDir="__pycache__", 
                                                blockFile=False,
                                                dirOnly=False
        )

        for i in recursFiles:
            countRecursFiles += 1
        
        # -- Delete comments and count comments will be deleted -- #            
        print("\n[+] Running delete comments in {} file(s)...\n".format(countRecursFiles))

        with Bar("Obfuscation ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        if re.match(Reg.pythonFileHeader, eachLine):
                            sys.stdout.write(eachLine)
                        else:
                            if multipleLinesComments == 1:
                                if re.match(Reg.quotesCommentsMultipleLines, eachLine):
                                    if self.utils.VerifyMultipleLinesComments(eachLine) == True:
                                        if multipleLinesComments == 1:
                                            countLineCommentInput += 1
                                            multipleLinesComments = 0
                                    else:
                                        countLineCommentInput += 1
                                else:
                                    countLineCommentInput += 1
                            elif noCommentsQuotes == 1:
                                if re.match(Reg.checkIfEndVarStdoutMultipleQuotes, eachLine):
                                    sys.stdout.write(eachLine)
                                    noCommentsQuotes = 0
                                else:
                                    sys.stdout.write(eachLine)
                            else:
                                if re.match(Reg.quotesCommentsOneLine, eachLine):
                                    countLineCommentInput += 1
                                else:
                                    if re.match(Reg.quotesCommentsMultipleLines, eachLine):
                                        if self.utils.VerifyMultipleLinesComments(eachLine) == True:
                                            countLineCommentInput += 1
                                            multipleLinesComments = 1
                                        else:
                                            sys.stdout.write(eachLine)
                                    else:
                                        if re.match(Reg.checkIfStdoutMultipleQuotes, eachLine) \
                                        or re.match(Reg.checkIfVarMultipleQuotes, eachLine):
                                            sys.stdout.write(eachLine)
                                            noCommentsQuotes = 1
                                        elif re.match(Reg.checkIfRegexMultipleQuotes, eachLine):
                                            sys.write.stdout(eachLine)
                                        else:
                                            sys.stdout.write(eachLine)

                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        if "coding" in eachLine or "#!" in eachLine:
                            sys.stdout.write(eachLine)
                        else:
                            if re.match(Reg.hashCommentsBeginLine, eachLine):
                                countLineCommentInput += 1
                            elif re.match(Reg.hashCommentsAfterLine, eachLine):
                                eachLineList = list(eachLine)
                                for i, v in enumerate(eachLineList):
                                    if v == "#":
                                        getIndexList.append(i)
                                for i in getIndexList:
                                    if self.utils.DetectIntoSimpleQuotes(eachLine, maxIndexLine=i) == False:
                                        countLineCommentInput += 1
                                        detectIntoSimpleQuotes = False
                                        break
                                    else:
                                        continue
                                if detectIntoSimpleQuotes == False:
                                    eachLineList = eachLineList[:getIndexList[-1]]
                                    eachLineList.append("\n")
                                    eachLine = "".join(eachLineList)
                                    sys.stdout.write(eachLine)
                                    detectIntoSimpleQuotes = None
                                    continue
                                else:
                                    sys.stdout.write(eachLine)
                            else:
                                sys.stdout.write(eachLine)

                bar.next(1)
            bar.finish()
            
        # -- Check if all comments are deleted -- #
        with Bar("Check       ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    numberLine = 0
                    for eachLine in readF:
                        numberLine += 1
                        if "coding" in eachLine or "#!" in eachLine:
                            continue
                        else:
                            if multipleLinesComments == 1:
                                if re.match(Reg.quotesCommentsMultipleLines, eachLine):
                                    if self.utils.VerifyMultipleLinesComments(eachLine) == True:
                                        if multipleLinesComments == 1:
                                            countLineCommentOutput += 1
                                            multipleLinesComments = 0
                                    else:
                                        countLineCommentOutput += 1
                                else:
                                    countLineCommentOutput += 1
                            elif noCommentsQuotes == 1:
                                if re.match(Reg.checkIfEndVarStdoutMultipleQuotes, eachLine):
                                    noCommentsQuotes = 0
                                else:
                                    continue
                            else:
                                if re.match(Reg.quotesCommentsOneLine, eachLine):
                                    countLineCommentOutput += 1
                                else:
                                    if re.match(Reg.quotesCommentsMultipleLines, eachLine):
                                        if self.utils.VerifyMultipleLinesComments(eachLine) == True:
                                            countLineCommentOutput += 1
                                            multipleLinesComments = 1
                                        else:
                                            continue
                                    else:
                                        if re.match(Reg.checkIfStdoutMultipleQuotes, eachLine) \
                                        or re.match(Reg.checkIfVarMultipleQuotes, eachLine):
                                            noCommentsQuotes = 1
                                        elif re.match(Reg.checkIfRegexMultipleQuotes, eachLine):
                                            continue
                                        else:
                                            continue
                  
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    numberLine = 0
                    for eachLine in readF:
                        numberLine += 1
                        if "coding" in eachLine or "#!" in eachLine:
                            continue
                        else:
                            if re.match(Reg.hashCommentsBeginLine, eachLine):
                                countLineCommentInput += 1
                            elif re.match(Reg.hashCommentsAfterLine, eachLine):
                                eachLineList = list(eachLine)
                                for i, v in enumerate(eachLineList):
                                    if v == "#":
                                        getIndexList.append(i)
                                for i in getIndexList:
                                    if self.utils.DetectIntoSimpleQuotes(eachLine, maxIndexLine=i) == False:
                                        countLineCommentInput += 1
                                        detectIntoSimpleQuotes = False
                                        break
                                    else:
                                        continue
                                if detectIntoSimpleQuotes == False:
                                    detectIntoSimpleQuotes = None
                                    continue
                                else:
                                    continue
                            else:
                                continue

                bar.next(1)  
            bar.finish()
        
        if countLineCommentOutput == 0:
            print("\n-> {} lines of comments deleted\n".format(countLineCommentInput))            
            return 0
        else:
            if verboseArg:
                print("\n[!] Comments that not been deleted... :\n")
                for key, value in checkDeleted.items():
                    print("\n-> File : {}".format(value))
                    if "multiple lines comments" in value:
                        print("-> Line : {} ( This is the end line of multiple lines comments )".format(key))
                    else:
                        print("-> Line : {}".format(key))
                print("\n-> {} lines of comments no deleted\n".format(countLineCommentOutput))
            return 1


    def TrashFiles(self, outputArg, verboseArg):
        countRecursFiles    = 0
        deleteFiles         = 0
        checkPycFile        = []
        currentPosition     = os.getcwd()

        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg, 
                                                detectFiles="pyc", 
                                                blockDir="__pycache__", 
                                                blockFile=False,
                                                dirOnly=False
        )

        for number in recursFiles:
            countRecursFiles += 1

        if countRecursFiles == 0:
            print("[!] No .pyc file(s) found in {}".format(outputArg))
            return 0

        print("\n[+] Running delete {} .pyc file(s)...\n".format(countRecursFiles))

        # -- Check if .pyc file(s) exists and delete it -- #
        with Bar("Setting up  ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                if re.match(Reg.detectPycFiles, file):
                    deleteFiles += 1
                    checkPycFile.append(file)

                bar.next(1)
            bar.finish()

        # -- Delete pyc file(s) -- #
        with Bar("Correction  ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:   
                if re.match(Reg.detectPycFiles, file):
                    extractPycFiles = re.search(r".*\.pyc$", file)
                    moveFolder      = re.sub(r".*\.pyc$", "", file)
                    os.chdir(moveFolder)
                    os.remove(extractPycFiles.group(0))
                    os.chdir(currentPosition)
                    
                bar.next(1)
            bar.finish()
        
        checkRecursFiles = self.utils.CheckFileDir(
                                                    output=outputArg, 
                                                    detectFiles="pyc", 
                                                    blockDir="__pycache__", 
                                                    blockFile=False,
                                                    dirOnly=False
        )

        if checkRecursFiles != []:
            if verboseArg:
                for pycFile in checkRecursFiles:
                    print("-> .pyc file no deleted : {}".format(pycFile))
            return 1
        else:
            if verboseArg:
                for pycFile in checkPycFile:
                    print("-> .pyc file deleted : {}".format(pycFile))
        print("\n-> {} .pyc file(s) deleted".format(deleteFiles))
        return 0
