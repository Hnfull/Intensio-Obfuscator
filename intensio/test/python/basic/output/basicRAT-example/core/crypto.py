# -*- coding: utf-8 -*-
import os
from Crypto import Random
from Crypto.Cipher import AES
from Crypto.Hash import SHA256
from common import tPXpCyYrbgDpBZclRpvsxwiCChsjWnpt, lbMazLjEhxnLSxcWBhYuCfylEwUYSQJB
iwzlVGUCpvcblcdfDUsxWbvDJsgQRlnf = 'b14ce95fa4c33ac2803782d18341869f'
class AMHZdPguEdgvyVsLCpUyHQfTzAQvqEWg(Exception):
    pass
def GCkmtidJcoFmELwVGnmQoBGgnAsxpUlL(rknKsknmzbgZguxvPWfDZEbmXwXYtPjR, hQyGwmoVHImpkNwwVJZOFszFVkWqesYS=AES.block_size):
    jPdTGopJITvbSMDmzXVqrGvkRpQKswKQ = (hQyGwmoVHImpkNwwVJZOFszFVkWqesYS - (len(rknKsknmzbgZguxvPWfDZEbmXwXYtPjR) % hQyGwmoVHImpkNwwVJZOFszFVkWqesYS))
    return rknKsknmzbgZguxvPWfDZEbmXwXYtPjR + (chr(jPdTGopJITvbSMDmzXVqrGvkRpQKswKQ)*jPdTGopJITvbSMDmzXVqrGvkRpQKswKQ)
def XPJzImEbesjgibAkmoizcTPitConIdFY(rknKsknmzbgZguxvPWfDZEbmXwXYtPjR):
    jPdTGopJITvbSMDmzXVqrGvkRpQKswKQ = rknKsknmzbgZguxvPWfDZEbmXwXYtPjR[-1]
    if rknKsknmzbgZguxvPWfDZEbmXwXYtPjR.endswith(jPdTGopJITvbSMDmzXVqrGvkRpQKswKQ*ord(jPdTGopJITvbSMDmzXVqrGvkRpQKswKQ)):
        return rknKsknmzbgZguxvPWfDZEbmXwXYtPjR[:-ord(jPdTGopJITvbSMDmzXVqrGvkRpQKswKQ)]
    raise AMHZdPguEdgvyVsLCpUyHQfTzAQvqEWg("PKCS7 improper padding {}".format(repr(rknKsknmzbgZguxvPWfDZEbmXwXYtPjR[-32:])))
def jkwBfxODkQDCazFRAKanySiAKxsUUphC(sock, PRCpieHPxysMjIISVuZIBnRlzYOUGeMe=True, bits=2048):
    CcvvDNfZOWCoPpeadrBYYzfQWvyJNQiO = 0xFFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE45B3DC2007CB8A163BF0598DA48361C55D39A69163FA8FD24CF5F83655D23DCA3AD961C62F356208552BB9ED529077096966D670C354E4ABC9804F1746C08CA18217C32905E462E36CE3BE39E772C180E86039B2783A2EC07A28FB5C55DF06F4C52C9DE2BCBF6955817183995497CEA956AE515D2261898FA051015728E5A8AACAA68FFFFFFFFFFFFFFFF;
    EMLFyDubKFLHdUvqLJKWmNyrendbLSsD = 2
    rGLazmPjwuKkihYLXVFSuAXjQJMYONbU = lbMazLjEhxnLSxcWBhYuCfylEwUYSQJB(os.urandom(32))
    wxiVvvarcKKrTHwodDsUWmKzzjIEOdPX = pow(EMLFyDubKFLHdUvqLJKWmNyrendbLSsD, rGLazmPjwuKkihYLXVFSuAXjQJMYONbU, CcvvDNfZOWCoPpeadrBYYzfQWvyJNQiO)
    if PRCpieHPxysMjIISVuZIBnRlzYOUGeMe:
        sock.send(tPXpCyYrbgDpBZclRpvsxwiCChsjWnpt(wxiVvvarcKKrTHwodDsUWmKzzjIEOdPX))
        SLZLwkDlSWngtZXvjHpmdKLlWnzMJUYs = lbMazLjEhxnLSxcWBhYuCfylEwUYSQJB(sock.recv(4096))
    else:
        SLZLwkDlSWngtZXvjHpmdKLlWnzMJUYs = lbMazLjEhxnLSxcWBhYuCfylEwUYSQJB(sock.recv(4096))
        sock.send(tPXpCyYrbgDpBZclRpvsxwiCChsjWnpt(wxiVvvarcKKrTHwodDsUWmKzzjIEOdPX))
    rknKsknmzbgZguxvPWfDZEbmXwXYtPjR = pow(SLZLwkDlSWngtZXvjHpmdKLlWnzMJUYs, rGLazmPjwuKkihYLXVFSuAXjQJMYONbU, CcvvDNfZOWCoPpeadrBYYzfQWvyJNQiO)
    return SHA256.new(tPXpCyYrbgDpBZclRpvsxwiCChsjWnpt(rknKsknmzbgZguxvPWfDZEbmXwXYtPjR)).digest()
def SKKkrmGLAJRDTUbwjJLaYtKBVMQbZzJS(PWKfVmUtHTYtKCOHeDHMAgPNZBKAMKEo, KEY):
    PWKfVmUtHTYtKCOHeDHMAgPNZBKAMKEo = GCkmtidJcoFmELwVGnmQoBGgnAsxpUlL(PWKfVmUtHTYtKCOHeDHMAgPNZBKAMKEo)
    gKfPAZsvHJQtHnLJzvmomAMRRtHXlvKn = Random.new().read(AES.block_size)
    AoqTNgrQjDcagVGAUrwtKyGGOYFfjFvW = AES.new(KEY, AES.MODE_CBC, gKfPAZsvHJQtHnLJzvmomAMRRtHXlvKn)
    return gKfPAZsvHJQtHnLJzvmomAMRRtHXlvKn + AoqTNgrQjDcagVGAUrwtKyGGOYFfjFvW.encrypt(PWKfVmUtHTYtKCOHeDHMAgPNZBKAMKEo)
def YRziRmEPPXlBbFMWPzvDXHZlVuNCrPBT(ciphertext, KEY):
    gKfPAZsvHJQtHnLJzvmomAMRRtHXlvKn = ciphertext[:AES.block_size]
    AoqTNgrQjDcagVGAUrwtKyGGOYFfjFvW = AES.new(KEY, AES.MODE_CBC, gKfPAZsvHJQtHnLJzvmomAMRRtHXlvKn)
    PWKfVmUtHTYtKCOHeDHMAgPNZBKAMKEo = AoqTNgrQjDcagVGAUrwtKyGGOYFfjFvW.decrypt(ciphertext[AES.block_size:])
    return XPJzImEbesjgibAkmoizcTPitConIdFY(PWKfVmUtHTYtKCOHeDHMAgPNZBKAMKEo)
