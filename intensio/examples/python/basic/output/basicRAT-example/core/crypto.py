# -*- coding: utf-8 -*-
import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from common import SNYDucfxYRhXDMuRJTDBCRnAkWNYSZBi, eCYwFUxuSOdzxlFJDXYkjfnEbtTZqEYg
NMraSVcvniQVJXqQpblxxHjwemfblPuc = 'b14ce95fa4c33ac2803782d18341869f'
class FbqdGhpbphqCOgKKzPeyIPMzoOAZuZoN(Exception):
    pass
def ghyswoXOfdunUcAShgjtFCukxwToMDzW(hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd, uhKbXIobsxIiifCMGPRzFNBHQAeJupJM=AES.block_size):
    kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs = (uhKbXIobsxIiifCMGPRzFNBHQAeJupJM - (len(hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd) % uhKbXIobsxIiifCMGPRzFNBHQAeJupJM))
    return hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd + (chr(kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs)*kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs)
def TNGOFiOIxhKYNPuXjlGCLVdzOuSuAuWn(hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd):
    kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs = hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd[-1]
    if hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd.endswith(kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs*ord(kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs)):
        return hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd[:-ord(kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs)]
    raise FbqdGhpbphqCOgKKzPeyIPMzoOAZuZoN("PKCS7 improper padding {}".format(repr(hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd[-32:])))
def GmCEpXaBzxpjGMiONYNnyrBNiwXoeFeX(sock, server=True, bits=2048):
    EbeRdzCAZECWPggcgqfQTNGJQAHVkhaL = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF;
    xmFrBlZJgnbFkUfIFBzOHEQSFhPkoGdg = 2
    FqjTVDtVVBnsDoOPQuzPyWSOWIMziGTk = eCYwFUxuSOdzxlFJDXYkjfnEbtTZqEYg(os.urandom(32))
    ygMUkMVpflZNdoolgYYHLSzmWyMzMkSD = pow(xmFrBlZJgnbFkUfIFBzOHEQSFhPkoGdg, FqjTVDtVVBnsDoOPQuzPyWSOWIMziGTk, EbeRdzCAZECWPggcgqfQTNGJQAHVkhaL)
    if server:
        sock.send(SNYDucfxYRhXDMuRJTDBCRnAkWNYSZBi(ygMUkMVpflZNdoolgYYHLSzmWyMzMkSD))
        b = eCYwFUxuSOdzxlFJDXYkjfnEbtTZqEYg(sock.recv(4096))
    else:
        b = eCYwFUxuSOdzxlFJDXYkjfnEbtTZqEYg(sock.recv(4096))
        sock.send(SNYDucfxYRhXDMuRJTDBCRnAkWNYSZBi(ygMUkMVpflZNdoolgYYHLSzmWyMzMkSD))
    hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd = pow(b, FqjTVDtVVBnsDoOPQuzPyWSOWIMziGTk, EbeRdzCAZECWPggcgqfQTNGJQAHVkhaL)
    return SHA256.new(SNYDucfxYRhXDMuRJTDBCRnAkWNYSZBi(hiloaptHmfBAMuDQCBVzsgNTKBsQiGsd)).digest()
def nWfpHMtglmECQdQYhOJEvgLDLAxncADh(gMOOMtqMIioNTEKvTvNRKJJWCoPpkpjT, KEY):
    gMOOMtqMIioNTEKvTvNRKJJWCoPpkpjT = ghyswoXOfdunUcAShgjtFCukxwToMDzW(gMOOMtqMIioNTEKvTvNRKJJWCoPpkpjT)
    eRKKNGnbXSeTlruoQGbihNVzcGvsowXt = Random.new().read(AES.block_size)
    BILumfNzNskgHDbYIMSzWxBVqRhZNqFk = AES.new(KEY, AES.MODE_CBC, eRKKNGnbXSeTlruoQGbihNVzcGvsowXt)
    return eRKKNGnbXSeTlruoQGbihNVzcGvsowXt + BILumfNzNskgHDbYIMSzWxBVqRhZNqFk.encrypt(gMOOMtqMIioNTEKvTvNRKJJWCoPpkpjT)
def PVayTxzTsXuVHdaTbmvmjjKYIcPvDCfp(ciphertext, KEY):
    eRKKNGnbXSeTlruoQGbihNVzcGvsowXt = ciphertext[:AES.block_size]
    BILumfNzNskgHDbYIMSzWxBVqRhZNqFk = AES.new(KEY, AES.MODE_CBC, eRKKNGnbXSeTlruoQGbihNVzcGvsowXt)
    gMOOMtqMIioNTEKvTvNRKJJWCoPpkpjT = BILumfNzNskgHDbYIMSzWxBVqRhZNqFk.decrypt(ciphertext[AES.block_size:])
    return TNGOFiOIxhKYNPuXjlGCLVdzOuSuAuWn(gMOOMtqMIioNTEKvTvNRKJJWCoPpkpjT)
