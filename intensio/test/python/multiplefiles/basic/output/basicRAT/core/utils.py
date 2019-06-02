# -*- coding: utf-8 -*-
from Crypto import Random
from Crypto.Cipher import AES
FDZJOzbZlEaOMIXDErBrZDIODBaeGYqr = 'bbc2d6c74c06f3403f425b7b107c2a07'
class OKFnZpuLIoJofWHZcXejiAyIffiMqHRo:
    def __init__(self):
        pass
    def zbYIvwdHBIbsVdlRVzLCXuHAEqetkrhD(self, PlrBJcHYEbLKfgUgAnkvPAhjuvGlTJhr):
        return PlrBJcHYEbLKfgUgAnkvPAhjuvGlTJhr + b'\0' * (AES.block_size - len(PlrBJcHYEbLKfgUgAnkvPAhjuvGlTJhr) % AES.block_size)
    def QIbNCccGvAWtRaFqgTqWYlOcWbLYpDqe(self, IMdkzbHxqqjhxbkMXpXBcLvAwSdXTViw):
        IMdkzbHxqqjhxbkMXpXBcLvAwSdXTViw = OKFnZpuLIoJofWHZcXejiAyIffiMqHRo.zbYIvwdHBIbsVdlRVzLCXuHAEqetkrhD(self, IMdkzbHxqqjhxbkMXpXBcLvAwSdXTViw)
        NKPkiReKJbluyfTgkmHBnaGcJFYTISTu = Random.new().read(AES.block_size)
        LuXWVwbqLNmYdDyQPXmVrCWDqinhbnzc = AES.new(FDZJOzbZlEaOMIXDErBrZDIODBaeGYqr, AES.MODE_CBC, NKPkiReKJbluyfTgkmHBnaGcJFYTISTu)
        return NKPkiReKJbluyfTgkmHBnaGcJFYTISTu + LuXWVwbqLNmYdDyQPXmVrCWDqinhbnzc.encrypt(IMdkzbHxqqjhxbkMXpXBcLvAwSdXTViw)
    def VGpMXRNguhNpETvZqAUNXQRSdFqIHikk(self, ciphertext):
        NKPkiReKJbluyfTgkmHBnaGcJFYTISTu = ciphertext[:AES.block_size]
        LuXWVwbqLNmYdDyQPXmVrCWDqinhbnzc = AES.new(FDZJOzbZlEaOMIXDErBrZDIODBaeGYqr, AES.MODE_CBC, NKPkiReKJbluyfTgkmHBnaGcJFYTISTu)
        IMdkzbHxqqjhxbkMXpXBcLvAwSdXTViw = LuXWVwbqLNmYdDyQPXmVrCWDqinhbnzc.decrypt(ciphertext[AES.block_size:])
        return IMdkzbHxqqjhxbkMXpXBcLvAwSdXTViw.rstrip(b'\0')
