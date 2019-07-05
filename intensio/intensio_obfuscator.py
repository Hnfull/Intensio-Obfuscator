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
                                                                                                   

-h, --help              ->  show this help message and exit
-i, --input             ->  source directory - indicate a directory that contain your file(s)
-c, --code              ->  language used in source directory, default value: [python] possible value: [python]
-o, --output            ->  output directory that will be obfuscated - indicate a empty directory that will contain your file(s)
-m, --mixerlevel        ->  length level of variables/classes/functions/files mix output, default  value: medium, 
                            possible values: [lower, medium, high]
-r, --replace           ->  activate the 'replace' obfuscation feature
-p, --padding           ->  activate the 'padding' obfuscation feature
-rc, --rcommentaries    ->  activate the 'rcommentaries' obfuscation feature
-rp, --rprint           ->  activate the 'rprint' obfuscation feature
-v, --verbose           ->  improve verbosity

"""

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import sys
import re
import time
import colorama

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

colorama.init(autoreset=True) # Reset colours

SUCESS_COLOUR   = colorama.Fore.GREEN + colorama.Style.BRIGHT
ERROR_COLOUR    = colorama.Fore.RED + colorama.Style.BRIGHT      
BANNER_COLOUR   = colorama.Fore.WHITE + colorama.Style.BRIGHT  
SECTION_COLOUR  = colorama.Fore.YELLOW + colorama.Style.BRIGHT

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
        from core.utils.intensio_utils import Utils
        from core.utils.intensio_usage import Args
        from core.utils.intensio_error import EXIT_SUCCESS, ERROR_BAD_ENVIRONMENT, ERROR_INVALID_PARAMETER, ERROR_BAD_ARGUMENTS,\
                                                ERROR_INVALID_FUNCTION, ERROR_FILE_NOT_FOUND
        from core.obfuscation.intensio_replace import ReplaceWords
        from core.obfuscation.intensio_padding import Padding
        from core.obfuscation.intensio_analyze import Analyze
        from core.obfuscation.intensio_remove import Remove
    except ImportError as e:
        print(ERROR_COLOUR + "[-] {0}\n".format(e))
        sys.exit(0)

    args    = Args()
    utils   = Utils()

    if len(sys.argv) > 1 and len(sys.argv) <= 14:
        pass
    else:
        print(ERROR_COLOUR + "[-] Incorrect number of arguments\n")
        args.GetArgHelp()
        sys.exit(ERROR_BAD_ARGUMENTS)
    
    if args.GetArgsValue().input:
        if args.GetArgsValue().output:
            if args.GetArgsValue().code:
                if re.match(r"^python$", args.GetArgsValue().code):
                    if args.GetArgsValue().mixerlevel:
                        if re.match(r"^lower$|^medium$|^high$", args.GetArgsValue().mixerlevel):
                            if not args.GetArgsValue().padding and not args.GetArgsValue().replace \
                                and not args.GetArgsValue().rcommentaries and not args.GetArgsValue().rprint:
                                print(ERROR_COLOUR + "\n[-] Need at least one argument [-r --replace] or [-p --padding] or [-rc --rcommentaries] or [-rp --rprint]")
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
    analyze = Analyze()

    if (analyze.InputAvailable(args.GetArgsValue().input, args.GetArgsValue().code, args.GetArgsValue().verbose) == EXIT_SUCCESS):
        print("\n[+] Analyze input argument '{0}' -> ".format(args.GetArgsValue().input) + SUCESS_COLOUR + "Successful")
    else:
        print("[-] Analyze input '{0}' -> ".format(args.GetArgsValue().input) + ERROR_COLOUR + "failed\n")
        sys.exit(ERROR_INVALID_FUNCTION)

    if (analyze.OutputAvailable(args.GetArgsValue().input, args.GetArgsValue().code, args.GetArgsValue().output, args.GetArgsValue().verbose) == EXIT_SUCCESS):
        print("\n[+] Analyze and setup output argument environment '{0}' -> ".format(args.GetArgsValue().output) + SUCESS_COLOUR + "Successful")
    else:
        print("[-] Analyze output '{0}' -> ".format(args.GetArgsValue().output) + ERROR_COLOUR + "failed\n")
        sys.exit(ERROR_INVALID_FUNCTION)
    
    # -- Obfuscation process -- #
    print(SECTION_COLOUR + "\n\n************************** [ Obfuscation Rcommentaries ] **************************\n")
    if args.GetArgsValue().rcommentaries:
        removeData = Remove()
        
        if (removeData.Commentaries(args.GetArgsValue().code, args.GetArgsValue().output) == EXIT_SUCCESS):
            print("[+] Obfuscation Rcommentaries -> " + SUCESS_COLOUR + "Successful")
        else:
            print("\n[-] Obfuscation Rcommentaries -> " + ERROR_COLOUR  + "Failed")
    else:
        print("[!] Obfuscation Rcommentaries no asked !")

    print(SECTION_COLOUR + "\n\n***************************** [ Obfuscation Replace ] *****************************\n")
    if args.GetArgsValue().replace:
        replaceWords = ReplaceWords()

        if (replaceWords.VarsDefinedByUser(args.GetArgsValue().code, args.GetArgsValue().output, args.GetArgsValue().mixerlevel, args.GetArgsValue().verbose) == EXIT_SUCCESS):
            print("[+] Obfuscation Replace -> " + SUCESS_COLOUR + "Successful")
        else:
            print("\n[-] Obfuscation Replace -> " + ERROR_COLOUR +  "Failed")
    else:
        print("[!] Obfuscation Replace no asked !")
    
    print(SECTION_COLOUR + "\n\n***************************** [ Obfuscation Padding ] *****************************\n")
    if args.GetArgsValue().padding:
        paddingScripts = Padding()

        if (paddingScripts.AddScripts(args.GetArgsValue().code, args.GetArgsValue().output, args.GetArgsValue().mixerlevel) == EXIT_SUCCESS):
            print("[+] Obfuscation Padding -> " + SUCESS_COLOUR + "Successful")
        else:
            print("\n[-] Obfuscation Padding -> " + ERROR_COLOUR + "Failed")
    else:
        print("[!] Obfuscation Padding no asked !")

    print(SECTION_COLOUR + "\n\n****************************** [ Obfuscation Rprint ] *****************************\n")
    if args.GetArgsValue().rprint:

        if (removeData.PrintFunc(args.GetArgsValue().code, args.GetArgsValue().output) == EXIT_SUCCESS):
            print("[+] Obfuscation Rprint -> " + SUCESS_COLOUR + "Successful\n")
        else:
            print("\n[-] Obfuscation Rprint -> " + ERROR_COLOUR + "Failed\n")
    else:
        print("[!] Obfuscation Rprint no asked !\n")
        
#----------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(ERROR_COLOUR + "\n[!] Exit program\n")
