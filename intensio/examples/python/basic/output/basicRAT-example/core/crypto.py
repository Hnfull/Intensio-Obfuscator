# -*- coding: utf-8 -*-
import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from common import zIOxQZlnenuWSYqbIVXqqgLtmuKPgxYo, RTpaPIWpGpFABEwdbcAAskicSRoJdbYQ
XWShqxSRKrLAhKvUPMMnmAidPbUnBENx = 'b14ce95fa4c33ac2803782d18341869f'
class RKKFvMbjnFvndTgOIpLnNGqPHXejSunk(Exception):
    pass
def awMqkTQZunxAJzPcQyJqtXcJifhIUFNc(KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc, cCFGuJunGDEUvQBpWRCOYIAXTWGvsmNL=AES.block_size):
    GCUjyZRZOtbOdqlCfwkIcZIwUsqyTIGd = (cCFGuJunGDEUvQBpWRCOYIAXTWGvsmNL - (len(KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc) % cCFGuJunGDEUvQBpWRCOYIAXTWGvsmNL))
    return KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc + (chr(GCUjyZRZOtbOdqlCfwkIcZIwUsqyTIGd)*GCUjyZRZOtbOdqlCfwkIcZIwUsqyTIGd)
def OjylQcBPqLZoQnPClGRoHyjZBjuORvDK(KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc):
    GCUjyZRZOtbOdqlCfwkIcZIwUsqyTIGd = KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc[-1]
    if KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc.endswith(GCUjyZRZOtbOdqlCfwkIcZIwUsqyTIGd*ord(GCUjyZRZOtbOdqlCfwkIcZIwUsqyTIGd)):
        return KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc[:-ord(GCUjyZRZOtbOdqlCfwkIcZIwUsqyTIGd)]
    raise RKKFvMbjnFvndTgOIpLnNGqPHXejSunk("PKCS7 improper padding {}".format(repr(KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc[-32:])))
def BBaZpepdXruqObrkEWSXhfoFORKlTPhH(sock, server=True, bits=2048):
    SNKtiLJIQqMCbBMmyfEurVwFeDorNnxo = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF;
    UwOmCEKWXZgCaTfrADPzUOTyusaIhcSc = 2
    QKAdTJhxhmIIBLQTFBXDBCeJTszUZydo = RTpaPIWpGpFABEwdbcAAskicSRoJdbYQ(os.urandom(32))
    lwxnZpNjqoJMxhIFrkMXCjKqzzTxdrWC = pow(UwOmCEKWXZgCaTfrADPzUOTyusaIhcSc, QKAdTJhxhmIIBLQTFBXDBCeJTszUZydo, SNKtiLJIQqMCbBMmyfEurVwFeDorNnxo)
    if server:
        sock.send(zIOxQZlnenuWSYqbIVXqqgLtmuKPgxYo(lwxnZpNjqoJMxhIFrkMXCjKqzzTxdrWC))
        b = RTpaPIWpGpFABEwdbcAAskicSRoJdbYQ(sock.recv(4096))
    else:
        b = RTpaPIWpGpFABEwdbcAAskicSRoJdbYQ(sock.recv(4096))
        sock.send(zIOxQZlnenuWSYqbIVXqqgLtmuKPgxYo(lwxnZpNjqoJMxhIFrkMXCjKqzzTxdrWC))
    KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc = pow(b, QKAdTJhxhmIIBLQTFBXDBCeJTszUZydo, SNKtiLJIQqMCbBMmyfEurVwFeDorNnxo)
    return SHA256.new(zIOxQZlnenuWSYqbIVXqqgLtmuKPgxYo(KPIPZKXcEaYQIwVRGpzmYTezTDpMADpc)).digest()
def NWRhKgbNSvkvMUDnFuZRlBpUMUnJgApy(qhZvPnSjYFlNTqDrdngPzRrqxyCqrZQb, KEY):
    qhZvPnSjYFlNTqDrdngPzRrqxyCqrZQb = awMqkTQZunxAJzPcQyJqtXcJifhIUFNc(qhZvPnSjYFlNTqDrdngPzRrqxyCqrZQb)
    fiaXYnpqizAwzwNrsKyoajSOEilfKxxU = Random.new().read(AES.block_size)
    vzkzmHbrFiUQOXngPXjUXmdKPGazECLk = AES.new(KEY, AES.MODE_CBC, fiaXYnpqizAwzwNrsKyoajSOEilfKxxU)
    return fiaXYnpqizAwzwNrsKyoajSOEilfKxxU + vzkzmHbrFiUQOXngPXjUXmdKPGazECLk.encrypt(qhZvPnSjYFlNTqDrdngPzRrqxyCqrZQb)
def LTqWdFNAWGRrOFnEzPNXLrpSVbprqLyx(ciphertext, KEY):
    fiaXYnpqizAwzwNrsKyoajSOEilfKxxU = ciphertext[:AES.block_size]
    vzkzmHbrFiUQOXngPXjUXmdKPGazECLk = AES.new(KEY, AES.MODE_CBC, fiaXYnpqizAwzwNrsKyoajSOEilfKxxU)
    qhZvPnSjYFlNTqDrdngPzRrqxyCqrZQb = vzkzmHbrFiUQOXngPXjUXmdKPGazECLk.decrypt(ciphertext[AES.block_size:])
    return OjylQcBPqLZoQnPClGRoHyjZBjuORvDK(qhZvPnSjYFlNTqDrdngPzRrqxyCqrZQb)
