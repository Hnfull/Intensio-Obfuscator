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


    def StringGenerator(self, stringLength):
        randomCharsList = []

        for i in range(stringLength):
           randomCharsList.append(random.choice(string.ascii_letters))
        
        return "".join(randomCharsList)
        

    def GetStringMixer(self, mixerLengthArgDefined):
        if mixerLengthArgDefined == "lower":
            return Mixer.StringGenerator(self, self.lengthLower)
        elif mixerLengthArgDefined == "medium":
            return Mixer.StringGenerator(self, self.lengthMedium)
        elif mixerLengthArgDefined == "high":
            return Mixer.StringGenerator(self, self.lengthHigh)