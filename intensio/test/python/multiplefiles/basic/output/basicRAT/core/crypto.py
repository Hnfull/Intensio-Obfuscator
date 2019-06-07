# -*- coding: utf-8 -*-
import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from common import RVNCwkPSBIUdLcMWFGqkfZVSuUtdnmJK, SVSoADWqihFxbJjTcDmCsIbhUruPAHkl
wiakvVQTpzJqrLISsvGBwPmKhkusZqOk = 'b14ce95fa4c33ac2803782d18341869f'
class LqAljIpgucJPwwjdcHzuRBCpqASakzoF(Exception):
    pass
def NEjddYCKNdRCLsYucRYMruesiLNjCftp(WerXeVRoSuIOUzPqeUfRcYEiijTiROFb, XQscUmwsqfTaichXZIRAKxqcojkAxStt=AES.block_size):
    hscswvelsmekdrdqbSsXHYBuqgXbSmcs = (XQscUmwsqfTaichXZIRAKxqcojkAxStt - (len(WerXeVRoSuIOUzPqeUfRcYEiijTiROFb) % XQscUmwsqfTaichXZIRAKxqcojkAxStt))
    return WerXeVRoSuIOUzPqeUfRcYEiijTiROFb + (chr(hscswvelsmekdrdqbSsXHYBuqgXbSmcs)*hscswvelsmekdrdqbSsXHYBuqgXbSmcs)
def tRjyELeiJvdryweBXSYxWtaHRNcPuroN(WerXeVRoSuIOUzPqeUfRcYEiijTiROFb):
    hscswvelsmekdrdqbSsXHYBuqgXbSmcs = WerXeVRoSuIOUzPqeUfRcYEiijTiROFb[-1]
    if WerXeVRoSuIOUzPqeUfRcYEiijTiROFb.endswith(hscswvelsmekdrdqbSsXHYBuqgXbSmcs*ord(hscswvelsmekdrdqbSsXHYBuqgXbSmcs)):
        return WerXeVRoSuIOUzPqeUfRcYEiijTiROFb[:-ord(hscswvelsmekdrdqbSsXHYBuqgXbSmcs)]
    raise LqAljIpgucJPwwjdcHzuRBCpqASakzoF("PKCS7 improper padding {}".format(repr(WerXeVRoSuIOUzPqeUfRcYEiijTiROFb[-32:])))
def uzwtEZAIcAlkEUgSDDweqaCnAdgheMQc(sock, jybzhUMtEcXpeFKNLZgKTPNKIrRsixZu=True, bits=2048):
    jumtownqyqZwmluxHsnMiRVGtzfFCykt = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF;
    hZAoCMGFDGzIDNmTAlmbOCwtcjfEkiLL = 2
    qItbZWUsfTFBRLghDxuMCwfxSFENCkvP = SVSoADWqihFxbJjTcDmCsIbhUruPAHkl(os.urandom(32))
    zcuyqwSczSCPIhCsBkRmqlSqVUgANOym = pow(hZAoCMGFDGzIDNmTAlmbOCwtcjfEkiLL, qItbZWUsfTFBRLghDxuMCwfxSFENCkvP, jumtownqyqZwmluxHsnMiRVGtzfFCykt)
    if jybzhUMtEcXpeFKNLZgKTPNKIrRsixZu:
        sock.send(RVNCwkPSBIUdLcMWFGqkfZVSuUtdnmJK(zcuyqwSczSCPIhCsBkRmqlSqVUgANOym))
        NIYIpDHJeURyexsaIpBUEediaUnCxdGW = SVSoADWqihFxbJjTcDmCsIbhUruPAHkl(sock.recv(4096))
    else:
        NIYIpDHJeURyexsaIpBUEediaUnCxdGW = SVSoADWqihFxbJjTcDmCsIbhUruPAHkl(sock.recv(4096))
        sock.send(RVNCwkPSBIUdLcMWFGqkfZVSuUtdnmJK(zcuyqwSczSCPIhCsBkRmqlSqVUgANOym))
    WerXeVRoSuIOUzPqeUfRcYEiijTiROFb = pow(NIYIpDHJeURyexsaIpBUEediaUnCxdGW, qItbZWUsfTFBRLghDxuMCwfxSFENCkvP, jumtownqyqZwmluxHsnMiRVGtzfFCykt)
    return SHA256.new(RVNCwkPSBIUdLcMWFGqkfZVSuUtdnmJK(WerXeVRoSuIOUzPqeUfRcYEiijTiROFb)).digest()
def aNZTYevmZkLIbpnXMxKrkTKZcOnrEXIu(VmPzpLmEJosdcHJsGwRXnlcIhPTqpVqp, KEY):
    VmPzpLmEJosdcHJsGwRXnlcIhPTqpVqp = NEjddYCKNdRCLsYucRYMruesiLNjCftp(VmPzpLmEJosdcHJsGwRXnlcIhPTqpVqp)
    PsBlqKAalFlHdivHxnihjxXaKlxxmoiV = Random.new().read(AES.block_size)
    XhsneKWCtMUfzHWqDBSeetdGhacvgxtk = AES.new(KEY, AES.MODE_CBC, PsBlqKAalFlHdivHxnihjxXaKlxxmoiV)
    return PsBlqKAalFlHdivHxnihjxXaKlxxmoiV + XhsneKWCtMUfzHWqDBSeetdGhacvgxtk.encrypt(VmPzpLmEJosdcHJsGwRXnlcIhPTqpVqp)
def CkoyYDxmdvqmpDqmiDQfNmYJEooZuJfR(ciphertext, KEY):
    PsBlqKAalFlHdivHxnihjxXaKlxxmoiV = ciphertext[:AES.block_size]
    XhsneKWCtMUfzHWqDBSeetdGhacvgxtk = AES.new(KEY, AES.MODE_CBC, PsBlqKAalFlHdivHxnihjxXaKlxxmoiV)
    VmPzpLmEJosdcHJsGwRXnlcIhPTqpVqp = XhsneKWCtMUfzHWqDBSeetdGhacvgxtk.decrypt(ciphertext[AES.block_size:])
    return tRjyELeiJvdryweBXSYxWtaHRNcPuroN(VmPzpLmEJosdcHJsGwRXnlcIhPTqpVqp)
