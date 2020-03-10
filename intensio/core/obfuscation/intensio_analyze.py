# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import shutil
import os
import sys
import glob
import re
from progress.bar import Bar

from core.utils.intensio_utils import Utils, Colors

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
                                                                                    self.utils.Platform(
                                                                                                        getOS=False, 
                                                                                                        getPathType=True
                                                                                    ), 
                                                                                    detectFiles), 
                                                                                    recursive=True
                                                                            )
                ]
 
                if recursFiles == []:
                    print(Colors.ERROR + "[-] {} directory empty or python file not found".format(inputArg) + Colors.DISABLE)
                    return 1

                for number in recursFiles:
                    countRecursFiles += 1
                
                print("\n[+] Running analyze input of {} file(s)...\n".format(countRecursFiles))
                
                with Bar("Analysis    ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
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
                                    print("-> {}".format(file))
                        
                                for file in inputFileEmpty:
                                    print("-> {} : empty".format(file))
                    
                        return 0
                
                    elif inputFileFoundCount == inputFileEmptyCount and inputFileFoundCount > 0:
                        print(Colors.ERROR + "[-] All files in directory specified are emtpy !" + Colors.DISABLE)
                        return 1
                    else:
                        print(Colors.ERROR + "[-] No file available in '{}'.".format(inputArg) + Colors.DISABLE)
                        return 1
            else:
                print(Colors.ERROR + "[-] '{}' is not a directory".format(inputArg) + Colors.DISABLE)
                return 1
        else:
            print(Colors.ERROR + "[-] '{}' not exists".format(inputArg) + Colors.DISABLE)
            return 1


    def OutputAvailable(self, inputArg, outputArg, verboseArg):
        outputFileFound         = []
        outputFileEmpty         = []
        outputFileFoundCount    = 0
        outputFileEmptyCount    = 0
        countRecursFiles        = 0

        if os.path.exists(outputArg) == True:
            deleteRequest = input("[!] Output '{}' already exists, do you want delete it ? (Y/N) : ".format(outputArg))
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
                                                                                                    self.utils.Platform(
                                                                                                                getOS=False, 
                                                                                                                getPathType=True
                                                                                                    ), 
                                                                                                    detectFiles), 
                                                                                                    recursive=True
                                                                                            )
                                ]

                                for number in recursFiles:
                                    countRecursFiles += 1

                                print("\n[+] Running analyze output of {} file(s)...\n".format(countRecursFiles))

                                if recursFiles == []:
                                    print(Colors.ERROR + "[-] {} directory empty, no copied file".format(inputArg) + \
                                        Colors.DISABLE)
                                    return 1
                                                                
                                with Bar("Analysis    ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
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
                                                    print("-> {}".format(file))
                                            
                                                for file in outputFileEmpty:
                                                    print("-> {} : empty".format(file))
                                                
                                        return 0
                                    else:
                                        print(Colors.ERROR + "[-] No files available in '{}'".format(outputArg) + Colors.DISABLE)
                                        return 1
                            else:
                                print(Colors.ERROR + "[-] Copy '{}' to '{}' failed, this is not a output directory copied"\
                                    .format(inputArg, outputArg) + Colors.DISABLE)
                                return 1
                        else:
                            print(Colors.ERROR + "[-] Copy '{}' to '{}' failed".format(inputArg, outputArg) + Colors.DISABLE)
                            return 1
                    else:
                        print(Colors.ERROR + "[-] Delete '{}' failed".format(outputArg) + Colors.DISABLE)
                        return 1

                except Exception as e:
                    print(Colors.ERROR + "[-] {}".format(e) + Colors.DISABLE)
                    return 1
            else:
                print(Colors.ERROR + "[-] Delete '{}' failed, the user has refused".format(outputArg) + Colors.DISABLE)
                return 1
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
                                                                                            self.utils.Platform(
                                                                                                                getOS=False, 
                                                                                                                getPathType=True
                                                                                            ), 
                                                                                            detectFiles), 
                                                                                            recursive=True
                                                                                    )
                        ]

                        for number in recursFiles:
                            countRecursFiles += 1

                        print("\n[+] Running analyze output of {} file(s)...\n".format(countRecursFiles))

                        if recursFiles == []:
                            print(Colors.ERROR + "[-] {} directory empty, no copied file".format(inputArg) + Colors.DISABLE)
                            return 1
                                                
                        with Bar("Analysis    ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
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
                                            print("-> {} : copy".format(file))
                                    
                                        for file in outputFileEmpty:
                                            print("-> {} : copy empty".format(file))
                                
                                return 0   
                            else:
                                print(Colors.ERROR + "[-] No files available in '{}'".format(outputArg) + Colors.DISABLE)
                                return 1                
                    else:
                        print(Colors.ERROR + "[-] Copy '{}' to '{}' failed, this is not a output directory copied !"\
                            .format(inputArg, outputArg) + Colors.DISABLE)
                        return 1
                else:
                    print(Colors.ERROR + "[-] Copy '{}' to '{}' failed".format(inputArg, outputArg) + Colors.DISABLE)
                    return 1

            except Exception as e:
                print(Colors.ERROR + "[-] {}".format(e) + Colors.DISABLE)
                return 1


    
            