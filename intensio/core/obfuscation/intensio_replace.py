# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import re
import fileinput
import os
import time
import sys
from progress.bar import Bar

from core.obfuscation.intensio_mixer import Mixer
from core.utils.intensio_utils import Utils, Colors, BreakLoop, Reg

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Replace:

    def __init__(self):
        self.mixer  = Mixer()
        self.utils  = Utils()
        self.pythonExcludeDefaultString = "exclude/string_to_string_mixed/exclude_word_do_not_modify.txt"
        self.pythonExcludeUserString    = "exclude/string_to_string_mixed/exclude_word_by_user.txt"
        self.pythonExcludeUserFileName  = "exclude/file_name/exclude_file_name_by_user.txt"


    def EachLine(self, line, dictionary, fileNameImport, listModuleImport):
        getIndexLineList    = []
        returnLine          = []
        charValue           = []
        checkCharAfterWord  = 1
        wordSetter          = 0
        checkGetKey         = ""
        checkGetWord        = ""
        getLine             = ""
        breakLine           = ""

        if listModuleImport == True:
            detectSpecialChars = Reg.detectSpecialChars
        else:
            detectSpecialChars = Reg.detectSpecialCharsWihtoutQuotes

        # -- Get list of all letters in line -- #
        for indexLine, letterLine in enumerate(line):
            getIndexLineList.append(letterLine)

        # -- Loop in each letter of line -- #
        for indexLine, letterLine in enumerate(line):
            # -- Add in final line list all chars mixed -- #
            if charValue != []:
                for obfIndex, obfValue in enumerate(charValue):
                    if obfIndex == 0: # First letter in string mixed are already added in the final line
                        continue
                    returnLine.append(obfValue)
                charValue = []

                # -- If the variable is only a letter, check if the next character is specific so as not to replace it -- #
                if re.match(detectSpecialChars, letterLine):
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
                        for key, value in dictionary:
                            for indexKey, letterKey in enumerate(key):
                                for letterValue in value:
                                    # -- Check if letter of word is equal to letter of key -- #
                                    if letterKey == letterLine:
                                        # -- Begin process to check -- #
                                        if indexKey == 0: # if equal to the first letter of word on <key> variable 
                                            indexExplore = indexLine + len(key) # Place index position after the word
                                            # -- If indexError return to next loop -- #
                                            try:
                                                getIndexLineList[indexExplore]
                                            except IndexError:
                                                continue

                                            # -- Check the char after and before the word -- #
                                            if re.match(detectSpecialChars, getIndexLineList[indexExplore]):
                                                # Index check if word found is not into the other word
                                                indexExploreBefore = indexLine - 1
                                                # Index check if char after the end of string is found with 'detectSpecialChars' regex
                                                indexExploreAfter = indexExplore

                                                try:
                                                    if not re.match(r"\w|\\|\%", getIndexLineList[indexExploreBefore]):
                                                        # -- Check if it's 'from' and 'import' file in line to avoid replace \
                                                        # name of file if variable is identical name to file -- #
                                                        getLine = "".join(getIndexLineList)
                                                        if fileNameImport == False:
                                                            if "import" in getLine:
                                                                if "from" in getLine:
                                                                    # -- Cut the line from the current index and check if it is \
                                                                    # not there is the keyword "import" in the line -- #
                                                                    breakLine = getIndexLineList[:indexLine]
                                                                    breakLine = "".join(breakLine)
                                                                    if not "import" in breakLine:
                                                                        # -- It's a file because only 'from'key word -- #
                                                                        checkCharAfterWord = 1
                                                                    else:
                                                                        checkCharAfterWord = 0
                                                                else:
                                                                    checkCharAfterWord = 1
                                                            # -- Check if after char of the word found by 'detectSpecialChars' is \
                                                            # not ' or " -- #
                                                            elif re.match(r"\"|\'", getIndexLineList[indexExploreAfter]):
                                                                if re.match(r"\[|\(|\{", getIndexLineList[indexExploreAfter - 1]):
                                                                    checkCharAfterWord = 0
                                                                else:
                                                                    checkCharAfterWord = 1
                                                            else:
                                                                checkCharAfterWord = 0
                                                        # -- Only for [-rfn, --replacefilsname] feature -- #
                                                        else:
                                                            # -- check if file name is imported - #
                                                            breakLine = getIndexLineList[:indexLine]
                                                            breakLine = "".join(breakLine)
                                                            # -- If file name is imported after 'import', the file name is not \
                                                            # replaced -- #
                                                            if "import" in breakLine:
                                                                checkCharAfterWord = 1
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
                                                getCharAllInKey = []
                                                getWord         = []

                                                indexExploreStart = indexLine
                                                # -- Delete -1, first letter is already increment -- #
                                                indexExploreEnd = indexLine + len(key) - 1

                                                # -- List contain all letters of key -- #
                                                for getLetterKey in key:
                                                    getCharAllInKey.append(getLetterKey)

                                                # -- Check if all letters of key is equal to all letters of word -- #
                                                for indexCheckLetter, checkLetter in enumerate(getIndexLineList):
                                                    if indexCheckLetter >= indexExploreStart and \
                                                    indexCheckLetter <= indexExploreEnd:
                                                        getWord.append(checkLetter)

                                                # -- Check if number of chars in key equal number of chars in word -- #
                                                if list(set(getCharAllInKey) - set(getWord)) == []:
                                                    checkGetWord = "".join(getWord)
                                                    checkGetKey = "".join(getCharAllInKey)

                                                    # -- Check if key == word -- #
                                                    if checkGetWord == checkGetKey:
                                                        # -- Check if word is not in strings quotes and if a variable 
                                                        # is in format() in end of multiple line -- #
                                                        if self.utils.DetectIntoSimpleQuotes(getLine, indexLine) == False \
                                                        or self.utils.DetectMultipleLinesQuotes(getLine) == True:
                                                            for obfChar in value:
                                                                charValue.append(obfChar)

                                                            letterLine = letterValue
                                                            raise BreakLoop
                                                        else:
                                                            break
                                                    else:
                                                        break
                                                else:
                                                    break
                                            else:
                                                break
                                        else:
                                            break
                                    else:
                                        break

                        raise BreakLoop

                    except BreakLoop:
                        returnLine.append(letterLine)

        # -- Rewrite the line -- #
        returnLine = "".join(returnLine)
        return returnLine[:]


    def StringToString(self, outputArg, mixerLengthArg, verboseArg):
        variablesDict               = {}
        classesDict                 = {}
        functionsDict               = {}
        allDict                     = {}
        classFuncDict               = {}
        checkWordsMixed             = []
        wordsExcludedUser           = []
        wordsExcludedUserFound      = []
        wordsExcludedDefault        = []
        wordsExcludedDefaultFound   = []
        checkAllWords               = []
        checkWordsError             = []
        checkKeyWordsMixed          = []
        checkCountWordsMixed        = 0
        checkCountWordsValue        = 0
        countRecursFiles            = 0
        multipleLinesQuotes         = 0

        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg,
                                                detectFiles="py",
                                                blockDir="__pycache__",
                                                blockFile=False,
                                                dirOnly=False
        )

        for file in recursFiles:
            countRecursFiles += 1

        print("\n[+] Running replacement of variables/classes/functions in " + str(countRecursFiles) + \
            " file(s), he can be long... you have time to make a coffee :)\n")

        # -- Replace variables/classes/functions to random strings with length defined -- #
        with Bar("Setting up  ", fill="=", max=100, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        # -- Variables -- #
                        search = re.search(Reg.detectSimpleVars, eachLine)
                        if search:
                            if "," in search.group(1):
                                modifySearch = search.group(1).replace(",", " ")
                                modifySearch = modifySearch.split()
                                for i in modifySearch:
                                    if i not in variablesDict:
                                        mixer = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                                        i = i.strip()
                                        variablesDict[i] = mixer
                            else:
                                if search.group(1) not in variablesDict:
                                    mixer = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                                    modifySearch = search.group(1).strip()
                                    variablesDict[modifySearch] = mixer

                        # -- Error variables -- #
                        search = re.search(Reg.detectErrorVars, eachLine)
                        if search:
                            mixer = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                            if search.group(2) not in variablesDict:
                                variablesDict[search.group(2)] = mixer

                        # -- Loop variables -- #
                        search = re.search(Reg.detectLoopVars, eachLine)
                        if search:
                            if "," in search.group(1):
                                modifySearch = search.group(1).replace(",", " ")
                                modifySearch = modifySearch.split()
                                for i in modifySearch:
                                    if i not in variablesDict:
                                        mixer = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                                        variablesDict[i] = mixer
                            else:
                                if search.group(1) not in variablesDict:
                                    mixer = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                                    variablesDict[search.group(1)] = mixer

                        # -- Function(s) -- #
                        search = re.search(Reg.detectFunctions, eachLine)
                        if search:
                            mixer = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                            if search.group(1) not in functionsDict:
                                if not "__init__" in search.group(1):
                                    functionsDict[search.group(1)] = mixer

                        # -- Class(es) -- #
                        search = re.search(Reg.detectClasses, eachLine)
                        if search:
                            mixer = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                            if search.group(1) not in classesDict:
                                classesDict[search.group(1)] = mixer
            bar.next(40)

            # -- Delete excluded variables/classes/functions defined from \
            # 'exclude/string_to_string_mixed/exclude_word_do_not_modify.txt' -- #
            if os.path.exists(self.pythonExcludeDefaultString) == True:
                with open(self.pythonExcludeDefaultString, "r") as readFile:
                    for word in readFile:
                        if "#" in word or word == "\n":
                            continue
                        else:
                            word = word.rstrip()
                            wordsExcludedDefault.append(word)
            else:
                print(Colors.ERROR + "[-] '{}' file not found".format(self.pythonExcludeDefaultString) + Colors.DISABLE \
                    + "\n")

            bar.next(10)

            # -- Delete excluded variables/classes/functions defined from \
            # 'exclude/string_to_string_mixed/exclude_word_by_user.txt' -- #
            if os.path.exists(self.pythonExcludeUserString) == True:
                with open(self.pythonExcludeUserString, "r") as readFile:
                    for word in readFile:
                        if "#" in word or word == "\n":
                            continue
                        else:
                            word = word.rstrip()
                            wordsExcludedUser.append(word)
            else:
                print(Colors.ERROR + "[-] '{}' file not found".format(self.pythonExcludeUserString) + Colors.DISABLE \
                    + "\n")

            bar.next(10)

            for word in wordsExcludedUser:
                if word in variablesDict.keys():
                    wordsExcludedUserFound.append(word)
                if word in classesDict.keys():
                    wordsExcludedUserFound.append(word)
                if word in functionsDict.keys():
                    wordsExcludedUserFound.append(word)
            
            bar.next(20)

            for word in wordsExcludedDefault:
                if word in variablesDict.keys():
                    wordsExcludedDefaultFound.append(word)
                if word in classesDict.keys():
                    wordsExcludedDefaultFound.append(word)
                if word in functionsDict.keys():
                    wordsExcludedDefaultFound.append(word)

            for word in wordsExcludedUserFound:
                if word in variablesDict.keys():
                    del variablesDict[word]
                if word in classesDict.keys():
                    del classesDict[word]
                if word in functionsDict.keys():
                    del functionsDict[word]

            for word in wordsExcludedDefaultFound:
                if word in variablesDict.keys():
                    del variablesDict[word]
                if word in classesDict.keys():
                    del classesDict[word]
                if word in functionsDict.keys():
                    del functionsDict[word]

            bar.next(20)
            bar.finish()

        # -- Display variables/classes/functions found -- #
        if verboseArg:
            print("\n[+] Variable(s) found :\n")
            if variablesDict == {}:
                print("-> No result")
            else:
                for key, value in variablesDict.items():
                    print("-> {} : {}".format(key, value))

            print("\n[+] Class(es) found :\n")
            if classesDict == {}:
                print("-> No result")
            else:
                for key, value in classesDict.items():
                    print("-> {} : {}".format(key, value))

            print("\n[+] Function(s) found :\n")
            if functionsDict == {}:
                print("-> No result")
            else:
                for key, value in functionsDict.items():
                    print("-> {} : {}".format(key, value))

            print("\n[+] String excluded found in '{}' that have been matched from '{}' :\n".format(
                                                                                                self.pythonExcludeUserString, 
                                                                                                outputArg
                                                                                                )
            )
            if wordsExcludedUserFound == []:
                print("-> No result")
            else:
                for word in wordsExcludedUserFound:
                    print("-> {} : excluded by user".format(word))

            print("\n[+] String excluded found in '{}' that have been matched from '{}' :\n".format(
                                                                                                self.pythonExcludeDefaultString, 
                                                                                                outputArg
                                                                                                )
            )
            if wordsExcludedDefaultFound == []:
                print("-> No result")
            else:
                for word in wordsExcludedDefaultFound:
                    print("-> {} : excluded by default".format(word))
            print("")

        # -- Merge all dicts -- #
        allDict         = self.utils.DictMerge(dict1=allDict, dict2=variablesDict)
        allDict         = self.utils.DictMerge(dict1=allDict, dict2=functionsDict)
        allDict         = self.utils.DictMerge(dict1=allDict, dict2=classesDict)
        classFuncDict   = self.utils.DictMerge(dict1=classFuncDict, dict2=classesDict)
        classFuncDict   = self.utils.DictMerge(dict1=classFuncDict, dict2=functionsDict)

        # -- Change variables/classes/functions to mixed values -- #
        with Bar("Obfuscation ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                # -- Replace variable(s) only -- #
                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        if not eachLine:
                            continue
                        else:
                            if multipleLinesQuotes == 1:
                                if re.match(Reg.checkIfEndVarStdoutMultipleQuotes, eachLine):
                                    if self.utils.DetectMultipleLinesQuotes(eachLine) == True:
                                        eachLine = Replace.EachLine(
                                                                self,
                                                                line=eachLine,
                                                                dictionary=allDict.items(),
                                                                fileNameImport=False,
                                                                listModuleImport=False
                                        )
                                        sys.stdout.write(eachLine)
                                        multipleLinesQuotes = 0
                                    else:
                                        sys.stdout.write(eachLine)
                                else:
                                    sys.stdout.write(eachLine)
                            elif re.match(Reg.checkIfVarMultipleQuotes, eachLine) \
                            or re.match(Reg.checkIfStdoutMultipleQuotes, eachLine):
                                if self.utils.DetectMultipleLinesQuotes(eachLine) == False:
                                    pass
                                else:
                                    multipleLinesQuotes = 1
                                eachLine = Replace.EachLine(
                                                            self,
                                                            line=eachLine,
                                                            dictionary=allDict.items(),
                                                            fileNameImport=False,
                                                            listModuleImport=False
                                )
                                sys.stdout.write(eachLine)
                                continue

                            else:
                                eachLine = Replace.EachLine(
                                                            self,
                                                            line=eachLine,
                                                            dictionary=allDict.items(),
                                                            fileNameImport=False,
                                                            listModuleImport=False
                                )
                                sys.stdout.write(eachLine)

                bar.next(1)
            bar.finish()

        with Bar("Check       ", fill="=", max=100, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                # -- Check if variables/classes/functions have been mixed -- #
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        for key, value in allDict.items():
                            if value in eachLine:
                                if re.match(r"\w+" + re.escape(value) + r"\w+", eachLine):
                                    pass
                                else:
                                    checkWordsMixed.append(value)
                                    checkKeyWordsMixed.append(key)
            
            bar.next(70)

            # -- Delete duplicated words -- #
            checkListWordsMixed = list(dict.fromkeys(checkWordsMixed))
            checkKeyWordsMixed  = list(dict.fromkeys(checkKeyWordsMixed))

            bar.next(15)

            for i in checkListWordsMixed:
                checkCountWordsMixed += 1
            for i in allDict.values():
                checkCountWordsValue += 1

            bar.next(15)
            bar.finish()

        if checkCountWordsMixed == checkCountWordsValue:
            print("\n-> {} variable(s)/class(es)/function(s) replaced in {} file(s)\n".format(
                                                                                            checkCountWordsValue, 
                                                                                            countRecursFiles
                                                                                            )
            )
            return 1
        else:
            if verboseArg:
                for key in allDict.keys():
                    checkAllWords.append(key)

                checkWordsError = list(set(checkAllWords) - set(checkKeyWordsMixed))

                print("\n[!] Word(s) that not been replaced, check if an error will appear when will launch your " + \
                    "obfuscated code... :\n")
                if checkWordsError != []:
                    for wordNoReplaced in checkWordsError:
                        print("-> Word : {}".format(wordNoReplaced))
            return 0


    def StringsToHex(self, outputArg, mixerLengthArg, verboseArg):
        checkHexError       = {}
        splitLetter         = []
        getLetterLineList   = []
        countRecursFiles    = 0
        checkPrint          = 0
        numberLine          = 0
        checkError          = False
        hexLine             = ""

        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg,
                                                detectFiles="py",
                                                blockDir="__pycache__",
                                                blockFile=False,
                                                dirOnly=False
        )

        for number in recursFiles:
            countRecursFiles += 1

        print("\n[+] Running replace all strings to their hexadecimal value in {} file(s)...\n".format(countRecursFiles))

        # -- Replace all strings to their hexadecimal value -- #
        with Bar("Obfuscation ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                # -- Add a new first random line and move the old first line to the second line to avoid replacing it -- #
                checkPrint = 0 # initialize check print() func at the begining of each file
                with open(file, "r") as inputFile:
                    stringRandomMixer = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                    firstLine   = "{}\n".format(stringRandomMixer)
                    line        = inputFile.readlines()

                    line.insert(0, firstLine)

                with open(file, "w") as inputFile:
                    inputFile.writelines(line)

                # -- Replace all lines-- #
                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        if checkPrint == 0:
                            varMixer = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                            sys.stdout.write(varMixer + "=\"\"\"")
                            checkPrint = 1
                        else:
                            getLetterLineList = []
                            for letterLine in eachLine:
                                if len(letterLine.encode("utf-8").hex()) > 2:
                                    splitLetter = []
                                    for i in letterLine.encode("utf-8").hex():
                                        splitLetter.append(i)
                                        if len(splitLetter) == 2:
                                            letterLine = "".join(splitLetter)
                                            letterToHex = "\\x" + str(letterLine)
                                            getLetterLineList.append(letterToHex)
                                            splitLetter = []
                                        else:
                                            continue
                                else:
                                    letterToHex = "\\x" + str(letterLine.encode("utf-8").hex())
                                    getLetterLineList.append(letterToHex) # Get list of all letters in line
                            hexLine = "".join(getLetterLineList)
                            sys.stdout.write(hexLine)

                # -- Add exec funtions to interpret hex code in strings -- #
                with open(file, "a") as inputFile:
                    inputFile.write("\"\"\"")
                    inputFile.write("\nexec({})".format(varMixer))

                bar.next(1)
            bar.finish()

        with Bar("Check       ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                numberLine = 0
                # -- Check if all lines are replaced of hexadecimal value -- #
                with open(file, "r") as inputFile:
                    for eachLine in inputFile:
                        numberLine += 1
                        if not eachLine:
                            continue
                        else:
                            if not "\\x" in eachLine:
                                if re.match(Reg.detectExecFunction, eachLine):
                                    continue
                                else:
                                    checkHexError[numberLine] = file
                                    checkError = True
                            else:
                                continue

                bar.next(1)
            bar.finish()

        if checkError == False:
            return 1
        else:
            if verboseArg:
                print("\n[!] Line(s) that have not been replaced by their hexadecimal values... :\n")
                for key, value in checkHexError.items():
                    print("\n-> File : {}".format(value))
                    print("-> Line : {}".format(key))
            else:
                print("\n" + Colors.ERROR + "[!] Launch Intensio-Obfuscator with verbose mode because line(s) have not been " + \
                    "replaced by their hexadecimal values" + Colors.DISABLE + "\n")
            return 0


    def FilesName(self, outputArg, mixerLengthArg, verboseArg):
        checkFilesFoundCompare  = {}
        filesNameDict           = {}
        filesNameDictNoExt      = {}
        filesNameFound          = []
        filesNameFoundNoExt     = []
        filesNameMixed          = []
        fileNameExcluded        = []
        fileNameExcludedFound   = []
        fileNameExcludedByUser  = []
        importNoCompliantFound  = []
        badNameDir              = []
        numberLine              = 0
        countRecursFiles        = 0
        checkCountRecursFiles   = 0
        currentPosition         = os.getcwd()

        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg,
                                                detectFiles="py",
                                                blockDir="__pycache__",
                                                blockFile="__init__",
                                                dirOnly=False
        )

        recursFilesWithInit = self.utils.CheckFileDir(
                                                        output=outputArg,
                                                        detectFiles="py",
                                                        blockDir="__pycache__",
                                                        blockFile=False,
                                                        dirOnly=False
        )

        recursDirs = self.utils.CheckFileDir(
                                            output=outputArg,
                                            detectFiles="",
                                            blockDir="__pycache__",
                                            blockFile=False,
                                            dirOnly=True
        )

        for file in recursFiles:
            countRecursFiles += 1

        print("\n[+] Running replace files name in {} file(s)...\n".format(countRecursFiles))

        with Bar("Setting up  ", fill="=", max=100, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                parseFilePath = file.split(self.utils.Platform(getOS=False, getPathType=True))
                mixer = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                filesNameDict[parseFilePath[-1]] = mixer + ".py"
                filesNameDictNoExt[parseFilePath[-1].replace(".py", "")] = mixer

                deleteExt = parseFilePath[-1].replace(".py","")

                filesNameFound.append(parseFilePath[-1])
                filesNameFoundNoExt.append(deleteExt)
                filesNameMixed.append(mixer + ".py")

            bar.next(30)

            # -- Check if directory have the same name
            for directory in recursDirs:
                for fileName in filesNameFoundNoExt:
                    if re.match(r".*" + re.escape(self.utils.Platform(getOS=False, getPathType=True)) + r"{1}" + \
                        re.escape(fileName) + re.escape(self.utils.Platform(getOS=False, getPathType=True)) + \
                        r"{1}.*", directory):
                        fileNameExcluded.append(fileName)
                        badNameDir.append(fileName)

            bar.next(20)

            # -- Delete if file name excluded by user from exclude/file_name/exclude_file_name_by_user.txt' -- #
            if os.path.exists(self.pythonExcludeUserFileName) == True:
                with open(self.pythonExcludeUserFileName) as readFile:
                    for fileName in readFile:
                        if "#" in fileName or fileName == "\n" or re.match(r"yourFileName[0-9]{1}", fileName):
                            continue
                        else:
                            fileName = fileName.rstrip()
                            fileNameExcluded.append(fileName)
                            fileNameExcludedByUser.append(fileName)
            else:
                print(Colors.ERROR + "[-] '{}' file not found".format(self.pythonExcludeUserFileName) + Colors.DISABLE + "\n")
                
            bar.next(10)

            # -- Delete file name excluded in dictionnary -- #
            for word in fileNameExcluded:
                for fileNameNoExt in filesNameFoundNoExt:
                    if fileNameNoExt == word:
                        fileNameExcludedFound.append(word)
                        filesNameFoundNoExt.remove(word)
                for fileName in filesNameFound:
                    if fileName == word:
                        filesNameFound.remove(word)
                if word in filesNameDictNoExt.keys():
                    del filesNameDictNoExt[word]
                word = word + ".py"
                if word in filesNameDict.keys():
                    del filesNameDict[word]

            bar.next(10)

            # -- Check if file name in code is after 'import' native python function --#
            for file in recursFiles:
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if re.match(Reg.detectPythonImport, eachLine):
                            searchFileName = re.search(r"(import\s+)(.*)", eachLine)
                            if searchFileName.group(2):
                                searchFileName = searchFileName.group(2).replace(",", "")
                                searchFileName = searchFileName.split()
                                for i in searchFileName:
                                    i = i.strip()
                                    for fileNameNoExt in filesNameFoundNoExt:
                                        if fileNameNoExt == i:
                                            importNoCompliantFound.append(i)
                                            filesNameFoundNoExt.remove(i)
                                    for fileName in filesNameFound:
                                        fileName = fileName.replace(".py", "")
                                        if fileName == i:
                                            i = i + ".py"
                                            filesNameFound.remove(i)
                                    if i in filesNameDictNoExt.keys():
                                        del filesNameDictNoExt[i]
                                    if i in filesNameDict.keys():
                                        del filesNameDict[i]

            bar.next(30)
            bar.finish()

        # -- Diplay all file name(s) found with their mixed values if verbose arg is actived -- #
        if verboseArg:
            print("\n[+] File name(s) found with their mixed values :\n")
            if filesNameDict == {}:
                print("-> No result")
            else:
                for key, value in filesNameDict.items():
                    print("-> {} : {}".format(key, value))

            print("\n[+] File name(s) excluded found in '{}' that have been matched from '{}' :\n".format(
                                                                                            self.pythonExcludeUserFileName, 
                                                                                            outputArg
                                                                                            )
            )
            if fileNameExcludedByUser == []:
                print("-> No result")
            else:
                for i in fileNameExcludedByUser:
                    print("-> {} : excluded by user".format(i))

            print("\n[+] File name(s) no compliant for 'replace file name' feature :\n")
            if importNoCompliantFound == []: 
                print("-> No result")
            else:
                for i in importNoCompliantFound:
                    print("-> {} : no compliant ( file name excluded automatically )".format(i))

            print("\n[+] Directory that have same name of python file(s) :\n")
            if badNameDir == []:
                print("-> No result")
            else:
                for i in badNameDir:
                    print("-> {} : no compliant ( file name excluded automatically )".format(i))
                    i = i.rstrip()
            print("")

        # -- Replace all file names to random strings with length and obfuscation level defined -- #
        with Bar("Obfuscation ", fill="=", max=100, suffix="%(percent)d%%") as bar:
            for fileInCode in recursFilesWithInit:
                # -- Rename all files in python code -- #
                with fileinput.input(fileInCode, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        if re.match(Reg.detectPythonImport, eachLine):
                            eachLine = Replace.EachLine(
                                                        self,
                                                        line=eachLine,
                                                        dictionary=filesNameDictNoExt.items(),
                                                        fileNameImport=True,
                                                        listModuleImport=False
                            )
                            sys.stdout.write(eachLine)
                            continue
                        else:
                            sys.stdout.write(eachLine)
            
            bar.next(50)

            for file in recursFiles:
                parseFilePath = file.split(self.utils.Platform(getOS=False, getPathType=True))
                # -- Rename all files in their directories -- #
                for key, value in filesNameDict.items():
                    if key == parseFilePath[-1]:
                        parseFilePath.remove(parseFilePath[-1])
                        parseFilePathToMove = self.utils.Platform(getOS=False, getPathType=True).join(parseFilePath)
                        os.chdir(parseFilePathToMove) # Move in directory to rename python file
                        os.rename(key, value)
                    else:
                        continue

                os.chdir(currentPosition)
            
            bar.next(50)
            bar.finish()

        checkRecursFiles = self.utils.CheckFileDir(
                                                    output=outputArg,
                                                    detectFiles="py",
                                                    blockDir="__pycache__",
                                                    blockFile="__init__",
                                                    dirOnly=False
        )

        for file in checkRecursFiles:
            checkCountRecursFiles += 1

        # -- Check if all files name are been replaced to random strings -- #
        with Bar("Check       ", fill="=", max=checkCountRecursFiles, suffix="%(percent)d%%") as bar:
            for file in checkRecursFiles:
                numberLine = 0
                # -- Check for file name in directory -- #
                for key, value in filesNameDict.items():
                    if key in file:
                        checkFilesFoundCompare[key] = value

                bar.next(1)
            bar.finish()

        if checkFilesFoundCompare != {} :
            if verboseArg:
                if checkFilesFoundCompare != {}:
                    print("\n[!] File name that have not been replaced by their random string value... :\n")
                    for key, value in checkFilesFoundCompare.items():
                        print("\n-> File : {}".format(key))
                        print("-> Value mixed : {}".format(value))
            else:
                print("\n" + Colors.ERROR + "[-] Launch intensio-obfuscatior with verbose mode [-v, --verbose] because " + \
                    "file name(s) have not been replaced by their random string value" + Colors.DISABLE)
            return 0
        else:
            return 1
