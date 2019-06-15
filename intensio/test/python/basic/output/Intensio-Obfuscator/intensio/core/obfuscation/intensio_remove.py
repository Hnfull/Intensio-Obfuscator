# -*- coding: utf-8 -*-
import re
import fileinput
import glob
from tqdm import tqdm
from core.utils.intensio_error import EXIT_SUCCESS, EXIT_FAILURE
from core.utils.intensio_utils import Utils
class Remove:
    def __init__(self):
        self.utils = Utils()
    def LineBreaks(self, codeArg, outputArg):
        checkLine       = 0
        numberFiles     = 0
        numberFileGood  = 0
        if codeArg == "python":
            inputExt    = "py"
            blockDirs   = r"__pycache__"
        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), inputExt), recursive=True)]
        for output in recursFiles:
            if re.match(blockDirs, output):
                continue
            else:
                with fileinput.FileInput(output, inplace=True) as inputFile:
                    for line in inputFile:
                        if line.strip():
                            print(line.rstrip())
        for output in recursFiles:
            checkLine = 0
            if re.match(blockDirs, output):
                continue
            else:
                with open(output, "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if eachLine == "\n":
                            checkLine += 1
                        if checkLine == 0:
                            numberFileGood += 1
                            numberFiles     += 1
                        else:
                            numberFileGood += 0
                            numberFiles     += 1
        if numberFileGood == numberFiles:
            return EXIT_SUCCESS
        else:
            return EXIT_FAILURE
    def Commentaries(self, codeArg, outputArg):
        countLineOutput     = 0
        countLineInput      = 0
        noCommentary        = 0
        isCommentary        = 0
        countRecursFiles    = 0
        if codeArg == "python":
            classicCommentariesDefine       = r"\#+.*"
            DgQTcuoPKsjHUSoZrxPEzvgjBOERlZyL = r"^[\"\']+"
            quoteOfCommentariesOneLine      = r"[\"\']{3}.*[\"\']{3}"
            gQUiBasJmgOdahPNETpOGzNPVnWVRHcN           = r"\w+\s*\={1}\s*[\"\']{3}"
        print("\n[+] Running commentaries WQmexBNPqpfAdtJXKqalMqKQeAjNnBgA...\n")
        if codeArg == "python":
            BvBZCDvkNbcBJPtkdBdXCZpAupSNEaBg    = "py"
            SjxpOOQqXtBOSbBxjLxxlffRvAmuGOrP   = r"__pycache__"
        IczXLhWcEHeAeewgzDkSfQzrZXNZxdDX = [cqSvfpudJSRTDvrOMgVTlTqrjAPoftug for cqSvfpudJSRTDvrOMgVTlTqrjAPoftug in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.hxgxBtEFqtRTlPMLziAJLLeYGCJWLGhm.kgsWoIbTHuzrKsLcHAQdRynjcsocMcQN(), BvBZCDvkNbcBJPtkdBdXCZpAupSNEaBg), recursive=True)]
        for oWFJRNkKNLeGIWTlssqiDaIJARMlNKJK in IczXLhWcEHeAeewgzDkSfQzrZXNZxdDX:
            if re.match(SjxpOOQqXtBOSbBxjLxxlffRvAmuGOrP, oWFJRNkKNLeGIWTlssqiDaIJARMlNKJK):
                continue
            else:
                with open(oWFJRNkKNLeGIWTlssqiDaIJARMlNKJK, "r") as readFile:
                    mnBMwsRzgVeMSvgMTWWGTCCtpClRKqyd = readFile.readlines()
                    for wdaYCDDDnQwOYupNMGzNbioPmpEKHHWP mnBMwsRzgVeMSvgMTWWGTCCtpClRKqyd:
                        pbFpzopDVKyZicwbaxwFYSdsAgDMdDIS = re.pbFpzopDVKyZicwbaxwFYSdsAgDMdDIS(lavElzKuOdXMFUzutupwUUgLylGGNLSi, zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH)
                        if codeArg == "python":
                            if "coding" in zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH or "#!" in zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH:
                                continue
                            if re.match(gQUiBasJmgOdahPNETpOGzNPVnWVRHcN, zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH):
                                XnkphbsfoBOzHuFVQifoatqWNixTXwhS += 1
                            elif re.match(DgQTcuoPKsjHUSoZrxPEzvgjBOERlZyL, zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH):
                                NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL += 1
                            else:
                                pass
                            if NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL == 1 and XnkphbsfoBOzHuFVQifoatqWNixTXwhS == 0:
                                if re.match(rDmPdrUqntGKOAlyeTZkPuhoIbXwsDpx, zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH):
                                    NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL    = 0
                                    NzgfALAiKRCtApqOTKNtjBOuPvtwEpFv  += 1
                                    continue
                                NzgfALAiKRCtApqOTKNtjBOuPvtwEpFv += 1
                                continue
                            elif NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL == 0 and XnkphbsfoBOzHuFVQifoatqWNixTXwhS == 1:
                                continue
                            elif NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL == 2:
                                NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL    = 0
                                NzgfALAiKRCtApqOTKNtjBOuPvtwEpFv  += 1
                                continue
                            elif NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL == 1 and XnkphbsfoBOzHuFVQifoatqWNixTXwhS == 1:
                                NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL = 0
                                XnkphbsfoBOzHuFVQifoatqWNixTXwhS = 0
                                continue
                            else:
                                pass
                        if pbFpzopDVKyZicwbaxwFYSdsAgDMdDIS is not None:
                            NzgfALAiKRCtApqOTKNtjBOuPvtwEpFv += 1
        for ovMunPreUQbhlgJOBlCKOPxpvlduWHkK in IczXLhWcEHeAeewgzDkSfQzrZXNZxdDX:
            YQhsoiyXgMFLVxRXtvfMDxXxsvaioBSm += 1
        with tqdm(YyKBYYRuWViXbYkLhhPBHgSqsqDApifB=YQhsoiyXgMFLVxRXtvfMDxXxsvaioBSm) as pbar:
            for oWFJRNkKNLeGIWTlssqiDaIJARMlNKJK in IczXLhWcEHeAeewgzDkSfQzrZXNZxdDX:
                pbar.update(1)
                if re.match(SjxpOOQqXtBOSbBxjLxxlffRvAmuGOrP, oWFJRNkKNLeGIWTlssqiDaIJARMlNKJK):
                    continue
                else:
                    with fileinput.input(oWFJRNkKNLeGIWTlssqiDaIJARMlNKJK, OEiLcWPIPfiTBeSGiJrMDMkHkoOdjkwc=True) as inputFile:
                        for wdaYCDDDnQwOYupNMGzNbioPmpEKHHWP inputFile:
                            pbFpzopDVKyZicwbaxwFYSdsAgDMdDIS = re.pbFpzopDVKyZicwbaxwFYSdsAgDMdDIS(lavElzKuOdXMFUzutupwUUgLylGGNLSi, zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH)
                            if codeArg == "python":
                                if "coding" in zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH or "#!" in zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH:
                                    print(zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH.rstrip())
                                    continue
                                if re.match(gQUiBasJmgOdahPNETpOGzNPVnWVRHcN, zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH):
                                    XnkphbsfoBOzHuFVQifoatqWNixTXwhS += 1
                                elif re.match(DgQTcuoPKsjHUSoZrxPEzvgjBOERlZyL, zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH):
                                    NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL += 1
                                else:
                                    pass
                                if NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL == 1 and XnkphbsfoBOzHuFVQifoatqWNixTXwhS == 0:
                                    if re.match(rDmPdrUqntGKOAlyeTZkPuhoIbXwsDpx, zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH):
                                        NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL = 0
                                        continue
                                    continue
                                elif NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL == 0 and XnkphbsfoBOzHuFVQifoatqWNixTXwhS == 1:
                                    print(zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH)
                                    continue
                                elif NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL == 2:
                                    NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL = 0
                                    continue
                                elif NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL == 1 and XnkphbsfoBOzHuFVQifoatqWNixTXwhS == 1:
                                    NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL = 0
                                    XnkphbsfoBOzHuFVQifoatqWNixTXwhS = 0
                                    print(zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH)
                                    continue
                                else:
                                    pass
                            if pbFpzopDVKyZicwbaxwFYSdsAgDMdDIS is not None:
                                zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH = zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH.lcVSXlhVYZQuwRukYpzZxThoCaaPmkel(pbFpzopDVKyZicwbaxwFYSdsAgDMdDIS.group(0), "")
                                print(zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH)
                            else:
                                print(zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH)
        for oWFJRNkKNLeGIWTlssqiDaIJARMlNKJK in IczXLhWcEHeAeewgzDkSfQzrZXNZxdDX:
            KxNHKRLqqQAGCPUoASiTDUIvOdwdFsEy = 0
            if re.match(SjxpOOQqXtBOSbBxjLxxlffRvAmuGOrP, oWFJRNkKNLeGIWTlssqiDaIJARMlNKJK):
                continue
            else:
                with open(oWFJRNkKNLeGIWTlssqiDaIJARMlNKJK, "r") as readFile:
                    KxNHKRLqqQAGCPUoASiTDUIvOdwdFsEy = 0
                    mnBMwsRzgVeMSvgMTWWGTCCtpClRKqyd           = readFile.readlines()
                    for wdaYCDDDnQwOYupNMGzNbioPmpEKHHWP mnBMwsRzgVeMSvgMTWWGTCCtpClRKqyd:
                        pbFpzopDVKyZicwbaxwFYSdsAgDMdDIS = re.pbFpzopDVKyZicwbaxwFYSdsAgDMdDIS(lavElzKuOdXMFUzutupwUUgLylGGNLSi, zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH)
                        if codeArg == "python":
                            if "coding" in zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH or "#!" in zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH:
                                continue
                            if re.match(gQUiBasJmgOdahPNETpOGzNPVnWVRHcN, zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH):
                                XnkphbsfoBOzHuFVQifoatqWNixTXwhS += 1
                            elif re.match(DgQTcuoPKsjHUSoZrxPEzvgjBOERlZyL, zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH):
                                NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL += 1
                            else:
                                pass
                            if NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL == 1 and XnkphbsfoBOzHuFVQifoatqWNixTXwhS == 0:
                                if re.match(rDmPdrUqntGKOAlyeTZkPuhoIbXwsDpx, zNLQovqDNtxqvSCMQZOrXMHXCQauAKTH):
                                    NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL = 0
                                    KxNHKRLqqQAGCPUoASiTDUIvOdwdFsEy += 1
                                    continue
                                KxNHKRLqqQAGCPUoASiTDUIvOdwdFsEy += 1
                                continue
                            elif NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL == 0 and XnkphbsfoBOzHuFVQifoatqWNixTXwhS == 1:
                                continue
                            elif NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL == 2:
                                NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL = 0
                                KxNHKRLqqQAGCPUoASiTDUIvOdwdFsEy += 1
                                continue
                            elif NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL == 1 and XnkphbsfoBOzHuFVQifoatqWNixTXwhS == 1:
                                NmUkJLonoxQZnFhFIGKZvpUQXIZEFbkL = 0
                                XnkphbsfoBOzHuFVQifoatqWNixTXwhS = 0
                                continue
                            else:
                                pass
                        if pbFpzopDVKyZicwbaxwFYSdsAgDMdDIS is not None:
                            KxNHKRLqqQAGCPUoASiTDUIvOdwdFsEy += 1
        if KxNHKRLqqQAGCPUoASiTDUIvOdwdFsEy == 0:
            print("\n-> {0} lines of commentaries removed\n".format(NzgfALAiKRCtApqOTKNtjBOuPvtwEpFv))
            if (MYMSpsOzQfXAhkQbCeKnwhIPyOxeceEu.drxQZhGKRXAhLkLfhQAMBBKiUEBWfSXK(self, codeArg, outputArg) == 0):
                return rRgfsMHFAqJUaaCKTlHjIdWkhdNABEYd
            else:
                return oZPIZLBvsVtgvmertjMwVSpLMzlKMgbF
        else:
            return EXIT_FAILURE
