# -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import fileinput
import random
import textwrap
import re
import glob

from core.obfuscation.intensio_mixer import Mixer
from core.obfuscation.intensio_remove import Remove
from core.utils.intensio_utils import Utils
from core.utils.intensio_error import EXIT_SUCCESS, EXIT_FAILURE, ERROR_BAD_ARGUMENTS

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Padding:

    def __init__(self):
        self.mixer  = Mixer()
        self.remove = Remove()
        self.utils  = Utils()

    def ScriptsGenerator(self, codeArg, mixerLevelArg):
        if mixerLevelArg == "lower":
            varFuckingRandom1   = self.mixer.GetStringMixer("lower")
            varFuckingRandom2   = self.mixer.GetStringMixer("lower")
            varFuckingRandom3   = self.mixer.GetStringMixer("lower")
            varFuckingRandom4   = self.mixer.GetStringMixer("lower")
            varFuckingRandom5   = self.mixer.GetStringMixer("lower")
            varFuckingRandom6   = self.mixer.GetStringMixer("lower")
            varFuckingRandom7   = self.mixer.GetStringMixer("lower")
            varFuckingRandom8   = self.mixer.GetStringMixer("lower")
            varFuckingRandom9   = self.mixer.GetStringMixer("lower")
            varFuckingRandom10  = self.mixer.GetStringMixer("lower")
            varFuckingRandom11  = self.mixer.GetStringMixer("lower")
            varFuckingRandom12  = self.mixer.GetStringMixer("lower")
        elif mixerLevelArg == "medium":
            varFuckingRandom1   = self.mixer.GetStringMixer("medium")
            varFuckingRandom2   = self.mixer.GetStringMixer("medium")
            varFuckingRandom3   = self.mixer.GetStringMixer("medium")
            varFuckingRandom4   = self.mixer.GetStringMixer("medium")
            varFuckingRandom5   = self.mixer.GetStringMixer("medium")
            varFuckingRandom6   = self.mixer.GetStringMixer("medium")
            varFuckingRandom7   = self.mixer.GetStringMixer("medium")
            varFuckingRandom8   = self.mixer.GetStringMixer("medium")
            varFuckingRandom9   = self.mixer.GetStringMixer("medium")
            varFuckingRandom10  = self.mixer.GetStringMixer("medium")
            varFuckingRandom11  = self.mixer.GetStringMixer("medium")
            varFuckingRandom12  = self.mixer.GetStringMixer("medium")
        elif mixerLevelArg == "high":
            varFuckingRandom1   = self.mixer.GetStringMixer("high")
            varFuckingRandom2   = self.mixer.GetStringMixer("high")
            varFuckingRandom3   = self.mixer.GetStringMixer("high")
            varFuckingRandom4   = self.mixer.GetStringMixer("high")
            varFuckingRandom5   = self.mixer.GetStringMixer("high")
            varFuckingRandom6   = self.mixer.GetStringMixer("high")
            varFuckingRandom7   = self.mixer.GetStringMixer("high")
            varFuckingRandom8   = self.mixer.GetStringMixer("high")
            varFuckingRandom9   = self.mixer.GetStringMixer("high")
            varFuckingRandom10  = self.mixer.GetStringMixer("high")
            varFuckingRandom11  = self.mixer.GetStringMixer("high")
            varFuckingRandom12  = self.mixer.GetStringMixer("high")

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
                                                    """).format(varFuckingRandom1, varFuckingRandom2, varFuckingRandom3, \
                                                        varFuckingRandom4, varFuckingRandom5, varFuckingRandom6, \
                                                        varFuckingRandom7, varFuckingRandom8, varFuckingRandom9, \
                                                        varFuckingRandom10)
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
                                                    """).format(varFuckingRandom1, varFuckingRandom2, varFuckingRandom3, \
                                                        varFuckingRandom4, varFuckingRandom5, varFuckingRandom6, \
                                                        varFuckingRandom7, varFuckingRandom8)
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
                                                    """).format(varFuckingRandom1, varFuckingRandom2, varFuckingRandom3, \
                                                        varFuckingRandom4, varFuckingRandom5, varFuckingRandom6, \
                                                        varFuckingRandom7, varFuckingRandom8, varFuckingRandom9, \
                                                        varFuckingRandom10, varFuckingRandom11, varFuckingRandom12)
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
                                                    """).format(varFuckingRandom1, varFuckingRandom2, varFuckingRandom3, \
                                                        varFuckingRandom4, varFuckingRandom5, varFuckingRandom6, \
                                                        varFuckingRandom7, varFuckingRandom8)
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
                                                    """).format(varFuckingRandom1, varFuckingRandom2, varFuckingRandom3, \
                                                        varFuckingRandom4, varFuckingRandom5, varFuckingRandom6, \
                                                        varFuckingRandom7, varFuckingRandom8, varFuckingRandom9, \
                                                        varFuckingRandom10, varFuckingRandom11, varFuckingRandom12)
                return scriptAssPadding5
    
    def AddScripts(self, oneFileArg, codeArg, outputArg, mixerLevelArg):
        countScriptsAdded   = 0
        countLineAdded      = 0
        countLine           = 0
        checkLine           = 0
        checkPassing        = 0

        print("############## [ Random scripts ] ###############\n")

        print("\n[+] Running adding of random scripts...\n")
        
        ######################################### One file only #########################################

        if oneFileArg:
            # -- Count the number of lines that will be checked before filling -- #
            with open(outputArg , "r") as readFile:
                readF = readFile.readlines()
                for eachLine in readF:
                    if not eachLine:
                        continue
                    countLine += 1

            # -- Padding scripts added -- #
            with fileinput.input(outputArg, inplace=True) as inputFile:
                for eachLine in inputFile:
                    print(eachLine)
                    if eachLine == "\n":
                        continue
                    else:
                        if codeArg == "python":
                            spaces                  = len(eachLine) - len(eachLine.lstrip()) # Check line indent
                            noAddScript             = r"(^[\#]+.*)|(\@|\s+\@)|(\s+return)|(\s+#\s{1,10}\w+)"
                            addIndentScript         = r".*\:{1}\s"
                            checkAddIndentScript    = r".*\:{1}\s\w+"

                            # -- Check if ',' char or '\' char,in end line -- #
                            listCheckEndLine = []
                            
                            for i in eachLine:
                                listCheckEndLine.append(i)
                            
                            if "," in listCheckEndLine[-2] or "\\" in listCheckEndLine[-2]:
                                continue

                            # -- Check code between """ or ''' -- #
                            if "\"\"\"" in eachLine or "\'\'\'" in eachLine:
                                checkPassing += 1

                            if checkPassing == 1: # Loop until the next """ or ''' 
                                continue
                            else:
                                checkPassing = 0    

                        if re.match(noAddScript, eachLine) is not None:
                            continue
                        elif re.match(addIndentScript, eachLine) is not None:
                            if re.match(checkAddIndentScript, eachLine) is not None:
                                continue
                            else:
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
                            else:
                                continue                    
                            
            # -- Check padding has added in output script -- #
            with open(outputArg , "r") as readFile:
                readF = readFile.readlines()
                for eachLine in readF:
                    if not eachLine:
                        continue
                    checkLine += 1

            countLineAdded = checkLine - countLine

            if checkLine > countLine:
                print("-> {0} scripts added\n".format(countScriptsAdded))
                print("-> {0} lines added\n".format(countLineAdded))
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

            # -- Count the number of lines that will be checked before filling -- #
            for output in recursFiles:
                if re.match(blockdirs, output):
                    continue
                else:
                    with open(output , "r") as readFile:
                        readF = readFile.readlines()
                        for eachLine in readF:
                            if not eachLine:
                                continue
                            countLine += 1

            # -- Padding scripts added -- #
            for output in recursFiles:
                if re.match(blockdirs, output):
                    continue
                else:
                    with fileinput.input(output, inplace=True) as inputFile:
                        for eachLine in inputFile:
                            print(eachLine)
                            if eachLine == "\n":
                                continue
                            else:
                                if codeArg == "python":
                                    spaces                  = len(eachLine) - len(eachLine.lstrip()) # Check line indent
                                    noAddScript             = r"(^[\#]+.*)|(\@|\s+\@)|(\s+return)|(\s+#\s{1,10}\w+)"
                                    addIndentScript         = r".*\:{1}\s"
                                    checkAddIndentScript    = r".*\:{1}\s\w+"

                                    # -- Check if ',' char or '\' char,in end line -- #
                                    listCheckEndLine = []
                                    
                                    for i in eachLine:
                                        listCheckEndLine.append(i)
                                    
                                    if "," in listCheckEndLine[-2] or "\\" in listCheckEndLine[-2]:
                                        continue

                                    # -- Check code between """ or ''' -- #
                                    if '\"\"\"' in eachLine or "\'\'\'" in eachLine:
                                        checkPassing += 1
                
                                    if checkPassing == 1: # Loop until the next """ or ''' 
                                        continue
                                    else:
                                        checkPassing = 0

                                if re.match(noAddScript, eachLine) is not None:
                                    continue
                                elif re.match(addIndentScript, eachLine) is not None:
                                    if re.match(checkAddIndentScript, eachLine) is not None:
                                        continue
                                    else:
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
                                    else:
                                        continue
                                
            # -- Check padding has added in output script -- #
            for output in recursFiles:
                if re.match(blockdirs, output):
                    continue
                else:
                    with open(output , "r") as readFile:
                        readF = readFile.readlines()
                        for eachLine in readF:
                            if not eachLine:
                                continue
                            checkLine += 1
            
            countLineAdded = checkLine - countLine

            if checkLine > countLine:
                print("-> {0} scripts added\n".format(countScriptsAdded))
                print("-> {0} lines added\n".format(countLineAdded))
                if (self.remove.LineBreaks(oneFileArg, codeArg, outputArg) == 0):
                    return EXIT_SUCCESS
                else:
                    return EXIT_FAILURE
            else:
                return EXIT_FAILURE
    