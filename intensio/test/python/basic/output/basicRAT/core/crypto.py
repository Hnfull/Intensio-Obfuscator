# -*- coding: utf-8 -*-
import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from common import vPhGiqobzraQogPhmSNMiLGlRsTTbltg, gHeYYFDraZaeMRPcoGgADweIrwuOaiwa
qNkLWKWWiPLVSaUTmEkWwZfDfyyDEorh = 'b14ce95fa4c33ac2803782d18341869f'
class gSINqCImJWJvnSoHzzjhuRNQgtvqMsXr(Exception):
    pass
def QaZuyzUdZrmoFNXyVecjWVumobsRLfZD(VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK, fGUUwosZVXGwgRYBPvfRLfNtGOJGqVoO=AES.block_size):
    oaUVjRZSEqOiYdoDRRraRJNSStGiPkYI = (fGUUwosZVXGwgRYBPvfRLfNtGOJGqVoO - (len(VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK) % fGUUwosZVXGwgRYBPvfRLfNtGOJGqVoO))
    return VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK + (chr(oaUVjRZSEqOiYdoDRRraRJNSStGiPkYI)*oaUVjRZSEqOiYdoDRRraRJNSStGiPkYI)
def QMiDxwDsauyOvePHTflrSPkZqkAFTjAx(VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK):
    oaUVjRZSEqOiYdoDRRraRJNSStGiPkYI = VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK[-1]
    if VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK.endswith(oaUVjRZSEqOiYdoDRRraRJNSStGiPkYI*ord(oaUVjRZSEqOiYdoDRRraRJNSStGiPkYI)):
        return VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK[:-ord(oaUVjRZSEqOiYdoDRRraRJNSStGiPkYI)]
    raise gSINqCImJWJvnSoHzzjhuRNQgtvqMsXr("PKCS7 improper padding {}".format(repr(VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK[-32:])))
def WgMnRzLdkIWLGgzowFdvUafwiPBCbvOk(sock, NALWfnGzUeuWyziYDnvFfiMmryRuvziU=True, bits=2048):
    ZSJpsSjHtBSoaVmoZQKZRaSwOtvwBfby = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF;
    YyFrvCZezfvqCEHvuyXHqZOEvjCRBytW = 2
    XmmaRyZddRfxXfJdsxeeLGoZRHuHBzMw = gHeYYFDraZaeMRPcoGgADweIrwuOaiwa(os.urandom(32))
    MNKyRAJlLfXUVInAeiygRTGCABhefsMr = pow(YyFrvCZezfvqCEHvuyXHqZOEvjCRBytW, XmmaRyZddRfxXfJdsxeeLGoZRHuHBzMw, ZSJpsSjHtBSoaVmoZQKZRaSwOtvwBfby)
    if NALWfnGzUeuWyziYDnvFfiMmryRuvziU:
        sock.send(vPhGiqobzraQogPhmSNMiLGlRsTTbltg(MNKyRAJlLfXUVInAeiygRTGCABhefsMr))
        SmlKstlNcUGBOrTNHgJavBmxaNfDyhgj = gHeYYFDraZaeMRPcoGgADweIrwuOaiwa(sock.recv(4096))
    else:
        SmlKstlNcUGBOrTNHgJavBmxaNfDyhgj = gHeYYFDraZaeMRPcoGgADweIrwuOaiwa(sock.recv(4096))
        sock.send(vPhGiqobzraQogPhmSNMiLGlRsTTbltg(MNKyRAJlLfXUVInAeiygRTGCABhefsMr))
    VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK = pow(SmlKstlNcUGBOrTNHgJavBmxaNfDyhgj, XmmaRyZddRfxXfJdsxeeLGoZRHuHBzMw, ZSJpsSjHtBSoaVmoZQKZRaSwOtvwBfby)
    return SHA256.new(vPhGiqobzraQogPhmSNMiLGlRsTTbltg(VHjCuCuNRvBpZpECbFwdRoufFlbNfsBK)).digest()
def TKQFCDOUTVgFyFAJmsSOIosLeXgEyzvM(MrpZNHvdwUIcJxwtJGbDuTbAaCULevLO, KEY):
    MrpZNHvdwUIcJxwtJGbDuTbAaCULevLO = QaZuyzUdZrmoFNXyVecjWVumobsRLfZD(MrpZNHvdwUIcJxwtJGbDuTbAaCULevLO)
    LHkJPzkZMxcRDxtOBpoAMxJCGqUyqldr = Random.new().read(AES.block_size)
    NIuGQNQuwNRIMZgBRuVUZYbvZwvBAkDk = AES.new(KEY, AES.MODE_CBC, LHkJPzkZMxcRDxtOBpoAMxJCGqUyqldr)
    return LHkJPzkZMxcRDxtOBpoAMxJCGqUyqldr + NIuGQNQuwNRIMZgBRuVUZYbvZwvBAkDk.encrypt(MrpZNHvdwUIcJxwtJGbDuTbAaCULevLO)
def ofRSbfGSJUJdJOMAHnOdMFDQhCuQDoiv(ciphertext, KEY):
    LHkJPzkZMxcRDxtOBpoAMxJCGqUyqldr = ciphertext[:AES.block_size]
    NIuGQNQuwNRIMZgBRuVUZYbvZwvBAkDk = AES.new(KEY, AES.MODE_CBC, LHkJPzkZMxcRDxtOBpoAMxJCGqUyqldr)
    MrpZNHvdwUIcJxwtJGbDuTbAaCULevLO = NIuGQNQuwNRIMZgBRuVUZYbvZwvBAkDk.decrypt(ciphertext[AES.block_size:])
    return QMiDxwDsauyOvePHTflrSPkZqkAFTjAx(MrpZNHvdwUIcJxwtJGbDuTbAaCULevLO)
