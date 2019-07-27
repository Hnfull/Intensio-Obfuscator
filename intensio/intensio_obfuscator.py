# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

"""

       /$$$$$$             /$$                                   /$$                               
      |_  $$_/            | $$                                  |__/                               
        | $$   /$$$$$$$  /$$$$$$    /$$$$$$  /$$$$$$$   /$$$$$$$ /$$  /$$$$$$                      
        | $$  | $$__  $$|_  $$_/   /$$__  $$| $$__  $$ /$$_____/| $$ /$$__  $$                     
        | $$  | $$  \ $$  | $$    | $$$$$$$$| $$  \ $$|  $$$$$$ | $$| $$  \ $$                     
        | $$  | $$  | $$  | $$ /$$| $$_____/| $$  | $$ \____  $$| $$| $$  | $$                     
       /$$$$$$| $$  | $$  |  $$$$/|  $$$$$$$| $$  | $$ /$$$$$$$/| $$|  $$$$$$/                     
      |______/|__/  |__/   \___/   \_______/|__/  |__/|_______/ |__/ \______/                      
                                                                                                   
                                                                                                   
                                                                                                   
  /$$$$$$  /$$        /$$$$$$                                           /$$                        
 /$$__  $$| $$       /$$__  $$                                         | $$                        
| $$  \ $$| $$$$$$$ | $$  \__//$$   /$$  /$$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$ 
| $$  | $$| $$__  $$| $$$$   | $$  | $$ /$$_____/ /$$_____/ |____  $$|_  $$_/   /$$__  $$ /$$__  $$
| $$  | $$| $$  \ $$| $$_/   | $$  | $$|  $$$$$$ | $$        /$$$$$$$  | $$    | $$  \ $$| $$  \__/
| $$  | $$| $$  | $$| $$     | $$  | $$ \____  $$| $$       /$$__  $$  | $$ /$$| $$  | $$| $$      
|  $$$$$$/| $$$$$$$/| $$     |  $$$$$$/ /$$$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      
 \______/ |_______/ |__/      \______/ |_______/  \_______/ \_______/   \___/   \______/ |__/      
                                                                                                   

-h, --help                  ->  show this help message and exit
-i, --input                 ->  source directory - indicate a directory that contain your file(s)
-c, --code                  ->  language used in source directory, default value: [python] possible value: [python]
-o, --output                ->  output directory that will be obfuscated - indicate a empty directory that will contain your file(s)
-m, --mixerlevel            ->  generate random strings of [lower:32 | medium:64 | high:128] chars when 'replacetostr' and 'paddingscripts' and 'replacetohex'\
                                features are specified, default value: [medium], possible values: [lower, medium, high]
-rts, --replacetostr        ->  activate the 'replace strings to strings mixed' obfuscation feature
-ps, --paddingscripts       ->  activate the 'padding scripts' obfuscation feature
-rc, --removecommentaries   ->  activate the 'remove commentaries' obfuscation feature
-rp, --removeprint          ->  activate the 'remove print' obfuscation feature
-rth, --replacetohex        ->  activate the 'replace strings to hex' obfuscation feature
-v, --verbose               ->  improve verbosity

"""

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import sys
import re
import time
import colorama

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

colorama.init(autoreset=True) # Reset colours

SUCESS_COLOUR   = colorama.Fore.GREEN   + colorama.Style.BRIGHT
FAILED_COLOUR   = colorama.Fore.RED     + colorama.Style.BRIGHT
ERROR_COLOUR    = colorama.Back.RED     + colorama.Style.BRIGHT      
BANNER_COLOUR   = colorama.Fore.WHITE   + colorama.Style.BRIGHT  
SECTION_COLOUR  = colorama.Fore.YELLOW  + colorama.Style.BRIGHT

#---------------------------------------------------------- [Main] ----------------------------------------------------------#

def main():
    if sys.version_info[0] != 3:
        print(ERROR_COLOUR + "[-] Intensio-Obfuscator only support Python 3.x")
        sys.exit(0)

    if sys.platform != "win32" and sys.platform != "linux":
        print(ERROR_COLOUR + "[-] This tool support [windows - Linux] only !")
        sys.exit(0)

    try:
        from core.utils.intensio_design import INTENSIO_BANNER
        from core.utils.intensio_utils  import Utils
        from core.utils.intensio_usage  import Args
        from core.utils.intensio_error  import EXIT_SUCCESS, ERROR_BAD_ENVIRONMENT, ERROR_INVALID_PARAMETER, \
                                                ERROR_BAD_ARGUMENTS, ERROR_INVALID_FUNCTION, ERROR_FILE_NOT_FOUND
        from core.obfuscation.intensio_replace  import Replace
        from core.obfuscation.intensio_padding  import Padding
        from core.obfuscation.intensio_analyze  import Analyze
        from core.obfuscation.intensio_remove   import Remove
    except ImportError as e:
        print(ERROR_COLOUR + "[-] {0}\n".format(e))
        sys.exit(0)

    args    = Args()
    utils   = Utils()

    if len(sys.argv) > 1 and len(sys.argv) <= 15:
        pass
    else:
        print(ERROR_COLOUR + "[-] Incorrect number of arguments\n")
        args.GetArgHelp()
        sys.exit(ERROR_BAD_ARGUMENTS)
    
    if args.GetArgsValue().input:
        if args.GetArgsValue().output:
            if args.GetArgsValue().code:
                if args.GetArgsValue().code == "python":
                    if args.GetArgsValue().mixerlevel:
                        if re.match(r"^lower$|^medium$|^high$", args.GetArgsValue().mixerlevel):
                            if not args.GetArgsValue().paddingscripts and not args.GetArgsValue().replacetostr \
                                and not args.GetArgsValue().removecommentaries and not args.GetArgsValue().removeprint \
                                and not args.GetArgsValue().replacetohex:
                                print(ERROR_COLOUR + "\n[-] Need at least one argument [-rts --replacetostr] or [-ps --paddingscripts] or [-rc --removecommentaries] or [-rp --removeprint] or [-rth --replacetohex]")
                                sys.exit(ERROR_BAD_ARGUMENTS)
                        else:
                            print(ERROR_COLOUR + "[-] Incorrect level of mixerlevel, [lower - medium - high] only supported\n")
                            sys.exit(ERROR_INVALID_PARAMETER)
                    else:
                        print(ERROR_COLOUR + "[-] Mixerlevel [-m --mixerlevel] argument missing\n")
                        sys.exit(ERROR_BAD_ARGUMENTS)
                else:
                    print(ERROR_COLOUR + "[-] '{0}' Incorrect code argument, [python] only supported\n".format(args.GetArgsValue().Code))
                    sys.exit(ERROR_INVALID_PARAMETER)
            else:
                print(ERROR_COLOUR + "[-] Code [-c --code] argument missing\n")
                sys.exit(ERROR_BAD_ARGUMENTS)
        else:
            print(ERROR_COLOUR + "[-] Output [-o --output] argument missing\n")
            sys.exit(ERROR_BAD_ARGUMENTS)
    else:
        print(ERROR_COLOUR + "[-] Input [-i --input] argument missing\n")
        sys.exit(ERROR_BAD_ARGUMENTS)

    for line in INTENSIO_BANNER.split("\n"):
        time.sleep(0.05)
        print(BANNER_COLOUR + line)

    # -- Analysis and set up of the work environment -- #
    print(SECTION_COLOUR + "\n\n*********************** [ Analyze and setup environment ] ************************\n")
    analyzeData = Analyze()

    if (analyzeData.InputAvailable(args.GetArgsValue().input, args.GetArgsValue().code, args.GetArgsValue().verbose) == EXIT_SUCCESS):
        print("\n[+] Analyze input argument '{0}' -> ".format(args.GetArgsValue().input) + SUCESS_COLOUR + "Successful")
    else:
        print("[-] Analyze input '{0}' -> ".format(args.GetArgsValue().input) + FAILED_COLOUR + "failed\n")
        sys.exit(ERROR_INVALID_FUNCTION)

    if (analyzeData.OutputAvailable(args.GetArgsValue().input, args.GetArgsValue().code, args.GetArgsValue().output, args.GetArgsValue().verbose) == EXIT_SUCCESS):
        print("\n[+] Analyze and setup output argument environment '{0}' -> ".format(args.GetArgsValue().output) + SUCESS_COLOUR + "Successful")
    else:
        print("[-] Analyze output '{0}' -> ".format(args.GetArgsValue().output) + FAILED_COLOUR + "failed\n")
        sys.exit(ERROR_INVALID_FUNCTION)
    
    # -- Obfuscation process -- #
    print(SECTION_COLOUR + "\n\n********************** [ Obfuscation remove commentaries ] **********************\n")
    if args.GetArgsValue().removecommentaries:
        removeData = Remove()
        
        if (removeData.Commentaries(args.GetArgsValue().code, args.GetArgsValue().output) == EXIT_SUCCESS):
            print("[+] Obfuscation remove commentaries -> " + SUCESS_COLOUR + "Successful")
        else:
            print("\n[-] Obfuscation remove commentaries -> " + FAILED_COLOUR  + "Failed")
    else:
        print("[!] Obfuscation remove commentaries no asked !")

    print(SECTION_COLOUR + "\n\n*************** [ Obfuscation replace strings to strings mixed ] ****************\n")
    if args.GetArgsValue().replacetostr:
        replaceData = Replace()

        if (replaceData.StringsToStrings(args.GetArgsValue().code, args.GetArgsValue().output, args.GetArgsValue().mixerlevel, args.GetArgsValue().verbose) == EXIT_SUCCESS):
            print("[+] Obfuscation replace strings to strings mixed -> " + SUCESS_COLOUR + "Successful")
        else:
            print("\n[-] Obfuscation replace strings to strings mixed-> " + FAILED_COLOUR +  "Failed")
    else:
        print("[!] Obfuscation replace strings to strings mixed no asked !")
    
    print(SECTION_COLOUR + "\n\n************************ [ Obfuscation padding scripts ] ************************\n")
    if args.GetArgsValue().paddingscripts:
        paddingData = Padding()

        if (paddingData.AddRandomScripts(args.GetArgsValue().code, args.GetArgsValue().output, args.GetArgsValue().mixerlevel) == EXIT_SUCCESS):
            print("[+] Obfuscation padding random scripts -> " + SUCESS_COLOUR + "Successful")
        else:
            print("\n[-] Obfuscation padding random scripts -> " + FAILED_COLOUR + "Failed")
    else:
        print("[!] Obfuscation add random scripts no asked !")


    print(SECTION_COLOUR + "\n\n************************* [ Obfuscation remove print ] **************************\n")
    if args.GetArgsValue().removeprint:

        if (removeData.PrintFunctions(args.GetArgsValue().code, args.GetArgsValue().output) == EXIT_SUCCESS):
            print("[+] Obfuscation remove print functions -> " + SUCESS_COLOUR + "Successful")
        else:
            print("\n[-] Obfuscation remove print functions -> " + FAILED_COLOUR + "Failed")
    else:
        print("[!] Obfuscation remove print functions no asked !")

    print(SECTION_COLOUR + "\n\n******************** [ Obfuscation replace strings to hex ] *********************\n")
    if args.GetArgsValue().replacetohex:
        if args.GetArgsValue().replacetostr:
            pass
        else:
            replaceData = Replace()

        if (replaceData.StringsToHex(args.GetArgsValue().code, args.GetArgsValue().output, args.GetArgsValue().mixerlevel) == EXIT_SUCCESS):
            print("\n[+] Obfuscation Replace strings to hex -> " + SUCESS_COLOUR + "Successful\n")
        else:
            print("\n[-] Obfuscation replace strings to hex -> " + FAILED_COLOUR + "Failed\n")
    else:
        print("[!] Obfuscation replace strings to hex no asked !\n")
        
#----------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(ERROR_COLOUR + "\n[!] Exit program\n")
