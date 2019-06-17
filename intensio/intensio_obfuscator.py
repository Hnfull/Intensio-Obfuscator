# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

"""

 /$$$$$$             /$$                                   /$$                  /$$$$$$  /$$        /$$$$$$                                           /$$
|_  $$_/            | $$                                  |__/                 /$$__  $$| $$       /$$__  $$                                         | $$
  | $$   /$$$$$$$  /$$$$$$    /$$$$$$  /$$$$$$$   /$$$$$$$ /$$  /$$$$$$       | $$  \ $$| $$$$$$$ | $$  \__//$$   /$$  /$$$$$$$  /$$$$$$$  /$$$$$$  /$$$$$$    /$$$$$$   /$$$$$$
  | $$  | $$__  $$|_  $$_/   /$$__  $$| $$__  $$ /$$_____/| $$ /$$__  $$      | $$  | $$| $$__  $$| $$$$   | $$  | $$ /$$_____/ /$$_____/ |____  $$|_  $$_/   /$$__  $$ /$$__  $$
  | $$  | $$  \ $$  | $$    | $$$$$$$$| $$  \ $$|  $$$$$$ | $$| $$  \ $$      | $$  | $$| $$  \ $$| $$_/   | $$  | $$|  $$$$$$ | $$        /$$$$$$$  | $$    | $$  \ $$| $$  \__/
  | $$  | $$  | $$  | $$ /$$| $$_____/| $$  | $$ \____  $$| $$| $$  | $$      | $$  | $$| $$  | $$| $$     | $$  | $$ \____  $$| $$       /$$__  $$  | $$ /$$| $$  | $$| $$
 /$$$$$$| $$  | $$  |  $$$$/|  $$$$$$$| $$  | $$ /$$$$$$$/| $$|  $$$$$$/      |  $$$$$$/| $$$$$$$/| $$     |  $$$$$$/ /$$$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$
|______/|__/  |__/   \___/   \_______/|__/  |__/|_______/ |__/ \______/        \______/ |_______/ |__/      \______/ |_______/  \_______/ \_______/   \___/   \______/ |__/


-h, --help              -> show this help message and exit
-i, --input             -> source directory - indicate a directory that contain your file(s)
-c, --code              -> language used in source directory, default value: [python] possible value: [python]
-o, --output            -> output directory that will be obfuscated - indicate a empty directory that will contain your file(s)
-m, --mixer             -> length level of variables/classes/functions/files mix output, default value: medium, possible values: [lower, medium, high]
-r, --replace           -> activate the 'replace' obfuscation feature
-p, --padding           -> activate the 'padding' obfuscation feature
-rm, --remove           -> activate the 'remove' obfuscation feature

"""

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import sys
import re
import time

#---------------------------------------------------------- [Main] ----------------------------------------------------------#

def main():
    if sys.version_info[0] != 3:
        print("[-] Intensio-Obfuscator only support Python 3.x")
        sys.exit(0)

    if sys.platform != "win32" and sys.platform != "linux":
        print("[-] This tool support [windows - Linux] only !")
        sys.exit(0)

    try:
        from core.utils.intensio_design import INTENSIO_BANNER
        from core.utils.intensio_utils import Utils
        from core.utils.intensio_usage import Args
        from core.utils.intensio_error import EXIT_SUCCESS, ERROR_BAD_ENVIRONMENT, ERROR_INVALID_PARAMETER, ERROR_BAD_ARGUMENTS,\
                                                ERROR_INVALID_FUNCTION, ERROR_FILE_NOT_FOUND
        from core.obfuscation.intensio_replace import Replace
        from core.obfuscation.intensio_padding import Padding
        from core.obfuscation.intensio_analyze import Analyze
        from core.obfuscation.intensio_remove import Remove
    except ImportError as e:
        print("[-] {0}\n".format(e))
        sys.exit(0)

    args    = Args()
    utils   = Utils()

    if len(sys.argv) > 1 and len(sys.argv) <= 13:
        if args.GetArgsValue().input:
            if args.GetArgsValue().output:
                for line in INTENSIO_BANNER.split("\n"):
                    time.sleep(0.05)
                    print(line)

                print("\n\n*********************** [ Analyze and setup environment ] ************************\n")
                # -- Analysis and set up of the work environment -- #
                if args.GetArgsValue().code:
                    if re.match(r"^python$", args.GetArgsValue().code):
                        analyze = Analyze()

                        if (analyze.InputAvailable(args.GetArgsValue().input, args.GetArgsValue().code) == EXIT_SUCCESS):
                            print("[+] Analyze input argument '{0}' -> Successful".format(args.GetArgsValue().input))

                            if (analyze.OutputAvailable(args.GetArgsValue().input, args.GetArgsValue().code, args.GetArgsValue().output) == EXIT_SUCCESS):
                                print("\n[+] Analyze and setup output argument environment '{0}' -> Successful".format(args.GetArgsValue().output))

                                if args.GetArgsValue().mixer:
                                    if re.match(r"(^lower$)|(^medium$)|(^high$)", args.GetArgsValue().mixer):
                                        if not args.GetArgsValue().padding and not args.GetArgsValue().replace and not args.GetArgsValue().rcommentaries and not args.GetArgsValue().rprint:
                                            print("\n[-] Need at least one argument [-r --replace] or [-p --padding] or [-rm -remove]")
                                            sys.exit(ERROR_BAD_ARGUMENTS)
                                        else:
                                            print("\n\n***************************** [ Obfuscation Replace ] *****************************\n")
                                            if args.GetArgsValue().replace:
                                                replace = Replace()

                                                if (replace.VarsDefinedByUser(args.GetArgsValue().code, args.GetArgsValue().output, args.GetArgsValue().mixer) == EXIT_SUCCESS):
                                                    print("[+] Obfuscation Replace -> Successful")
                                                else:
                                                    print("\n[-] Obfuscation Replace -> Failed")
                                            else:
                                                print("[!] Obfuscation Replace no asked !")

                                            print("\n\n***************************** [ Obfuscation Padding ] *****************************\n")
                                            if args.GetArgsValue().padding:
                                                paddingScripts = Padding()

                                                if (paddingScripts.AddScripts(args.GetArgsValue().code, args.GetArgsValue().output, args.GetArgsValue().mixer) == EXIT_SUCCESS):
                                                    print("[+] Obfuscation Padding -> Successful")
                                                else:
                                                    print("\n[-] Obfuscation Padding -> Failed")
                                            else:
                                                print("[!] Obfuscation Padding no asked !")

                                            print("\n\n************************** [ Obfuscation Rcommentaries ] **************************\n")
                                            if args.GetArgsValue().rcommentaries:
                                                removeData = Remove()

                                                if (removeData.Commentaries(args.GetArgsValue().code, args.GetArgsValue().output) == EXIT_SUCCESS):
                                                    print("[+] Obfuscation Rcommentaries -> Successful")
                                                else:
                                                    print("\n[-] Obfuscation Rcommentaries -> Failed")
                                            else:
                                                print("[!] Obfuscation Rcommentaries no asked !")

                                            print("\n\n****************************** [ Obfuscation Rprint ] *****************************\n")
                                            if args.GetArgsValue().rprint:
                                                removeData = Remove()

                                                if (removeData.PrintFunc(args.GetArgsValue().code, args.GetArgsValue().output) == EXIT_SUCCESS):
                                                    print("[+] Obfuscation Rprint -> Successful\n")
                                                else:
                                                    print("\n[-] Obfuscation Rprint -> Failed\n")
                                            else:
                                                print("[!] Obfuscation Rprint no asked !\n")
                                    else:
                                        print("[-] Incorrect level of mixer, [lower - medium - high] only supported\n")
                                        sys.exit(ERROR_INVALID_PARAMETER)
                                else:
                                    print("[-] Mixer [-m --mixer] argument missing\n")
                                    sys.exit(ERROR_BAD_ARGUMENTS)
                            else:
                                print("[-] Analyze output '{0}' failed\n".format(args.GetArgsValue().output))
                                sys.exit(ERROR_INVALID_FUNCTION)
                        else:
                            print("[-] Analyze input '{0}' failed\n".format(args.GetArgsValue().input))
                            sys.exit(ERROR_INVALID_FUNCTION)
                    else:
                        print("[-] '{0}' Incorrect code argument, [python] only currently supported\n".format(args.GetArgsValue().Code))
                        sys.exit(ERROR_INVALID_PARAMETER)
                else:
                    print("[-] Code [-c --code] argument missing\n")
                    sys.exit(ERROR_BAD_ARGUMENTS)
            else:
                print("[-] Output [-o --output] argument missing\n")
                sys.exit(ERROR_BAD_ARGUMENTS)
        else:
            print("[-] Input [-i --input] argument missing\n")
            sys.exit(ERROR_BAD_ARGUMENTS)
    else:
        print("[-] Incorrect number of arguments\n")
        args.GetArgHelp()
        sys.exit(ERROR_BAD_ARGUMENTS)

#----------------------------------------------------------------------------------------------------------------------------#

#----------------------------------------------------------------------------------------------------------------------------#

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Exit program\n")
