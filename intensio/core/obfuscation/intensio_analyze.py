# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import shutil
import os
import glob
import re
import colorama
from progress.bar import Bar

from core.utils.intensio_utils import Utils
from core.utils.intensio_error import EXIT_SUCCESS, ERROR_FILE_NOT_FOUND, ERROR_PATH_NOT_FOUND,ERROR_FILE_EMPTY,\
                                        ERROR_CAN_NOT_COPY, ERROR_CAN_NOT_DELETE, ERROR_DIR_NOT_FOUND, EXIT_FAILURE, \
                                        ERROR_DIR_EMPTY

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

ERROR_COLOUR    = colorama.Back.RED + colorama.Style.BRIGHT
PROGRESS_COLOUR = colorama.Fore.BLUE + colorama.Style.BRIGHT 

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Analyze:
    

    def __init__(self):
        self.utils = Utils()


    def InputAvailable(self, inputArg, verboseArg):
        inputFileFound      = []
        inputFileEmpty      = []
        inputFileFoundCount = 0
        inputFileEmptyCount = 0
        countRecursFiles    = 0 
        numberLine          = 0

        if os.path.exists(inputArg) == True:
            if os.path.isdir(inputArg) == True:     
                detectFiles = "py"
                blockDir    = "__pycache__"

                recursFiles = [
                                file for file in glob.glob("{0}{1}**{1}*.{2}".format(
                                                                                    inputArg, 
                                                                                    self.utils.Platform(), 
                                                                                    detectFiles), 
                                                                                    recursive=True
                                                                            )
                ]
 
                if recursFiles == []:
                    print(ERROR_COLOUR + "[-] {0} directory empty or python file not found".format(inputArg))
                    return ERROR_DIR_EMPTY

                for number in recursFiles:
                    countRecursFiles += 1
                
                print("\n[+] Running analyze input of {0} file(s)...\n".format(countRecursFiles))
                
                with Bar(PROGRESS_COLOUR + "Analysis    ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
                    for file in recursFiles:
                        if blockDir in file:
                            continue
                        else:
                            if os.path.getsize(file) > 0:
                                inputFileFound.append(file)
                                inputFileFoundCount += inputFileFoundCount + 1
                            else:
                                inputFileEmpty.append(file)
                                inputFileEmptyCount += inputFileEmptyCount + 1

                        bar.next(1)
                    bar.finish()

                    if inputFileFoundCount >= 1 and inputFileEmptyCount < inputFileFoundCount:
                        if verboseArg:
                            print("\n\n[+] File input found :\n")
                            
                            if inputFileFound == []:
                                print("-> no result")
                            else:
                                for file in inputFileFound:
                                    print("-> {0}".format(file))
                        
                                for file in inputFileEmpty:
                                    print("-> {0} : empty".format(file))
                    
                        return EXIT_SUCCESS
                
                    elif inputFileFoundCount == inputFileEmptyCount and inputFileFoundCount > 0:
                        print(ERROR_COLOUR + "[-] All files in directory specified are emtpy !")
                        return ERROR_FILE_EMPTY
                    else:
                        print(ERROR_COLOUR + "[-] No file available in '{0}'.".format(inputArg))
                        return ERROR_FILE_NOT_FOUND
            else:
                print(ERROR_COLOUR + "[-] '{0}' is not a directory".format(inputArg))
                return ERROR_DIR_NOT_FOUND
        else:
            print(ERROR_COLOUR + "[-] '{0}' not exists".format(inputArg))
            return ERROR_PATH_NOT_FOUND


    def OutputAvailable(self, inputArg, outputArg, verboseArg):
        outputFileFound         = []
        outputFileEmpty         = []
        outputFileFoundCount    = 0
        outputFileEmptyCount    = 0
        countRecursFiles        = 0

        if os.path.exists(outputArg) == True:
            deleteRequest = input("[!] Output '{0}' already exists, do you want delete it ? (Y/N) : ".format(outputArg))
            deleteRequest = deleteRequest.upper()
            if deleteRequest == "Y":
                try:
                    shutil.rmtree(outputArg)
                    if os.path.exists(outputArg) == False:
                        shutil.copytree(inputArg, outputArg)
                        if os.path.exists(outputArg) == True:
                            if os.path.isdir(outputArg) == True:
                                detectFiles = "py"
                                blockDir    = "__pycache__"

                                recursFiles = [
                                                file for file in glob.glob("{0}{1}**{1}*.{2}".format(
                                                                                                    outputArg, 
                                                                                                    self.utils.Platform(), 
                                                                                                    detectFiles), 
                                                                                                    recursive=True
                                                                                            )
                                ]


                                for number in recursFiles:
                                    countRecursFiles += 1

                                print("\n[+] Running analyze output of {0} file(s)...\n".format(countRecursFiles))

                                if recursFiles == []:
                                    print(ERROR_COLOUR + "[-] {0} directory empty, no copied file".format(inputArg))
                                    return ERROR_DIR_EMPTY
                                                                
                                with Bar(PROGRESS_COLOUR + "Analysis    ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
                                    for file in recursFiles:
                                        if blockDir in file:
                                            continue
                                        else:
                                            if os.path.getsize(file) > 0:
                                                outputFileFound.append(file)
                                                outputFileFoundCount += outputFileFoundCount + 1
                                            else:
                                                outputFileEmpty.append(file)
                                                outputFileEmptyCount += outputFileEmptyCount + 1

                                        bar.next(1)
                                    bar.finish()
                                
                                    if outputFileFoundCount >= 1 and outputFileFoundCount > outputFileEmptyCount:
                                        if verboseArg:
                                            print("\n\n[+] Output files copy :\n")

                                            if outputFileFound == []:
                                                print("-> no result")
                                            else:
                                                for file in outputFileFound:
                                                    print("-> {0}".format(file))
                                            
                                                for file in outputFileEmpty:
                                                    print("-> {0} : empty".format(file))
                                                
                                        return EXIT_SUCCESS
                                    else:
                                        print(ERROR_COLOUR + "[-] No files available in '{0}'".format(outputArg))
                                        return ERROR_FILE_NOT_FOUND
                            else:
                                print(ERROR_COLOUR + "[-] Copy '{0}' to '{1}' failed, this is not a output directory copied".format(inputArg, outputArg))
                                return ERROR_DIR_NOT_FOUND
                        else:
                            print(ERROR_COLOUR + "[-] Copy '{0}' to '{1}' failed".format(inputArg, outputArg))
                            return ERROR_CAN_NOT_COPY
                    else:
                        print(ERROR_COLOUR + "[-] Delete '{0}' failed".format(outputArg))
                        return ERROR_CAN_NOT_DELETE

                except Exception as e:
                    print(ERROR_COLOUR + "[-] {0}".format(e))
                    return EXIT_FAILURE
            else:
                print(ERROR_COLOUR + "[-] Delete '{0}' failed, the user has refused".format(outputArg))
                return ERROR_CAN_NOT_DELETE
        else:    
            try:
                shutil.copytree(inputArg, outputArg)
                if os.path.exists(outputArg) == True:
                    if os.path.isdir(outputArg) == True:
                        detectFiles = "py"
                        blockDir    = "__pycache__"

                        recursFiles = [
                                        file for file in glob.glob("{0}{1}**{1}*.{2}".format(
                                                                                            outputArg, 
                                                                                            self.utils.Platform(), 
                                                                                            detectFiles), 
                                                                                            recursive=True
                                                                                    )
                        ]


                        for number in recursFiles:
                            countRecursFiles += 1

                        print("\n[+] Running analyze output of {0} file(s)...\n".format(countRecursFiles))

                        if recursFiles == []:
                            print(ERROR_COLOUR + "[-] {0} directory empty, no copied file".format(inputArg))
                            return ERROR_DIR_EMPTY
                                                
                        with Bar(PROGRESS_COLOUR + "Analysis    ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
                            for file in recursFiles:
                                if blockDir in file:
                                    continue
                                else:
                                    if os.path.getsize(file) > 0:
                                        outputFileFound.append(file)
                                        outputFileFoundCount += outputFileFoundCount + 1
                                    else:
                                        outputFileEmpty.append(file)
                                        outputFileEmptyCount += outputFileEmptyCount + 1

                                bar.next(1)
                            bar.finish()    

                            if outputFileFoundCount >= 1 and outputFileFoundCount > outputFileEmptyCount:
                                if verboseArg:
                                    print("\n\n[+] File output found :\n")

                                    if outputFileFound == []:
                                        print("-> no result")
                                    else:
                                        for file in outputFileFound:
                                            print("-> {0} : copy".format(file))
                                    
                                        for file in outputFileEmpty:
                                            print("-> {0} : copy empty".format(file))
                                
                                return EXIT_SUCCESS   
                            else:
                                print(ERROR_COLOUR + "[-] No files available in '{0}'".format(outputArg))
                                return ERROR_FILE_NOT_FOUND                
                    else:
                        print(ERROR_COLOUR + "[-] Copy '{0}' to '{1}' failed, this is not a output directory copied !".format(inputArg, outputArg))
                        return ERROR_DIR_NOT_FOUND
                else:
                    print(ERROR_COLOUR + "[-] Copy '{0}' to '{1}' failed".format(inputArg, outputArg))
                    return ERROR_CAN_NOT_COPY

            except Exception as e:
                print(ERROR_COLOUR + "[-] {0}".format(e))
                return EXIT_FAILURE


    
            