# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import re
import fileinput
import glob
from tqdm import tqdm

from core.utils.intensio_error import EXIT_SUCCESS, EXIT_FAILURE
from core.utils.intensio_utils import Utils

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Remove:
    def __init__(self):
        self.utils = Utils()

    def LineBreaks(self, codeArg, outputArg):
        checkLine       = 0
        numberFiles     = 0
        numberFileGood  = 0
        
        if codeArg == "python":
            detectFile  = "py"
            blockDirs   = r"__pycache__"

        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), detectFile), recursive=True)]

        # -- Delete line breaks -- #
        for output in recursFiles:
            if re.match(blockDirs, output):
                continue
            else:
                with fileinput.FileInput(output, inplace=True) as inputFile:
                    for line in inputFile:
                        if line.strip():
                            print(line.rstrip())
    
        # -- Check if all line breaks are deleted -- #
        for output in recursFiles:
            checkLine = 0 # Initialize check vars for the next file 

            if re.match(blockDirs, output):
                continue
            else:
                with open(output, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if eachLine == "\n":
                            checkLine += 1
                        if checkLine == 0:
                            numberFileGood += 1
                            numberFiles += 1
                        else:
                            numberFileGood += 0
                            numberFiles += 1

        if numberFileGood == numberFiles:
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
            classicCommentariesAfterLine    = r"\s+\#.*"                        # '#' after line of code 
            classicCommentariesBeginLine    = r"^\#.*"                          # begin '#'
            quoteOfCommentariesMultipleLine = r"^[\"\']{3}$"                    # """ and ''' without before variables and if commentaries is over multiple lines
            quoteOfCommentariesOneLine      = r"[\"|\']{3}.*[\"|\']{3}"         # """ and ''' without before variables and if commentary is over one line, (""" commentaries """)
            noQuoteOfCommentaries           = r"\w+\s*[\=|\(]{1}\s*[\"|\']{3}"  # """ and ''' with before variables
        
            detectFile  = "py"
            blockDirs   = r"__pycache__"

        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), detectFile), recursive=True)]

        # -- Count commentaries will be removed -- #
        for output in recursFiles:
            if re.match(blockDirs, output):
                continue
            else:
                with open(output, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if codeArg == "python":
                            searchClassicCommentariesAfterLine = re.search(classicCommentariesAfterLine, eachLine)
                            searchClassicCommentariesBeginLine = re.search(classicCommentariesBeginLine, eachLine)
                            if "coding" in eachLine or "#!" in eachLine:
                                continue
                            
                            if re.match(noQuoteOfCommentaries, eachLine):
                                noCommentary += 1
                            elif re.match(quoteOfCommentariesMultipleLine, eachLine):
                                isCommentary += 1
                            else:
                                pass

                            if isCommentary == 1 and noCommentary == 0:
                                if re.match(quoteOfCommentariesOneLine, eachLine):
                                    isCommentary = 0
                                    countLineInput += 1
                                    continue
                                countLineInput += 1
                                continue
                            elif isCommentary == 0 and noCommentary == 1:
                                continue
                            elif isCommentary == 2:
                                isCommentary = 0
                                countLineInput += 1
                                continue
                            elif isCommentary == 1 and noCommentary == 1:
                                isCommentary = 0
                                noCommentary = 0
                                continue
                            else:
                                pass

                        if searchClassicCommentariesBeginLine is not None:
                            countLineInput += 1
                        elif searchClassicCommentariesAfterLine is not None:
                            countLineInput += 1
                        else:
                            pass

        # -- Initialize vars -- #
        isCommentary = 0
        noCommentary = 0            
        
        # -- Remove commentaries -- #
        for number in recursFiles:
            countRecursFiles += 1

        print("\n[+] Running remove commentaries in {0} file(s)...\n".format(countRecursFiles))

        with tqdm(total=countRecursFiles) as pbar:
            for output in recursFiles:
                pbar.update(1)
                if re.match(blockDirs, output):
                    continue
                else:
                    # -- Remove commentaries -- #
                    with fileinput.input(output, inplace=True) as inputFile:
                        for eachLine in inputFile:
                            searchClassicCommentariesAfterLine = re.search(classicCommentariesAfterLine, eachLine)
                            searchClassicCommentariesBeginLine = re.search(classicCommentariesBeginLine, eachLine)
                            if codeArg == "python":
                                if "coding" in eachLine or "#!" in eachLine:
                                    print(eachLine)
                                    continue
                                
                                if re.match(noQuoteOfCommentaries, eachLine):
                                    noCommentary += 1
                                elif re.match(quoteOfCommentariesMultipleLine, eachLine):
                                    isCommentary += 1
                                else:
                                    pass

                                if isCommentary == 1 and noCommentary == 0:
                                    if re.match(quoteOfCommentariesOneLine, eachLine):
                                        isCommentary = 0
                                        continue
                                    continue
                                elif isCommentary == 0 and noCommentary == 1:
                                    print(eachLine)
                                    continue
                                elif isCommentary == 2:
                                    isCommentary = 0
                                    continue
                                elif isCommentary == 1 and noCommentary == 1:
                                    isCommentary = 0
                                    noCommentary = 0
                                    print(eachLine)
                                    continue
                                else:
                                    pass
                            
                            if searchClassicCommentariesBeginLine is not None:
                                eachLine = eachLine.replace(searchClassicCommentariesBeginLine.group(0), "")
                                print(eachLine)
                            elif searchClassicCommentariesAfterLine is not None:
                                eachLine = eachLine.replace(searchClassicCommentariesAfterLine.group(0), "")
                                print(eachLine)
                            else:
                                print(eachLine)

        # -- Initialize vars -- #
        isCommentary = 0
        noCommentary = 0

        # -- Check if all commentaries are removed -- #
        for output in recursFiles:
            countLineOutput = 0

            if re.match(blockDirs, output):
                continue
            else:
                with open(output, "r") as readFile:
                    countLineOutput = 0
                    readF           = readFile.readlines()

                    for eachLine in readF:
                        searchClassicCommentariesAfterLine = re.search(classicCommentariesAfterLine, eachLine)
                        searchClassicCommentariesBeginLine = re.search(classicCommentariesBeginLine, eachLine)
                        if codeArg == "python":
                            if "coding" in eachLine or "#!" in eachLine:
                                continue
                            
                            if re.match(noQuoteOfCommentaries, eachLine):
                                noCommentary += 1
                            elif re.match(quoteOfCommentariesMultipleLine, eachLine):
                                isCommentary += 1
                            else:
                                pass

                            if isCommentary == 1 and noCommentary == 0:
                                if re.match(quoteOfCommentariesOneLine, eachLine):
                                    isCommentary = 0
                                    countLineOutput += 1
                                    continue
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

                        if searchClassicCommentariesBeginLine is not None:
                            countLineOutput += 1
                        elif searchClassicCommentariesAfterLine is not None:
                            countLineOutput += 1
                        else:
                            pass

        if (Remove.LineBreaks(self, codeArg, outputArg) == 0):
            if countLineOutput == 0:
                print("\n-> {0} lines of commentaries removed\n".format(countLineInput))            
                return EXIT_SUCCESS
            else:
                return EXIT_FAILURE
        else:
            return EXIT_FAILURE

    def PrintFunc(self, codeArg, outputArg):
        countPrintLine      = 0
        countCheckPrintLine = 0
        countRecursFiles    = 0

        if codeArg == "python":
            detectPrint = r"\s{2,}print|^print"
            detectFile  = "py"
            blockDirs   = r"__pycache__"

        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), detectFile), recursive=True)]

        for number in recursFiles:
            countRecursFiles += 1

        print("\n[+] Running remove print function in {0} file(s)...\n".format(countRecursFiles))

        with tqdm(total=countRecursFiles) as pbar:
            for output in recursFiles:
                pbar.update(1)
                if re.match(blockDirs, output):
                    continue
                else:
                    # -- Remove all print functions -- #
                    with fileinput.input(output, inplace=True) as inputFile:
                        for eachLine in inputFile:
                        
                            if re.match(detectPrint, eachLine):
                                countPrintLine += 1
                                continue
                            else:
                                print(eachLine)

        # -- Check if all print functions are removed -- #
        for output in recursFiles:
            if re.match(blockDirs, output):
                continue
            else:
                with open(output, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if re.match(detectPrint, eachLine):
                            countCheckPrintLine += 1

        if (Remove.LineBreaks(self, codeArg, outputArg) == 0):
            if countCheckPrintLine == 0:
                print("\n-> {0} lines of print functions removed\n".format(countPrintLine))
                return EXIT_SUCCESS
            else:
                return EXIT_FAILURE
        else:
            return EXIT_FAILURE

