# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import re
import fileinput
import glob
import colorama
import os
from progress.bar import Bar

from core.utils.intensio_error import EXIT_SUCCESS, EXIT_FAILURE, ERROR_NOT_FILE
from core.utils.intensio_utils import Utils

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

ERROR_COLOUR    = colorama.Back.RED + colorama.Style.BRIGHT
PROGRESS_COLOUR = colorama.Fore.BLUE + colorama.Style.BRIGHT 

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Remove:

    def __init__(self):
        self.utils = Utils()


    def Backslashes(self, codeArg, outputArg):
        checkLine       = 0
        numberFiles     = 0
        numberGoodFile  = 0
        
        if codeArg == "python":
            detectFiles = "py"
            blockDir    = "__pycache__"

        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), detectFiles), recursive=True)]

        # -- Delete line breaks -- #
        for file in recursFiles:
            if blockDir in file:
                continue
            else:
                with fileinput.FileInput(file, inplace=True) as inputFile:
                    for line in inputFile:
                        if line.strip():
                            print(line.rstrip())
    
        # -- Check if all line breaks are deleted -- #
        for file in recursFiles:
            if blockDir in file:
                continue
            else:
                checkLine = 0 # Initialize check vars for the next file 
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if eachLine == "\n":
                            checkLine += 1
                        if checkLine == 0:
                            numberGoodFile += 1
                            numberFiles += 1
                        else:
                            numberGoodFile += 0
                            numberFiles += 1

        if numberGoodFile == numberFiles:
            return EXIT_SUCCESS
        else:
            return EXIT_FAILURE


    def Commentaries(self, codeArg, outputArg):
        countLineOutput     = 0
        countLineInput      = 0
        noCommentary        = 0
        isCommentary        = 0
        countRecursFiles    = 0

        if codeArg == "python": 
            detectFiles = "py"
            blockDir    = "__pycache__"
            
            commentariesBeginLine               = r"^\#.*"                      # Begin '#'
            quoteOfCommentariesMultipleLines    = r"^\s*[\"|\']{3}$"            # """ and ''' without before variables and if commentaries is over multiple lines
            quoteInRegex                        = r"\={1}\s*r[\"|\']{1}"        # If quote in regex
            quoteOfEndCommentariesMultipleLines = r"^\s*[\"|\']{3}\)?\.?"       # """ and ''' without before variables, if commentaries is over multiple lines and he finish by .format() funtion
            quoteOfCommentariesOneLine          = r"[\"|\']{3}.*[\"|\']{3}$"    # """ and ''' without before variables and if commentary is over one line, (""" commentaries """)
            quoteIntoVariable                   = r".*\={1}\s*\w*\.?\w*[\(|\.]{1}[\"|\']{3}|.*\={1}\s*[\"|\']{3}"   # """ and ''' with before variables
            commentariesAfterLine               = r"\s*\#[^\"|^\'|^\.|^\?|^\*|^\!|^\]|^\[|^\\|^\)|^\(|^\{|^\}].*"   # '#' after line of code

        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), detectFiles), recursive=True)]

        # -- Remove commentaries and Count commentaries will be removed -- #
        for number in recursFiles:
            countRecursFiles += 1
            
        print("\n[+] Running remove commentaries in {0} file(s)...\n".format(countRecursFiles))

        with Bar(PROGRESS_COLOUR + 'Processing', max=countRecursFiles) as bar:
            for file in recursFiles:
                if blockDir in file:
                    continue
                else:
                    # -- Remove commentaries -- #
                    with fileinput.input(file, inplace=True) as inputFile:
                        for eachLine in inputFile:
                            searchCommentariesAfterLine = re.search(commentariesAfterLine, eachLine)
                            searchCommentariesBeginLine = re.search(commentariesBeginLine, eachLine)
                            if codeArg == "python":
                                if "coding" in eachLine or "#!" in eachLine:
                                    print(eachLine)
                                    continue
                                
                                if re.match(quoteInRegex, eachLine):
                                    continue
                                elif re.match(quoteIntoVariable, eachLine):
                                    noCommentary += 1
                                elif re.match(quoteOfCommentariesMultipleLines, eachLine) or re.match(quoteOfEndCommentariesMultipleLines, eachLine):
                                    isCommentary += 1
                                else:
                                    pass
                                
                                if re.match(quoteOfCommentariesOneLine, eachLine):
                                    countLineInput += 1
                                    isCommentary = 0
                                    continue
                                elif isCommentary == 1 and noCommentary == 0:
                                    countLineInput += 1
                                    continue
                                elif isCommentary == 0 and noCommentary == 1:
                                    print(eachLine)
                                    continue
                                elif isCommentary == 2:
                                    countLineInput += 1
                                    isCommentary = 0
                                    continue
                                elif isCommentary == 1 and noCommentary == 1:
                                    isCommentary = 0
                                    noCommentary = 0
                                    print(eachLine)
                                    continue
                                else:
                                    pass
                            
                            if searchCommentariesBeginLine is not None:
                                countLineInput += 1
                                eachLine = eachLine.replace(searchCommentariesBeginLine.group(0), "")
                                print(eachLine)
                            elif searchCommentariesAfterLine is not None:
                                eachLine = eachLine.replace(searchCommentariesAfterLine.group(0), "")
                                countLineInput += 1
                                print(eachLine)
                            else:
                                print(eachLine)
                bar.next(1)
            bar.finish()

        # -- Initialize vars -- #
        isCommentary = 0
        noCommentary = 0

        # -- Check if all commentaries are removed -- #
        for file in recursFiles:
            countLineOutput = 0
            if blockDir in file:
                continue
            else:
                with open(file, "r") as readFile:
                    countLineOutput = 0
                    readF           = readFile.readlines()
                    for eachLine in readF:
                        searchCommentariesAfterLine = re.search(commentariesAfterLine, eachLine)
                        searchCommentariesBeginLine = re.search(commentariesBeginLine, eachLine)
                        if codeArg == "python":
                            if "coding" in eachLine or "#!" in eachLine:
                                continue
                            
                            if re.match(quoteInRegex, eachLine):
                                continue
                            elif re.match(quoteIntoVariable, eachLine):
                                noCommentary += 1
                            elif re.match(quoteOfCommentariesMultipleLines, eachLine) or re.match(quoteOfEndCommentariesMultipleLines, eachLine):
                                isCommentary += 1
                            else:
                                pass
                            
                            if re.match(quoteOfCommentariesOneLine, eachLine):
                                isCommentary = 0
                                countLineOutput += 1
                                continue
                            elif isCommentary == 1 and noCommentary == 0:
                                countLineOutput += 1
                                continue
                            elif isCommentary == 0 and noCommentary == 1:
                                continue
                            elif isCommentary == 2:
                                isCommentary = 0
                                countLineOutput += 1
                                continue
                            elif isCommentary == 1 and noCommentary == 1:
                                isCommentary = 0
                                noCommentary = 0
                                continue
                            else:
                                pass

                        if searchCommentariesBeginLine is not None:
                            countLineOutput += 1
                        elif searchCommentariesAfterLine is not None:
                            countLineOutput += 1
                        else:
                            pass

        if (Remove.Backslashes(self, codeArg, outputArg) == 0):
            if countLineOutput == 0:
                print("\n-> {0} lines of commentaries removed\n".format(countLineInput))            
                return EXIT_SUCCESS
            else:
                return EXIT_FAILURE
        else:
            return EXIT_FAILURE


    def PrintFunctions(self, codeArg, outputArg):
        countPrintLine              = 0
        countCheckPrintLine         = 0
        countRecursFiles            = 0
        checkPrintPy3MultipleLines  = 0
        checkPrintPy2MultipleLines  = 0

        if codeArg == "python":
            detectFiles = "py"
            blockDir    = "__pycache__"

            detectPrint                     = r"\s*print"
            detectPythonPrint2              = r"\s*print\s*[\"|\']{1}"
            detectPythonPrint3              = r"\s*print\s*\({1}"
            detectPythonPrintMultipleLines  = r"^\s+[\"\']{1}\s*\w+|^[\"\']{1}\s*\w+"

        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), detectFiles), recursive=True)]

        for number in recursFiles:
            countRecursFiles += 1

        print("\n[+] Running remove print function in {0} file(s)...\n".format(countRecursFiles))

        with Bar(PROGRESS_COLOUR + 'Processing', max=countRecursFiles) as bar:
            for file in recursFiles:
                if blockDir in file:
                    continue
                else: 
                    # -- Remove all print functions -- #
                    with fileinput.input(file, inplace=True) as inputFile:
                        for eachLine in inputFile:
                            if re.match(detectPrint, eachLine):
                                countPrintLine += 1
                                # -- If print() python 3 is multiple lines -- #
                                if re.match(detectPythonPrint3, eachLine):
                                    if "(" in eachLine and not ")" in eachLine:
                                        checkPrintPy3MultipleLines += 1
                                        continue
                                    else:
                                        continue
                                # -- If print python 2 is multiple lines -- #        
                                elif re.match(detectPythonPrint2, eachLine):
                                    checkPrintPy2MultipleLines += 1
                                    continue
                            else:
                                if checkPrintPy3MultipleLines == 1:
                                    if ")" in eachLine and not "(" in eachLine:
                                        checkPrintPy3MultipleLines = 0
                                        continue
                                    else:
                                        continue
                                elif checkPrintPy2MultipleLines > 0:
                                    if re.match(detectPythonPrintMultipleLines, eachLine):
                                        checkPrintPy2MultipleLines += 1
                                        continue
                                    else:
                                        checkPrintPy2MultipleLines = 0
                                        print(eachLine)
                                        continue
                                else:
                                    print(eachLine)
                bar.next(1)
            bar.finish()

        # -- Check if all print functions are removed -- #
        for file in recursFiles:
            if blockDir in file:
                continue
            else:
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if re.match(detectPrint, eachLine):
                            countCheckPrintLine += 1

        if (Remove.Backslashes(self, codeArg, outputArg) == 0):
            if countCheckPrintLine == 0:
                print("\n-> {0} print functions removed\n".format(countPrintLine))
                return EXIT_SUCCESS
            else:
                return EXIT_FAILURE
        else:
            return EXIT_FAILURE


    def TrashFiles(self, codeArg, outputArg):
        removeFiles = 0

        if codeArg == "python":
            detectFiles = "pyc"
            blockDir    = "__pycache__"

            detectPycFiles  = r"\w+\.{1}pyc"

        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), detectFiles), recursive=True)]
        
        try:
            # Check if .pyc file(s) exists
            for file in recursFiles:
                removeFiles += removeFiles + 1
            
            if removeFiles == 0:
                return removeFiles
            else:
                # -- Remove pyc file(s)
                for file in recursFiles:    
                    os.remove(file)

                # -- Check if pyc file(s) are removed
                for file in recursFiles:
                    if re.match(detectFilesPycFile, file):
                        return EXIT_FAILURE

                return removeFiles
        except Exception as e:
            print(ERROR_COLOUR + "[-] {0}".format(e))
            return EXIT_FAILURE

