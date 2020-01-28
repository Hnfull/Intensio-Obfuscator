# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import random
import string

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Mixer:
    
    def __init__(self):
        self.lenLower   = 32
        self.lenMedium  = 64
        self.lenHigh    = 128
        self.charsGroup = {
                            "chars0" : "abcdK",
                            "chars1" : "efghL",
                            "chars2" : "ijklM",
                            "chars3" : "mnopN",
                            "chars4" : "qrstO",
                            "chars5" : "uvwxP",
                            "chars6" : "yzABQ",
                            "chars7" : "CDEFR",
                            "chars8" : "GHIJS",
                            "chars9" : "TUVWXYZ"
        }


    def StringGeneratorSimple(self, stringLength):
        return "".join(random.choice(string.ascii_letters) for i in range(stringLength))
    

    def StringGeneratorHarder(self, stringLength):
        randomCharsList = []

        if stringLength == 32:
            randNumber = random.randrange(10000000000000000000000000000000)
        elif stringLength == 64:
            randNumber = random.randrange(1000000000000000000000000000000000000000000000000000000000000000)
        elif stringLength == 128:
            randNumber = random.randrange(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

        randNumber = str(randNumber)

        for i in randNumber:
            if i == "0":
                chooseList = random.randrange(0, 9)
                if chooseList < 1:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars0")))
                else:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars{0}".format(chooseList))))
            elif i == "1":
                chooseList = random.randrange(0, 9)
                if chooseList < 2:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars1")))
                else:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars{0}".format(chooseList))))
            elif i == "2":
                chooseList = random.randrange(0, 9)
                if chooseList < 3:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars2")))
                else:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars{0}".format(chooseList))))
            elif i == "3":
                chooseList = random.randrange(0, 9)
                if chooseList < 4:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars3")))
                else:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars{0}".format(chooseList))))
            elif i == "4":
                chooseList = random.randrange(0, 9)
                if chooseList < 5:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars4")))
                else:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars{0}".format(chooseList))))
            elif i == "5":
                chooseList = random.randrange(0, 9)
                if chooseList < 6:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars5")))
                else:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars{0}".format(chooseList))))
            elif i == "6":
                chooseList = random.randrange(0, 9)
                if chooseList < 7:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars6")))
                else:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars{0}".format(chooseList))))
            elif i == "7":
                chooseList = random.randrange(0, 9)
                if chooseList < 8:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars7")))
                else:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars{0}".format(chooseList))))
            elif i == "8":
                chooseList = random.randrange(0, 9)
                if chooseList < 9:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars8")))
                else:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars{0}".format(chooseList))))
            elif i == "9":
                chooseList = random.randrange(0, 10)
                if chooseList < 5:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars9")))
                else:
                    randomCharsList.append(random.choice(self.charsGroup.get("chars{0}".format(chooseList))))

        random.shuffle(randomCharsList)
        return "".join(randomCharsList)


    def GetStringMixer(self, mixerLengthArgDefined, mixerLevelArgDefined):
        if mixerLevelArgDefined == "simple":
            if mixerLengthArgDefined == "lower":
                return Mixer.StringGeneratorSimple(self, self.lenLower)
            elif mixerLengthArgDefined == "medium":
                return Mixer.StringGeneratorSimple(self, self.lenMedium)
            elif mixerLengthArgDefined == "high":
                return Mixer.StringGeneratorSimple(self, self.lenHigh)
        elif mixerLevelArgDefined == "hard":
            if mixerLengthArgDefined == "lower":
                return Mixer.StringGeneratorHarder(self, self.lenLower)
            elif mixerLengthArgDefined == "medium":
                return Mixer.StringGeneratorHarder(self, self.lenMedium)
            elif mixerLengthArgDefined == "high":
                return Mixer.StringGeneratorHarder(self, self.lenHigh)