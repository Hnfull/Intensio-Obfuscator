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
-mlen, --mixerlength        ->  define length of random strings generated [lower:32 | medium:64 | high:128] (number of chars) when 'replacetostr' - 'paddingscript' - 'replacefilename'\
                                - 'replacetohex' features are specified, default value: [medium], possible values: [lower, medium, high]"
-mlvl, --mixerlevel         ->  define the obfuscation level of random strings generated when 'replacetostr' - 'paddingscript' - 'replacefilename'\
                                - 'replacetohex' features are specified, default value: [simple], possible values: [simple, hard]"
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

from core.utils.intensio_design import INTENSIO_BANNER
from core.utils.intensio_utils  import Utils, Colors
from core.utils.intensio_usage  import Args
from core.utils.intensio_error  import EXIT_SUCCESS, ERROR_INVALID_PARAMETER, ERROR_BAD_ARGUMENTS, ERROR_INVALID_FUNCTION
from core.obfuscation.intensio_replace  import Replace
from core.obfuscation.intensio_padding  import Padding
from core.obfuscation.intensio_analyze  import Analyze
from core.obfuscation.intensio_delete   import Delete

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

def main():
    if sys.version_info[0] != 3:
        print(Colors.ERROR + "[-] Intensio-Obfuscator only support Python 3.x" + Colors.DISABLE)
        sys.exit(1)

    if sys.platform != "win32" and sys.platform != "linux":
        print(Colors.ERROR + "[-] This tool support [windows - Linux] only !" + Colors.DISABLE)
        sys.exit(1)

    args    = Args()
    utils   = Utils()

    if len(sys.argv) > 1 and len(sys.argv) <= 15:
        pass
    else:
        print(Colors.ERROR + "[-] Incorrect number of arguments\n" + Colors.DISABLE)
        args.GetArgHelp()
        sys.exit(ERROR_BAD_ARGUMENTS)
    
    if args.GetArgsValue().input:
        if args.GetArgsValue().output:
            if re.match(r"^lower$|^medium$|^high$", args.GetArgsValue().mixerlength):
                if args.GetArgsValue().mixerlevel:
                    if not args.GetArgsValue().paddingscript and not args.GetArgsValue().replacetostr \
                        and not args.GetArgsValue().replacefilename and not args.GetArgsValue().replacetohex:
                        print(Colors.ERROR + "\n[-] Need at least one argument [-rts] - [-ps] - [-rfn] - [-rth]" + Colors.DISABLE)
                        sys.exit(ERROR_BAD_ARGUMENTS)
                else:
                    print(Colors.ERROR + "[-] Incorrect level defined of mixerlevel argument, [simple - hard] only supported\n" + Colors.DISABLE)
                    sys.exit(ERROR_INVALID_PARAMETER)
            else:
                print(Colors.ERROR + "[-] Incorrect length defined of mixerlength argument, [lower - medium - high] only supported\n" + Colors.DISABLE)
                sys.exit(ERROR_INVALID_PARAMETER)
        else:
            print(Colors.ERROR + "[-] Output [-o, --output] argument missing\n" + Colors.DISABLE)
            sys.exit(ERROR_BAD_ARGUMENTS)
    else:
        print(Colors.ERROR + "[-] Input [-i, --input] argument missing\n" + Colors.DISABLE)
        sys.exit(ERROR_BAD_ARGUMENTS)

    for line in INTENSIO_BANNER.split("\n"):
        time.sleep(0.05)
        print(line)

    # -- Analysis and set up of the work environment -- #
    print(Colors.SECTION + "\n\n*********************** [ Analyze and setup environment ] ************************\n" + Colors.DISABLE)
    analyzeData         = Analyze()
    analyseDataInEnv    = analyzeData.InputAvailable(
                                                    inputArg=args.GetArgsValue().input,  
                                                    verboseArg=args.GetArgsValue().verbose
    )
    if analyseDataInEnv == EXIT_SUCCESS:
        print("\n[+] Analyze input argument '{0}' -> ".format(args.GetArgsValue().input) + Colors.SUCCESS + "Successful" + Colors.DISABLE)
    else:
        print("[-] Analyze input '{0}' -> ".format(args.GetArgsValue().input) + Colors.ERROR + "failed\n" + Colors.DISABLE)
        sys.exit(ERROR_INVALID_FUNCTION)

    analyseDataOutEnv = analyzeData.OutputAvailable(
                                                    inputArg=args.GetArgsValue().input, 
                                                    outputArg=args.GetArgsValue().output, 
                                                    verboseArg=args.GetArgsValue().verbose
    )
    if analyseDataOutEnv == EXIT_SUCCESS:
        print("\n[+] Analyze and setup output argument environment '{0}' -> " \
                .format(args.GetArgsValue().output) + Colors.SUCCESS + "Successful" + Colors.DISABLE)
    else:
        print("[-] Analyze output '{0}' -> ".format(args.GetArgsValue().output) + Colors.ERROR + "failed\n" + Colors.DISABLE)
        sys.exit(ERROR_INVALID_FUNCTION)
    
    # -- Obfuscation process -- #    
    print(Colors.SECTION + "\n\n************************* [ Obfuscation delete comments ] *************************\n" + Colors.DISABLE)
    deleteData = Delete()    
    deleteCommentsData = deleteData.Comments(
                                            outputArg=args.GetArgsValue().output,
                                            verboseArg=args.GetArgsValue().verbose
    )
    if deleteCommentsData == EXIT_SUCCESS:
        print("[+] Obfuscation delete comments -> " + Colors.SUCCESS + "Successful" + Colors.DISABLE)
    else:
        print("\n[-] Obfuscation delete comments -> " + Colors.ERROR  + "Failed" + Colors.DISABLE)
        if not args.GetArgsValue().verbose:
            print("\n[!] Retry with [-v, --verbose] parameter")

    print(Colors.SECTION + "\n\n*********************** [ Obfuscation delete line space(s) ] ***********************\n" + Colors.DISABLE)
    if deleteData:
        pass
    else:    
        deleteData = Delete()    
    
    deleteLinesSpacesData = deleteData.LinesSpaces(
                                                    outputArg=args.GetArgsValue().output, 
                                                    verboseArg=args.GetArgsValue().verbose
    )

    if deleteLinesSpacesData == EXIT_SUCCESS:
        print("[+] Obfuscation delete lines spaces -> " + Colors.SUCCESS + "Successful" + Colors.DISABLE)
    else:
        print("\n[-] Obfuscation delete lines spaces -> " + Colors.ERROR  + "Failed" + Colors.DISABLE)
        if not args.GetArgsValue().verbose:
            print("\n[!] Retry with [-v, --verbose] parameter")

      # -- If empty class (avert to generate an error) -- #
    print(Colors.SECTION + "\n\n*********************** [ Correction padding empty class(es) ] *********************\n" + Colors.DISABLE)
    paddingData             = Padding()
    paddingDataEmptyClass   = paddingData.EmptyClasses(
                                                        outputArg=args.GetArgsValue().output, 
                                                        mixerLengthArg=args.GetArgsValue().mixerlength,
                                                        mixerLevelArg=args.GetArgsValue().mixerlevel,
                                                        verboseArg=args.GetArgsValue().verbose
    ) 
    if paddingDataEmptyClass == EXIT_SUCCESS:
        pass
    else:
        print("\n[-] Padding empty class -> " + Colors.ERROR + "Failed" + Colors.DISABLE)
        if not args.GetArgsValue().verbose:
            print("\n[!] Retry with [-v, --verbose] parameter")

    # -- If empty functions (avert to generate an error) -- #
    print(Colors.SECTION + "\n\n********************** [ Correction padding empty function(s) ] ********************\n" + Colors.DISABLE)
    if paddingData:
        pass
    else:
        paddingData = Padding()
    
    paddingDataEmptyFunc = paddingData.EmptyFunctions(
                                                    outputArg=args.GetArgsValue().output, 
                                                    mixerLengthArg=args.GetArgsValue().mixerlength,
                                                    mixerLevelArg=args.GetArgsValue().mixerlevel,
                                                    verboseArg=args.GetArgsValue().verbose
    ) 
    if paddingDataEmptyFunc == EXIT_SUCCESS:
        pass
    else:    
        print("\n[-] Padding empty function -> " + Colors.ERROR + "Failed" + Colors.DISABLE)
        if not args.GetArgsValue().verbose:
            print("\n[!] Retry with [-v, --verbose] parameter")

    print(Colors.SECTION + "\n\n************** [ Obfuscation replace string(s) to string(s) mixed ] ****************\n" + Colors.DISABLE)
    if args.GetArgsValue().replacetostr:
        replaceData = Replace()

        replaceDataStrStr = replaceData.StringToString(
                                                        outputArg=args.GetArgsValue().output, 
                                                        mixerLengthArg=args.GetArgsValue().mixerlength,
                                                        mixerLevelArg=args.GetArgsValue().mixerlevel, 
                                                        verboseArg=args.GetArgsValue().verbose
        ) 

        if replaceDataStrStr == EXIT_SUCCESS:
            print("[+] Obfuscation replace string to string mixed -> " + Colors.SUCCESS + "Successful" + Colors.DISABLE)
        else:
            print("\n[-] Obfuscation replace string to string mixed -> " + Colors.ERROR +  "Failed" + Colors.DISABLE)
            if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")
    else:
        print("[!] Obfuscation [ replace string to string ] mixed no asked !")
    
    print(Colors.SECTION + "\n\n********************* [ Obfuscation adding padding script(s) ] *********************\n" + Colors.DISABLE)
    if args.GetArgsValue().paddingscript:
        if paddingData:
            pass
        else:
            paddingData = Padding()

        paddingDataGarbage = paddingData.AddRandomScripts(
                                                        outputArg=args.GetArgsValue().output,
                                                        mixerLengthArg=args.GetArgsValue().mixerlength,
                                                        mixerLevelArg=args.GetArgsValue().mixerlevel,
                                                        verboseArg=args.GetArgsValue().verbose
        )
        if paddingDataGarbage == EXIT_SUCCESS:
            print("[+] Obfuscation padding script -> " + Colors.SUCCESS + "Successful" + Colors.DISABLE)
        else:
            print("\n[-] Obfuscation padding script -> " + Colors.ERROR + "Failed" + Colors.DISABLE)
            if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")
    else:
        print("[!] Obfuscation [ padding script ] no asked !")

    print(Colors.SECTION + "\n\n********************** [ Obfuscation replace file(s) name ] ************************\n" + Colors.DISABLE)
    if args.GetArgsValue().replacefilename:
        if args.GetArgsValue().replacetostr:
            pass
        else:
            replaceData = Replace()

        replaceDataStrFname = replaceData.FilesName(
                                                    outputArg=args.GetArgsValue().output,
                                                    mixerLengthArg=args.GetArgsValue().mixerlength,
                                                    mixerLevelArg=args.GetArgsValue().mixerlevel,
                                                    verboseArg=args.GetArgsValue().verbose
        )
        if replaceDataStrFname == EXIT_SUCCESS:
            print("\n[+] Obfuscation replace file name -> " + Colors.SUCCESS + "Successful" + Colors.DISABLE)
        else:
            print("\n[-] Obfuscation replace file name -> " + Colors.ERROR + "Failed" + Colors.DISABLE)
            if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")
    else:
        print("[!] Obfuscation [ replace file name ] feature no asked !")
    
    print(Colors.SECTION + "\n\n******************** [ Obfuscation replace string(s) to hex ] **********************\n" + Colors.DISABLE)
    if args.GetArgsValue().replacetohex:
        if args.GetArgsValue().replacetostr or args.GetArgsValue().replacefilename:
            pass
        else:
            replaceData = Replace()

        replaceDataStrHex = replaceData.StringsToHex(
                                                    outputArg=args.GetArgsValue().output, 
                                                    mixerLengthArg=args.GetArgsValue().mixerlength,
                                                    mixerLevelArg=args.GetArgsValue().mixerlevel,
                                                    verboseArg=args.GetArgsValue().verbose
        ) 
        if replaceDataStrHex == EXIT_SUCCESS:
            print("\n[+] Obfuscation replace string to hex -> " + Colors.SUCCESS + "Successful" + Colors.DISABLE)
        else:
            print("\n[-] Obfuscation replace string to hex -> " + Colors.ERROR + "Failed" + Colors.DISABLE)
            if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")
    else:
        print("[!] Obfuscation [ replace string to hex ] feature no asked !")

    # -- Delete if python pyc file in output directory -- #
    print(Colors.SECTION + "\n\n*********************** [ Correction delete .pyc file(s) ] *************************\n" + Colors.DISABLE)
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
        print("\n[-] Delete .pyc file in {0} directory -> ".format(args.GetArgsValue().output) + Colors.ERROR + "Failed" + Colors.DISABLE)
        if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")

#----------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    try:
        main()
        print("\n")
    except KeyboardInterrupt:
        print(Colors.ERROR + "\n[!] Exit program\n" + Colors.DISABLE)
