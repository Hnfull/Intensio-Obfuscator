 # -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import base64
import time 

from core.lolz.intensio_design_skill import WELCOME, POWER, YOUR_ARE, OBFUSCATOR_MAN, SMILE_MAN
from core.utils.intensio_error import EXIT_SUCCESS

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

def BestFunctionOfTheWorld(stupid):
    if stupid == "YES-YES-YES!!":
        fullScreen = input("\n[!]  Please for a better user experience put the shell in full screen (Y/N) : ")
        fullScreen = fullScreen.upper()

        if fullScreen == "Y":
            print("\nYEEEEEEAH MAN !\n")
            hacker = input("\nDo you want to become OBFUSCATOR MAN ? (Y/N) : ")
            hacker = hacker.upper()

            if hacker == "Y":
                print("\nDownloading skills...\n")
                time.sleep(3)

                for line in WELCOME.split("\n"):
                    print(line)

                skill = input("\nWhat is this SSd2ZSBnb3QgdGhlIHBvb293ZXI= ?  clear string expected : ")

                if skill == base64.b64decode("SSd2ZSBnb3QgdGhlIHBvb293ZXI=").decode():
                    for line in POWER.split("\n"):
                        print(line)

                    time.sleep(3)
                    for line in YOUR_ARE.split("\n"):
                        time.sleep(0.08)
                        print(line) 

                    time.sleep(3)
                    for line in OBFUSCATOR_MAN.split("\n"):
                        print(line)

                    time.sleep(5)
                    return EXIT_SUCCESS
                else:
                    print("\nkrrrrr krrrr krrrr :,)\n")
                    for line in SMILE_MAN.split("\n"):
                        print(line)

            elif hacker == "N":
                print("\nSorry this tools is only used by OBFUSCATOR MAN !\n")
            else:
                print("\n(-_-') Y or N, I SAID !!!\n")

        elif fullScreen == "N":
            print("\nBad man... sorry\n")
        else:
            print("\n(-_-') Y or N, I SAID !!!\n")
    else:
        print("\nReally ?\n")
