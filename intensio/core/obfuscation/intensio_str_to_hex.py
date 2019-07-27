# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import glob
import re
import tqdm
import fileinput

from core.utils.intensio_utils import Utils
from core.obfuscation.intensio_mixer import Mixer
from core.obfuscation.intensio_remove import Remove
from core.utils.intensio_error import EXIT_SUCCESS, EXIT_FAILURE

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

def StringsToHex(codeArg, outputArg, mixerLevelArg):
    getLetterLineList   = []
    countRecursFiles    = 0
    checkPrint          = 0
    checkHexError       = False
    checkPrintError     = False
    hexLine             = ""
    utils               = Utils()
    mixer               = Mixer()
    remove              = Remove()

    if codeArg == "python":
        detectFile          = "py"
        blockDirs           = "__pycache__"

    recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, utils.Platform(), detectFile), recursive=True)]

    for number in recursFiles:
            countRecursFiles += 1

    print("\n[+] Running replace all strings to their hexadecimal value in {0} file(s)...\n".format(countRecursFiles))

    # -- Replace all strings to their hexadecimal value -- #
    with tqdm.tqdm(total=countRecursFiles) as pbar:
        for file in recursFiles:
            checkPrint = 0 # initialize check print() func at the begining of each file
            pbar.update(1)
            if blockDirs in file:
                continue
            else:
                # -- Add a new first random line and move the old first line to the second line to avoid replacing it -- #
                with open(file, "r") as inputFile:
                    stringRandomMixer = mixer.GetStringMixer(mixerLevelArg)
                    firstLine = "{0}\n".format(stringRandomMixer)
                    line      = inputFile.readlines()
                    line.insert(0, firstLine)

                with open(file, "w") as inputFile:
                    inputFile.writelines(line)

                # -- Replace all lines-- #
                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        if checkPrint == 0:
                            varMixer = mixer.GetStringMixer(mixerLevelArg)
                            print(varMixer + "=\"\"\"")
                            checkPrint = 1   
                        else:
                            getLetterLineList = [] # initialize list     
                            for letterLine in eachLine:
                                letterToHex = "\\x" + str(letterLine.encode().hex())
                                getLetterLineList.append(letterToHex) # Get list of all letters in line          
                            hexLine = "".join(getLetterLineList)
                            print(hexLine)
                
                with open(file, "a") as inputFile:
                    inputFile.write("\"\"\"")
                    inputFile.write("\nexec({0})".format(varMixer))

    # -- Check if all line are replaced of hexadecimal value -- #
    for file in recursFiles: 
        with open(file, "r") as inputFile:
            for eachLine in inputFile:
                if blockDirs in file:
                    continue
                else:
                    if not eachLine:
                        continue
                    else:
                        if not re.match(r"\\x", eachLine) and re.match(r"[\'|\"]{3}", eachLine):
                            checkError = True
    
    if (remove.Backslashes(codeArg, outputArg) == 0):
        if checkHexError == False:
            return EXIT_SUCCESS        
        else:
            return EXIT_FAILURE
    else:
        return EXIT_FAILURE





                        



