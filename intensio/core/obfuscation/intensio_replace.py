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
        self.mixer              = Mixer()
        self.remove             = Remove()
        self.utils              = Utils()
        self.pythonExcludeWords = "exclude_python_words.txt"
        self.pythonIncludeWords = "include_python_words.txt"

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

        if codeArg == "python":
            regReplace = r"(\.)|(:)|(\))|(\()|(=)|(\[)|(\])|({)|(})|(,)|(\+)|(\s)|(\*)|(\+)|(\-)"

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
                if re.match(regReplace, letterLine):
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
                                            if re.match(regReplace, getIndexLineList[indexExplore]):
                                                # -- Check word finded is not into the other word -- #
                                                indexExplore = indexLine - 1
                                                if not re.match(r"(\w)", getIndexLineList[indexExplore]):
                                                    if codeArg == "python":
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
        checkVarsMixed      = []
        wordsExcluded       = []
        wordsExcludedFound  = []
        wordsInclude        = []
        checkCountVarsMixed = 0
        checkCountVarsValue = 0
        checkPassing        = 0
        numberReplaced      = 0
        isCommentary        = 0
        noCommentary        = 0

        if codeArg == "python":
            variablesDefined            = r"(^\w+|\w+)([\s|^\s]*=[\s|\w|\"|\'])"    # Classic variables
            variablesErrorDefined       = r"except(\s+\w+\sas\s)(\w)"               # Error variables
            variablesLoopDefined        = r"for\s([\w\s?\,?]{1,})(\sin)"            # Loop variables
            functionsDefined            = r"def\s(\w+)"                             # Functions
            classDefined                = r"class\s(\w+)"                           # Classes

            quoteOfCommentariesOneLine  = r"[\"\']{3}.*[\"\']{3}"       # """ and ''' without before variables and if commentary is over one line, (""" commentaries """)
            noQuoteOfCommentaries       = r"\s*\w+\s*\={1}\s*[\"\']{3}" # """ and ''' with before variables

        print("######## [ Variables-Classes-Functions ] ########\n")

        ######################################### One file only #########################################

        if oneFileArg:
            # -- Find variables - classes - functions and mixed it -- #
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

                    # -- Classes -- #
                    search = re.search(classDefined, eachLine)
                    if search != None:
                        mixer = self.mixer.GetStringMixer(mixerLevelArg)
                        if search.group(1) not in variablesDict:
                            variablesDict[search.group(1)] = mixer

            # -- Delete excluded variables - classes - functions from excluded_python_varaibles.txt in dict -- #
            if os.path.exists(self.pythonExcludeWords) == True:
                with open(self.pythonExcludeWords, "r") as readFile:
                    for word in readFile:
                        if "#" in word or word == "\n":
                            continue
                        else:
                            word = word.rstrip()    
                            wordsExcluded.append(word)
            else:
                print("[-] File '{0}' not found\n".format(self.pythonExcludeWords))
            
            for word in wordsExcluded:
                if word in variablesDict.keys():
                    wordsExcludedFound.append(word)
                    del variablesDict[word]

            # -- Include variables - classes - functions defined from include_python_words.txt in dict -- #
            if os.path.exists(self.pythonIncludeWords) == True:
                with open(self.pythonIncludeWords, "r") as readFile:
                    for word in readFile:
                        if "#" in word or word == "\n":
                            continue
                        else:
                            word = word.rstrip()
                            wordsInclude.append(word)
            else:
                print("[-] File '{0}' not found\n".format(self.pythonIncludeWords))
            
            for word in wordsInclude:
                if word not in variablesDict.keys():
                    mixer = self.mixer.GetStringMixer(mixerLevelArg)
                    variablesDict[word] = mixer

            print("\n[+] Variables - Classes - Functions found :\n")
            
            for key, value in variablesDict.items():
                print("-> {0} : {1}".format(key, value))
            
            for word in wordsExcludedFound:
                print("-> {0} : excluded".format(word))
            
            print("\n[+] Running replacement of Variables - Classes - Functions...\n")

            # -- Change variables - classes - functions to mixed values -- #
            with fileinput.input(outputArg, inplace=True) as inputFile:
                for eachLine in inputFile:
                    if not eachLine:
                        continue
                    else:
                        if codeArg == "python":
                            # -- Check code in """ or ''' -- #
                            if "\"\"\"" in eachLine or "\'\'\'" in eachLine:
                                if re.match(quoteOfCommentariesOneLine, eachLine):
                                    print(eachLine)
                                    continue
                                elif re.match(noQuoteOfCommentaries, eachLine):
                                    eachLine = Replace.EachLine(self, codeArg, eachLine, variablesDict.items())
                                    print(eachLine)
                                    checkPassing += 1
                                    continue
                                else:
                                    checkPassing += 1

                            if checkPassing == 1:
                                print(eachLine)
                                continue
                            else:
                                checkPassing = 0
                                eachLine = Replace.EachLine(self, codeArg, eachLine, variablesDict.items())
                                print(eachLine)

            # -- Check if variables - classes - functions have been mixed -- #
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
                print("-> {0} variables - classes - functions replaced\n".format(checkCountVarsValue))
                if (self.remove.LineBreaks(oneFileArg, codeArg, outputArg) == 0):
                    return EXIT_SUCCESS
                else:
                    return EXIT_FAILURE
            else:
                return EXIT_FAILURE

        ######################################### Multiple files #########################################

        else:
            if codeArg == "python":
                inputExt    = "py"
                blockdirs   = r"__pycache__"

            recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), inputExt), recursive=True)]

            # -- Find variables - classes - functions and mixed it -- #
            for output in recursFiles:
                if re.match(blockdirs, output):
                    continue
                else:
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

                            # -- Classes -- #
                            search = re.search(classDefined, eachLine)
                            if search != None:
                                mixer = self.mixer.GetStringMixer(mixerLevelArg)
                                if search.group(1) not in variablesDict:
                                    variablesDict[search.group(1)] = mixer

            # -- Remove excluded variables - classes - functions defined from excluded_python_words.txt in dict -- #
            if os.path.exists(self.pythonExcludeWords) == True:
                with open(self.pythonExcludeWords, "r") as readFile:
                    for word in readFile:
                        if "#" in word or word == "\n":
                            continue
                        else:
                            word = word.rstrip()    
                            wordsExcluded.append(word)
            else:
                print("[-] File '{0}' not found\n".format(self.pythonExcludeWords))
            
            for word in wordsExcluded:
                if word in variablesDict.keys():
                    wordsExcludedFound.append(word)
                    del variablesDict[word]

            # -- Include variables - classes - functions defined from include_python_words.txt in dict -- #
            if os.path.exists(self.pythonIncludeWords) == True:
                with open(self.pythonIncludeWords, "r") as readFile:
                    for word in readFile:
                        if "#" in word or word == "\n":
                            continue
                        else:
                            word = word.rstrip()
                            wordsInclude.append(word)
            else:
                print("[-] File '{0}' not found\n".format(self.pythonIncludeWords))
            
            for word in wordsInclude:
                if word not in variablesDict.keys():
                    mixer = self.mixer.GetStringMixer(mixerLevelArg)
                    variablesDict[word] = mixer

            print("\n[+] Variables - Classes - Functions found :\n")

            for key, value in variablesDict.items():
                print("-> {0} : {1}".format(key, value))

            for word in wordsExcludedFound:
                print("-> {0} : excluded".format(word))
            
            print("\n[+] Running replacement of Variables - Classes - Functions...\n")

            # -- Change variables - classes - functions to mixed values -- #
            for output in recursFiles:
                if re.match(blockdirs, output):
                    continue
                else:
                    with fileinput.input(output, inplace=True) as inputFile:
                        for eachLine in inputFile:    
                            if not eachLine:
                                continue
                            else:
                                if codeArg == "python":
                                    # -- Check code in """ or ''' -- #
                                    if "\"\"\"" in eachLine or "\'\'\'" in eachLine:
                                        if re.match(quoteOfCommentariesOneLine, eachLine):
                                            print(eachLine)
                                            continue
                                        elif re.match(noQuoteOfCommentaries, eachLine):
                                            eachLine = Replace.EachLine(self, codeArg, eachLine, variablesDict.items())
                                            print(eachLine)
                                            checkPassing += 1
                                            continue
                                        else:
                                            checkPassing += 1

                                    if checkPassing == 1:
                                        print(eachLine)
                                        continue
                                    else:
                                        checkPassing = 0
                                        eachLine = Replace.EachLine(self, codeArg, eachLine, variablesDict.items())
                                        print(eachLine)

            # -- Check if variables - classes - functions have been mixed -- #
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
                print("-> {0} variables - classes - functions replaced\n".format(checkCountVarsValue))
                if (self.remove.LineBreaks(oneFileArg, codeArg, outputArg) == 0):
                    return EXIT_SUCCESS
                else:
                    return EXIT_FAILURE
            else:
                return EXIT_FAILURE
