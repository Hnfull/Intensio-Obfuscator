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
from core.utils.intensio_utils import Utils, Reg

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Padding:
    
    def __init__(self):
        self.mixer          = Mixer()
        self.utils          = Utils()
        self.simpleSpace    = " "


    def CheckBasicIndentation(self, recursPythonFiles):
        # -- Check basic indentation (2 - 4 - 8) of python files -- #
        allNumIndentations  = []

        for file in recursPythonFiles:
            with open(file, "r") as inputFile:
                for eachLine in inputFile:
                    if re.match(Reg.pythonFileHeader, eachLine):
                        continue
                    else:
                        spaces = len(eachLine) - len(eachLine.lstrip())
                        if spaces == 0 or spaces == 1:
                            continue
                        else:
                            allNumIndentations.append(spaces)

        if allNumIndentations == []:
            return 0
        else:
            allNumIndentations.sort()
            return allNumIndentations[0]


    def ScriptsGenerator(self, randomClassesFunctions, mixerLengthArg):
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

        # ---------- Python random snippets code ---------- #
        if randomClassesFunctions == True:
            rand = random.randint(1, 15)
        else:
            rand = random.randint(1, 9)

        # -- snippet 1 -- #
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

        # -- snippet 2 -- #
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

        # -- snippet 3 -- #
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

        # -- snippet 4 -- #
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

        # -- snippet 5 -- #
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
    
        # -- snippet 6 -- #
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
        
        # -- snippet 7 -- #
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

        # -- snippet 8 -- #
        elif rand == 8:
            scriptPadding8 = textwrap.dedent("""
                                                {0} = '{1}'
                                                """).format(varRandom1, varRandom2)
            return scriptPadding8

        # -- snippet 9 -- #
        elif rand == 9:
            scriptPadding9 = textwrap.dedent("""
                                                {0} = '{1}'
                                                {2} = '{3} {1}'
                                                """).format(varRandom1, varRandom2, varRandom3, \
                                                            varRandom4,)
            return scriptPadding9

        # ---------- Python random functions ---------- #
        # -- snippet 10 -- #
        elif rand == 10:
            scriptPadding10 = textwrap.dedent("""
                                                def {0}():
                                                    {1} = '{2}'
                                                    {3} = True
                                                """).format(varRandom1, varRandom2, varRandom3, \
                                                            varRandom4,)
            return scriptPadding10

        # -- snippet 11 -- #
        elif rand == 11:
            scriptPadding11 = textwrap.dedent("""
                                                def {0}({1}):
                                                    {1} = '{2}'
                                                    {3} = '{4}'

                                                    if {1} == {3}:
                                                        for {5} in {3}:
                                                            if {5} == {3}:
                                                                continue
                                                            else:
                                                                {6} = False
                                                """).format(varRandom1, varRandom2, varRandom3, \
                                                            varRandom4, varRandom5, varRandom6, \
                                                            varRandom7)
            return scriptPadding11

        # -- snippet 12 -- #
        elif rand == 12:
            scriptPadding12 = textwrap.dedent("""
                                                def {0}({1}, {2}):
                                                    {1} = '{3}'
                                                    {2} = '{4}'

                                                    try:
                                                        for {5} in {1}:
                                                            if {5} == {2}:
                                                                {6} = []
                                                                {7} = None
                                                            else:
                                                                pass
                                                    except:
                                                        pass
                                                """).format(varRandom1, varRandom2, varRandom3, \
                                                            varRandom4, varRandom5, varRandom6, \
                                                            varRandom7, varRandom8)
            return scriptPadding12

        # -- snippet 13 -- #
        elif rand == 13:
            scriptPadding13 = textwrap.dedent("""
                                                def {0}({1}, {2}, {3}):
                                                    {1} = '{4}'
                                                    {2} = '{5}'
                                                    {6} = True

                                                    while {6}:
                                                        break

                                                    for {6} in {2}:
                                                        {3} = False
                                                """).format(varRandom1, varRandom2, varRandom3, \
                                                            varRandom4, varRandom5, varRandom6, \
                                                            varRandom7)
            return scriptPadding13

        # ---------- Python random classes ---------- #
        # -- snippet 14 -- #
        elif rand == 14:
            scriptPadding14 = textwrap.dedent("""
                                                class {0}:
                                                    def __init__(self):
                                                        self.{1} = '{2}'
                                                        self.{3} = '{4}'
                                                    
                                                    def {5}(self):
                                                        {6} = True
                                                        while {6}:
                                                            break
                                                """).format(varRandom1, varRandom2, varRandom3, \
                                                            varRandom4, varRandom5, varRandom6, \
                                                            varRandom7)
            return scriptPadding14

        # -- snippet 15 -- #
        elif rand == 15:
            scriptPadding15 = textwrap.dedent("""
                                                class {0}:
                                                    def __init__(self):
                                                        self.{1} = '{2}'
                                                        self.{3} = '{4}'
                                                        self.{5} = []

                                                    def {6}(self):
                                                        self.{5} = True
                                                        self.{3} = '{7}'
                                                """).format(varRandom1, varRandom2, varRandom3, \
                                                            varRandom4, varRandom5, varRandom6, \
                                                            varRandom7, varRandom8)
            return scriptPadding15

            
    def AddRandomScripts(self, outputArg, mixerLengthArg, verboseArg):
        countScriptsAdded       = 0
        countLineAdded          = 0
        countLine               = 0
        checkLine               = 0
        countRecursFiles        = 0
        multipleLinesQuotes     = 0
        basicIndentation        = None

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

        # --  Add padding script -- #
        with Bar("Obfuscation ", fill="=", max=countRecursFiles, suffix="%(percent)d%%") as bar:
            for file in recursFiles:
                with fileinput.input(file, inplace=True) as inputFile:
                    for eachLine in inputFile:
                        sys.stdout.write(eachLine)
                        if eachLine == "\n":
                            continue
                        else:
                            spaces = len(eachLine) - len(eachLine.lstrip())

                            if multipleLinesQuotes == 1:
                                if re.match(Reg.checkIfEndVarStdoutMultipleQuotes, eachLine):
                                    if self.utils.DetectMultipleLinesQuotes(eachLine) == True:
                                        multipleLinesQuotes = 0
                                        pass
                                    else:
                                        continue
                                else:
                                    continue
                            elif re.match(Reg.checkIfVarMultipleQuotes, eachLine) \
                            or re.match(Reg.checkIfStdoutMultipleQuotes, eachLine):
                                if self.utils.DetectMultipleLinesQuotes(eachLine) == False:
                                    pass
                                else:
                                    multipleLinesQuotes = 1
                                    continue
                            else:
                                pass

                            if re.match(Reg.noAddScript, eachLine):
                                continue
                            # -- Adding scripts -- #
                            elif re.match(Reg.addIndentScript, eachLine):
                                spaces = spaces + basicIndentation # add indentation
                                sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(
                                                                                        self,
                                                                                        randomClassesFunctions=False,
                                                                                        mixerLengthArg=mixerLengthArg), 
                                                                                        self.simpleSpace * spaces)
                                )
                                countScriptsAdded += 1
                            else:
                                if spaces == 0:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(
                                                                                            self,
                                                                                            randomClassesFunctions=True,
                                                                                            mixerLengthArg=mixerLengthArg), 
                                                                                            self.simpleSpace * spaces)
                                    )
                                    countScriptsAdded += 1
                                else:
                                    sys.stdout.write(textwrap.indent(Padding.ScriptsGenerator(
                                                                                            self,
                                                                                            randomClassesFunctions=False,
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

                # -- Find empty class(es) in dict -- #
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
                        if re.match(Reg.checkClassInLine, eachLine):
                            spacesClass = len(eachLine) - len(eachLine.lstrip())
                            if numberLine == numberLineInFile: # If empty class in last line
                                search = re.search(Reg.detectClasses, eachLine)
                                if search:
                                    emptyClassInfo[search.group(1)] = file
                            else: 
                                counterToCheckIndent += 1
                                search = re.search(Reg.detectClasses, eachLine)
    
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
                        if re.match(Reg.checkClassInLine, eachLine):
                            spacesClass = len(eachLine) - len(eachLine.lstrip())
                            if numberLine == numberLineInFile: # If empty class in last line
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
                            if re.match(Reg.checkClassInLine, eachLine):
                                spacesClass = len(eachLine) - len(eachLine.lstrip())
                                if numberLine == numberLineInFile: # If empty class in last line
                                    search = re.search(Reg.detectClasses, eachLine)
                                    if search:
                                        emptyClassInfo[search.group(1)] = file
                                else: 
                                    counterToCheckIndent += 1
                                    search = re.search(Reg.detectClasses, eachLine)

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

                # -- Find empty function(s) in dict -- #
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
                        if re.match(Reg.checkFunctionInLine, eachLine):
                            spacesFunc = len(eachLine) - len(eachLine.lstrip())
                            if numberLine == numberLineInFile: # If empty function last line
                                search = re.search(Reg.detectFunctions, eachLine)
                                if search:
                                    emptyFuncInfo[search.group(1)] = file
                            else: 
                                counterToCheckIndent += 1
                                search = re.search(Reg.detectFunctions, eachLine)

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
                        if re.match(Reg.checkFunctionInLine, eachLine):
                            spacesFunc = len(eachLine) - len(eachLine.lstrip())
                            if numberLine == numberLineInFile: # IIf empty function last line
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
                            if re.match(Reg.checkFunctionInLine, eachLine):
                                spacesFunc = len(eachLine) - len(eachLine.lstrip())
                                if numberLine == numberLineInFile: # If empty function last line
                                    search = re.search(Reg.detectFunctions, eachLine)
                                    if search:
                                        emptyFuncInfoCheck[search.group(1)] = file
                                else: 
                                    counterToCheckIndent += 1
                                    search = re.search(Reg.detectFunctions, eachLine)

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