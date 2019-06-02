 # -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import shutil
import os
import glob
import re

from core.utils.intensio_utils import Utils
from core.utils.intensio_error import EXIT_SUCCESS, ERROR_FILE_NOT_FOUND, ERROR_PATH_NOT_FOUND,ERROR_FILE_EMPTY,\
                                ERROR_BAD_FILE_TYPE, ERROR_BAD_ARGUMENTS, ERROR_CANNOT_COPY, ERROR_CANNOT_REMOVE, \
                                ERROR_NOT_DIR, ERROR_NOT_FILE, EXIT_FAILURE

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Analyze:

    def __init__(self):
        self.utils = Utils()

    def InputAvailable(self, oneFileArg, inputArg, codeArg):
        inputFileFound      = []
        inputFileEmpty      = []
        inputFileFoundCount = 0
        inputFileEmptyCount = 0
        inputExt            = ""

        # -- One file -- #
        if oneFileArg == True:
            if os.path.exists(inputArg) == True:
                if os.path.isfile(inputArg) == True:
                    if codeArg == "python":
                        if ".py" in inputArg:
                            if os.path.getsize(inputArg) > 0:
                                return EXIT_SUCCESS         
                            else:
                                print("[-] '{0}' is empty.".format(inputArg))
                                return ERROR_FILE_EMPTY
                        else:
                            print("[-] '{0}' is not python file.".format(inputArg))
                            return ERROR_BAD_FILE_TYPE
                else:
                    print("[-] '{0}' is not a file.".format(inputArg))
                    return ERROR_BAD_FILE_TYPE
            else:
                print("[-] '{0}' not exists.".format(inputArg))
                return ERROR_PATH_NOT_FOUND

        # -- Multiple files -- #
        else:
            if os.path.exists(inputArg) == True:
                if os.path.isdir(inputArg) == True:     
                    if codeArg == "python":
                        inputExt    = "py"
                        blockdirs   = r"__pycache__"

                    recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(inputArg, self.utils.Platform(), inputExt), recursive=True)]
        
                    for output in recursFiles:
                        if re.match(blockdirs, output):
                            continue
                        else:
                            if os.path.getsize(output) > 0:
                                inputFileFound.append(output)
                                inputFileFoundCount += inputFileFoundCount + 1
                            else:
                                inputFileEmpty.append(output)
                                inputFileEmptyCount += inputFileEmptyCount + 1

                    if inputFileFoundCount >= 2 and inputFileEmptyCount < 2:
                        return EXIT_SUCCESS
                    elif inputFileFoundCount == 1:
                        print("[-] Only one file available found in '{0}', select [-f --onefile] argument.".format(inputArg))
                        return ERROR_BAD_ARGUMENTS
                    elif inputFileFoundCount == inputFileEmptyCount and inputFileEmptyCount > 0 and inputFileEmptyCount > 0:
                        print("[-] All files output specified are emtpy !.")
                        return ERROR_FILE_EMPTY
                    else:
                        print("[-] No file available in '{0}'.".format(inputArg))
                        return ERROR_FILE_NOT_FOUND
                else:
                    print("[-] '{0}' is not a directory.".format(inputArg))
                    return ERROR_NOT_DIR
            else:
                print("'{0}' not exists.".format(inputArg))
                return ERROR_PATH_NOT_FOUND
    
    def OutputAvailable(self, oneFileArg, inputArg, codeArg, outputArg):
        outputFileFound         = []
        outputFileEmpty         = []
        outputFileFoundCount    = 0
        outputFileEmptyCount    = 0
        outputExt               = ""

        if os.path.exists(outputArg) == True:
            removeRequest = input("[!] output '{0}' already exists, do you want remove it ? (Y/N) : ".format(outputArg))
            removeRequest = removeRequest.upper()
            if removeRequest == "Y":
                # -- One file -- #
                if oneFileArg == True:
                    try:
                        os.remove(outputArg)
                        if os.path.exists(outputArg) == False:
                            shutil.copy(inputArg, outputArg)
                            if os.path.exists(outputArg) == True:
                                if os.path.isfile(outputArg) == True:
                                    if os.path.getsize(outputArg) > 0:
                                        return  EXIT_SUCCESS
                                    else:
                                        print("[-] Copy '{0}' to '{1}' failed, the files is empty !.".format(inputArg, outputArg))
                                        return ERROR_FILE_EMPTY
                                else:
                                    print("[-] Copy '{0}' to '{1}' failed, this is not a output file copy !.".format(inputArg, outputArg))
                                    return ERROR_NOT_FILE
                            else:
                                print("[-] Copy '{0}' to '{1}' failed.".format(inputArg, outputArg))
                                return ERROR_CANNOT_COPY
                        else:
                            print("[-] Remove '{0}' failed.".format(outputArg))
                            return ERROR_CANNOT_REMOVE

                    except Exception as e:
                        print("[-] {0}".format(e))
                        return EXIT_FAILURE

                # -- Multiple files -- #
                else:
                    try:
                        shutil.rmtree(outputArg)
                        if os.path.exists(outputArg) == False:
                            shutil.copytree(inputArg, outputArg)
                            if os.path.exists(outputArg) == True:
                                if os.path.isdir(outputArg) == True:
                                    if codeArg == "python":
                                        inputExt    = "py"
                                        blockdirs   = r"__pycache__"

                                    recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(inputArg, self.utils.Platform(), inputExt), recursive=True)]
                        
                                    for output in recursFiles:
                                        if re.match(blockdirs, output):
                                            continue
                                        else:
                                            if os.path.getsize(output) > 0:
                                                outputFileFound.append(output)
                                                outputFileFoundCount += outputFileFoundCount + 1
                                            else:
                                                outputFileEmpty.append(output)
                                                outputFileEmptyCount += outputFileEmptyCount + 1

                                    if outputFileFoundCount >= 2 and outputFileEmptyCount < 2:
                                        return EXIT_SUCCESS
                                    else:
                                        print("[-] No files available in '{0}'.".format(outputArg))
                                        return ERROR_FILE_NOT_FOUND
                                else:
                                    print("[-] Copy '{0}' to '{1}' failed, this is not a output directory copied !.".format(inputArg, outputArg))
                                    return ERROR_NOT_DIR
                            else:
                                print("[-] Copy '{0}' to '{1}' failed.".format(inputArg, outputArg))
                                return ERROR_CANNOT_COPY
                        else:
                            print("[-] Remove '{0}' failed.".format(outputArg))
                            return ERROR_CANNOT_REMOVE

                    except Exception as e:
                        print("[-] {0}".format(e))
                        return EXIT_FAILURE
            else:
                print("[-] Remove '{0}' failed, the user has refused.".format(outputArg))
                return ERROR_CANNOT_REMOVE
        else:
            # -- One file -- #
            if oneFileArg == True:
                try:
                    shutil.copy(inputArg, outputArg)
                    if os.path.exists(outputArg) == True:
                        if os.path.isfile(outputArg) == True:
                            if os.path.getsize(outputArg) > 0:
                                return EXIT_SUCCESS
                            else:
                                print("[-] Copy '{0}' to '{1}' failed, the file is empty !.".format(inputArg, outputArg))
                                return ERROR_CANNOT_COPY
                        else:
                            print("[-] Copy '{0}' to '{1}' failed, this is not a output file copied !.".format(inputArg, outputArg))
                            return ERROR_NOT_FILE
                    else:
                        print("[-] Copy '{0}' to '{1}' failed.".format(inputArg, outputArg))
                        return ERROR_CANNOT_COPY

                except Exception as e:
                    print("[-] {0}".format(e))
                    return EXIT_FAILURE

            # -- Multiple files -- #
            else:
                try:
                    shutil.copytree(inputArg, outputArg)
                    if os.path.exists(outputArg) == True:
                        if os.path.isdir(outputArg) == True:
                            if codeArg == "python":
                                inputExt    = "py"
                                blockdirs   = r"__pycache__"

                            recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(inputArg, self.utils.Platform(), inputExt), recursive=True)]
                
                            for output in recursFiles:
                                if re.match(blockdirs, output):
                                    continue
                                else:
                                    if os.path.getsize(output) > 0:
                                        outputFileFound.append(output)
                                        outputFileFoundCount += outputFileFoundCount + 1
                                    else:
                                        outputFileEmpty.append(output)
                                        outputFileEmptyCount += outputFileEmptyCount + 1

                            if outputFileFoundCount >= 2 and outputFileEmptyCount < 2:
                                return EXIT_SUCCESS
                            else:
                                print("[-] No files available in '{0}'.".format(outputArg))
                                return ERROR_FILE_NOT_FOUND
                        else:
                            print("[-] Copy '{0}' to '{1}' failed, this is not a output directory copied !.".format(inputArg, outputArg))
                            return ERROR_NOT_DIR
                    else:
                        print("[-] Copy '{0}' to '{1}' failed.".format(inputArg, outputArg))
                        return ERROR_CANNOT_COPY

                except Exception as e:
                    print("[-] {0}".format(e))
                    return EXIT_FAILURE


    
            