# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import re
import fileinput
import glob
import os
import keyword

from core.obfuscation.intensio_mixer import Mixer
from core.obfuscation.intensio_remove import Remove
from core.utils.intensio_error import BreakLoop, EXIT_SUCCESS, EXIT_FAILURE
from core.utils.intensio_utils import Utils

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Replace:

    def __init__(self):
        self.mixer      = Mixer()
        self.remove     = Remove()
        self.utils      = Utils()
        self.exclude    = "excluded_variables.txt"

    def EachLine(self, codeArg, eachLine, Dict):
        getIndexLineList    = []
        returnLine          = []
        charValue           = []
        checkCharAfterWord  = 1
        wordSetter          = 0
        checkGetKey         = ""
        checkGetWord        = ""
        getLine             = ""
        breakLine           = ""

        # -- Get list of all letters in line -- #
        for indexLine, letterLine in enumerate(eachLine):
            getIndexLineList.append(letterLine)

        # -- Loop in each letter of line -- #
        for indexLine, letterLine in enumerate(eachLine):
            # -- Add in final line list all chars mixed -- #
            if charValue != []:
                for obfIndex, obfValue in enumerate(charValue):
                    if obfIndex == 0: # First letter in string mixed are already add in the final line
                        continue
                    returnLine.append(obfValue)
                charValue = []

                # -- If the variable is only a letter, check if the next character is specific so as not to replace it -- #
                if re.match(r"(\.)|(:)|(\))|(\()|(=)|(\[)|(\])|({)|(})|(,)|(\+)|(\s)", letterLine):
                    returnLine.append(letterLine)

                # -- Count indexes of word to move after it --#
                countDeleteIndex = 0
                for i in getWord:
                    countDeleteIndex += 1
                wordSetter = countDeleteIndex - 2 # -2 Is to letter already append and the letter in progress
            else:
                # -- The index numbers of variable is decremented to add the mixed letters that be replaced -- #
                if wordSetter > 0:
                    wordSetter -= 1
                    continue
                else:
                    try:
                        # -- Loop in the dictionary with already mixed values-- #
                        for key, value in Dict:
                            for indexKey, letterKey in enumerate(key):
                                for letterValue in value:
                                    # -- Check if letter of word is equal to letter of key -- #
                                    if letterKey == letterLine:
                                        # -- Begin process to check  -- #
                                        if indexKey == 0:
                                            # -- Place index position after the word -- #
                                            indexExplore = indexLine + len(key)

                                            # -- If indexError return to next loop -- #
                                            try:
                                                getIndexLineList[indexExplore]
                                            except IndexError: 
                                                continue

                                            # -- Check the char after the word -- #
                                            if codeArg == "python":
                                                if re.match(r"(\.)|(:)|(\))|(\()|(=)|(\[)|(\])|({)|(})|(,)|(\+)|(\s)", getIndexLineList[indexExplore]):
                                                    # -- Check word finded is not into the other word -- #
                                                    indexExplore = indexLine - 1
                                                    if not re.match(r"(\w)", getIndexLineList[indexExplore]):
                                                        # -- Check if it's 'from' and 'import' word key in line to avoid replace name of file if variable is identic name to file -- #
                                                        getLine = "".join(getIndexLineList)
                                                        if "import" in getLine:
                                                            if "from" in getLine:
                                                                # -- Cut the line from the current index and check if it is not there is the keyword "import" in the line -- #
                                                                breakLine = getIndexLineList[:indexLine]
                                                                breakLine = "".join(breakLine)
                                                                if not "import" in breakLine:
                                                                    # -- It's file because only 'from'key word -- #
                                                                    checkCharAfterWord = 1
                                                                else:
                                                                    checkCharAfterWord = 0
                                                            else:
                                                                checkCharAfterWord = 0
                                                        else:
                                                            checkCharAfterWord = 0
                                                    else:
                                                        checkCharAfterWord = 1
                                                else:
                                                    checkCharAfterWord = 1

                                            if checkCharAfterWord == 0:
                                                # -- Initialize vars -- #
                                                getCharAllInKey     = []
                                                getWord             = []

                                                indexExploreStart   = indexLine
                                                indexExploreEnd     = indexLine + len(key) - 1 # Remove -1, first letter is already increment

                                                # -- List contain all letters of key -- #
                                                for getLetterKey in key:
                                                    getCharAllInKey.append(getLetterKey)

                                                # -- Check if all letters of key is equal to all letters of word -- #
                                                for indexCheckLetter, checkLetter in enumerate(getIndexLineList):
                                                    if indexCheckLetter >= indexExploreStart and indexCheckLetter <= indexExploreEnd:
                                                        getWord.append(checkLetter)

                                                # -- Check if number of chars in key equal number of chars in word -- #
                                                if list(set(getCharAllInKey) - set(getWord)) == []:
                                                    checkGetWord    = "".join(getWord)
                                                    checkGetKey     = "".join(getCharAllInKey)

                                                    # -- Check if key == word -- #
                                                    if checkGetWord == checkGetKey:
                                                        for obfChar in value:
                                                            charValue.append(obfChar)

                                                        letterLine = letterValue
                                                        raise BreakLoop
                                                    else:
                                                        continue
                                                else:
                                                    continue
                                            else:
                                                continue
                                        else:
                                            continue
                                    else:
                                        continue

                        raise BreakLoop

                    except BreakLoop:
                        returnLine.append(letterLine)

        # -- Rewrite the line -- #
        returnLine = "".join(returnLine)
        return returnLine[:]
    
    def VarsDefinedByUser(self, oneFileArg, codeArg, outputArg, mixerLevelArg):
        variablesDict       = {}
        removeDict          = []
        checkVarsMixed      = []
        wordsExcluded       = []
        wordsExcludedFound  = []
        checkCountVarsMixed = 0
        checkCountVarsValue = 0

        pythonVariablesRegex        = r"(^\w+|\w+)([\s|^\s]*=[\s|\w|\"|\'])"    # Classic variables
        pythonConditionErrorRegex   = r"except(\s+\w+\sas\s)(\w)"               # Error variables
        pythonConditionLoopRegex    = r"for\s([\w\s?\,?]{1,})(\sin)"            # Loop variables
        pythonFunctionsRegex        = r"def\s(\w+)"                             # Functions
        pythonClassRegex            = r"class\s(\w+)"                           # Class

        if codeArg == "python":
            variablesDefined        = pythonVariablesRegex
            variablesErrorDefined   = pythonConditionErrorRegex
            variablesLoopDefined    = pythonConditionLoopRegex
            functionsDefined        = pythonFunctionsRegex
            classDefined            = pythonClassRegex

        # -- One file -- #
        if oneFileArg:
            # -- Find variables and mixed it -- #
            with open(outputArg, "r") as readFile:
                readF = readFile.readlines()
                for eachLine in readF:
                    
                    # -- Classic variables -- #     
                    search = re.search(variablesDefined, eachLine)
                    if search != None:
                        # -- Detect mixer -- #
                        mixer = self.mixer.GetStringMixer(mixerLevelArg)
                        # -- Add the mixer value of variables -- #
                        if search.group(1) not in variablesDict:
                            variablesDict[search.group(1)] = mixer
                    
                    # -- Error variables -- #
                    search = re.search(variablesErrorDefined, eachLine)
                    if search != None:
                        mixer = self.mixer.GetStringMixer(mixerLevelArg)
                        if search.group(2) not in variablesDict:
                            variablesDict[search.group(2)] = mixer
                    
                    # -- Loop variables -- #
                    search = re.search(variablesLoopDefined, eachLine)
                    if search != None:
                        if "," in search.group(1):
                            varsInFor = []
                            modifySearch = search.group(1).replace(",", " ")
                            modifySearch = modifySearch.split()
                            for i in modifySearch:
                                if i not in variablesDict:
                                    mixer = self.mixer.GetStringMixer(mixerLevelArg)
                                    variablesDict[i] = mixer 
                        else:
                            if search.group(1) not in variablesDict:
                                mixer = self.mixer.GetStringMixer(mixerLevelArg)
                                variablesDict[search.group(1)] = mixer
                    
                    # -- Functions -- #         
                    search = re.search(functionsDefined, eachLine)
                    if search != None:
                        mixer = self.mixer.GetStringMixer(mixerLevelArg)
                        if search.group(1) not in variablesDict:
                            if codeArg == "python":
                                if not re.match(r"(^__init__$)", search.group(1)):
                                    variablesDict[search.group(1)] = mixer

                    # -- Class -- #
                    search = re.search(classDefined, eachLine)
                    if search != None:
                        mixer = self.mixer.GetStringMixer(mixerLevelArg)
                        if search.group(1) not in variablesDict:
                            variablesDict[search.group(1)] = mixer

            # -- Check if not words key python in dict -- #
            for key in keyword.kwlist:
                if key in variablesDict.keys():
                    del variablesDict[key]

            # -- Delete excluded variables in dict -- #
            if os.path.exists(self.exclude) == True:
                with open(self.exclude, "r") as readFile:
                    for word in readFile:
                        word = word.rstrip()    
                        wordsExcluded.append(word)
            else:
                print("[-] File '{0}' not found\n".format(self.exclude))
            
            for word in wordsExcluded:
                if word in variablesDict.keys():
                    wordsExcludedFound.append(word)
                    del variablesDict[word]
                    
            print("############# [ Variables mixer ] ##############\n")
            
            for key, value in variablesDict.items():
                print("-> {0} : {1}".format(key, value))
            
            for word in wordsExcludedFound:
                print("-> {0} : excluded".format(word))
            print("")

            # -- Change variables to mixed values -- #
            with fileinput.input(outputArg, inplace=True) as inputFile:
                for eachLine in inputFile:
                    if not eachLine:
                        continue
                    else:
                        eachLine = Replace.EachLine(self, codeArg, eachLine, variablesDict.items())
                        print(eachLine)

            # -- Check if variables have been mixed -- #
            with open(outputArg, "r") as readFile:
                readF = readFile.readlines()
                for eachLine in readF:
                    for value in variablesDict.values():
                        if value in eachLine:
                            checkVarsMixed.append(value)
                
                # -- Remove duplicated key -- #
                checkListVarsMixed = list(dict.fromkeys(checkVarsMixed))
        
                for i in checkListVarsMixed:
                    checkCountVarsMixed += 1
                for i in variablesDict.values():
                    checkCountVarsValue += 1

            if checkCountVarsMixed == checkCountVarsValue:
                if (self.remove.NewLines(oneFileArg, codeArg, outputArg) == 0):
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
                    # -- Find variables and mixed it -- #
                    with open(output, "r") as readFile:
                        readF = readFile.readlines()
                        for eachLine in readF:
                            
                            # -- Classic variables -- #     
                            search = re.search(variablesDefined, eachLine)
                            if search != None:
                                # -- Detect mixer -- #
                                mixer = self.mixer.GetStringMixer(mixerLevelArg)
                                # -- Add the mixer value of variables -- #
                                if search.group(1) not in variablesDict:
                                    variablesDict[search.group(1)] = mixer
                            
                            # -- Error variables -- #
                            search = re.search(variablesErrorDefined, eachLine)
                            if search != None:
                                mixer = self.mixer.GetStringMixer(mixerLevelArg)
                                if search.group(2) not in variablesDict:
                                    variablesDict[search.group(2)] = mixer
                            
                            # -- Loop variables -- #
                            search = re.search(variablesLoopDefined, eachLine)
                            if search != None:
                                if "," in search.group(1):
                                    varsInFor = []
                                    modifySearch = search.group(1).replace(",", " ")
                                    modifySearch = modifySearch.split()
                                    for i in modifySearch:
                                        if i not in variablesDict:
                                            mixer = self.mixer.GetStringMixer(mixerLevelArg)
                                            variablesDict[i] = mixer 
                                else:
                                    if search.group(1) not in variablesDict:
                                        mixer = self.mixer.GetStringMixer(mixerLevelArg)
                                        variablesDict[search.group(1)] = mixer
                            
                            # -- Functions -- #         
                            search = re.search(functionsDefined, eachLine)
                            if search != None:
                                mixer = self.mixer.GetStringMixer(mixerLevelArg)
                                if search.group(1) not in variablesDict:
                                    if codeArg == "python":
                                        if not re.match(r"(^__init__$)", search.group(1)):
                                            variablesDict[search.group(1)] = mixer

                            # -- Class -- #
                            search = re.search(classDefined, eachLine)
                            if search != None:
                                mixer = self.mixer.GetStringMixer(mixerLevelArg)
                                if search.group(1) not in variablesDict:
                                    variablesDict[search.group(1)] = mixer

            # -- Check if not words key python in dict -- #
            for key in keyword.kwlist:
                if key in variablesDict.keys():
                    del variablesDict[key]

            # -- Delete excluded variables in dict -- #
            if os.path.exists(self.exclude) == True:
                with open(self.exclude, "r") as readFile:
                    for word in readFile:
                        word = word.rstrip()    
                        wordsExcluded.append(word)
            else:
                print("[-] File '{0}' not found\n".format(self.exclude))
            
            for word in wordsExcluded:
                if word in variablesDict.keys():
                    wordsExcludedFound.append(word)
                    del variablesDict[word]

            print("############# [ Variables mixer ] ##############\n")

            for key, value in variablesDict.items():
                print("-> {0} : {1}".format(key, value))
                
            for word in wordsExcludedFound:
                print("-> {0} : excluded".format(word))
            print("")

            # -- Change variables to mixed values -- #
            for output in recursFiles:
                if re.match(blockdirs, output):
                    continue
                else:
                    with fileinput.input(output, inplace=True) as inputFile:
                        for eachLine in inputFile:
                            if not eachLine:
                                continue
                            else:
                                eachLine = Replace.EachLine(self, codeArg, eachLine, variablesDict.items())
                                print(eachLine)

            # -- Check if variables have been mixed -- #
            for output in recursFiles:
                if re.match(blockdirs, output):
                    continue
                else:
                    with open(output, "r") as readFile:
                        readF = readFile.readlines()
                        for eachLine in readF:
                            for value in variablesDict.values():
                                if value in eachLine:
                                    checkVarsMixed.append(value)
                
            # -- Remove duplicated key -- #
            checkListVarsMixed = list(dict.fromkeys(checkVarsMixed))
            
            for i in checkListVarsMixed:
                checkCountVarsMixed += 1
            for i in variablesDict.values():
                checkCountVarsValue += 1

            if checkCountVarsMixed == checkCountVarsValue:
                if (self.remove.NewLines(oneFileArg, codeArg, outputArg) == 0):
                    return EXIT_SUCCESS
                else:
                    return EXIT_FAILURE
            else:
                return EXIT_FAILURE
