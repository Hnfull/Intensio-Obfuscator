# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import re
import fileinput
import glob

from core.utils.intensio_error import EXIT_SUCCESS, EXIT_FAILURE
from core.utils.intensio_utils import Utils

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Remove:
    def __init__(self):
        self.utils = Utils()

    def NewLines(self, oneFileArg, codeArg, outputArg):
        checkLine       = 0
        numberFiles     = 0
        numberCheckGood = 0
        
        # -- One file -- #
        if oneFileArg:
            # -- Delete new lines -- #
            with fileinput.FileInput(outputArg, inplace=True) as inputFile:
                for line in inputFile:
                    if line.strip():
                        print(line.rstrip())

            # -- Check if all new lines are deleted -- #
            with open(outputArg, "r") as readFile:
                readF = readFile.readlines()
                for eachLine in readF:
                    if eachLine == "\n":
                        checkLine += 1
                    if checkLine == 0:
                        return EXIT_SUCCESS
                    else:
                        return EXIT_FAILURE

        # -- Multiple files -- #
        else:
            if codeArg == "python":
                inputExt    = "py"
                blockdirs   = r"__pycache__"

            recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), inputExt), recursive=True)]

            # -- Delete new lines -- #
            for output in recursFiles:
                if re.match(blockdirs, output):
                    continue
                else:
                    with fileinput.FileInput(output, inplace=True) as inputFile:
                        for line in inputFile:
                            if line.strip():
                                print(line.rstrip())

            # -- Check if all new lines are deleted -- #
            for output in recursFiles:
                checkLine = 0 # Initialize check vars for the next file 

                if re.match(blockdirs, output):
                    continue
                else:
                    with open(output, "r") as readFile:
                        readF = readFile.readlines()
                        for eachLine in readF:
                            if eachLine == "\n":
                                checkLine += 1
                            if checkLine == 0:
                                numberCheckGood += 1
                                numberFiles     += 1
                            else:
                                numberCheckGood += 0
                                numberFiles     += 1
                        
            if numberCheckGood == numberFiles:
                return EXIT_SUCCESS
            else:
                return EXIT_FAILURE

    def Commentaries(self, oneFileArg, codeArg, outputArg):
        countLine       = 0
        numberFiles     = 0
        numberCheckGood = 0

        pythonCommentariesRegex = r"\#+.*"

        if codeArg == "python":
            commentariesDefine = pythonCommentariesRegex

        print("########## [ Commentaries delete ] ##########\n")

        # -- One file -- #
        if oneFileArg:
            # -- Count commentaries will be deleted -- #
            with open(outputArg, "r") as readFile:
                readF = readFile.readlines()
                for eachLine in readF:
                    search = re.search(commentariesDefine, eachLine)
                    if "coding" in eachLine or "#!" in eachLine:
                        continue
                    else:
                        if search is not None:
                            countLine += 1
                    
                print("-> {0} lines of commentaries deleted\n".format(countLine))

            # -- Remove commentaries -- #
            with fileinput.input(outputArg, inplace=True) as inputFile:
                for eachLine in inputFile:
                    search = re.search(commentariesDefine, eachLine)
                    if "coding" in eachLine or "#!" in eachLine:
                        print(eachLine)
                        continue
                    else:
                        if search is not None:
                            eachLine = eachLine.replace(search.group(0), "")
                            print(eachLine.rstrip())
                        else:
                            print(eachLine.rstrip())

            # -- Check if all commentaries are deleted -- #
            with open(outputArg, "r") as readFile:
                countLine   = 0
                readF       = readFile.readlines()

                for eachLine in readF:
                    search = re.search(commentariesDefine, eachLine)
                    if "coding" in eachLine or "#!" in eachLine:
                        continue
                    else:
                        if search is not None:
                            countLine += 1

            if countLine == 0:
                if (Remove.NewLines(self, oneFileArg, codeArg, outputArg) == 0):
                    return EXIT_SUCCESS
                else:
                    return EXIT_FAILURE
            else:
                return EXIT_FAILURE

        # -- Multiple files -- #
        else:
            if codeArg == "python":
                inputExt    = "py"
                blockdirs   = r"__pycache__"

            recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), inputExt), recursive=True)]

            # -- Count commentaries will be deleted -- #
            for output in recursFiles:
                if re.match(blockdirs, output):
                    continue
                else:
                    with open(output, "r") as readFile:
                        readF = readFile.readlines()
                        for eachLine in readF:
                            search = re.search(commentariesDefine, eachLine)
                            if "coding" in eachLine or "#!" in eachLine:
                                continue
                            else:
                                if search is not None:
                                    countLine += 1
                            
            print("-> {0} lines of commentaries deleted\n".format(countLine))

            # -- Remove commentaries -- #
            for output in recursFiles:
                if re.match(blockdirs, output):
                    continue
                else:
                    # -- Remove commentaries -- #
                    with fileinput.input(output, inplace=True) as inputFile:
                        for eachLine in inputFile:
                            search = re.search(commentariesDefine, eachLine)
                            if "coding" in eachLine or "#!" in eachLine:
                                print(eachLine)
                                continue
                            else:
                                if search is not None:
                                    eachLine = eachLine.replace(search.group(0), "")
                                    print(eachLine.rstrip())
                                else:
                                    print(eachLine.rstrip())

            # -- Check if all commentaries are deleted -- #
            for output in recursFiles:
                countLine = 0

                if re.match(blockdirs, output):
                    continue
                else:
                    with open(output, "r") as readFile:
                        countLine   = 0
                        readF       = readFile.readlines()

                        for eachLine in readF:
                            search = re.search(commentariesDefine, eachLine)
                            if "coding" in eachLine or "#!" in eachLine:
                                continue
                            else:
                                if search is not None:
                                    countLine += 1

                    if countLine == 0:  
                        numberCheckGood += 1
                        numberFiles     += 1
                    else:
                        numberCheckGood += 0
                        numberFiles += 1

            if numberCheckGood == numberFiles:
                if (Remove.NewLines(self, oneFileArg, codeArg, outputArg) == 0):
                    return EXIT_SUCCESS
                else:
                    return EXIT_FAILURE
            else:
                return EXIT_FAILURE