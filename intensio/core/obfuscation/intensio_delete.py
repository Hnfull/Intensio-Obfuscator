# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import re
import fileinput
import os
import sys
from progress.bar import Bar

from core.utils.intensio_utils import Utils

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Delete:

    def __init__(self):
        self.utils = Utils()


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
        checkNumQuote           = []
        checkDeleted            = {}
        countLineOutput         = 0
        countLineInput          = 0
        noComments              = 0
        multipleLinesComments   = 0
        countRecursFiles        = 0
        numberLine              = 0
            
        commentsBeginLine               = r"^\#.*"
        quoteOfCommentsEndLines         = r".*[\'\|\"]{3}\s*$"
        quoteInRegex                    = r"={1}\s*r[\"|\']{3}"
        quoteOfCommentsMultipleLines    = r"^\s+[\"|\']{3}|^[\"|\']{3}"
        quoteIntoVariableOrPrint        = r"s*print.*\(?[\"|\']{3}|.*\=\s*[\"|\']{3}"
        quoteOfCommentsOneLine          = r".*[\"]{3}.*[\"]{3}|.*[\']{3}.*[\']{3}\s*$"
        commentsAfterLine               = r"\#[^\"|^\'|^\.|^\?|^\*|^\!|^\]|^\[|^\\|^\)|^\(|^\{|^\}].*"

        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg, 
                                                detectFiles="py", 
                                                blockDir="__pycache__", 
                                                blockFile=False,
                                                dirOnly=False
        )

        for i in recursFiles:
            countRecursFiles += 1
        
        # -- Delete comments and Count comments will be deleted -- #            
        print("\n[+] Running delete comments in {} file(s)...\n".format(countRecursFiles))

        with Bar("Obfuscation ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                # -- Delete comments -- #
                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        if "coding" in eachLine or "#!" in eachLine:
                            sys.stdout.write(eachLine)
                            continue
                        if multipleLinesComments == 1 or noComments == 1:
                            if re.match(quoteOfCommentsEndLines, eachLine):
                                if re.match(quoteInRegex, eachLine):
                                    countLineInput += 1
                                    continue
                                elif re.match(quoteIntoVariableOrPrint, eachLine):
                                    countLineInput += 1
                                    continue
                                else:
                                    if multipleLinesComments == 1:
                                        multipleLinesComments = 0
                                        countLineInput += 1
                                    else:
                                        noComments = 0
                                        sys.stdout.write(eachLine)
                                    continue
                            else:
                                if noComments == 1:
                                    sys.stdout.write(eachLine)
                                else:
                                    countLineInput += 1
                                continue
                        elif multipleLinesComments == 0:
                            if re.match(quoteOfCommentsMultipleLines, eachLine):   
                                if re.match(quoteOfCommentsOneLine, eachLine):
                                    countLineInput += 1
                                    continue
                                else:
                                    countLineInput += 1
                                    multipleLinesComments = 1
                                    continue
                            elif re.match(quoteIntoVariableOrPrint, eachLine):
                                noComments = 1
                                sys.stdout.write(eachLine)
                                continue
                            else:
                                sys.stdout.write(eachLine)
                        else:
                            sys.stdout.write(eachLine)

                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        if "coding" in eachLine or "#!" in eachLine:
                            sys.stdout.write(eachLine)
                            continue
                        searchCommentsAfterLine = re.search(commentsAfterLine, eachLine)
                        searchCommentsBeginLine = re.search(commentsBeginLine, eachLine)
                        if searchCommentsBeginLine:
                            countLineInput += 1
                            eachLine = eachLine.replace(searchCommentsBeginLine.group(0), "")
                            sys.stdout.write(eachLine)
                        elif searchCommentsAfterLine:
                            if re.match(r"\#\s*.+[\"]{1}|\#\s*.+[\']{1}", searchCommentsAfterLine.group(0)): # Check if '#' char is in a string
                                sys.stdout.write(eachLine)
                            else:
                                eachLine = eachLine.replace(searchCommentsAfterLine.group(0), "")
                                countLineInput += 1
                                sys.stdout.write(eachLine)

                        else:
                            sys.stdout.write(eachLine)

                bar.next(1)
            bar.finish()
            
        # -- Check if all comments are deleted -- #
        noComments              = 0
        multipleLinesComments   = 0

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
                            if multipleLinesComments == 1 or noComments == 1:
                                if re.match(quoteOfCommentsEndLines, eachLine):
                                    if re.match(quoteInRegex, eachLine):
                                        countLineOutput += 1
                                        continue
                                    elif re.match(quoteIntoVariableOrPrint, eachLine):
                                        countLineOutput += 1
                                        continue
                                    else:
                                        if multipleLinesComments == 1:
                                            multipleLinesComments = 0
                                            checkDeleted[numberLine] = "{} ( multiple lines comments )".format(file)
                                            countLineOutput += 1
                                        else:
                                            noComments = 0
                                        continue
                                else:
                                    if noComments == 1:
                                        pass
                                    else:
                                        countLineOutput += 1
                                    continue
                            elif multipleLinesComments == 0:
                                if re.match(quoteOfCommentsMultipleLines, eachLine):   
                                    if re.match(quoteOfCommentsOneLine, eachLine):
                                        checkDeleted[numberLine] = file
                                        countLineOutput += 1
                                        continue
                                    else:
                                        countLineOutput += 1
                                        multipleLinesComments = 1
                                        continue
                                elif re.match(quoteIntoVariableOrPrint, eachLine):
                                    noComments = 1
                                    continue
                                else:
                                    pass
                            else:
                                pass
                  
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    numberLine = 0
                    for eachLine in readF:
                        numberLine += 1
                        if "coding" in eachLine or "#!" in eachLine:
                            continue
                        else:
                            searchCommentsAfterLine = re.search(commentsAfterLine, eachLine)
                            searchCommentsBeginLine = re.search(commentsBeginLine, eachLine)
                            if searchCommentsBeginLine:
                                checkDeleted[numberLine] = file
                                countLineOutput += 1
                            elif searchCommentsAfterLine:
                                checkDeleted[numberLine] = file
                                countLineOutput += 1
                            else:
                                pass

                bar.next(1)  
            bar.finish()
        
        if countLineOutput == 0:
            print("\n-> {} lines of comments deleted\n".format(countLineInput))            
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
                print("\n-> {} lines of comments no deleted\n".format(countLineOutput))
            return 1


    def TrashFiles(self, outputArg, verboseArg):
        countRecursFiles    = 0
        deleteFiles         = 0
        checkPycFile        = []
        currentPosition     = os.getcwd()

        detectPycFiles  = r".*\.pyc$"
        deletePycFiles  = r"\w+\.pyc$"

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
                if re.match(detectPycFiles, file):
                    deleteFiles += 1
                    checkPycFile.append(file)

                bar.next(1)
            bar.finish()

        # -- Delete pyc file(s) -- #
        with Bar("Correction  ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:   
                if re.match(detectPycFiles, file):
                    extractPycFiles = re.search(deletePycFiles, file)
                    moveFolder      = re.sub(deletePycFiles, "", file)
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
