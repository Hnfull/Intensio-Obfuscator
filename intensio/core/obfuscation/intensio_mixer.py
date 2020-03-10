# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import random
import string

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Mixer:
    
    def __init__(self):
        self.lengthLower    = 32
        self.lengthMedium   = 64
        self.lengthHigh     = 128
        self.charsGroup     = {
                                "chars0" : "abcd",
                                "chars1" : "efgh",
                                "chars2" : "ijkl",
                                "chars3" : "mnop",
                                "chars4" : "qrst",
                                "chars5" : "uvwx",
                                "chars6" : "yzAB",
                                "chars7" : "CDEF",
                                "chars8" : "GHIJ",
                                "chars9" : "KLMN",
                                "chars10": "OPQR",
                                "chars11": "STUV",
                                "chars12": "WXYZ"
        }


    def StringGenerator(self, stringLength):
        randomCharsList = []
        uRandom         = random.SystemRandom() # use random string from os.urandom

        # -- choose integer between 0 to string length chosen by user -- #
        if stringLength == self.lengthLower:
            randNumber = uRandom.randrange(10000000000000000000000000000000)
        elif stringLength == self.lengthMedium:
            randNumber = uRandom.randrange(1000000000000000000000000000000000000000000000000000000000000000)
        elif stringLength == self.lengthHigh:
            randNumber = uRandom.randrange(10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)

        randNumber = str(randNumber) # convert number generated into str

        # -- for each number in number generated -- #
        for i in randNumber:
            # -- if number is equal to number between quotes defined manually -- #
            if i == "0":
                # -- generate a number depending of number of keys in dictionnary defined above -- #
                chooseList = uRandom.randrange(0, 12)
                # -- if number obtained is smaller of number defined manually, the key used from \ -- #
                # -- dictionnary is selected randomly, also is defined manually and choice a letter \ -- #
                # -- in value of the key and is added in a list -- # 
                if chooseList < 1:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars0")))
                else:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars{}".format(chooseList))))
            elif i == "1":
                chooseList = uRandom.randrange(0, 12)
                if chooseList < 2:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars1")))
                else:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars{}".format(chooseList))))
            elif i == "2":
                chooseList = uRandom.randrange(0, 12)
                if chooseList < 3:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars2")))
                else:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars{}".format(chooseList))))
            elif i == "3":
                chooseList = uRandom.randrange(0, 12)
                if chooseList < 4:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars3")))
                else:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars{}".format(chooseList))))
            elif i == "4":
                chooseList = uRandom.randrange(0, 12)
                if chooseList < 5:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars4")))
                else:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars{}".format(chooseList))))
            elif i == "5":
                chooseList = uRandom.randrange(0, 12)
                if chooseList < 6:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars5")))
                else:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars{}".format(chooseList))))
            elif i == "6":
                chooseList = uRandom.randrange(0, 12)
                if chooseList < 7:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars6")))
                else:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars{}".format(chooseList))))
            elif i == "7":
                chooseList = uRandom.randrange(0, 12)
                if chooseList < 8:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars7")))
                else:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars{}".format(chooseList))))
            elif i == "8":
                chooseList = uRandom.randrange(0, 12)
                if chooseList < 9:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars8")))
                else:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars{}".format(chooseList))))
            elif i == "9":
                chooseList = uRandom.randrange(0, 12)
                if chooseList < 10:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars9")))
                else:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars{}".format(chooseList))))
            elif i == "10":
                chooseList = uRandom.randrange(0, 12)
                if chooseList < 11:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars10")))
                else:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars{}".format(chooseList))))
            elif i == "11":
                chooseList = uRandom.randrange(0, 12)
                if chooseList < 12:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars11")))
                else:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars{}".format(chooseList))))
            elif i == "12":
                chooseList = uRandom.randrange(0, 12)
                if chooseList < 13:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars12")))
                else:
                    randomCharsList.append(uRandom.choice(self.charsGroup.get("chars{}".format(chooseList))))

        # -- at the end the list is again randomized and convert into an strings with length defined by user -- #
        uRandom.shuffle(randomCharsList)
        return "".join(randomCharsList)


    def GetStringMixer(self, mixerLengthArgDefined):
        if mixerLengthArgDefined == "lower":
            return Mixer.StringGenerator(self, self.lengthLower)
        elif mixerLengthArgDefined == "medium":
            return Mixer.StringGenerator(self, self.lengthMedium)
        elif mixerLengthArgDefined == "high":
            return Mixer.StringGenerator(self, self.lengthHigh)