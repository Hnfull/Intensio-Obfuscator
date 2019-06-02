# -*- coding: utf-8 -*-

# ==================================================== Test python file ==================================================== #

BANNER = """

$$$$$$$$\                    $$\     
\__$$  __|                   $$ |    
   $$ | $$$$$$\   $$$$$$$\ $$$$$$\   
   $$ |$$  __$$\ $$  _____|\_$$  _|  
   $$ |$$$$$$$$ |\$$$$$$\    $$ |    
   $$ |$$   ____| \____$$\   $$ |$$\ 
   $$ |\$$$$$$$\ $$$$$$$  |  \$$$$  |
   \__| \_______|\_______/    \____/ 

"""
#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import sys
import random
from os import path

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

# I am a commentary
### Commentaries ###
# -- others commentary -- #
#-- A girl as no name --#

#####################
#                   #
#                   #
#        H          #
#                   #
#                   #
#####################

varTest1="varTest1"
varTest2= 0
varTest3 =None
varTest4 = ""
varTest5 = False
varTest6 =[]
varTest7 = {}
varTest8        ="ugly"


#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

class Error (Exception):
    pass

class ClassTest1:

    def __init__(self):
        self.test="test"
        self.toto   = "toto"

    def GetDisplayVar(self):
        print(varTest1)

    def GetConstruct(self):
        print(self.test)

    def MyPrint(self, string):
        print(string)

def GetFunctionAddress(functionDecorator):

    def FunctionTest(*args, **kwargs):
        print("the address of function is {0}".format(functionDecorator))

    return FunctionTest

@GetFunctionAddress
def TestDecorator(r):
    print("{0} Big boobs ?".format(r))

def GetDisplayTwoString(i , r ):
    print("{0} {1}".format(i, r))

#---------------------------------------------------------- [Main] ----------------------------------------------------------#

def main():
    classTest1  = ClassTest1()
    error       = Error()

    for i in BANNER.split("\n"):
        print(i)
        
    print("All types of python syntax\n") # who is Jaqen H'ghar ?

    varTest2 = varTest1
    if varTest1 == varTest2:
        classTest1.GetDisplayVar()
    else:
        sys.exit(0)

    resultRand = random.randint(1, 10)

    if resultRand >= 5:
        varTest3 = False
        varTest5 = True
        varTest2 = varTest3
    else:
        pass

    varTest6 = ["one", "two, three", "four"] 
    varTest7["test"]     = "yes"
    varTest7["goodTest?"] = "no"
    
    try:
        for icorn, verb in  enumerate(varTest6):
            if icorn == 0:
                continue
        classTest1.MyPrint("do you understand this test?")
    except Exception as r:
        print(r)
        GetDisplayTwoString("exception...", "exception again... (-_-)")
        pass

    while True:
        randRandRandAgain = random.randint(1, 10)
        if randRandRandAgain == 5:
            break

    TestDecorator("toto")

    classTest1.GetDisplayVar()
    
    classTest1.MyPrint("I am not inspired...")
    
    GetDisplayTwoString("nooooooooooo", "oooooookayyyyyyyyyy")
    
    GetFunctionAddress

    print(varTest1 + " " + varTest1)
    print("{0} {0}".format(varTest1))

    TestDecorator("You like")
    classTest1.MyPrint("Finish")
    
#----------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------------#

if __name__ == "__main__":
    main()