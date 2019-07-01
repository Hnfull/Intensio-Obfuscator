# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import fileinput
import random
import textwrap
import re
import glob
from tqdm import tqdm

from core.obfuscation.intensio_mixer import Mixer
from core.obfuscation.intensio_remove import Remove
from core.utils.intensio_utils import Utils
from core.utils.intensio_error import EXIT_SUCCESS, EXIT_FAILURE, ERROR_BAD_ARGUMENTS

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Padding:

    def __init__(self):
        self.mixer  = Mixer()
        self.remove = Remove()
        self.utils  = Utils()

    def ScriptsGenerator(self, codeArg, mixerLevelArg):
        if mixerLevelArg == "lower":
            varRandom1   = self.mixer.GetStringMixer("lower")
            varRandom2   = self.mixer.GetStringMixer("lower")
            varRandom3   = self.mixer.GetStringMixer("lower")
            varRandom4   = self.mixer.GetStringMixer("lower")
            varRandom5   = self.mixer.GetStringMixer("lower")
            varRandom6   = self.mixer.GetStringMixer("lower")
            varRandom7   = self.mixer.GetStringMixer("lower")
            varRandom8   = self.mixer.GetStringMixer("lower")
            varRandom9   = self.mixer.GetStringMixer("lower")
            varRandom10  = self.mixer.GetStringMixer("lower")
            varRandom11  = self.mixer.GetStringMixer("lower")
            varRandom12  = self.mixer.GetStringMixer("lower")
        elif mixerLevelArg == "medium":
            varRandom1   = self.mixer.GetStringMixer("medium")
            varRandom2   = self.mixer.GetStringMixer("medium")
            varRandom3   = self.mixer.GetStringMixer("medium")
            varRandom4   = self.mixer.GetStringMixer("medium")
            varRandom5   = self.mixer.GetStringMixer("medium")
            varRandom6   = self.mixer.GetStringMixer("medium")
            varRandom7   = self.mixer.GetStringMixer("medium")
            varRandom8   = self.mixer.GetStringMixer("medium")
            varRandom9   = self.mixer.GetStringMixer("medium")
            varRandom10  = self.mixer.GetStringMixer("medium")
            varRandom11  = self.mixer.GetStringMixer("medium")
            varRandom12  = self.mixer.GetStringMixer("medium")
        elif mixerLevelArg == "high":
            varRandom1   = self.mixer.GetStringMixer("high")
            varRandom2   = self.mixer.GetStringMixer("high")
            varRandom3   = self.mixer.GetStringMixer("high")
            varRandom4   = self.mixer.GetStringMixer("high")
            varRandom5   = self.mixer.GetStringMixer("high")
            varRandom6   = self.mixer.GetStringMixer("high")
            varRandom7   = self.mixer.GetStringMixer("high")
            varRandom8   = self.mixer.GetStringMixer("high")
            varRandom9   = self.mixer.GetStringMixer("high")
            varRandom10  = self.mixer.GetStringMixer("high")
            varRandom11  = self.mixer.GetStringMixer("high")
            varRandom12  = self.mixer.GetStringMixer("high")

        # ---------- Python random scripts ---------- #
        if codeArg == "python":
            rand = random.randint(1, 5)

            # -- script 1 -- #
            if rand == 1:
                scriptAssPadding1 = textwrap.dedent("""
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
                return scriptAssPadding1

            # -- script 2 -- #
            elif rand == 2:
                scriptAssPadding2 = textwrap.dedent("""
                                                    {0} = '{4}'
                                                    {1} = '{5}'
                                                    if {0} != {1}:
                                                        {2} = '{6}'
                                                        {3} = '{7}'
                                                        {3} = {2}
                                                    """).format(varRandom1, varRandom2, varRandom3, varRandom4, varRandom5, \
                                                                varRandom6, varRandom7, varRandom8)
                return scriptAssPadding2

            # -- script 3 -- #
            elif rand == 3:
                scriptAssPadding3 = textwrap.dedent("""
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
                return scriptAssPadding3

            # -- script 4 -- #
            elif rand == 4:
                scriptAssPadding4 = textwrap.dedent("""
                                                    {0} = '{4}'
                                                    {1} = '{5}'
                                                    {3} = '{7}'
                                                    if {0} == {1}:
                                                        {2} = '{6}'
                                                        {2} = {0}
                                                    else:
                                                        {2} = '{6}'
                                                        {2} = {3}
                                                    """).format(varRandom1, varRandom2, varRandom3, varRandom4, \
                                                                varRandom5, varRandom6, varRandom7, varRandom8)
                return scriptAssPadding4

            # -- script 5 -- #
            elif rand == 5:
                scriptAssPadding5 = textwrap.dedent("""
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
                return scriptAssPadding5
    
    
    def AddScripts(self, codeArg, outputArg, mixerLevelArg):
        listCheckLineWhitoutSpace       = []
        listCheckLine                   = []
        countBackSlash                  = 0
        countScriptsAdded               = 0
        countLineAdded                  = 0
        countLine                       = 0
        checkLine                       = 0
        checkQuotePassing               = 0
        checkCharPassing                = 0
        countRecursFiles                = 0
        checkParenthesesCharPassing     = 0
        checkBracketsCharPassing        = 0
        checkBracesCharPassing          = 0
        
        if codeArg == "python":
            detectFile  = "py"
            blockDirs   = r"__pycache__"

        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), detectFile), recursive=True)]

        # -- Count the number of lines that will be checked before filling -- #
        for file in recursFiles:
            if re.match(blockDirs, file):
                continue
            else:
                with open(file , "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if not eachLine:
                            continue
                        countLine += 1

        for number in recursFiles:
            countRecursFiles += 1

        print("\n[+] Running adding of random scripts in {0} file(s)...\n".format(countRecursFiles))

        # -- Padding scripts added -- #
        with tqdm(total=countRecursFiles) as pbar:
            for file in recursFiles:
                pbar.update(1)
                if re.match(blockDirs, file):
                    continue
                else:
                    with fileinput.input(file, inplace=True) as inputFile:
                        for eachLine in inputFile:
                            print(eachLine)
                            if eachLine == "\n" or "coding" in eachLine:
                                continue
                            else:
                                if codeArg == "python":
                                    listCheckLine                       = [] # Initialize var
                                    spaces                              = len(eachLine) - len(eachLine.lstrip()) # Check line indent

                                    detectStringVar                     = r".*\w+\s*\={1}\s*r+[\"|\']{1}"
                                    noAddScript                         = r"^\@|\s+\@|\s+return|\s*def\s+.+\s*\:{1}|^class\s+.+\s*\:{1}|.*[\[|\(|\{|\,|\\]$|\s+[\)|\]|\}]$"
                                    addIndentScript                     = r".*\:{1}\s"
                                    quoteIntoVariable                   = r".*\={1}\s*\w*\.?\w*[\(|\.]{1}[\"|\']{3}|.*\={1}\s*[\"|\']{3}" # """ and ''' before an variables
                                    quoteOfCommentariesMultipleLines    = r"^\s*[\"|\']{3}$"        # """ and ''' without before variables and if commentaries is over multiple lines
                                    quoteOfEndCommentariesMultipleLines = r"^\s*[\"|\']{3}\)?\.?"   # """ and ''' without before variables, if commentaries is over multiple lines and he finish by .format() funtion
                                    
                                    for i in eachLine:
                                        listCheckLine.append(i)

                                    # -- Check line below after '\' backslash char -- #     
                                    if re.match(r".+\\$", eachLine):
                                        countBackSlash += 1
                                    if countBackSlash > 0:
                                        if re.match(r".+\\$", eachLine) is None:
                                            countBackSlash = 0
                                            continue

                                    # -- Check if end char in line is " or ' -- #
                                    if re.match(r"\"|\'", listCheckLine[-2]):
                                        try:
                                            if re.match(r"\'|\"", listCheckLine[-3]) and re.match(r"\'|\"", listCheckLine[-4]):
                                                pass
                                            else:
                                                if re.match(detectStringVar, eachLine):
                                                    pass
                                                else:
                                                    continue
                                        except IndexError:
                                            continue
        
                                    # -- Check code into """ or ''' -- #
                                    if re.match(quoteIntoVariable, eachLine):
                                        checkQuotePassing += 1
                                        continue
                                    elif re.match(quoteOfCommentariesMultipleLines, eachLine) or re.match(quoteOfEndCommentariesMultipleLines, eachLine):
                                        checkQuotePassing += 1
                                        if checkQuotePassing == 2:
                                            checkQuotePassing = 0
                                        continue

                                    if checkQuotePassing == 1:
                                        continue
                                    elif checkQuotePassing == 2:
                                        checkQuotePassing = 0
                                        continue
                                    else:
                                        checkQuotePassing = 0

                                # -- Add scripts -- #
                                if re.match(noAddScript, eachLine) is not None:
                                    continue
                                elif re.match(addIndentScript, eachLine) is not None:
                                    if spaces == 0:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg),"    "))
                                        countScriptsAdded += 1                                                                
                                    elif spaces == 4:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "        "))
                                        countScriptsAdded += 1
                                    elif spaces == 8:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "            "))
                                        countScriptsAdded += 1
                                    elif spaces == 12:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                "))
                                        countScriptsAdded += 1
                                    elif spaces == 16:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                    "))
                                        countScriptsAdded += 1
                                    elif spaces == 20:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                        "))
                                        countScriptsAdded += 1
                                    elif spaces == 24:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                            "))
                                        countScriptsAdded += 1
                                    elif spaces == 28:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                "))
                                        countScriptsAdded += 1
                                    elif spaces == 32:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                    "))
                                        countScriptsAdded += 1
                                    elif spaces == 36:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                        "))
                                        countScriptsAdded += 1
                                    elif spaces == 40:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                            "))
                                        countScriptsAdded += 1
                                    elif spaces == 44:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                                "))
                                        countScriptsAdded += 1
                                    elif spaces == 48:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                                    "))
                                        countScriptsAdded += 1
                                    elif spaces == 52:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                                        "))
                                        countScriptsAdded += 1
                                    elif spaces == 56:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                                            "))
                                        countScriptsAdded += 1
                                    elif spaces == 60:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                                                "))
                                        countScriptsAdded += 1
                                    else:
                                        continue
                                else:
                                    if spaces == 0:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg),""))
                                        countScriptsAdded += 1
                                    elif spaces == 4:                                                                       
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "    "))
                                        countScriptsAdded += 1
                                    elif spaces == 8:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "        "))
                                        countScriptsAdded += 1
                                    elif spaces == 12:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "            "))
                                        countScriptsAdded += 1
                                    elif spaces == 16:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                "))
                                        countScriptsAdded += 1
                                    elif spaces == 20:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                    "))
                                        countScriptsAdded += 1
                                    elif spaces == 24:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                        "))
                                        countScriptsAdded += 1
                                    elif spaces == 28:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                            "))
                                        countScriptsAdded += 1
                                    elif spaces == 32:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                "))
                                        countScriptsAdded += 1
                                    elif spaces == 36:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                    "))
                                        countScriptsAdded += 1
                                    elif spaces == 40:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                        "))
                                        countScriptsAdded += 1
                                    elif spaces == 44:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                            "))
                                        countScriptsAdded += 1
                                    elif spaces == 48:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                                "))
                                        countScriptsAdded += 1
                                    elif spaces == 52:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                                    "))
                                        countScriptsAdded += 1
                                    elif spaces == 56:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                                        "))
                                        countScriptsAdded += 1
                                    elif spaces == 60:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                                                            "))
                                        countScriptsAdded += 1
                                    else:
                                        continue
                                
        # -- Check padding has added in output script -- #
        for file in recursFiles:
            if re.match(blockDirs, file):
                continue
            else:
                with open(file , "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if not eachLine:
                            continue    
                        checkLine += 1
        
        countLineAdded = checkLine - countLine

        if (self.remove.LineBreaks(codeArg, outputArg) == 0):
            if checkLine > countLine:    
                print("\n-> {0} scripts added in {1} file(s)\n".format(countScriptsAdded, countRecursFiles))
                print("-> {0} lines added in {1} file(s)\n".format(countLineAdded, countRecursFiles))
                return EXIT_SUCCESS
                
            else:
                return EXIT_FAILURE
        else:
            return EXIT_FAILURE