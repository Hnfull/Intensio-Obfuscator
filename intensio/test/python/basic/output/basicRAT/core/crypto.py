# -*- coding: utf-8 -*-
import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from common import JEqwwHNMplUHQfmnFPmPIJLLPpMZzJbE, MpwmxlKlKgQYqNUMJWAaAamYutewCGjo
lfnJteDWQMeRDlqkHzcmwQtnNbocIbdO = 'b14ce95fa4c33ac2803782d18341869f'
class QwugjchtcNSGzuXLEdEmrePiMzEyhGuo(Exception):
    pass
def COSPdDtulmRNzsGjqdoNlpJhnAwynuQQ(CbHagqpBcIpeEWUyuBbobjCzudqKrPsR, rOesvkMFGGmrLOmCvjPALTJFpQwssmGm=AES.block_size):
    ceQRFUOFrPawwBpzwyuNDqxyGzBNWzOZ = (rOesvkMFGGmrLOmCvjPALTJFpQwssmGm - (len(CbHagqpBcIpeEWUyuBbobjCzudqKrPsR) % rOesvkMFGGmrLOmCvjPALTJFpQwssmGm))
    return CbHagqpBcIpeEWUyuBbobjCzudqKrPsR + (chr(ceQRFUOFrPawwBpzwyuNDqxyGzBNWzOZ)*ceQRFUOFrPawwBpzwyuNDqxyGzBNWzOZ)
def zOoSSCPRFcJgCcrCYloVGRTDqNDIvOFo(CbHagqpBcIpeEWUyuBbobjCzudqKrPsR):
    ceQRFUOFrPawwBpzwyuNDqxyGzBNWzOZ = CbHagqpBcIpeEWUyuBbobjCzudqKrPsR[-1]
    if CbHagqpBcIpeEWUyuBbobjCzudqKrPsR.endswith(ceQRFUOFrPawwBpzwyuNDqxyGzBNWzOZ*ord(ceQRFUOFrPawwBpzwyuNDqxyGzBNWzOZ)):
        return CbHagqpBcIpeEWUyuBbobjCzudqKrPsR[:-ord(ceQRFUOFrPawwBpzwyuNDqxyGzBNWzOZ)]
    raise QwugjchtcNSGzuXLEdEmrePiMzEyhGuo("PKCS7 improper padding {}".format(repr(CbHagqpBcIpeEWUyuBbobjCzudqKrPsR[-32:])))
def VxWgDmRXKUkHaoZGUVlfsqoqGmMDDtWS(sock, DpHxMbqtwYrYxBYzSMIcLuBCkkFQKRTR=True, bits=2048):
    xAjjXmPqxOqrzSvtOzBKwEqMKLHzWGeR = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF;
    kFXCVgKDwcelUcXhnuQPPYOjAcyJsBav = 2
    BydkDdrxdfAXrftvAKyrifGnDywBhZhq = MpwmxlKlKgQYqNUMJWAaAamYutewCGjo(os.urandom(32))
    ARCydHXqpuGGdfCuMzrSHXUKqtVApNIa = pow(kFXCVgKDwcelUcXhnuQPPYOjAcyJsBav, BydkDdrxdfAXrftvAKyrifGnDywBhZhq, xAjjXmPqxOqrzSvtOzBKwEqMKLHzWGeR)
    if DpHxMbqtwYrYxBYzSMIcLuBCkkFQKRTR:
        sock.send(JEqwwHNMplUHQfmnFPmPIJLLPpMZzJbE(ARCydHXqpuGGdfCuMzrSHXUKqtVApNIa))
        JrpEhCiJhfWsaZKzcgwpfvSOoWOPuHYq = MpwmxlKlKgQYqNUMJWAaAamYutewCGjo(sock.recv(4096))
    else:
        JrpEhCiJhfWsaZKzcgwpfvSOoWOPuHYq = MpwmxlKlKgQYqNUMJWAaAamYutewCGjo(sock.recv(4096))
        sock.send(JEqwwHNMplUHQfmnFPmPIJLLPpMZzJbE(ARCydHXqpuGGdfCuMzrSHXUKqtVApNIa))
    CbHagqpBcIpeEWUyuBbobjCzudqKrPsR = pow(JrpEhCiJhfWsaZKzcgwpfvSOoWOPuHYq, BydkDdrxdfAXrftvAKyrifGnDywBhZhq, xAjjXmPqxOqrzSvtOzBKwEqMKLHzWGeR)
    return SHA256.new(JEqwwHNMplUHQfmnFPmPIJLLPpMZzJbE(CbHagqpBcIpeEWUyuBbobjCzudqKrPsR)).digest()
def atPheiSoAtFBPAPiSWphKMBoMpifCYtC(uhyZegefhktFUkmnbgwJfMPMOwbpUFYa, KEY):
    uhyZegefhktFUkmnbgwJfMPMOwbpUFYa = COSPdDtulmRNzsGjqdoNlpJhnAwynuQQ(uhyZegefhktFUkmnbgwJfMPMOwbpUFYa)
    LDDmrKJdPyEBtPgEOyKXNjfXvWjOEMbD = Random.new().read(AES.block_size)
    dBXAjNCOhbXuqQcywrPrSMUBKzOreosf = AES.new(KEY, AES.MODE_CBC, LDDmrKJdPyEBtPgEOyKXNjfXvWjOEMbD)
    return LDDmrKJdPyEBtPgEOyKXNjfXvWjOEMbD + dBXAjNCOhbXuqQcywrPrSMUBKzOreosf.encrypt(uhyZegefhktFUkmnbgwJfMPMOwbpUFYa)
def JwCsVFlvwSXxzwZKpzKYaxboNPDvwiug(ciphertext, KEY):
    LDDmrKJdPyEBtPgEOyKXNjfXvWjOEMbD = ciphertext[:AES.block_size]
    dBXAjNCOhbXuqQcywrPrSMUBKzOreosf = AES.new(KEY, AES.MODE_CBC, LDDmrKJdPyEBtPgEOyKXNjfXvWjOEMbD)
    uhyZegefhktFUkmnbgwJfMPMOwbpUFYa = dBXAjNCOhbXuqQcywrPrSMUBKzOreosf.decrypt(ciphertext[AES.block_size:])
    return zOoSSCPRFcJgCcrCYloVGRTDqNDIvOFo(uhyZegefhktFUkmnbgwJfMPMOwbpUFYa)
