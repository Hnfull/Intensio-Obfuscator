# -*- coding: utf-8 -*-
import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from common import cjWJPHhmHvOfdjCYBIZOITrlWvhfxxTn, svVkciCZRFfIjhmmHqXSsWhoUFxDvlwE
uUBuERckVPGVVmHCVIFwulDAONCCXHGi = 'b14ce95fa4c33ac2803782d18341869f'
class TtlqFHobRuHxbDhZtuWGuTkjaVurlauX(Exception):
    pass
def jtCbEXSxtKJCIKZopiVTDnxRvplergdA(NnAHEyzstOAhyDIxNvEBiZNNgIEkjaKT, rebEvpHIZfFttHfSqgXhlsUaSuKvngca=AES.block_size):
    TSDrrqyYNWidFcjDhHTyswywnlivHMNy = (rebEvpHIZfFttHfSqgXhlsUaSuKvngca - (len(NnAHEyzstOAhyDIxNvEBiZNNgIEkjaKT) % rebEvpHIZfFttHfSqgXhlsUaSuKvngca))
    return NnAHEyzstOAhyDIxNvEBiZNNgIEkjaKT + (chr(TSDrrqyYNWidFcjDhHTyswywnlivHMNy)*TSDrrqyYNWidFcjDhHTyswywnlivHMNy)
def WiToVrYpMsrLNYMrpjpuqvYhohTEXgLk(NnAHEyzstOAhyDIxNvEBiZNNgIEkjaKT):
    TSDrrqyYNWidFcjDhHTyswywnlivHMNy = NnAHEyzstOAhyDIxNvEBiZNNgIEkjaKT[-1]
    if NnAHEyzstOAhyDIxNvEBiZNNgIEkjaKT.endswith(TSDrrqyYNWidFcjDhHTyswywnlivHMNy*ord(TSDrrqyYNWidFcjDhHTyswywnlivHMNy)):
        return NnAHEyzstOAhyDIxNvEBiZNNgIEkjaKT[:-ord(TSDrrqyYNWidFcjDhHTyswywnlivHMNy)]
    raise TtlqFHobRuHxbDhZtuWGuTkjaVurlauX("PKCS7 improper padding {}".format(repr(NnAHEyzstOAhyDIxNvEBiZNNgIEkjaKT[-32:])))
def ejviyCNkcSZJfLMoBkJdCaGLsZpnMUmN(sock, VDmlsrDtexgyuVPCdUUHUFLHIfLGCbOF=True, bits=2048):
    PZwxtEhxIBMWmNPphOSinnBnZSiBAWjP = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF;
    WKBlNSFNoYwelfDYwDTnIhvSCutbKxmc = 2
    tNsFzGZkNTLFtUJqjeANdSmPXDdQBMZi = svVkciCZRFfIjhmmHqXSsWhoUFxDvlwE(os.urandom(32))
    iEDOsUtBVqlCCANVbvqQjEkBRZOVpwMV = pow(WKBlNSFNoYwelfDYwDTnIhvSCutbKxmc, tNsFzGZkNTLFtUJqjeANdSmPXDdQBMZi, PZwxtEhxIBMWmNPphOSinnBnZSiBAWjP)
    if VDmlsrDtexgyuVPCdUUHUFLHIfLGCbOF:
        sock.send(cjWJPHhmHvOfdjCYBIZOITrlWvhfxxTn(iEDOsUtBVqlCCANVbvqQjEkBRZOVpwMV))
        YIubVPuaZhSVDCOhuGJXHNrbNrtlCfsL = svVkciCZRFfIjhmmHqXSsWhoUFxDvlwE(sock.recv(4096))
    else:
        YIubVPuaZhSVDCOhuGJXHNrbNrtlCfsL = svVkciCZRFfIjhmmHqXSsWhoUFxDvlwE(sock.recv(4096))
        sock.send(cjWJPHhmHvOfdjCYBIZOITrlWvhfxxTn(iEDOsUtBVqlCCANVbvqQjEkBRZOVpwMV))
    NnAHEyzstOAhyDIxNvEBiZNNgIEkjaKT = pow(YIubVPuaZhSVDCOhuGJXHNrbNrtlCfsL, tNsFzGZkNTLFtUJqjeANdSmPXDdQBMZi, PZwxtEhxIBMWmNPphOSinnBnZSiBAWjP)
    return SHA256.new(cjWJPHhmHvOfdjCYBIZOITrlWvhfxxTn(NnAHEyzstOAhyDIxNvEBiZNNgIEkjaKT)).digest()
def yMJpVmADtfOFNuYBnBVUdcWvfJqpMgZu(HvSYeuwkbinaeSHdudKOXRkLAazbBDTd, KEY):
    HvSYeuwkbinaeSHdudKOXRkLAazbBDTd = jtCbEXSxtKJCIKZopiVTDnxRvplergdA(HvSYeuwkbinaeSHdudKOXRkLAazbBDTd)
    rtlGfEUYzDaGRuieoSoEUIAhcONbIsQU = Random.new().read(AES.block_size)
    AVMprCjbbKpczlcmriqrUbiMpuIbxrZb = AES.new(KEY, AES.MODE_CBC, rtlGfEUYzDaGRuieoSoEUIAhcONbIsQU)
    return rtlGfEUYzDaGRuieoSoEUIAhcONbIsQU + AVMprCjbbKpczlcmriqrUbiMpuIbxrZb.encrypt(HvSYeuwkbinaeSHdudKOXRkLAazbBDTd)
def bWtlivskZCwkkAfMYrPiAvIokwvvoWcD(ciphertext, KEY):
    rtlGfEUYzDaGRuieoSoEUIAhcONbIsQU = ciphertext[:AES.block_size]
    AVMprCjbbKpczlcmriqrUbiMpuIbxrZb = AES.new(KEY, AES.MODE_CBC, rtlGfEUYzDaGRuieoSoEUIAhcONbIsQU)
    HvSYeuwkbinaeSHdudKOXRkLAazbBDTd = AVMprCjbbKpczlcmriqrUbiMpuIbxrZb.decrypt(ciphertext[AES.block_size:])
    return WiToVrYpMsrLNYMrpjpuqvYhohTEXgLk(HvSYeuwkbinaeSHdudKOXRkLAazbBDTd)
