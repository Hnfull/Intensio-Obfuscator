# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import re
import fileinput
import glob
import os
import time
import colorama
from progress.bar import Bar

from core.obfuscation.intensio_mixer import Mixer
from core.obfuscation.intensio_remove import Remove
from core.utils.intensio_error import BreakLoop, EXIT_SUCCESS, EXIT_FAILURE
from core.utils.intensio_utils import Utils

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

ERROR_COLOUR    = colorama.Back.RED + colorama.Style.BRIGHT
PROGRESS_COLOUR = colorama.Fore.BLUE + colorama.Style.BRIGHT 

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Replace:

    def __init__(self):
        self.mixer              = Mixer()
        self.remove             = Remove()
        self.utils              = Utils()
        self.pythonExcludeWords = "exclude/python/exclude_python_words.txt"
        self.pythonIncludeWords = "include/python/include_python_words.txt"


    def EachLine(self, codeArg, eachLine, Dict, forFilesName):
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
            regReplace = r"\.|\:|\)|\(|\=|\[|\]|\{|\}|\,|\+|\s|\*|\-"

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
                                        # -- Begin process to check -- #s
                                        if indexKey == 0:
                                            indexExplore = indexLine + len(key) # Place index position after the word

                                            # -- If indexError return to next loop -- #
                                            try:
                                                getIndexLineList[indexExplore]
                                            except IndexError: 
                                                continue
                                                
                                            # -- Check the char after and before the word -- #
                                            if re.match(regReplace, getIndexLineList[indexExplore]):
                                                indexExploreBefore  = indexLine - 1 # Index check if word finded is not into the other word
                                                indexExploreAfter   = indexLine + 2 # Index check char after the the char finded with regReplace regex
                                                
                                                if codeArg == "python":
                                                    try:
                                                        if not re.match(r"\w|\\", getIndexLineList[indexExploreBefore]):
                                                            # -- Check if it's 'from' and 'import' word key in line to avoid replace name of file if variable is identic name to file -- #
                                                            getLine = "".join(getIndexLineList)
                                                            if forFilesName == False:
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
                                                                # -- Check if after char find by 'regReplace' variable there no is ' or " -- #
                                                                elif re.match(r"\"|\'", getIndexLineList[indexExploreAfter]):
                                                                    checkCharAfterWord = 1
                                                                else:
                                                                    checkCharAfterWord = 0
                                                            # -- Only for -rfn, --replacefilesname feature -- #
                                                            else:
                                                                checkCharAfterWord = 0
                                                        else:
                                                            checkCharAfterWord = 1
                                                    except IndexError:
                                                        checkCharAfterWord = 0
                                                        pass
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
    
     
    def StringsToStrings(self, codeArg, outputArg, mixerLevelArg, verboseArg):
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
        checkAllWords           = []
        checkWordsError         = []
        checkKeyWordsMixed      = []
        checkCountWordsMixed    = 0
        checkCountWordsValue    = 0
        checkQuotePassing       = 0
        numberReplaced          = 0
        countRecursFiles        = 0

        if codeArg == "python":
            detectFiles = "py"
            blockDir    = "__pycache__"
            blockFile   = "__init__"

            functionsDefined        = r"def\s(\w+)"                             # Functions
            classDefined            = r"class\s(\w+)"                           # Classes
            variablesErrorDefined   = r"except(\s+\w+\sas\s)(\w)"               # Error variables
            variablesLoopDefined    = r"for\s+([\w\s\,]+)(\s+in\s+)"            # Loop variables
            variablesDefined        = r"(^\w+|\w+)([\s|^\s]*=[\s|\w|\"|\'])"    # Variables
            
            quoteOfCommentariesMultipleLines    = r"^\s*[\"|\']{3}$"        # """ and ''' without before variables and if commentaries is over multiple lines
            quoteInRegex                        = r"\={1}\s*r[\"|\']{1}"    # If quote in regex
            quoteOfEndCommentariesMultipleLines = r"^\s*[\"|\']{3}\)?\.?"   # """ and ''' without before variables, if commentaries is over multiple lines and he finish by .format() funtion
            quoteIntoVariable                   = r".*\={1}\s*\w*\.?\w*[\(|\.]{1}[\"|\']{3}|.*\={1}\s*[\"|\']{3}" # """ and ''' with before variables

        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), detectFiles), recursive=True)]

        # -- Replace variables/classes/functions to random strings with length defined -- #
        for file in recursFiles:
            if blockDir in file:
                continue
            else:
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        # -- Variables -- #     
                        search = re.search(variablesDefined, eachLine)
                        if search != None:
                            mixer = self.mixer.GetStringMixer(mixerLevelArg)
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
                                    if not blockFile in search.group(1):
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
            if blockDir in file:
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

        with Bar(PROGRESS_COLOUR + "Processing", max=countRecursFiles) as bar:
            for file in recursFiles:
                if blockDir in file:
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
                                        eachLine = Replace.EachLine(self, codeArg, eachLine, allDict.items(), False)
                                        print(eachLine)
                                        continue
                                    elif re.match(quoteOfCommentariesMultipleLines, eachLine) or re.match(quoteOfEndCommentariesMultipleLines, eachLine):
                                        checkQuotePassing += 1
                                        eachLine = Replace.EachLine(self, codeArg, eachLine, allDict.items(), False)
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
                                        eachLine = Replace.EachLine(self, codeArg, eachLine, allDict.items(), False)
                                        print(eachLine)
                                        continue

                    # -- Check if variables/classes/functions have been mixed -- #
                    with open(file, "r") as readFile:
                        readF = readFile.readlines()
                        for eachLine in readF:
                            for key, value in allDict.items():
                                if value in eachLine:
                                    checkWordsMixed.append(value)
                                    checkKeyWordsMixed.append(key)

                bar.next(1)
            bar.finish()

        # -- Remove duplicated words -- #
        checkListWordsMixed = list(dict.fromkeys(checkWordsMixed))
        checkKeyWordsMixed  = list(dict.fromkeys(checkKeyWordsMixed))

        for i in checkListWordsMixed:
            checkCountWordsMixed += 1
        for i in allDict.values():
            checkCountWordsValue += 1

        if (self.remove.Backslashes(codeArg, outputArg) == 0):
            if checkCountWordsMixed == checkCountWordsValue:
                print("\n-> {0} variables/classes/functions replaced in {1} file(s)\n".format(checkCountWordsValue, countRecursFiles))
                return EXIT_SUCCESS
            else:
                if verboseArg:
                    for key in allDict.keys():
                        checkAllWords.append(key)

                    checkWordsError = list(set(checkAllWords) - set(checkKeyWordsMixed))

                    print("\n" + ERROR_COLOUR + "[-] Words that not be replaced and have generate an error :\n")
                    for i in checkWordsError:
                        print(i)    

                return EXIT_FAILURE
        else:
            return EXIT_FAILURE


    def StringsToHex(self, codeArg, outputArg, mixerLevelArg):
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
            detectFiles = "py"
            blockDir    = "__pycache__"

            detectExecFunc  = r"exec\(\w+\)"
            detectQuotes    = r"[\'|\"]{3}"

        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, utils.Platform(), detectFiles), recursive=True)]

        for number in recursFiles:
                countRecursFiles += 1

        print("\n[+] Running replace all strings to their hexadecimal value in {0} file(s)...\n".format(countRecursFiles))

        # -- Replace all strings to their hexadecimal value -- #
        with Bar(PROGRESS_COLOUR + "Processing", max=countRecursFiles) as bar:
            for file in recursFiles:
                if blockDir in file:
                    continue
                else:
                    # -- Add a new first random line and move the old first line to the second line to avoid replacing it -- #
                    checkPrint = 0 # initialize check print() func at the begining of each file
                    with open(file, "r") as inputFile:
                        stringRandomMixer   = mixer.GetStringMixer(mixerLevelArg)
                        firstLine           = "{0}\n".format(stringRandomMixer)
                        line                = inputFile.readlines()

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

                    # -- Add exec funtions to interpret hex code in strings -- #
                    with open(file, "a") as inputFile:
                        inputFile.write("\"\"\"")
                        inputFile.write("\nexec({0})".format(varMixer))
            
                    # -- Check if all lines are replaced of hexadecimal value -- #
                    with open(file, "r") as inputFile:
                        for eachLine in inputFile:
                            if not eachLine:
                                continue
                            else:
                                if not "\\x" in eachLine:
                                    if re.match(detectQuotes, eachLine):
                                        continue
                                    elif re.match(detectExecFunc, eachLine):
                                        continue
                                    else:
                                        checkError = True
                                else:
                                    continue
                bar.next(1)
            bar.finish()

        if (remove.Backslashes(codeArg, outputArg) == 0):
            if checkHexError == False:
                return EXIT_SUCCESS        
            else:
                return EXIT_FAILURE
        else:
            return EXIT_FAILURE


    def FilesName(self, codeArg, outputArg, mixerLevelArg, verboseArg):
        filesNameDict           = {}
        filesNameDictNoExt      = {}
        filesNameFound          = []
        filesNameFoundNoExt     = []
        filesNameMixed          = []
        checkFilesFound         = []
        countRecursFiles        = 0
        checkRenameInDir        = 0
        checkRenameInCode       = 0
        unix                    = False
        win                     = False
        currentPosition         = os.getcwd()
        utils                   = Utils()
        mixer                   = Mixer()
        remove                  = Remove()

        if codeArg == "python":
            detectFiles = "py"
            blockDir    = "__pycache__"
            blockFile   = "__init__"

            detectImport = r"\s*from\s+|\s*import\s+"
    
        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, utils.Platform(), detectFiles), recursive=True)]

        for number in recursFiles:
                countRecursFiles += 1

        for file in recursFiles:
            if blockDir in file or blockFile in file:
                continue
            else:
                if "\"" in file:
                    parseFilePath = file.split("\"")
                    win = True
                else:
                    parseFilePath = file.split("/")
                    unix = True

                checkFilesFound.append(file)

                mixer = self.mixer.GetStringMixer(mixerLevelArg)
                filesNameDict[parseFilePath[-1]] = mixer + ".py" 
                filesNameDictNoExt[parseFilePath[-1].replace(".py", "")] = mixer
                
                filesNameFound.append(parseFilePath[-1])
                filesNameMixed.append(mixer + ".py")

                removeExt = parseFilePath[-1].replace(".py","")
                filesNameFoundNoExt.append(removeExt)
            
        # -- Diplay all files found with their mixed values if verbose arg is actived -- #
        if verboseArg:
            print("\n[+] Files name found with their mixed values :\n")
            for key, value in filesNameDict.items():
                print("-> {0} : {1}".format(key, value))
        
        print("\n[+] Running replace files name in {0} file(s)...\n".format(countRecursFiles))
        
        # -- Replace all files name to random strings with length defined -- #
        with Bar(PROGRESS_COLOUR + "Processing", max=countRecursFiles) as bar:
            for file in recursFiles:
                if blockDir in file:
                    continue
                else:
                    # -- Rename all files in python code -- #
                    with fileinput.input(file, inplace=True) as inputFile:
                        for eachLine in inputFile:
                            try:
                                for fileName in filesNameFound:
                                   for fileNameNoExt in filesNameFoundNoExt:
                                        if fileName in eachLine or fileNameNoExt in eachLine:
                                            if not ".py" in eachLine:
                                                if re.match(detectImport, eachLine):
                                                    eachLine = Replace.EachLine(self, codeArg, eachLine, filesNameDictNoExt.items(), True)
                                                    print(eachLine)
                                                    raise BreakLoop
                                                else:
                                                    continue
                                            else: 
                                                eachLine = Replace.EachLine(self, codeArg, eachLine, filesNameDict.items(), True)
                                                print(eachLine)
                                                raise BreakLoop
                                        else:
                                            continue
                                print(eachLine) 
                            except BreakLoop:
                                continue

                    # -- Rename all files in their directories -- #
                    if "\"" in file:
                        parseFilePath = file.split("\"")
                        win = True
                    else:
                        parseFilePath = file.split("/")
                        unix = True

                    for key, value in filesNameDict.items():        
                        if key == parseFilePath[-1]:
                            parseFilePath.remove(parseFilePath[-1])
                            if unix == True:
                                parseFilePathToMove = "/".join(parseFilePath)
                            else:
                                parseFilePathToMove = "\"".join(parseFilePath)
                            os.chdir(parseFilePathToMove) # Move in directory to rename python file
                            os.rename(key, value)
                        else:
                            continue
                    os.chdir(currentPosition) # Return to old position   
                bar.next(1)
            bar.finish()

        # -- Check if all files name are been replaced to random strings with length defined -- #    
        for i in checkFilesFound:
            i.replace(".py", "")

        # -- Check for file(s) name -- #
        for file in recursFiles:
            if blockDir in file or blockFile in file:
                continue
            else:
                for i in checkFilesFound:
                    if i in file:
                        checkFilesFound.remove(i)
                        continue

        # -- Check for code if file(s) name -- #
        if checkFilesFound != []:
            for file in recursFiles:
                if blockDir in file or blockFile in file:
                    continue
                else:
                    with open(file, "r") as inputFile:
                        for line in inputFile:
                            for i in checkFilesFound:
                                if i in line:
                                    checkFilesFound.remove(i)
                                    continue

        if checkFilesFound == []:
            if (remove.Backslashes(codeArg, outputArg) == 0):    
                return EXIT_SUCCESS        
            else:
                return EXIT_FAILURE
        else:
            return EXIT_FAILURE




