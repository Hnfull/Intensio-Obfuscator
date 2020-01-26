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
-i, --input                 ->  source directory - indicate a directory that contain your file
-o, --output                ->  output directory that will be obfuscated - indicate a empty directory that will contain your file
-m, --mixerlevel            ->  generate random strings of [lower:32 | medium:64 | high:128] chars when 'replacetostr' - 'paddingscript' - 'replacefilename'\
                                - 'replacetohex' parameters are specified, default value: [medium], possible values: [lower, medium, high]
-rts, --replacetostr        ->  activate 'replace string to string mixed' obfuscation feature
-ps, --paddingscript        ->  activate 'padding script' obfuscation feature
-rfn, --replacefilename     ->  activate 'replace file name' obfuscation feature
-rth, --replacetohex        ->  activate 'replace string to hex' obfuscation feature
-v, --verbose               ->  improve verbosity

"""

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import sys
import re
import time
import colorama

from core.utils.intensio_design import INTENSIO_BANNER
from core.utils.intensio_utils  import Utils, Colors
from core.utils.intensio_usage  import Args
from core.utils.intensio_error  import EXIT_SUCCESS, ERROR_INVALID_PARAMETER, ERROR_BAD_ARGUMENTS, ERROR_INVALID_FUNCTION
from core.obfuscation.intensio_replace  import Replace
from core.obfuscation.intensio_padding  import Padding
from core.obfuscation.intensio_analyze  import Analyze
from core.obfuscation.intensio_delete   import Delete

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

colorama.init(autoreset=True) # Reset colors

SUCESS_COLOR   = Colors.SUCCESS
FAILED_COLOR   = Colors.ERROR
BANNER_COLOR   = colorama.Fore.WHITE   + colorama.Style.BRIGHT  
SECTION_COLOR  = colorama.Fore.YELLOW  + colorama.Style.BRIGHT
ERROR_COLOR    = Colors.ERROR

def main():
    if sys.version_info[0] != 3:
        print(ERROR_COLOR + "[-] Intensio-Obfuscator only support Python 3.x")
        sys.exit(1)

    if sys.platform != "win32" and sys.platform != "linux":
        print(ERROR_COLOR + "[-] This tool support [windows - Linux] only !")
        sys.exit(1)

    args    = Args()
    utils   = Utils()

    if len(sys.argv) > 1 and len(sys.argv) <= 13:
        pass
    else:
        print(ERROR_COLOR + "[-] Incorrect number of arguments\n")
        args.GetArgHelp()
        sys.exit(ERROR_BAD_ARGUMENTS)
    
    if args.GetArgsValue().input:
        if args.GetArgsValue().output:
            if args.GetArgsValue().mixerlevel:
                if re.match(r"^lower$|^medium$|^high$", args.GetArgsValue().mixerlevel):
                    if not args.GetArgsValue().paddingscript and not args.GetArgsValue().replacetostr \
                        and not args.GetArgsValue().replacefilename and not args.GetArgsValue().replacetohex:
                        print(ERROR_COLOR + "\n[-] Need at least one argument [-rts] - [-ps] - [-rfn] - [-rth]")
                        sys.exit(ERROR_BAD_ARGUMENTS)
                else:
                    print(ERROR_COLOR + "[-] Incorrect level of mixerlevel, [lower - medium - high] only supported\n")
                    sys.exit(ERROR_INVALID_PARAMETER)
            else:
                print(ERROR_COLOR + "[-] Mixerlevel [-m, --mixerlevel] argument missing\n")
                sys.exit(ERROR_BAD_ARGUMENTS)
        else:
            print(ERROR_COLOR + "[-] Output [-o, --output] argument missing\n")
            sys.exit(ERROR_BAD_ARGUMENTS)
    else:
        print(ERROR_COLOR + "[-] Input [-i, --input] argument missing\n")
        sys.exit(ERROR_BAD_ARGUMENTS)

    for line in INTENSIO_BANNER.split("\n"):
        time.sleep(0.05)
        print(BANNER_COLOR + line)

    # -- Analysis and set up of the work environment -- #
    print(SECTION_COLOR + "\n\n*********************** [ Analyze and setup environment ] ************************\n")
    analyzeData         = Analyze()
    analyseDataInEnv    = analyzeData.InputAvailable(
                                                    inputArg=args.GetArgsValue().input,  
                                                    verboseArg=args.GetArgsValue().verbose
    )
    if analyseDataInEnv == EXIT_SUCCESS:
        print("\n[+] Analyze input argument '{0}' -> ".format(args.GetArgsValue().input) + SUCESS_COLOR + "Successful")
    else:
        print("[-] Analyze input '{0}' -> ".format(args.GetArgsValue().input) + FAILED_COLOR + "failed\n")
        sys.exit(ERROR_INVALID_FUNCTION)

    analyseDataOutEnv = analyzeData.OutputAvailable(
                                                    inputArg=args.GetArgsValue().input, 
                                                    outputArg=args.GetArgsValue().output, 
                                                    verboseArg=args.GetArgsValue().verbose
    )
    if analyseDataOutEnv == EXIT_SUCCESS:
        print("\n[+] Analyze and setup output argument environment '{0}' -> " \
                .format(args.GetArgsValue().output) + SUCESS_COLOR + "Successful")
    else:
        print("[-] Analyze output '{0}' -> ".format(args.GetArgsValue().output) + FAILED_COLOR + "failed\n")
        sys.exit(ERROR_INVALID_FUNCTION)
    
    # -- Obfuscation process -- #    
    print(SECTION_COLOR + "\n\n************************ [ Obfuscation delete comments ] *************************\n")
    deleteData = Delete()    
    deleteCommentsData = deleteData.Comments(
                                            outputArg=args.GetArgsValue().output,
                                            verboseArg=args.GetArgsValue().verbose
    )
    if deleteCommentsData == EXIT_SUCCESS:
        print("[+] Obfuscation delete comments -> " + SUCESS_COLOR + "Successful")
    else:
        print("\n[-] Obfuscation delete comments -> " + FAILED_COLOR  + "Failed")
        if not args.GetArgsValue().verbose:
            print("\n[!] Retry with [-v, --verbose] parameter")

    print(SECTION_COLOR + "\n\n*********************** [ Obfuscation delete line space(s) ] ***********************\n")
    if deleteData:
        pass
    else:    
        deleteData = Delete()    
    
    deleteLinesSpacesData = deleteData.LinesSpaces(
                                                    outputArg=args.GetArgsValue().output, 
                                                    verboseArg=args.GetArgsValue().verbose
    )

    if deleteLinesSpacesData == EXIT_SUCCESS:
        print("[+] Obfuscation delete lines spaces -> " + SUCESS_COLOR + "Successful")
    else:
        print("\n[-] Obfuscation delete lines spaces -> " + FAILED_COLOR  + "Failed")
        if not args.GetArgsValue().verbose:
            print("\n[!] Retry with [-v, --verbose] parameter")

      # -- If empty class (avert to generate an error) -- #
    print(SECTION_COLOR + "\n\n*********************** [ Correction padding empty class(es) ] **********************\n")
    paddingData             = Padding()
    paddingDataEmptyClass   = paddingData.EmptyClasses(
                                                        outputArg=args.GetArgsValue().output, 
                                                        mixerLevelArg=args.GetArgsValue().mixerlevel,
                                                        verboseArg=args.GetArgsValue().verbose
    ) 
    if paddingDataEmptyClass == EXIT_SUCCESS:
        pass
    else:
        print("\n[-] Padding empty class -> " + FAILED_COLOR + "Failed")
        if not args.GetArgsValue().verbose:
            print("\n[!] Retry with [-v, --verbose] parameter")

    # -- If empty functions (avert to generate an error) -- #
    print(SECTION_COLOR + "\n\n********************** [ Correction padding empty function(s) ] ********************\n")
    if paddingData:
        pass
    else:
        paddingData = Padding()
    
    paddingDataEmptyFunc = paddingData.EmptyFunctions(
                                                    outputArg=args.GetArgsValue().output, 
                                                    mixerLevelArg=args.GetArgsValue().mixerlevel,
                                                    verboseArg=args.GetArgsValue().verbose
    ) 
    if paddingDataEmptyFunc == EXIT_SUCCESS:
        pass
    else:    
        print("\n[-] Padding empty function -> " + FAILED_COLOR + "Failed")
        if not args.GetArgsValue().verbose:
            print("\n[!] Retry with [-v, --verbose] parameter")

    print(SECTION_COLOR + "\n\n**************** [ Obfuscation replace string(s) to string(s) mixed ] *****************\n")
    if args.GetArgsValue().replacetostr:
        replaceData = Replace()

        replaceDataStrStr = replaceData.StringToString(
                                                        outputArg=args.GetArgsValue().output, 
                                                        mixerLevelArg=args.GetArgsValue().mixerlevel, 
                                                        verboseArg=args.GetArgsValue().verbose
        ) 

        if replaceDataStrStr == EXIT_SUCCESS:
            print("[+] Obfuscation replace string to string mixed -> " + SUCESS_COLOR + "Successful")
        else:
            print("\n[-] Obfuscation replace string to string mixed -> " + FAILED_COLOR +  "Failed")
            if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")
    else:
        print("[!] Obfuscation [ replace string to string ] mixed no asked !")
    
    print(SECTION_COLOR + "\n\n********************* [ Obfuscation adding padding script(s) ] *********************\n")
    if args.GetArgsValue().paddingscript:
        if paddingData:
            pass
        else:
            paddingData = Padding()

        paddingDataGarbage = paddingData.AddRandomScripts(
                                                        outputArg=args.GetArgsValue().output,
                                                        mixerLevelArg=args.GetArgsValue().mixerlevel,
                                                        verboseArg=args.GetArgsValue().verbose
        )
        if paddingDataGarbage == EXIT_SUCCESS:
            print("[+] Obfuscation padding script -> " + SUCESS_COLOR + "Successful")
        else:
            print("\n[-] Obfuscation padding script -> " + FAILED_COLOR + "Failed")
            if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")
    else:
        print("[!] Obfuscation [ padding script ] no asked !")

    print(SECTION_COLOR + "\n\n********************** [ Obfuscation replace file(s) name ] ************************\n")
    if args.GetArgsValue().replacefilename:
        if args.GetArgsValue().replacetostr:
            pass
        else:
            replaceData = Replace()

        replaceDataStrFname = replaceData.FilesName(
                                                    outputArg=args.GetArgsValue().output, 
                                                    mixerLevelArg=args.GetArgsValue().mixerlevel, 
                                                    verboseArg=args.GetArgsValue().verbose
        )
        if replaceDataStrFname == EXIT_SUCCESS:
            print("\n[+] Obfuscation replace file name -> " + SUCESS_COLOR + "Successful")
        else:
            print("\n[-] Obfuscation replace file name -> " + FAILED_COLOR + "Failed")
            if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")
    else:
        print("[!] Obfuscation [ replace file name ] feature no asked !")
    
    print(SECTION_COLOR + "\n\n******************** [ Obfuscation replace string(s) to hex ] **********************\n")
    if args.GetArgsValue().replacetohex:
        if args.GetArgsValue().replacetostr or args.GetArgsValue().replacefilename:
            pass
        else:
            replaceData = Replace()

        replaceDataStrHex = replaceData.StringsToHex(
                                                    outputArg=args.GetArgsValue().output, 
                                                    mixerLevelArg=args.GetArgsValue().mixerlevel,
                                                    verboseArg=args.GetArgsValue().verbose
        ) 
        if replaceDataStrHex == EXIT_SUCCESS:
            print("\n[+] Obfuscation replace string to hex -> " + SUCESS_COLOR + "Successful")
        else:
            print("\n[-] Obfuscation replace string to hex -> " + FAILED_COLOR + "Failed")
            if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")
    else:
        print("[!] Obfuscation [ replace string to hex ] feature no asked !")

    # -- Delete if python pyc file in output directory -- #
    print(SECTION_COLOR + "\n\n*********************** [ Correction delete .pyc file(s) ] *************************\n")
    if deleteData:
        pass
    else:
        deleteData = Delete()

    deletePycData = deleteData.TrashFiles(
                                        outputArg=args.GetArgsValue().output, 
                                        verboseArg=args.GetArgsValue().verbose,
    )
    if deletePycData == EXIT_SUCCESS:
        pass
    else:
        print("\n[-] Delete .pyc file in {0} directory -> ".format(args.GetArgsValue().output) + FAILED_COLOR + "Failed")
        if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")

#----------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    try:
        main()
        print("\n")
    except KeyboardInterrupt:
        print(ERROR_COLOR + "\n[!] Exit program\n")
