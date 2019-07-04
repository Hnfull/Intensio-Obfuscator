# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import re
import fileinput
import glob
import os
import time
import colorama
import tqdm

from core.obfuscation.intensio_mixer import Mixer
from core.obfuscation.intensio_remove import Remove
from core.utils.intensio_error import BreakLoop, EXIT_SUCCESS, EXIT_FAILURE
from core.utils.intensio_utils import Utils

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

ERROR_COLOUR = colorama.Fore.RED + colorama.Style.BRIGHT

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class ReplaceWords:

    def __init__(self):
        self.mixer              = Mixer()
        self.remove             = Remove()
        self.utils              = Utils()
        self.pythonExcludeWords = "exclude/python/exclude_python_words.txt"
        self.pythonIncludeWords = "include/python/include_python_words.txt"

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
                                                indexExploreBefore  = indexLine - 1
                                                if not re.match(r"\w|\\", getIndexLineList[indexExploreBefore]):                                                
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
    
    
    def VarsDefinedByUser(self, codeArg, outputArg, mixerLevelArg, verboseArg):
        variablesDict           = {}
        classesDict             = {}
        functionsDict           = {}
        includeDict             = {}
        allDict                 = {}
        checkWordsMixed         = []
        wordsExcluded           = []
        wordsExcludedFound      = []
        wordsIncludedFound      = []
        wordsIncludedNotFound   = []
        checkCountWordsMixed    = 0
        checkCountWordsValue    = 0
        checkQuotePassing       = 0
        numberReplaced          = 0
        countRecursFiles        = 0

        if codeArg == "python":
            variablesDefined        = r"(^\w+|\w+)([\s|^\s]*=[\s|\w|\"|\'])"    # Variables
            variablesErrorDefined   = r"except(\s+\w+\sas\s)(\w)"               # Error variables
            variablesLoopDefined    = r"for\s+([\w\s\,]+)(\s+in\s+)"            # Loop variables
            functionsDefined        = r"def\s(\w+)"                             # Functions
            classDefined            = r"class\s(\w+)"                           # Classes
            
            quoteOfEndCommentariesMultipleLines = r"^\s*[\"|\']{3}\)?\.?"   # """ and ''' without before variables, if commentaries is over multiple lines and he finish by .format() funtion
            quoteOfCommentariesMultipleLines    = r"^\s*[\"|\']{3}$"        # """ and ''' without before variables and if commentaries is over multiple lines
            quoteInRegex                        = r"\={1}\s*r[\"|\']{1}"    # If quote in regex
            quoteIntoVariable                   = r".*\={1}\s*\w*\.?\w*[\(|\.]{1}[\"|\']{3}|.*\={1}\s*[\"|\']{3}"   # """ and ''' with before variables
            
            detectFile  = "py"
            blockDirs   = r"__pycache__"

        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), detectFile), recursive=True)]

        # -- Find variables/classes/functions and mixed it -- #
        for file in recursFiles:
            if re.match(blockDirs, file):
                continue
            else:
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        # -- Variables -- #     
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
                            if search.group(1) not in functionsDict:
                                if codeArg == "python":
                                    if not re.match(r"__init__", search.group(1)):
                                        functionsDict[search.group(1)] = mixer

                        # -- Classes -- #
                        search = re.search(classDefined, eachLine)
                        if search != None:
                            mixer = self.mixer.GetStringMixer(mixerLevelArg)
                            if search.group(1) not in classesDict:
                                classesDict[search.group(1)] = mixer

        # -- Remove excluded variables/classes/functions defined from 'exclude/python/exclude_python_words.txt' in dict -- #
        if os.path.exists(self.pythonExcludeWords) == True:
            with open(self.pythonExcludeWords, "r") as readFile:
                for word in readFile:
                    if "#" in word or word == "\n":
                        continue
                    else:
                        word = word.rstrip()    
                        wordsExcluded.append(word)
        else:
            print(ERROR_COLOUR + "[-] '{0}' file not found\n".format(self.pythonExcludeWords))
        
        for word in wordsExcluded:
            if word in variablesDict.keys():
                wordsExcludedFound.append(word)
                del variablesDict[word]
            if word in classesDict.keys():
                wordsExcludedFound.append(word)
                del classesDict[word]
            if word in functionsDict.keys():
                wordsExcludedFound.append(word)
                del functionsDict[word]

        # -- Include variables/classes/functions defined from 'include/python/include_python_words.txt' in dict -- #
        if os.path.exists(self.pythonIncludeWords) == True:
            with open(self.pythonIncludeWords, "r") as readFile:
                for word in readFile:
                    if "#" in word or word == "\n":
                        continue
                    else:
                        word = word.rstrip()
                        wordsIncludedFound.append(word)
        else:
            print(ERROR_COLOUR + "[-] '{0}' file not found\n".format(self.pythonIncludeWords))
        
        for word in wordsIncludedFound:
            if word not in variablesDict.keys() and word not in classesDict.keys() and word not in functionsDict.keys():
                mixer = self.mixer.GetStringMixer(mixerLevelArg)
                includeDict[word] = mixer
                wordsIncludedNotFound.append(word)

        for file in recursFiles:
            if re.match(blockDirs, file):
                continue
            else:
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:        
                        for word in wordsIncludedNotFound:
                            if word in eachLine:
                                wordsIncludedNotFound.remove(word)

        for word in wordsIncludedNotFound:
            if word in includeDict.keys():
                del includeDict[word]
        
        # -- Display variables/classes/functions found -- #
        if verboseArg:
            print("\n[+] Variables found :\n")

            if variablesDict == {}:
                print("-> No result")
            else:
                for key, value in variablesDict.items():
                    print("-> {0} : {1}".format(key, value))
            
            print("\n[+] Classes found :\n")
            
            if classesDict == {}:
                print("-> No result")
            else:
                for key, value in classesDict.items():
                    print("-> {0} : {1}".format(key, value))
            
            print("\n[+] Functions found :\n")

            if functionsDict == {}:
                print("-> No result")
            else:
                for key, value in functionsDict.items():
                    print("-> {0} : {1}".format(key, value))

            print("\n[+] Include found :\n")

            if includeDict == {}:
                print("-> No result")
            else:
                for key, value in includeDict.items():
                    print("-> {0} : {1}".format(key, value))

            print("\n[+] Exclude found :\n")

            if wordsExcludedFound == []:
                print("-> No result")
            else:
                for word in wordsExcludedFound:
                    print("-> {0} : excluded".format(word))

        # -- Merge all dicts -- #
        allDict = self.utils.DictMerge(allDict, variablesDict)
        allDict = self.utils.DictMerge(allDict, classesDict)
        allDict = self.utils.DictMerge(allDict, functionsDict)
        allDict = self.utils.DictMerge(allDict, includeDict)
        
        for number in recursFiles:
            countRecursFiles += 1

        # -- Change variables/classes/functions to mixed values -- #
        print("\n[+] Running replacement of variables/classes/functions in {0} file(s)...\n".format(countRecursFiles))

        with tqdm.tqdm(total=countRecursFiles) as pbar:
            for file in recursFiles:
                pbar.update(1)
                if re.match(blockDirs, file):
                    continue
                else:
                    with fileinput.input(file, inplace=True) as inputFile:
                        for eachLine in inputFile:
                            if not eachLine:
                                continue
                            else:
                                if codeArg == "python":
                                    # -- Check code into """ or ''' -- #
                                    if re.match(quoteIntoVariable, eachLine):
                                        checkQuotePassing += 1
                                        eachLine = ReplaceWords.EachLine(self, codeArg, eachLine, allDict.items())
                                        print(eachLine)
                                        continue
                                    elif re.match(quoteOfCommentariesMultipleLines, eachLine) or re.match(quoteOfEndCommentariesMultipleLines, eachLine):
                                        checkQuotePassing += 1
                                        eachLine = ReplaceWords.EachLine(self, codeArg, eachLine, allDict.items())
                                        print(eachLine)
                                        if checkQuotePassing == 2:
                                            checkQuotePassing = 0
                                        continue

                                    if checkQuotePassing == 1:
                                        print(eachLine)
                                        continue
                                    elif checkQuotePassing == 2:
                                        checkQuotePassing = 0
                                        continue
                                    else:
                                        eachLine = ReplaceWords.EachLine(self, codeArg, eachLine, allDict.items())
                                        print(eachLine)
                                        continue
                            
        # -- Check if variables/classes/functions have been mixed -- #
        for file in recursFiles:
            if re.match(blockDirs, file):
                continue
            else:
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        for value in allDict.values():
                            if value in eachLine:
                                checkWordsMixed.append(value)
            
        # -- Remove duplicated key -- #
        checkListWordsMixed = list(dict.fromkeys(checkWordsMixed))
        
        for i in checkListWordsMixed:
            checkCountWordsMixed += 1
        for i in allDict.values():
            checkCountWordsValue += 1

        if (self.remove.LineBreaks(codeArg, outputArg) == 0):
            if checkCountWordsMixed == checkCountWordsValue:
                print("\n-> {0} variables/classes/functions replaced in {1} file(s)\n".format(checkCountWordsValue, countRecursFiles))
                return EXIT_SUCCESS
            else:
                return EXIT_FAILURE
        else:
            return EXIT_FAILURE
