# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import fileinput
import random
import textwrap
import re
import sys
from progress.bar import Bar

from core.obfuscation.intensio_mixer import Mixer
from core.utils.intensio_utils import Utils

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Padding:
    
    def __init__(self):
        self.mixer          = Mixer()
        self.utils          = Utils()
        self.simpleSpace    = " "


    def CheckBasicIndentation(self, recursPythonFiles):
        # -- Check basic indentation (2 - 4 - 8) of python files -- #
        allNumIndentations  = []
        headerPythonFile    = r"\s*#!.*[python|1-9]|\s*#.*-*-$"

        for file in recursPythonFiles:
            with open(file, "r") as inputFile:
                for eachLine in inputFile:
                    if re.match(headerPythonFile, eachLine):
                        continue
                    else:
                        spaces = len(eachLine) - len(eachLine.lstrip())
                        if spaces == 0 or spaces == 1:
                            continue
                        else:
                            allNumIndentations.append(spaces)

        allNumIndentations.sort()
        return allNumIndentations[0]

    def ScriptsGenerator(self, mixerLengthArg):
        varRandom1  = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
        varRandom2  = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
        varRandom3  = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
        varRandom4  = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
        varRandom5  = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
        varRandom6  = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
        varRandom7  = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
        varRandom8  = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
        varRandom9  = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
        varRandom10 = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
        varRandom11 = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
        varRandom12 = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
        varRandom13 = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
        varRandom14 = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)

        # ---------- Python random scripts ---------- #
        rand = random.randint(1, 7)

        # -- script 1 -- #
        if rand == 1:
            scriptPadding1 = textwrap.dedent("""
                                                {0} = '{5}'
                                                {1} = '{6}'
                                                {2} = '{7}'
                                                {3} = '{8}'
                                                {4} = '{9}'
                                                if {0} in {1}:
                                                    {0} = {4}
                                                    if {1} in {2}:
                                                        {1} = {3}
                                                elif {1} in {0}:
                                                    {2} = {1}
                                                    if {2} in {1}:
                                                        {1} = {4}
                                                """).format(varRandom1, varRandom2, varRandom3, varRandom4, varRandom5, \
                                                            varRandom6, varRandom7, varRandom8, varRandom9, varRandom10)
            return scriptPadding1

        # -- script 2 -- #
        elif rand == 2:
            scriptPadding2 = textwrap.dedent("""
                                                {0} = '{2}'
                                                {1} = '{3}'
                                                if {0} != {1}:
                                                    {0} = '{3}'
                                                    {1} = {0}
                                                    {0} = '{2}'
                                                """).format(varRandom1, varRandom2, varRandom3, varRandom4)
            return scriptPadding2

        # -- script 3 -- #
        elif rand == 3:
            scriptPadding3 = textwrap.dedent("""
                                                {0} = '{6}'
                                                {1} = '{7}'
                                                {2} = '{8}'
                                                {3} = '{9}'
                                                {4} = '{10}'
                                                {5} = '{11}'
                                                if {0} != {3}:
                                                    {1} = {2}
                                                    for {5} in {3}:
                                                        if {5} != {2}:
                                                            {1} = {1}
                                                        else:
                                                            {4} = {0}
                                                else:
                                                    {2} = {0}
                                                    {0} = {4}
                                                    if {2} == {0}:
                                                        for {5} in {0}:
                                                            if {5} == {2}:
                                                                {2} = {0}
                                                            else:
                                                                {2} = {4}
                                                """).format(varRandom1, varRandom2, varRandom3, varRandom4, varRandom5, \
                                                            varRandom6, varRandom7, varRandom8, varRandom9, varRandom10, \
                                                            varRandom11, varRandom12)
            return scriptPadding3

        # -- script 4 -- #
        elif rand == 4:
            scriptPadding4 = textwrap.dedent("""
                                                {0} = '{3}'
                                                {1} = '{4}'
                                                {2} = '{5}'
                                                if {0} == {1}:
                                                    {2} = '{5}'
                                                    {2} = {0}
                                                else:
                                                    {2} = '{5}'
                                                    {2} = '{3}'
                                                """).format(varRandom1, varRandom2, varRandom3, varRandom4, \
                                                            varRandom5, varRandom6,)
            return scriptPadding4

        # -- script 5 -- #
        elif rand == 5:
            scriptPadding5 = textwrap.dedent("""
                                                {0} = '{6}'
                                                {1} = '{7}'
                                                {2} = '{8}'
                                                {3} = '{9}'
                                                {4} = '{10}'
                                                {5} = '{11}'
                                                if {2} == {3}:
                                                    for {5} in {4}:
                                                        if {5} == {3}:
                                                            {4} = {0}
                                                        else:
                                                            {3} = {1}
                                                """).format(varRandom1, varRandom2, varRandom3, \
                                                            varRandom4, varRandom5, varRandom6, \
                                                            varRandom7, varRandom8, varRandom9, \
                                                            varRandom10, varRandom11, varRandom12)
            return scriptPadding5
    
        # -- script 6 -- #
        elif rand == 6:
            scriptPadding6 = textwrap.dedent("""
                                                {0} = '{4}'
                                                {1} = '{5}'
                                                {2} = '{6}'
                                                {3} = '{7}'
                                                if {1} == {0}:
                                                    for {0} in {1}:
                                                        if {1} == {1}:
                                                            {2} = '{3}'
                                                        elif {2} == {3}:
                                                            {3} = {0}
                                                        else:
                                                            {0} = {1}
                                                elif {2} == {2}:
                                                    for {2} in {1}:
                                                        if {3} == {1}:
                                                            {2} = '{3}'
                                                        elif {2} == {3}:
                                                            {3} = {0}
                                                        else:
                                                            {0} = {1}
                                                            for {2} in {1}:
                                                                if {3} == {1}:
                                                                    {2} = '{3}'
                                                                elif {2} == {3}:
                                                                    {3} = {0}
                                                                else:
                                                                    {0} = {3}
                                                else:
                                                    {0} = {1}
                                                """).format(varRandom1, varRandom2, varRandom3, \
                                                            varRandom4, varRandom5, varRandom6, \
                                                            varRandom7, varRandom8)
            return scriptPadding6
        
        # -- script 7 -- #
        elif rand == 7:
            scriptPadding7 = textwrap.dedent("""
                                                {0} = '{7}'
                                                {1} = '{8}'
                                                {2} = '{9}'
                                                {3} = '{10}'
                                                {4} = '{11}'
                                                {5} = '{12}'
                                                {6} = [
                                                        '{7}',
                                                        '{9}',
                                                        '{11}',
                                                        '{13}'
                                                ]
                                                for {0} in {5}:
                                                    for {1} in {2}:
                                                        if {3} == {4}:
                                                            {1} = {0}
                                                        elif {4} == {1}:
                                                            {1} = {5}
                                                        else:
                                                            {4} = {5}
                                                            for {1} in {6}:
                                                                {2} = {1}
                                                """).format(varRandom1, varRandom2, varRandom3, \
                                                            varRandom4, varRandom5, varRandom6, \
                                                            varRandom7, varRandom8, varRandom9, \
                                                            varRandom10, varRandom11, varRandom12, \
                                                            varRandom13, varRandom14)
            return scriptPadding7


    def AddRandomScripts(self, outputArg, mixerLengthArg, verboseArg):
        countScriptsAdded       = 0
        countLineAdded          = 0
        countLine               = 0
        checkLine               = 0
        checkQuotePassing       = 0
        checkCharPassing        = 0
        checkOtherCharPassing   = 0
        countRecursFiles        = 0
        basicIndentation        = None

        addIndentScript         = r".*\:{1}\s*$"
        quotesIntoVariable      = r".*={1}\s*[\"|\']{3}"
        quotesEndMultipleLines  = r"^\s*[\"|\']{3}\)?\.?"
        quotesInRegex           = r"={1}\s*r{1}[\"|\']{3}"
        noAddScript             = r"^\@|\s+\@|\s+return|\s*def\s+.+\s*\:{1}|^class\s+.+\s*\:{1}|.*[\{|\[|\(|\)|\]|\}|,|\\|^]\s*$|\s+yield.*|\s+raise.*"

        recursFiles = self.utils.CheckFileDir(
                                            output=outputArg, 
                                            detectFiles="py", 
                                            blockDir="__pycache__", 
                                            blockFile=False,
                                            dirOnly=False
        )

        if verboseArg:
            print("\n[*] Check basic indentation...\n")
        
        basicIndentation = Padding.CheckBasicIndentation(self, recursFiles)

        if verboseArg:
            print("[*] Basic indentation : {} spaces".format(basicIndentation))

        for number in recursFiles:
            countRecursFiles += 1

        print("\n[+] Running add of random scripts in {} file(s)...\n".format(countRecursFiles))

        # -- Count the number of lines that will be checked before filling -- #
        with Bar("Setting up  ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                with open(file , "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if not eachLine:
                            continue
                        countLine += 1

                bar.next(1)
            bar.finish()

        # -- Padding script added -- #
        with Bar("Obfuscation ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        sys.stdout.write(eachLine)
                        if eachLine == "\n":
                            continue
                        else:
                            spaces = len(eachLine) - len(eachLine.lstrip())

                            # -- Detect code into 3 quotes excepted comments -- #
                            if re.match(quotesIntoVariable, eachLine):
                                if re.match(quotesInRegex, eachLine):
                                    pass
                                else:
                                    checkQuotePassing += 1
                                    continue
                            elif re.match(quotesEndMultipleLines, eachLine):
                                if re.match(quotesInRegex, eachLine):
                                    pass
                                else:
                                    checkQuotePassing += 1
                                    if checkQuotePassing == 2:
                                        checkQuotePassing = 0
                                    continue
                            if checkQuotePassing == 1:
                                continue
                            elif checkQuotePassing == 2:
                                checkQuotePassing = 0
                                pass
                            else:
                                pass
                            
                            # -- Check dict, list, tuple in multiple lines -- #
                            if checkCharPassing == 1:
                                if re.match(r".*[\"|\'|\)|\]|\}|\w]\s*$", eachLine):
                                    checkCharPassing = 0
                                    continue
                                else:
                                    continue
                            elif checkOtherCharPassing >= 1:
                                if re.match(r".*[\"|\'|\)|\]|\}|\w]\s*$", eachLine):
                                    checkOtherCharPassing -= 1
                                    continue
                                else:
                                    if re.match(r".*[\(|\{|\[]\s*$", eachLine):
                                        checkOtherCharPassing += 1
                                        continue
                            else:
                                pass

                            if re.match(noAddScript, eachLine):
                                if re.match(r".*[\\|,]\s*$", eachLine):
                                    if checkCharPassing == 1:
                                        continue
                                    else:
                                        checkCharPassing = 1
                                        continue
                                elif re.match(r".*[\(|\{|\[]\s*$", eachLine):
                                    checkOtherCharPassing += 1
                                    continue
                                else:
                                    continue
                            # -- Adding scripts -- #
                            elif re.match(addIndentScript, eachLine):
                                spaces = spaces + basicIndentation # add indentation
                                sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(
                                                                                        self, 
                                                                                        mixerLengthArg=mixerLengthArg), 
                                                                                        self.simpleSpace * spaces)
                                )
                                countScriptsAdded += 1
                            else:
                                sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(
                                                                                        self, 
                                                                                        mixerLengthArg=mixerLengthArg), 
                                                                                        self.simpleSpace * spaces)
                                )
                                countScriptsAdded += 1

                bar.next(1)
            bar.finish()

        # -- Check if padding has added in output script -- #
        with Bar("Check       ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                with open(file , "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if not eachLine:
                            continue    
                        checkLine += 1

                bar.next(1)
            bar.finish()

        countLineAdded = checkLine - countLine

        if checkLine > countLine:    
            print("\n-> {} scripts added in {} file(s)\n".format(countScriptsAdded, countRecursFiles))
            print("-> {} lines added in {} file(s)\n".format(countLineAdded, countRecursFiles))
            return 0
        else:
            return 1
    
    
    def EmptyClasses(self, outputArg, mixerLengthArg, verboseArg):
        countRecursFiles        = 0
        counterToCheckIndent    = 0
        numberLine              = 0
        numberLineInFile        = 0
        emptyClassInfo          = {}
        emptyClassInfoCheck     = {}
        basicIndentation        = None

        classDefined        = r"class\s+(\w+)"
        detectClass         = r"^class\s+\w+|\s+class\s+\w+"        
        
        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg, 
                                                detectFiles="py", 
                                                blockDir="__pycache__", 
                                                blockFile=False,
                                                dirOnly=False
        )

        basicIndentation = Padding.CheckBasicIndentation(self, recursFiles)

        for number in recursFiles:
            countRecursFiles += 1

        with Bar("Correction  ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                numberLineInFile    = 0
                numberLine          = 0
                # -- Count all line(s) in file -- #
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        numberLineInFile += 1

                # -- Find and put empty class(es) in dict -- #
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        numberLine += 1
                        if counterToCheckIndent == 1: 
                            spacesAfterClass = len(eachLine) - len(eachLine.lstrip())
                            counterToCheckIndent = 0
                            if spacesAfterClass == spacesClass:
                                if search:
                                    emptyClassInfo[search.group(1)] = file
                                    numberLineInFile += 1 # Adding one line because padding will be added
                                    numberLine += 1 # Adding one line because padding will be added
                        if re.match(detectClass, eachLine):
                            spacesClass = len(eachLine) - len(eachLine.lstrip())
                            if numberLine == numberLineInFile:
                                search = re.search(classDefined, eachLine)
                                if search:
                                    emptyClassInfo[search.group(1)] = file
                            else: 
                                counterToCheckIndent += 1
                                search = re.search(classDefined, eachLine)
                
                # -- Add padding in empty class(es) -- #
                numberLine = 0
                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        numberLine += 1
                        if counterToCheckIndent == 1:
                            spacesAfterClass = len(eachLine) - len(eachLine.lstrip())
                            counterToCheckIndent = 0
                            if spacesAfterClass == spacesClass:
                                paddingVar1 = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                                paddingVar2 = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                                finalVarPadding = "{} = '{}'\n".format(paddingVar1, paddingVar2)
                                spacesClass = spacesClass + basicIndentation
                                sys.stdout.write(textwrap.indent(finalVarPadding, self.simpleSpace * spacesClass))                                                                
                                numberLine += 1
                        sys.stdout.write(eachLine)
                        if re.match(detectClass, eachLine):
                            spacesClass = len(eachLine) - len(eachLine.lstrip())
                            if numberLine == numberLineInFile:
                                paddingVar1 = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                                paddingVar2 = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                                finalVarPadding = "{} = '{}'\n".format(paddingVar1, paddingVar2)
                                spacesClass = spacesClass + basicIndentation
                                sys.stdout.write(textwrap.indent(finalVarPadding, self.simpleSpace * spacesClass))  
                            else:
                                counterToCheckIndent += 1

                bar.next(1)
            bar.finish()

        # -- Check if class(es) is still empty -- #
        if emptyClassInfo != {}:
            with Bar("Check       ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
                for file in recursFiles:
                    numberLineInFile    = 0
                    numberLine          = 0
                    with open(file, "r") as readFile:
                        readF = readFile.readlines()
                        for eachLine in readF:
                            numberLine += 1
                            if counterToCheckIndent == 1:
                                spacesAfterClass = len(eachLine) - len(eachLine.lstrip())
                                counterToCheckIndent = 0
                                if spacesAfterClass == spacesClass:
                                    if search:
                                        emptyClassInfo[search.group(1)] = file
                                        numberLineInFile += 1
                                        numberLine += 1
                            if re.match(detectClass, eachLine):
                                spacesClass = len(eachLine) - len(eachLine.lstrip())
                                if numberLine == numberLineInFile:
                                    search = re.search(classDefined, eachLine)
                                    if search:
                                        emptyClassInfo[search.group(1)] = file
                                else: 
                                    counterToCheckIndent += 1
                                    search = re.search(classDefined, eachLine)

                    bar.next(1)
                bar.finish()
        
            if emptyClassInfoCheck == {}:
                for key, value in emptyClassInfo.items():
                    print("\n-> File : {}".format(value))
                    print("-> Padding added in : {} ( empty class )".format(key))
                return 0   
            else:
                if verboseArg:
                    print("\n[!] No padding added to empty class(es)... :\n")
                    for key, value in emptyClassInfoCheck.items():
                        print("\n-> File : {}".format(value))
                        print("-> Class : {}".format(key))
                return 1
        else:
            print("[!] No empty class found in {}".format(outputArg))
            return 0

    
    def EmptyFunctions(self, outputArg, mixerLengthArg, verboseArg):
        countRecursFiles        = 0
        counterToCheckIndent    = 0
        numberLine              = 0
        numberLineInFile        = 0
        emptyFuncInfo           = {}
        emptyFuncInfoCheck      = {}
        basicIndentation        = None

        functionDefined = r"def\s+(\w+)"   
        detectFunction  = r"^def\s+\w+|\s+def\s\w+"
        
        recursFiles = self.utils.CheckFileDir(
                                                output=outputArg, 
                                                detectFiles="py", 
                                                blockDir="__pycache__", 
                                                blockFile=False,
                                                dirOnly=False
        )

        basicIndentation = Padding.CheckBasicIndentation(self, recursFiles)

        for number in recursFiles:
            countRecursFiles += 1

        with Bar("Correction  ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                numberLineInFile    = 0
                numberLine          = 0
                # -- Count all line(s) in file -- #
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        numberLineInFile += 1

                # -- Find and put empty function(s) in dict -- #
                with open(file, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        numberLine += 1
                        if counterToCheckIndent == 1:
                            spacesAfterFunc = len(eachLine) - len(eachLine.lstrip())
                            counterToCheckIndent = 0
                            if spacesAfterFunc == spacesFunc:
                                if search:
                                    emptyFuncInfo[search.group(1)] = file
                                    numberLineInFile += 1 # Adding one line because padding will be added
                                    numberLine += 1 # Adding one line because padding will be added
                        if re.match(detectFunction, eachLine):
                            spacesFunc = len(eachLine) - len(eachLine.lstrip())
                            if numberLine == numberLineInFile:
                                search = re.search(functionDefined, eachLine)
                                if search:
                                    emptyFuncInfo[search.group(1)] = file
                            else: 
                                counterToCheckIndent += 1
                                search = re.search(functionDefined, eachLine)

                # -- Add padding in empty function(s) -- #
                numberLine = 0
                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        numberLine += 1
                        if counterToCheckIndent == 1:
                            spacesAfterFunc = len(eachLine) - len(eachLine.lstrip())
                            counterToCheckIndent = 0
                            if spacesAfterFunc == spacesFunc:
                                paddingVar1 = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                                paddingVar2 = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                                finalVarPadding = "{} = '{}'\n".format(paddingVar1, paddingVar2)
                                spacesFunc = spacesFunc + basicIndentation
                                sys.stdout.write(textwrap.indent(finalVarPadding, self.simpleSpace * spacesFunc))                                                                
                                numberLine += 1 
                        sys.stdout.write(eachLine)
                        if re.match(detectFunction, eachLine):
                            spacesFunc = len(eachLine) - len(eachLine.lstrip())
                            if numberLine == numberLineInFile:
                                paddingVar1 = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                                paddingVar2 = self.mixer.GetStringMixer(mixerLengthArgDefined=mixerLengthArg)
                                finalVarPadding = "{} = '{}'\n".format(paddingVar1, paddingVar2)
                                spacesFunc = spacesFunc + basicIndentation
                                sys.stdout.write(textwrap.indent(finalVarPadding, self.simpleSpace * spacesFunc))          
                            else:
                                counterToCheckIndent += 1

                bar.next(1)
            bar.finish()

        # -- Check if function(s) is still empty -- #
        if emptyFuncInfo != {}:
            with Bar("Check       ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
                for file in recursFiles:
                    numberLineInFile    = 0
                    numberLine          = 0
                    with open(file, "r") as readFile:
                        readF = readFile.readlines()
                        for eachLine in readF:
                            numberLine += 1
                            if counterToCheckIndent == 1:
                                spacesAfterFunc = len(eachLine) - len(eachLine.lstrip())
                                counterToCheckIndent = 0
                                if spacesAfterFunc == spacesFunc:
                                    if search:
                                        emptyFuncInfoCheck[search.group(1)] = file
                                        numberLineInFile += 1
                                        numberLine += 1
                            if re.match(detectFunction, eachLine):
                                spacesFunc = len(eachLine) - len(eachLine.lstrip())
                                if numberLine == numberLineInFile:
                                    search = re.search(functionDefined, eachLine)
                                    if search:
                                        emptyFuncInfoCheck[search.group(1)] = file
                                else: 
                                    counterToCheckIndent += 1
                                    search = re.search(functionDefined, eachLine)

                    bar.next(1)
                bar.finish()

            if emptyFuncInfoCheck == {}:
                for key, value in emptyFuncInfo.items():
                    print("\n-> File : {}".format(value))
                    print("-> Padding added in : {} ( empty function )".format(key))
                return 0
            else:
                if verboseArg:
                    print("\n[!] No padding added to empty function(s)... :\n")
                    for key, value in emptyFuncInfoCheck.items():
                        print("\n-> File : {}".format(value))
                        print("-> Function : {}".format(key))
                return 1
        else:
            print("[!] No empty function found in {}".format(outputArg))
            return 0