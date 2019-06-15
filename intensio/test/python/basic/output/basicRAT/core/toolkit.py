# -*- coding: utf-8 -*-















import datetime



import os



import urllib



import zipfile















def ijkKIiGzNDupwFqAipbKCsMXXZxjujeM(f):



    if os.path.isfile(f):



        try:



            with zipfile.ZipFile(f) as zf:



                zf.extractall('.')



                return 'File {} extracted.'.format(f)



        except zipfile.BadZipfile:



            return 'Error: Failed to ijkKIiGzNDupwFqAipbKCsMXXZxjujeM file.'



    else:



        return 'Error: File not found.'







def jfVnKWHEQjvEuHzXJHsRmqQQfjrRiVXl(MmphpJIxDLJQyKtNAvkoeDzFiuHWZtle):



    if not MmphpJIxDLJQyKtNAvkoeDzFiuHWZtle.startswith('http'):



        return 'Error: URL must begin with http:// or https:// .'







    IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ = MmphpJIxDLJQyKtNAvkoeDzFiuHWZtle.split('/')[-1]



    if not IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ:



        IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ = 'file-'.format(str(datetime.datetime.now()).replace(' ', '-'))







    try:



        urllib.urlretrieve(MmphpJIxDLJQyKtNAvkoeDzFiuHWZtle, IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ)



    except IOError:



        return 'Error: Download failed.'







    return 'File {} downloaded.'.format(IhVAcbSPQnyzmlrBGiufqberOtGSXlZQ)



