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
-mlen, --mixerlength        ->  define length of random strings generated [lower:32|medium:64|high:128] (number of chars) \
                                when 'replacetostr' - 'paddingscript' - 'replacefilename' - 'replacetohex' features are specified \
                                possible values: [lower|medium|high]
-ind, --indent              ->  indicate the indentation of your python source code, possible values: [2|4|8]
-rts, --replacetostr        ->  enable 'replace string to string mixed' obfuscation feature
-ps, --paddingscript        ->  enable 'padding script' obfuscation feature
-rfn, --replacefilename     ->  enable 'replace file name' obfuscation feature
-rth, --replacetohex        ->  enable 'replace string to hex' obfuscation feature
-v, --verbose               ->  improve verbosity

"""

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import sys
import re
import time

from core.utils.intensio_design import INTENSIO_BANNER
from core.utils.intensio_utils  import Utils, Colors, Reg
from core.utils.intensio_usage  import Args
from core.obfuscation.intensio_replace  import Replace
from core.obfuscation.intensio_padding  import Padding
from core.obfuscation.intensio_analyze  import Analyze
from core.obfuscation.intensio_delete   import Delete

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

def main():
    if sys.version_info[0] != 3:
        print(Colors.ERROR + "[-] Intensio-Obfuscator only support Python 3.x" + Colors.DISABLE)
        sys.exit(0)

    if sys.platform != "win32" and sys.platform != "linux":
        print(Colors.ERROR + "[-] This tool support [windows - Linux] only !" + Colors.DISABLE)
        sys.exit(0)

    args = Args()
    utils = Utils()

    if len(sys.argv) > 1 and len(sys.argv) <= 15:
        pass
    else:
        print(Colors.ERROR + "[-] Incorrect number of arguments" + Colors.DISABLE + "\n")
        args.GetArgHelp()
        sys.exit(0)

    if args.GetArgsValue().input:
        if args.GetArgsValue().output:
            if re.match(Reg.detectMlenArg, str(args.GetArgsValue().mixerlength)):
                if re.match(Reg.detectIndentArg, str(args.GetArgsValue().indent)):
                    pass
                else:
                    print("\n" + Colors.ERROR + "[-] -ind, --indent argument [2|4|8] missing" + Colors.DISABLE + "\n")
                    sys.exit(0)
            else:
                print("\n" + Colors.ERROR + "[-] -mlen, --mixerlength argument [lower|medium|high] missing" + Colors.DISABLE + "\n")
                sys.exit(0)
        else:
            print("\n" + Colors.ERROR + "[-] Output [-o, --output] argument missing" + Colors.DISABLE + "\n")
            sys.exit(0)
    else:
        print("\n" + Colors.ERROR + "[-] Input [-i, --input] argument missing" + Colors.DISABLE + "\n")
        sys.exit(0)

    for line in INTENSIO_BANNER.split("\n"):
        time.sleep(0.05)
        print(line)

    print("\n\n" + Colors.SECTION + "********************************* [ START ] **********************************" \
        + Colors.DISABLE + "\n")
    
    # -- Analysis and set up of the work environment -- #
    print("\n\n" + Colors.SECTION + "********************* [ Analyze and setup environment ] **********************" \
        + Colors.DISABLE + "\n")
    analyzeData     = Analyze()
    analyseDataInEnv = analyzeData.InputAvailable(
                                                    inputArg=args.GetArgsValue().input,  
                                                    verboseArg=args.GetArgsValue().verbose
    )
    if analyseDataInEnv == 1:
        print("\n[+] Analyze input argument '{}' -> ".format(args.GetArgsValue().input) + Colors.SUCCESS + \
            "Successful" + Colors.DISABLE)
    else:
        print("[-] Analyze input '{}' -> ".format(args.GetArgsValue().input) + Colors.ERROR + "failed" + Colors.DISABLE + "\n")
        sys.exit(0)

    analyseDataOutEnv = analyzeData.OutputAvailable(
                                                    inputArg=args.GetArgsValue().input, 
                                                    outputArg=args.GetArgsValue().output, 
                                                    verboseArg=args.GetArgsValue().verbose
    )
    if analyseDataOutEnv == 1:
        print("\n[+] Analyze and setup output argument environment '{}' -> " \
                .format(args.GetArgsValue().output) + Colors.SUCCESS + "Successful" + Colors.DISABLE)
    else:
        print("[-] Analyze output '{}' -> ".format(args.GetArgsValue().output) + Colors.ERROR + "failed" + Colors.DISABLE + "\n")
        sys.exit(0)

    # -- Obfuscation process -- #    
    startObfuscationTime = time.time()
    
    print("\n\n" + Colors.SECTION + "********************** [ Obfuscation delete comments ] ***********************" \
     + Colors.DISABLE + "\n")
    deleteData = Delete()    
    deleteCommentsData = deleteData.Comments(
                                            outputArg=args.GetArgsValue().output,
                                            verboseArg=args.GetArgsValue().verbose
    )
    if deleteCommentsData == 1:
        print("[+] Obfuscation delete comments -> " + Colors.SUCCESS + "Successful" + Colors.DISABLE)
    else:
        print("\n[-] Obfuscation delete comments -> " + Colors.ERROR  + "Failed" + Colors.DISABLE)
        if not args.GetArgsValue().verbose:
            print("\n[!] Retry with [-v, --verbose] parameter")
    
    print("\n\n" + Colors.SECTION + "******************** [ Obfuscation delete line space(s) ] ********************" \
        + Colors.DISABLE + "\n")
    if deleteData:
        pass
    else:    
        deleteData = Delete()    
    
    deleteLinesSpacesData = deleteData.LinesSpaces(
                                                    outputArg=args.GetArgsValue().output, 
                                                    verboseArg=args.GetArgsValue().verbose
    )

    if deleteLinesSpacesData == 1:
        print("[+] Obfuscation delete lines spaces -> " + Colors.SUCCESS + "Successful" + Colors.DISABLE)
    else:
        print("\n[-] Obfuscation delete lines spaces -> " + Colors.ERROR  + "Failed" + Colors.DISABLE)
        if not args.GetArgsValue().verbose:
            print("\n[!] Retry with [-v, --verbose] parameter")

      # -- If empty class (avert to generate an error) -- #
    print("\n\n" + Colors.SECTION + "******************* [ Correction padding empty class(es) ] *******************" \
        + Colors.DISABLE + "\n")
    paddingData             = Padding()
    paddingDataEmptyClass   = paddingData.EmptyClasses(
                                                        outputArg=args.GetArgsValue().output, 
                                                        mixerLengthArg=args.GetArgsValue().mixerlength,
                                                        basicIndentArg=args.GetArgsValue().indent,
                                                        verboseArg=args.GetArgsValue().verbose
    ) 
    if paddingDataEmptyClass == 1:
        pass
    else:
        print("\n[-] Padding empty class -> " + Colors.ERROR + "Failed" + Colors.DISABLE)
        if not args.GetArgsValue().verbose:
            print("\n[!] Retry with [-v, --verbose] parameter")
    
    # -- If empty functions (avert to generate an error) -- #
    print("\n\n" + Colors.SECTION + "****************** [ Correction padding empty function(s) ] ******************" \
        + Colors.DISABLE + "\n")
    if paddingData:
        pass
    else:
        paddingData = Padding()
    
    paddingDataEmptyFunc = paddingData.EmptyFunctions(
                                                    outputArg=args.GetArgsValue().output, 
                                                    mixerLengthArg=args.GetArgsValue().mixerlength,
                                                    basicIndentArg=args.GetArgsValue().indent,
                                                    verboseArg=args.GetArgsValue().verbose
    ) 
    if paddingDataEmptyFunc == 1:
        pass
    else:    
        print("\n[-] Padding empty function -> " + Colors.ERROR + "Failed" + Colors.DISABLE)
        if not args.GetArgsValue().verbose:
            print("\n[!] Retry with [-v, --verbose] parameter")
    
    print("\n\n" + Colors.SECTION + "************ [ Obfuscation replace string(s) to string(s) mixed ] ************" \
        + Colors.DISABLE + "\n")
    if args.GetArgsValue().replacetostr:
        replaceData = Replace()

        replaceDataStrStr = replaceData.StringToString(
                                                        outputArg=args.GetArgsValue().output, 
                                                        mixerLengthArg=args.GetArgsValue().mixerlength,
                                                        verboseArg=args.GetArgsValue().verbose
        ) 
        if replaceDataStrStr == 1:
            print("[+] Obfuscation replace string to string mixed -> " + Colors.SUCCESS + "Successful" + Colors.DISABLE)
        else:
            print("\n[-] Obfuscation replace string to string mixed -> " + Colors.ERROR +  "Failed" + Colors.DISABLE)
            if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")
    else:
        print("[!] Obfuscation [ replace string to string ] mixed no asked !")
    
    print("\n\n" + Colors.SECTION + "****************** [ Obfuscation adding padding script(s) ] ******************" \
        + Colors.DISABLE + "\n")
    if args.GetArgsValue().paddingscript:
        if paddingData:
            pass
        else:
            paddingData = Padding()

        paddingDataGarbage = paddingData.AddRandomScripts(
                                                        outputArg=args.GetArgsValue().output,
                                                        mixerLengthArg=args.GetArgsValue().mixerlength,
                                                        basicIndentArg=args.GetArgsValue().indent,
                                                        verboseArg=args.GetArgsValue().verbose
        )
        if paddingDataGarbage == 1:
            print("[+] Obfuscation padding script -> " + Colors.SUCCESS + "Successful" + Colors.DISABLE)
        else:
            print("\n[-] Obfuscation padding script -> " + Colors.ERROR + "Failed" + Colors.DISABLE)
            if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")
    else:
        print("[!] Obfuscation [ padding script ] no asked !")

    print("\n\n" + Colors.SECTION + "******************** [ Obfuscation replace file(s) name ] ********************" \
        + Colors.DISABLE + "\n")
    if args.GetArgsValue().replacefilename:
        if args.GetArgsValue().replacetostr:
            pass
        else:
            replaceData = Replace()

        replaceDataStrFname = replaceData.FilesName(
                                                    outputArg=args.GetArgsValue().output,
                                                    mixerLengthArg=args.GetArgsValue().mixerlength,
                                                    verboseArg=args.GetArgsValue().verbose
        )
        if replaceDataStrFname == 1:
            print("\n[+] Obfuscation replace file name -> " + Colors.SUCCESS + "Successful" + Colors.DISABLE)
        else:
            print("\n[-] Obfuscation replace file name -> " + Colors.ERROR + "Failed" + Colors.DISABLE)
            if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")
    else:
        print("[!] Obfuscation [ replace file name ] feature no asked !")
    
    print("\n\n" + Colors.SECTION + "****************** [ Obfuscation replace string(s) to hex ] ******************" \
        + Colors.DISABLE + "\n")
    if args.GetArgsValue().replacetohex:
        if args.GetArgsValue().replacetostr or args.GetArgsValue().replacefilename:
            pass
        else:
            replaceData = Replace()

        replaceDataStrHex = replaceData.StringsToHex(
                                                    outputArg=args.GetArgsValue().output, 
                                                    mixerLengthArg=args.GetArgsValue().mixerlength,
                                                    verboseArg=args.GetArgsValue().verbose
        ) 
        if replaceDataStrHex == 1:
            print("\n[+] Obfuscation replace string to hex -> " + Colors.SUCCESS + "Successful" + Colors.DISABLE)
        else:
            print("\n[-] Obfuscation replace string to hex -> " + Colors.ERROR + "Failed" + Colors.DISABLE)
            if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")
    else:
        print("[!] Obfuscation [ replace string to hex ] feature no asked !")

     # -- Delete line spaces of padding scripts -- #
    if args.GetArgsValue().paddingscript:
        print("\n\n" + Colors.SECTION + "******************** [ Obfuscation delete line space(s) ] ********************" \
            + Colors.DISABLE + "\n")
        if deleteData:
            pass
        else:    
            deleteData = Delete()    
    
        deleteLinesSpacesData = deleteData.LinesSpaces(
                                                        outputArg=args.GetArgsValue().output, 
                                                        verboseArg=args.GetArgsValue().verbose
        )
        if deleteLinesSpacesData == 1:
            print("[+] Obfuscation delete lines spaces of padding scripts-> " + Colors.SUCCESS + "Successful" + Colors.DISABLE)
        else:
            print("\n[-] Obfuscation delete lines spaces of padding scripts -> " + Colors.ERROR  + "Failed" + Colors.DISABLE)
            if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter")

    # -- Delete if python pyc file in output directory -- #
    print("\n\n" + Colors.SECTION + "********************* [ Correction delete .pyc file(s) ] *********************" \
        + Colors.DISABLE + "\n")
    if deleteData:
        pass
    else:
        deleteData = Delete()

    deletePycData = deleteData.TrashFiles(
                                        outputArg=args.GetArgsValue().output, 
                                        verboseArg=args.GetArgsValue().verbose,
    )
    if deletePycData == 1:
        pass
    else:
        print("\n[-] Delete .pyc file from {} directory -> ".format(args.GetArgsValue().output) + Colors.ERROR + \
            "Failed" + Colors.DISABLE)
        if not args.GetArgsValue().verbose:
                print("\n[!] Retry with [-v, --verbose] parameter for more informations")

    print("\n\n" + Colors.SECTION + "********************************** [ END ] ************************************" \
        + Colors.DISABLE + "\n")

    # -- Result of execution time -- #
    endObfuscationTime  = time.time()
    executionTime       = endObfuscationTime - startObfuscationTime
    executionTime       = str(executionTime)
    executionTime       = executionTime.split(".")

    print("[*] Obfuscation Time : {} second(s)".format(executionTime[0]))
    
#----------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    try:
        main()
        print("\n")
    except KeyboardInterrupt:
        print("\n" + Colors.ERROR + "[!] Exit program" + Colors.DISABLE + "\n")
        sys.exit(0)
