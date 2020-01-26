# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import random
import string

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Mixer:
    
    def __init__(self):
        self.lenLower   = 32
        self.lenMedium  = 64
        self.lenHigh    = 128


    def StringGenerator(self, stringLenght):
        return "".join(random.choice(string.ascii_letters) for i in range(stringLenght))
    

    def GetStringMixer(self, lenght):
        if lenght == "lower":
            return Mixer.StringGenerator(self, self.lenLower)
        elif lenght == "medium":
            return Mixer.StringGenerator(self, self.lenMedium)
        elif lenght == "high":
            return Mixer.StringGenerator(self, self.lenHigh)

