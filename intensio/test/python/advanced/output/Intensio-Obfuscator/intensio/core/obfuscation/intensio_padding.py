# -*- coding: utf-8 -*-
import fileinput
import random
import textwrap
import re
import glob
from tqdm import tqdm
from core.obfuscation.intensio_mixer import Mixer
from core.obfuscation.intensio_remove import Remove
from core.utils.intensio_utils import Utils
from core.utils.intensio_error import EXIT_SUCCESS, EXIT_FAILURE, ERROR_BAD_ARGUMENTS
class Padding:
    def __init__(self):
        self.mixer  = Mixer()
        self.remove = Remove()
        self.utils  = Utils()
    def ScriptsGenerator(self, codeArg, mixerLevelArg):
        if mixerLevelArg == "lower":
            varRandom1   = self.mixer.GetStringMixer("lower")
            varRandom2   = self.mixer.GetStringMixer("lower")
            varRandom3   = self.mixer.GetStringMixer("lower")
            varRandom4   = self.mixer.GetStringMixer("lower")
            varRandom5   = self.mixer.GetStringMixer("lower")
            varRandom6   = self.mixer.GetStringMixer("lower")
            varRandom7   = self.mixer.GetStringMixer("lower")
            varRandom8   = self.mixer.GetStringMixer("lower")
            varRandom9   = self.mixer.GetStringMixer("lower")
            varRandom10  = self.mixer.GetStringMixer("lower")
            varRandom11  = self.mixer.GetStringMixer("lower")
            varRandom12  = self.mixer.GetStringMixer("lower")
        elif mixerLevelArg == "medium":
            varRandom1   = self.mixer.GetStringMixer("medium")
            varRandom2   = self.mixer.GetStringMixer("medium")
            varRandom3   = self.mixer.GetStringMixer("medium")
            varRandom4   = self.mixer.GetStringMixer("medium")
            varRandom5   = self.mixer.GetStringMixer("medium")
            varRandom6   = self.mixer.GetStringMixer("medium")
            varRandom7   = self.mixer.GetStringMixer("medium")
            varRandom8   = self.mixer.GetStringMixer("medium")
            varRandom9   = self.mixer.GetStringMixer("medium")
            varRandom10  = self.mixer.GetStringMixer("medium")
            varRandom11  = self.mixer.GetStringMixer("medium")
            varRandom12  = self.mixer.GetStringMixer("medium")
        elif mixerLevelArg == "high":
            varRandom1   = self.mixer.GetStringMixer("high")
            varRandom2   = self.mixer.GetStringMixer("high")
            varRandom3   = self.mixer.GetStringMixer("high")
            varRandom4   = self.mixer.GetStringMixer("high")
            varRandom5   = self.mixer.GetStringMixer("high")
            varRandom6   = self.mixer.GetStringMixer("high")
            varRandom7   = self.mixer.GetStringMixer("high")
            varRandom8   = self.mixer.GetStringMixer("high")
            varRandom9   = self.mixer.GetStringMixer("high")
            varRandom10  = self.mixer.GetStringMixer("high")
            varRandom11  = self.mixer.GetStringMixer("high")
            varRandom12  = self.mixer.GetStringMixer("high")
        if codeArg == "python":
            rand = random.randint(1, 5)
            if rand == 1:
                XmLoBbEZvHxLpaPsjhlXFuvhRsRfbraA = textwrap.dedent("""
                                                    {0} = '{5}'
                                                    {1} = '{6}'
                                                    {2} = '{7}'
                                                    {3} = '{8}'
                                                    {4} = '{9}'
                                                    if {0} in {1}:
                                                        {0} = {4}
                                                        if {1} in {2}:
                                                            {1} = {3}
                                                    elif {1} in {0}:
                                                        {2} = {1}
                                                        if {2} in {1}:
                                                            {1} = {4}
                                                    """).format(varRandom1, varRandom2, varRandom3, varRandom4, varRandom5, \
                                                                varRandom6, varRandom7, varRandom8, varRandom9, varRandom10)
                return scriptAssPadding1
            kUxzHeADCYTNJkESTShAUzJIgnOnpOpp = 'qMDIFhitHOjKtspciLOeknQRuIdAwEfT'
            wzyOHfHzCIWnUGgNfAJxWvucTdgDOzXX = 'UqvDuVmlYOjGanYDKMcJmRyZGoUILuPv'
            NBtWshmLmSOtwNoaHXNnbraottOgvQhr = 'FDrGrQEKClZQjojILZvtIEYzycDrfpfx'
            if kUxzHeADCYTNJkESTShAUzJIgnOnpOpp == wzyOHfHzCIWnUGgNfAJxWvucTdgDOzXX:
                TyppHqJtpimkxQvZCseAeNwAuAmAsLeK = 'akMgBlaOcwJUihJPajucRbSLkbFtACNF'
                TyppHqJtpimkxQvZCseAeNwAuAmAsLeK = kUxzHeADCYTNJkESTShAUzJIgnOnpOpp
            else:
                TyppHqJtpimkxQvZCseAeNwAuAmAsLeK = 'akMgBlaOcwJUihJPajucRbSLkbFtACNF'
                TyppHqJtpimkxQvZCseAeNwAuAmAsLeK = NBtWshmLmSOtwNoaHXNnbraottOgvQhr
            elif rand == 2:
                vyjfKBTNIjvshHZIXJTtDphfUwArDJJa = 'TOFPmJkbcVfGerEayDSsimTlNayKXVGf'
                dYlbSoClrxKhQMjLstOhFlKYuQIWvPPG = 'ocUMDWZTNDfQHaLhoRzmNzadQGlcvCVF'
                ZgPCaMudhjdZrgmXLMWGoyLZMhHPYVLY = 'WNYWMballptgegMBiBfOqljBPZbaOqVm'
                zBTptlqRdHnExmpMFHgpOMOTrJzhdoNU = 'uAAkbCXpkgSmBiatLTOhOuanlpMPiKVR'
                DdZvtoplcpMZcHDdvtdJsmWhWcaBLbWZ = 'RdzAxGEwAxyibTAtCtNqqGQOcfkuLcnP'
                YXxBkvGaJCOcWBlpJOuAXxTgvdpTjwAj = 'kdGmvhyLTMJiFxvVocYCwVfuYjIqnVcl'
                if vyjfKBTNIjvshHZIXJTtDphfUwArDJJa != zBTptlqRdHnExmpMFHgpOMOTrJzhdoNU:
                    dYlbSoClrxKhQMjLstOhFlKYuQIWvPPG = ZgPCaMudhjdZrgmXLMWGoyLZMhHPYVLY
                    for YXxBkvGaJCOcWBlpJOuAXxTgvdpTjwAj in zBTptlqRdHnExmpMFHgpOMOTrJzhdoNU:
                        if YXxBkvGaJCOcWBlpJOuAXxTgvdpTjwAj != ZgPCaMudhjdZrgmXLMWGoyLZMhHPYVLY:
                            dYlbSoClrxKhQMjLstOhFlKYuQIWvPPG = dYlbSoClrxKhQMjLstOhFlKYuQIWvPPG
                        else:
                            DdZvtoplcpMZcHDdvtdJsmWhWcaBLbWZ = vyjfKBTNIjvshHZIXJTtDphfUwArDJJa
                else:
                    ZgPCaMudhjdZrgmXLMWGoyLZMhHPYVLY = vyjfKBTNIjvshHZIXJTtDphfUwArDJJa
                    vyjfKBTNIjvshHZIXJTtDphfUwArDJJa = DdZvtoplcpMZcHDdvtdJsmWhWcaBLbWZ
                    if ZgPCaMudhjdZrgmXLMWGoyLZMhHPYVLY == vyjfKBTNIjvshHZIXJTtDphfUwArDJJa:
                        for YXxBkvGaJCOcWBlpJOuAXxTgvdpTjwAj in vyjfKBTNIjvshHZIXJTtDphfUwArDJJa:
                            if YXxBkvGaJCOcWBlpJOuAXxTgvdpTjwAj == ZgPCaMudhjdZrgmXLMWGoyLZMhHPYVLY:
                                ZgPCaMudhjdZrgmXLMWGoyLZMhHPYVLY = vyjfKBTNIjvshHZIXJTtDphfUwArDJJa
                            else:
                                ZgPCaMudhjdZrgmXLMWGoyLZMhHPYVLY = DdZvtoplcpMZcHDdvtdJsmWhWcaBLbWZ
                EdCYlrsfHvSxlUQRkHrMfFwzbtjhXGkH = textwrap.dedent("""
                                                    {0} = '{4}'
                                                    {1} = '{5}'
                                                    if {0} != {1}:
                                                        {2} = '{6}'
                                                        {3} = '{7}'
                                                        {3} = {2}
                                                    """).format(varRandom1, varRandom2, varRandom3, varRandom4, varRandom5, \
                                                                varRandom6, varRandom7, varRandom8)
                return scriptAssPadding2
            elif rand == 3:
                ZZhdnBsQqNJYyTtRoXjBeRvKaTxtooqN = textwrap.dedent("""
                                                    {0} = '{6}'
                                                    {1} = '{7}'
                                                    {2} = '{8}'
                                                    {3} = '{9}'
                                                    {4} = '{10}'
                                                    {5} = '{11}'
                                                    if {0} != {3}:
                                                        {1} = {2}
                                                        for {5} in {3}:
                                                            if {5} != {2}:
                                                                {1} = {1}
                                                            else:
                                                                {4} = {0}
                                                    else:
                                                        {2} = {0}
                                                        {0} = {4}
                                                        if {2} == {0}:
                                                            for {5} in {0}:
                                                                if {5} == {2}:
                                                                    {2} = {0}
                                                                else:
                                                                    {2} = {4}
                                                    """).format(varRandom1, varRandom2, varRandom3, varRandom4, varRandom5, varRandom6, \
                                                                varRandom7, varRandom8, varRandom9, varRandom10, varRandom11, varRandom12)
                return scriptAssPadding3
            drditbJMBdcSMRzMMkAlOyVxhLviFHmS = 'aJLYlRYIhzDSrErPyxXyvyQusLSvTTBF'
            xLFbmRPDrIFAKFIzOoxthpCZOtCoCtLu = 'ctdplpWIAEcKFyCNvxJWAoJSPuAGHgmz'
            if drditbJMBdcSMRzMMkAlOyVxhLviFHmS != xLFbmRPDrIFAKFIzOoxthpCZOtCoCtLu:
                wHqZZerYddGyZkAfQcSIoNxdgTQCiaca = 'NkrjNooaoKTXrMmvhvlaUwiDZwzhzCfu'
                woLmXhJtAziTzOtygXwDZNKBorDCBCNQ = 'QxiwYwjjCUxoIUCTiGvRcktaGAJwpGRk'
                woLmXhJtAziTzOtygXwDZNKBorDCBCNQ = wHqZZerYddGyZkAfQcSIoNxdgTQCiaca
            elif rand == 4:
                wkngzXohqYSJNQbTIgyEcDtbEwuGkQAM = 'mRNrFaLnSHvBrIUpvUPmVVlcrFWvuwVK'
                sXjpxJiNCUqQfEnmjHwxxpYQYDHIENyJ = 'WRQHCltbseLPczCQKbrKTfVtRAembQxr'
                NmQJQgwfNRbCiYHZLMOkCmwUSTQBNMFN = 'QbsTIwJRlQIlTeoeDueiyUTODLHYMSZl'
                jbuvdfLFjIJkJFhPXwxslPPAohDebhLD = 'QjErojQnobKkuBuluSldFHzMcALGXXPk'
                UkOUcWDxjWVeIEzzuhCmIsyJLhictUqb = 'yNrmIqsCKVNuVIKdEDcAuidmDmrsnwUs'
                vLqXpnHsKXZFtVkhRZlRLJJiRZqFIvjX = 'dtvUuNGEAMJIODrhICFicfkqXgtFuGqi'
                if NmQJQgwfNRbCiYHZLMOkCmwUSTQBNMFN == jbuvdfLFjIJkJFhPXwxslPPAohDebhLD:
                    for vLqXpnHsKXZFtVkhRZlRLJJiRZqFIvjX in UkOUcWDxjWVeIEzzuhCmIsyJLhictUqb:
                        if vLqXpnHsKXZFtVkhRZlRLJJiRZqFIvjX == jbuvdfLFjIJkJFhPXwxslPPAohDebhLD:
                            UkOUcWDxjWVeIEzzuhCmIsyJLhictUqb = wkngzXohqYSJNQbTIgyEcDtbEwuGkQAM
                        else:
                            jbuvdfLFjIJkJFhPXwxslPPAohDebhLD = sXjpxJiNCUqQfEnmjHwxxpYQYDHIENyJ
                UeGesyMDhYdAurjeIYHFhCwExEEqQSvd = textwrap.dedent("""
                                                    {0} = '{4}'
                                                    {1} = '{5}'
                                                    {3} = '{7}'
                                                    if {0} == {1}:
                                                        {2} = '{6}'
                                                        {2} = {0}
                                                    else:
                                                        {2} = '{6}'
                                                        {2} = {3}
                                                    """).format(varRandom1, varRandom2, varRandom3, varRandom4, \
                                                                varRandom5, varRandom6, varRandom7, varRandom8)
                return scriptAssPadding4
            elif rand == 5:
                NsSNnPZrryaurGXTMOAJcoDIQFOatcZF = textwrap.dedent("""
                                                    {0} = '{6}'
                                                    {1} = '{7}'
                                                    {2} = '{8}'
                                                    {3} = '{9}'
                                                    {4} = '{10}'
                                                    {5} = '{11}'
                                                    if {2} == {3}:
                                                        for {5} in {4}:
                                                            if {5} == {3}:
                                                                {4} = {0}
                                                            else:
                                                                {3} = {1}
                                                    """).format(varRandom1, varRandom2, varRandom3, \
                                                        varRandom4, varRandom5, varRandom6, \
                                                        varRandom7, varRandom8, varRandom9, \
                                                        varRandom10, varRandom11, varRandom12)
                return scriptAssPadding5
    def AddScripts(self, codeArg, outputArg, mixerLevelArg):
        jeTaEmipUtCUCkgIvSlkdtAzLvguZnKy = 'LsKDADVvcghwJjXkDIOZGkRNOVUnvoSi'
        sEOEuvZoiIvRbnRVTBPkoiYEfMbegUQq = 'mmBPWdVzPOekTkVbOtjrEXpkMRzSueyU'
        if jeTaEmipUtCUCkgIvSlkdtAzLvguZnKy != sEOEuvZoiIvRbnRVTBPkoiYEfMbegUQq:
            JbOdyrfSBEDeatswSJnGDBCHkbhKcSIF = 'xsBxPwxIoVxXMeVTDZDRRPnoOHffOMrq'
            CGFVeLTfOZRoGmWCDeRMLXenYcZMiupM = 'LWEcFfEXFUkAHMoyLwvWJsAccoPjpUwu'
            CGFVeLTfOZRoGmWCDeRMLXenYcZMiupM = JbOdyrfSBEDeatswSJnGDBCHkbhKcSIF
        countScriptsAdded   = 0
        UxFmTARrHaMuVPZCBQdZPhRzHALfjJNo = 'oybSkxugYMeZmijExLRhXTUKxgAfouVx'
        ZtIcXOwHZMZQuesJFnAjXkElnyawzpAb = 'ZQSQsXWTEoeQnGPUHfnOFOwEcDEbAHhj'
        qSlDxQQvZxtmHHfXfuiViLdSyOoRiXLI = 'MyyjyMGtEazIWRtxhworQgFHVTnDFUcQ'
        LwRXxoIBqVjfQiMNchUdJvppsJEfRjwh = 'xgiXgawHeuffKvZAweVWxAqpYjZnoOzK'
        yDNrIHPwSYfXPqDgXOTaFqIgLDFimMyF = 'GnyYvzSQQtsZjbBSwNCfqitxKCQsTsTG'
        if UxFmTARrHaMuVPZCBQdZPhRzHALfjJNo in ZtIcXOwHZMZQuesJFnAjXkElnyawzpAb:
            UxFmTARrHaMuVPZCBQdZPhRzHALfjJNo = yDNrIHPwSYfXPqDgXOTaFqIgLDFimMyF
            if ZtIcXOwHZMZQuesJFnAjXkElnyawzpAb in qSlDxQQvZxtmHHfXfuiViLdSyOoRiXLI:
                ZtIcXOwHZMZQuesJFnAjXkElnyawzpAb = LwRXxoIBqVjfQiMNchUdJvppsJEfRjwh
        elif ZtIcXOwHZMZQuesJFnAjXkElnyawzpAb in UxFmTARrHaMuVPZCBQdZPhRzHALfjJNo:
            qSlDxQQvZxtmHHfXfuiViLdSyOoRiXLI = ZtIcXOwHZMZQuesJFnAjXkElnyawzpAb
            if qSlDxQQvZxtmHHfXfuiViLdSyOoRiXLI in ZtIcXOwHZMZQuesJFnAjXkElnyawzpAb:
                ZtIcXOwHZMZQuesJFnAjXkElnyawzpAb = yDNrIHPwSYfXPqDgXOTaFqIgLDFimMyF
        countLineAdded      = 0
        DCTzCgMJtFqZHJsTwTiipxcPNqdydAaM = 'xmOVXDlQdFvILLCdQHaWGQgfwnJMcPBV'
        MJWAWlLDnfhUcudZjSRnPVDNdoKEIXam = 'QfbzTOzxjVFctEEniTWQGmVBygZSyaYj'
        cknnNUUGrmdgHkPPcffZlZluUsAxWJrU = 'shzUwbTYGKFvSUKrCGyWsYkSyCuzvTwk'
        YDXGKLCbHIOdIjsGAABIJRhpUrqFPKKX = 'XtmkvdSJcUkhUEBOPwuQMxXbnWMbSihc'
        mMfYmnHIuVLBhkaEkbIyeFDnCAFLygpd = 'JPaDLJSmVNzNdYTnemBGHCNFDepTHuAF'
        if DCTzCgMJtFqZHJsTwTiipxcPNqdydAaM in MJWAWlLDnfhUcudZjSRnPVDNdoKEIXam:
            DCTzCgMJtFqZHJsTwTiipxcPNqdydAaM = mMfYmnHIuVLBhkaEkbIyeFDnCAFLygpd
            if MJWAWlLDnfhUcudZjSRnPVDNdoKEIXam in cknnNUUGrmdgHkPPcffZlZluUsAxWJrU:
                MJWAWlLDnfhUcudZjSRnPVDNdoKEIXam = YDXGKLCbHIOdIjsGAABIJRhpUrqFPKKX
        elif MJWAWlLDnfhUcudZjSRnPVDNdoKEIXam in DCTzCgMJtFqZHJsTwTiipxcPNqdydAaM:
            cknnNUUGrmdgHkPPcffZlZluUsAxWJrU = MJWAWlLDnfhUcudZjSRnPVDNdoKEIXam
            if cknnNUUGrmdgHkPPcffZlZluUsAxWJrU in MJWAWlLDnfhUcudZjSRnPVDNdoKEIXam:
                MJWAWlLDnfhUcudZjSRnPVDNdoKEIXam = mMfYmnHIuVLBhkaEkbIyeFDnCAFLygpd
        countLine           = 0
        tIsxVKbumlyqLmYeveEEYNNIibCEoLEs = 'KKOhQvAqsAhWpzPHWZVmPagPinMTuYiU'
        VOPbJHhFnVSwOLQCuPxNLbdmfpKtShxd = 'jkPfnFrJNzqWYppZtHFnEajAvsUXirXU'
        LqTZgFbsGxPAsXmPsgWbVYCSeySKTWgQ = 'ksLIXpYXNJGmrCwcVPzOieSgMqJmRNHC'
        XgAlzroIcEQtqldBGtDXBiiiLyGhzSWN = 'ajayTLTYOcZRrJgcywkkQOhJSinVaJsx'
        WwTLdQdDJrHYAFKyeBILPPcPVKiRNdex = 'VpfQmzCGKUQjVnRrUVQeMeswszNQaRnN'
        eqXzolwJCCZvUUwDxgwrPBnmRhvdlhyy = 'HIUCYmRlAKdRDgISftAIqYUgmGOAihjG'
        if tIsxVKbumlyqLmYeveEEYNNIibCEoLEs != XgAlzroIcEQtqldBGtDXBiiiLyGhzSWN:
            VOPbJHhFnVSwOLQCuPxNLbdmfpKtShxd = LqTZgFbsGxPAsXmPsgWbVYCSeySKTWgQ
            for eqXzolwJCCZvUUwDxgwrPBnmRhvdlhyy in XgAlzroIcEQtqldBGtDXBiiiLyGhzSWN:
                if eqXzolwJCCZvUUwDxgwrPBnmRhvdlhyy != LqTZgFbsGxPAsXmPsgWbVYCSeySKTWgQ:
                    VOPbJHhFnVSwOLQCuPxNLbdmfpKtShxd = VOPbJHhFnVSwOLQCuPxNLbdmfpKtShxd
                else:
                    WwTLdQdDJrHYAFKyeBILPPcPVKiRNdex = tIsxVKbumlyqLmYeveEEYNNIibCEoLEs
        else:
            LqTZgFbsGxPAsXmPsgWbVYCSeySKTWgQ = tIsxVKbumlyqLmYeveEEYNNIibCEoLEs
            tIsxVKbumlyqLmYeveEEYNNIibCEoLEs = WwTLdQdDJrHYAFKyeBILPPcPVKiRNdex
            if LqTZgFbsGxPAsXmPsgWbVYCSeySKTWgQ == tIsxVKbumlyqLmYeveEEYNNIibCEoLEs:
                for eqXzolwJCCZvUUwDxgwrPBnmRhvdlhyy in tIsxVKbumlyqLmYeveEEYNNIibCEoLEs:
                    if eqXzolwJCCZvUUwDxgwrPBnmRhvdlhyy == LqTZgFbsGxPAsXmPsgWbVYCSeySKTWgQ:
                        LqTZgFbsGxPAsXmPsgWbVYCSeySKTWgQ = tIsxVKbumlyqLmYeveEEYNNIibCEoLEs
                    else:
                        LqTZgFbsGxPAsXmPsgWbVYCSeySKTWgQ = WwTLdQdDJrHYAFKyeBILPPcPVKiRNdex
        checkLine           = 0
        fPdmOkmJMAgcALMiUPvRNoWvCftYDJDb = 'klAdkOUtOfVbZnUIllgHZzZHvSopbPQR'
        JFAEyBaJIPkMKehKJwmAsYRjFBCoytQY = 'HdJIvqyvTIEQwZKNIYxKZSTDsMwjEqAt'
        VcfPjkOQVHbsdQEzcFZdcBTNVEHmodBD = 'SeGeKGPYzjFfgMwSVWVcSxNfGGNQQcJe'
        tOvDvKtvMgDywkRLNfxtjmPNxiFnriee = 'vWitUDfVPSLNuTfKzBvOFVVlEKgenlPn'
        qQdvRCGBVUJWeZtcqqXFgZPtsNEcpKNX = 'qmRgvTRwAfPnznPkTpFxIgjIiZrMeGdQ'
        if fPdmOkmJMAgcALMiUPvRNoWvCftYDJDb in JFAEyBaJIPkMKehKJwmAsYRjFBCoytQY:
            fPdmOkmJMAgcALMiUPvRNoWvCftYDJDb = qQdvRCGBVUJWeZtcqqXFgZPtsNEcpKNX
            if JFAEyBaJIPkMKehKJwmAsYRjFBCoytQY in VcfPjkOQVHbsdQEzcFZdcBTNVEHmodBD:
                JFAEyBaJIPkMKehKJwmAsYRjFBCoytQY = tOvDvKtvMgDywkRLNfxtjmPNxiFnriee
        elif JFAEyBaJIPkMKehKJwmAsYRjFBCoytQY in fPdmOkmJMAgcALMiUPvRNoWvCftYDJDb:
            VcfPjkOQVHbsdQEzcFZdcBTNVEHmodBD = JFAEyBaJIPkMKehKJwmAsYRjFBCoytQY
            if VcfPjkOQVHbsdQEzcFZdcBTNVEHmodBD in JFAEyBaJIPkMKehKJwmAsYRjFBCoytQY:
                JFAEyBaJIPkMKehKJwmAsYRjFBCoytQY = qQdvRCGBVUJWeZtcqqXFgZPtsNEcpKNX
        checkPassing        = 0
        sGaXPTDsknFyAKxTLQXbBViPRADHGKsV = 'daMqdjkrfKkseeVVWBxeODbvSHAwATXS'
        MtuaKfEKyjiuDuNyKbJmGSGiQlviVORL = 'khJaGSYhvfVSNDmdTFltjurtxtzqvFUe'
        cwFeTYwSBHvmxtasAHZcqFphAfvIDmHp = 'rlgnNGmfxjSuaaaEUpjdWxyrAPsfnkzt'
        gXAfDaMqGoCFqOevtpWstnDutjYQGexH = 'NzrGQVFHvKwMqfOqiNZlrYfMdSlRuuDE'
        cUeteacRgFWZBIdiUfWEZSoRbIeLMzxx = 'LmdaGbyLrCWtdCQdIkYyHjqXxzesOOlI'
        AqGKGfxmyokfUEUCczbtWTYRXDSwzfOo = 'llwixZwTHnUmWNgetMbofpOBQVnDsLRY'
        if cwFeTYwSBHvmxtasAHZcqFphAfvIDmHp == gXAfDaMqGoCFqOevtpWstnDutjYQGexH:
            for AqGKGfxmyokfUEUCczbtWTYRXDSwzfOo in cUeteacRgFWZBIdiUfWEZSoRbIeLMzxx:
                if AqGKGfxmyokfUEUCczbtWTYRXDSwzfOo == gXAfDaMqGoCFqOevtpWstnDutjYQGexH:
                    cUeteacRgFWZBIdiUfWEZSoRbIeLMzxx = sGaXPTDsknFyAKxTLQXbBViPRADHGKsV
                else:
                    gXAfDaMqGoCFqOevtpWstnDutjYQGexH = MtuaKfEKyjiuDuNyKbJmGSGiQlviVORL
        countRecursFiles    = 0
        WScLUgraSnUWOoeuZOnjvSzuCVhsPXIz = 'EACaXIzpSDHDHoVWNUVOvHvdYxvgjDij'
        fWHuqeLDgpUaZwdBKGakfDVRwmZwSQQd = 'cpHMrQTdJKnMaQixHlxrDcVGPCwLPvVi'
        yMOpmLHJIBwWgmdfbKKEVfzeDHiQVZZv = 'hKhhZBpsxJXCRkxgLDexrhQIOrLeuDgp'
        JWnCUTiqYZBGBTGWAqEaurvqmJLcanUs = 'mmaLwvOsapkBVbaAujNLFUvzEiKlwfIs'
        ksfsokGPyGheaGfUbmXJIsFUAQTtTIUm = 'BbKbXnDKCQGSsUXZooewcigshCnvAMWc'
        PAJvFzCEKleuryEuibtZqAyzuzSEGgZm = 'KdafdYtCxyChWsrrGuwHIyNQAFTAmquG'
        if yMOpmLHJIBwWgmdfbKKEVfzeDHiQVZZv == JWnCUTiqYZBGBTGWAqEaurvqmJLcanUs:
            for PAJvFzCEKleuryEuibtZqAyzuzSEGgZm in ksfsokGPyGheaGfUbmXJIsFUAQTtTIUm:
                if PAJvFzCEKleuryEuibtZqAyzuzSEGgZm == JWnCUTiqYZBGBTGWAqEaurvqmJLcanUs:
                    ksfsokGPyGheaGfUbmXJIsFUAQTtTIUm = WScLUgraSnUWOoeuZOnjvSzuCVhsPXIz
                else:
                    JWnCUTiqYZBGBTGWAqEaurvqmJLcanUs = fWHuqeLDgpUaZwdBKGakfDVRwmZwSQQd
        if codeArg == "python":
            eObEMCDGnNguWRWTHNMHJpyteYYPbzJB = 'pASlmFsBMNSteNMAtJxyBJbPfbWKRBGV'
            LTnhSmeviwFjHkoALmyvRJToChKlRRHj = 'GAHWfJxCOGsEUXxeAWDWVSnpNTQnUwwt'
            if eObEMCDGnNguWRWTHNMHJpyteYYPbzJB != LTnhSmeviwFjHkoALmyvRJToChKlRRHj:
                NXhneTElwiGIoXxyTjQMLMnyQaEefEvc = 'wEoJbUvyOTgKmTFLKLBwkBmPuNfHWsRP'
                UFmNWcrCfgVEWaPRtCXOzbubpBSZFTib = 'qISXTPazZxiXsaoybOsHWAUTkWvJGSax'
                UFmNWcrCfgVEWaPRtCXOzbubpBSZFTib = NXhneTElwiGIoXxyTjQMLMnyQaEefEvc
            inputExt    = "py"
            eYNHGgHljlkgsDVQWKvgEjbKLxMqDrIY = 'dTvVIaKEcbGbVHgoAkAAudOOqXQIYqSR'
            xrwfDRbRhqsBcgtVRxkSEEFaBHZjyRZa = 'ROLWDKFosNxtedEDNnHsviLoLEWGWfgl'
            if eYNHGgHljlkgsDVQWKvgEjbKLxMqDrIY != xrwfDRbRhqsBcgtVRxkSEEFaBHZjyRZa:
                SUpvMaxgWkYGHaoAJchSwblSWSGcSZjA = 'dVmVOyKqZUPVFqJnmlmYUrIFyxsNbDAM'
                vLqbbkLWOVlLPplygAgrYftLJSurDWmC = 'BeZNCCLigQoRZoAefEBPnMZNkGnWUHry'
                vLqbbkLWOVlLPplygAgrYftLJSurDWmC = SUpvMaxgWkYGHaoAJchSwblSWSGcSZjA
            blockDirs   = r"__pycache__"
            eQDjUprjmkyYNbONMrekWuDjsKlpYPmp = 'iYCDPrtlJMUrtJbxOSrUKFqkVnLTPklt'
            pamjlfqfqsuhQXwfGRgwYaMhGByzmzBv = 'NGDvTgjUKOHvRuxVHYczoHIVgfUllVDC'
            if eQDjUprjmkyYNbONMrekWuDjsKlpYPmp != pamjlfqfqsuhQXwfGRgwYaMhGByzmzBv:
                aLHtxvXhEnXUjDHFxUqSKMBhSbHDddKV = 'IxJfMmUiCJhppFsfjBAXqPPnaXIIggOp'
                tkqNtrevULvxJtXcDqYMWHKqDPXEFcbg = 'KgsibFNTqATQCtyciICTFoRfvUQKbKfz'
                tkqNtrevULvxJtXcDqYMWHKqDPXEFcbg = aLHtxvXhEnXUjDHFxUqSKMBhSbHDddKV
        recursFiles = [f for f in glob.glob("{0}{1}**{1}*.{2}".format(outputArg, self.utils.Platform(), inputExt), recursive=True)]
        tJsOrdNNfnpcyCPayuCzllItAtiKHSRx = 'fvfMoYmhSOPHTcEQHbOyrxgzFiUVJxAg'
        iIwGMWPcjDPRmdTybNhBOdkcoppeMKmm = 'AfvNuTVamCQhZRWugqbdWnHVdUtdhTIT'
        RYqgSBttmzBGfmeEofjZwmPibtSCqNoi = 'QAEXeDXoRKZcvvmHwSfILxLVctgNBwRv'
        if tJsOrdNNfnpcyCPayuCzllItAtiKHSRx == iIwGMWPcjDPRmdTybNhBOdkcoppeMKmm:
            pMSNmydZNPJiaTEWxMWokUihDoLsILFU = 'fnTYCGfhnXZTGGBfJWtqhPrJOnxasNeH'
            pMSNmydZNPJiaTEWxMWokUihDoLsILFU = tJsOrdNNfnpcyCPayuCzllItAtiKHSRx
        else:
            pMSNmydZNPJiaTEWxMWokUihDoLsILFU = 'fnTYCGfhnXZTGGBfJWtqhPrJOnxasNeH'
            pMSNmydZNPJiaTEWxMWokUihDoLsILFU = RYqgSBttmzBGfmeEofjZwmPibtSCqNoi
        SUczkvqnCWgkCEIiMptueTeYchUJdJmD = 'mxWfGRiwKieJSFqeLZdXssUzsTPZLUua'
        zlskrzBmnCNWlHZRyiXppJuhPOJaiakH = 'APivFDVWcDPGcpSROXNTPxUhjGVKNgfS'
        eqfxxcmPQhAqTSHxtZHRLrAGUoEDIjKi = 'LpdaurujewnPMlojVnJSqFfPFbBIrfJZ'
        ClPzweNFrbCgDRXyXQqaXKhzLkSadMni = 'qNiFTCESryxKRtDjSEHOiJZoaXyxKxqP'
        VMhhcRjnJOKZtYULnKmJheaYfexDaecd = 'zhdPgSQbQkRjbXGMYZpUbAoRccXmxkbb'
        HNfMHZohTUcDkbDsJvGZjvonPYaMiclO = 'DXGzjJAuCjFAktOwQeAOtOgSXzRzrTJr'
        if SUczkvqnCWgkCEIiMptueTeYchUJdJmD != ClPzweNFrbCgDRXyXQqaXKhzLkSadMni:
            zlskrzBmnCNWlHZRyiXppJuhPOJaiakH = eqfxxcmPQhAqTSHxtZHRLrAGUoEDIjKi
            for HNfMHZohTUcDkbDsJvGZjvonPYaMiclO in ClPzweNFrbCgDRXyXQqaXKhzLkSadMni:
                if HNfMHZohTUcDkbDsJvGZjvonPYaMiclO != eqfxxcmPQhAqTSHxtZHRLrAGUoEDIjKi:
                    zlskrzBmnCNWlHZRyiXppJuhPOJaiakH = zlskrzBmnCNWlHZRyiXppJuhPOJaiakH
                else:
                    VMhhcRjnJOKZtYULnKmJheaYfexDaecd = SUczkvqnCWgkCEIiMptueTeYchUJdJmD
        else:
            eqfxxcmPQhAqTSHxtZHRLrAGUoEDIjKi = SUczkvqnCWgkCEIiMptueTeYchUJdJmD
            SUczkvqnCWgkCEIiMptueTeYchUJdJmD = VMhhcRjnJOKZtYULnKmJheaYfexDaecd
            if eqfxxcmPQhAqTSHxtZHRLrAGUoEDIjKi == SUczkvqnCWgkCEIiMptueTeYchUJdJmD:
                for HNfMHZohTUcDkbDsJvGZjvonPYaMiclO in SUczkvqnCWgkCEIiMptueTeYchUJdJmD:
                    if HNfMHZohTUcDkbDsJvGZjvonPYaMiclO == eqfxxcmPQhAqTSHxtZHRLrAGUoEDIjKi:
                        eqfxxcmPQhAqTSHxtZHRLrAGUoEDIjKi = SUczkvqnCWgkCEIiMptueTeYchUJdJmD
                    else:
                        eqfxxcmPQhAqTSHxtZHRLrAGUoEDIjKi = VMhhcRjnJOKZtYULnKmJheaYfexDaecd
        for output in recursFiles:
            aFNhwolDASjnRnJDGTdKdVkQAZtZdVBH = 'LdLGRWZDGseXiDaClXpGbIfyDNKaEopO'
            oDsfqZUVIraDhZbhCPGXVUpRNZjBiazN = 'FLGMyoEqxdOWlGuhsWGrcOKLfpiaaKBA'
            if aFNhwolDASjnRnJDGTdKdVkQAZtZdVBH != oDsfqZUVIraDhZbhCPGXVUpRNZjBiazN:
                XSzRURafpnHKiMRQupfzvPSLSpHpcFEs = 'miUuNDbmDwEwjeNofvrfKdVsTGQqiLTF'
                ZwLInShhwDFAsJxUWHEBCWCFQXUdRGbU = 'pkUxsNyuzOoEYatqVdWXUkzZCwMrAVVj'
                ZwLInShhwDFAsJxUWHEBCWCFQXUdRGbU = XSzRURafpnHKiMRQupfzvPSLSpHpcFEs
            if re.match(blockDirs, output):
                ehEElHYAHprIwmWxQOxyxeSUzpfzELwJ = 'VIvkGWldqAikIRvnZTnushDPWlwPGYJW'
                DuQpdqvhzxQYwDltTccijHiynAjxzDnC = 'VrjQZdYyHzgLTTJKqsILJThmDxzhudao'
                prLITByJjtHHgtJWSfdrjzseCupvAzZJ = 'JbDqicaCgWPmCGnyrIzylXrgFenbIswJ'
                INZGeqfxCfNbKLFdMtKweYnkapuDdwgQ = 'IQQDdEwKdyFQjNfEVIBLedCQHZRCIsSK'
                KuAYwRLmnGWEjmmYRhAeOFYTLrqsZQld = 'aMUWuGizXSaBjaOfktmbBJNRiVZjvjyp'
                MmbSUyfKnRoFbKPnvwqbbklIRCdIcLkx = 'QQFQqIaanBOIPDxcHOmIsXzFPHzQqzsF'
                if ehEElHYAHprIwmWxQOxyxeSUzpfzELwJ != INZGeqfxCfNbKLFdMtKweYnkapuDdwgQ:
                    DuQpdqvhzxQYwDltTccijHiynAjxzDnC = prLITByJjtHHgtJWSfdrjzseCupvAzZJ
                    for MmbSUyfKnRoFbKPnvwqbbklIRCdIcLkx in INZGeqfxCfNbKLFdMtKweYnkapuDdwgQ:
                        if MmbSUyfKnRoFbKPnvwqbbklIRCdIcLkx != prLITByJjtHHgtJWSfdrjzseCupvAzZJ:
                            DuQpdqvhzxQYwDltTccijHiynAjxzDnC = DuQpdqvhzxQYwDltTccijHiynAjxzDnC
                        else:
                            KuAYwRLmnGWEjmmYRhAeOFYTLrqsZQld = ehEElHYAHprIwmWxQOxyxeSUzpfzELwJ
                else:
                    prLITByJjtHHgtJWSfdrjzseCupvAzZJ = ehEElHYAHprIwmWxQOxyxeSUzpfzELwJ
                    ehEElHYAHprIwmWxQOxyxeSUzpfzELwJ = KuAYwRLmnGWEjmmYRhAeOFYTLrqsZQld
                    if prLITByJjtHHgtJWSfdrjzseCupvAzZJ == ehEElHYAHprIwmWxQOxyxeSUzpfzELwJ:
                        for MmbSUyfKnRoFbKPnvwqbbklIRCdIcLkx in ehEElHYAHprIwmWxQOxyxeSUzpfzELwJ:
                            if MmbSUyfKnRoFbKPnvwqbbklIRCdIcLkx == prLITByJjtHHgtJWSfdrjzseCupvAzZJ:
                                prLITByJjtHHgtJWSfdrjzseCupvAzZJ = ehEElHYAHprIwmWxQOxyxeSUzpfzELwJ
                            else:
                                prLITByJjtHHgtJWSfdrjzseCupvAzZJ = KuAYwRLmnGWEjmmYRhAeOFYTLrqsZQld
                continue
            else:
                MlwioWaIMWheCNLnybCeyIMuFKNZPHRA = 'aurYqnOyONjTyRuUZbPAPSHqJoGhvSTY'
                FVhuiJwTObOFQSVaELPnHxOyrfibULZe = 'zYuoAJvJgYeMOKTiUPdjpecyZiUAyWWQ'
                ZSzRvlqOgcIrwkZCzuErpZnLxBhGJbgU = 'GaakCKEbtAftXqwqpMdzHOeMNEYQabXT'
                WjERlmhyecqtSUcFPAEpeoVrNxcsmTNf = 'VZCHQIZgnAUCzTyNBIOGHEvBcBBhcqca'
                RmXsxwJHSclrdwjqfGTsqPCFjjWWmmCJ = 'nzMcSbVCtpJKXKldOStGQIiJrApjHyiw'
                gjowINVCaFAKlzWXbbJDvuXthTOIYiEU = 'ezWngyOtUKCWYWdPwgsGKdUtzxCyYcCL'
                if ZSzRvlqOgcIrwkZCzuErpZnLxBhGJbgU == WjERlmhyecqtSUcFPAEpeoVrNxcsmTNf:
                    for gjowINVCaFAKlzWXbbJDvuXthTOIYiEU in RmXsxwJHSclrdwjqfGTsqPCFjjWWmmCJ:
                        if gjowINVCaFAKlzWXbbJDvuXthTOIYiEU == WjERlmhyecqtSUcFPAEpeoVrNxcsmTNf:
                            RmXsxwJHSclrdwjqfGTsqPCFjjWWmmCJ = MlwioWaIMWheCNLnybCeyIMuFKNZPHRA
                        else:
                            WjERlmhyecqtSUcFPAEpeoVrNxcsmTNf = FVhuiJwTObOFQSVaELPnHxOyrfibULZe
                with open(output , "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if not eachLine:
                            continue
                        countLine += 1
        for number in recursFiles:
            klvhGVEdDszMiVzzghyTZxYCpFRzAkEa = 'ZhzZrMYwLKaGeDqQvpSKZnaHlyzdOukO'
            muzhcCZGqWJZtYYijCjvHqqcJlaeHAhO = 'bAIHEjyrymBqyqYpedTVqBsrhlQjOBXE'
            if klvhGVEdDszMiVzzghyTZxYCpFRzAkEa != muzhcCZGqWJZtYYijCjvHqqcJlaeHAhO:
                pkicwVjNFLMdoBKMdbYtpYkVjKbPRNIs = 'tKjzTlPccIxXzxsrCCNOLDgJFLKmyhQL'
                UWRpAiKyrtPJWvZyiCWlYLCMaoljRaeM = 'XrIKQEPATendyZyFvofSmOIprwvbrCsz'
                UWRpAiKyrtPJWvZyiCWlYLCMaoljRaeM = pkicwVjNFLMdoBKMdbYtpYkVjKbPRNIs
            countRecursFiles += 1
            vmUSkZHzdpKeWbwUYckMpSZGMLdfXwem = 'CGOysfgTPEjarotbCiRGSLYrbdedSlvw'
            iqIxneGpRSjfbnAaCjyzxlGUSihDtPGN = 'HdlsvAOZSRGzHcOaeoSUFnbhsKdhFqAz'
            if vmUSkZHzdpKeWbwUYckMpSZGMLdfXwem != iqIxneGpRSjfbnAaCjyzxlGUSihDtPGN:
                ecmYbzNcpiWQaIyKqsKSpcAHdcLFRhRv = 'RjGBsHwBXbpcsFaemYqFAVMkKYnghiHu'
                HaDyqQBHNnEwmMBfuufgXGHeqKCzQnVt = 'nXAfCzXccDSGvlWTHPSFzYbetEEJtsIg'
                HaDyqQBHNnEwmMBfuufgXGHeqKCzQnVt = ecmYbzNcpiWQaIyKqsKSpcAHdcLFRhRv
        print("\n[+] Running adding of random scripts in {0} file(s)...\n".format(countRecursFiles))
        UgOYSMIktExIaIdGlfXzIiJTAKeEVYZP = 'lyIDpxwzgExQTpvhLBTNaIKcHPfICtKK'
        btsLEWeCSEltVdPqSPDZxtPDFYYbsFdF = 'OQqgdzaHyquFxzufAEhOuMzckglZYqsu'
        if UgOYSMIktExIaIdGlfXzIiJTAKeEVYZP != btsLEWeCSEltVdPqSPDZxtPDFYYbsFdF:
            sBrbnrzJczfUtTMgylRivEnJpnodaQVR = 'QOWbJsrphNkVJlYopvmmXXehbJzyLhnf'
            kPdBSegeSYAoZXkNCYrhkDGtOSBgAzEA = 'XTJSpaUXGsXWFgwosEEXsSmZMXODleyF'
            kPdBSegeSYAoZXkNCYrhkDGtOSBgAzEA = sBrbnrzJczfUtTMgylRivEnJpnodaQVR
        QRzTnhZeBZuVXJSouSQlxefOnwvqFNDO = 'irtOuiBHprehtMZgYvYSuxRMrBnSsoMW'
        HZhESAMJooBQUqrRKyGtQKQrrhEWYxBQ = 'KcsKvWchMjOxkCoZwxneezDaHaTAMjHh'
        ufhSaTjZCGyrUJNKjgKJGJhffBfedIKP = 'zEPGnSQCqwmcEqajxkhukdIOuctWQfMY'
        cJiaLJnCwJBHEUHSHAbGoartxuJwDiQL = 'sBLqEBwxXqFCtDJVaCSnyjgORwSLmTXf'
        sOqbazIUBBTkayEjQXidKebgcHtKDuuL = 'NhYVNNGnoscIYqODMTDjPvVfFKXClEFt'
        KbcsgPPYEpSQWAhYbCOPPdsJCQxpGovL = 'TAaXpbpshMUGKzLvTAIlzeWkLVDcCXbx'
        if ufhSaTjZCGyrUJNKjgKJGJhffBfedIKP == cJiaLJnCwJBHEUHSHAbGoartxuJwDiQL:
            for KbcsgPPYEpSQWAhYbCOPPdsJCQxpGovL in sOqbazIUBBTkayEjQXidKebgcHtKDuuL:
                if KbcsgPPYEpSQWAhYbCOPPdsJCQxpGovL == cJiaLJnCwJBHEUHSHAbGoartxuJwDiQL:
                    sOqbazIUBBTkayEjQXidKebgcHtKDuuL = QRzTnhZeBZuVXJSouSQlxefOnwvqFNDO
                else:
                    cJiaLJnCwJBHEUHSHAbGoartxuJwDiQL = HZhESAMJooBQUqrRKyGtQKQrrhEWYxBQ
        with tqdm(total=countRecursFiles) as pbar:
            hBwsfhEtTzdNqLGKSxFLicEgwzQrqfeQ = 'xbdQIoDZzFUPCkFAHolZxiCRkWIomuig'
            kCWyUnYvlGBEuQByiouYGOnAcyhiaSEA = 'zeqMsbdstAWGgxzOPDwTYdujZGQhMBSX'
            if hBwsfhEtTzdNqLGKSxFLicEgwzQrqfeQ != kCWyUnYvlGBEuQByiouYGOnAcyhiaSEA:
                zmuaNiAWuYcxaKwMkXUDEdinZzCtSujK = 'XyEOwFSYPywQKwaARgiCFThNIsDsaYtH'
                MImqkjjRqSJNVYyTSDAHUCnSfdBlsbCt = 'uiAHeDPUuydYBnLXHjWmrZtacIoxpvFN'
                MImqkjjRqSJNVYyTSDAHUCnSfdBlsbCt = zmuaNiAWuYcxaKwMkXUDEdinZzCtSujK
            for output in recursFiles:
                DSOrLDYVCAkXuZzYSiOtXnZMcRRWnMZX = 'DBReiwjtHvHFBhtXrrAIwXuSEoAbKZes'
                AaKQUkCGZpJxpaGaWaULWLCxADEBFjpH = 'fhavtwWavUquPgibLvsmPwnmaBEOhuXZ'
                if DSOrLDYVCAkXuZzYSiOtXnZMcRRWnMZX != AaKQUkCGZpJxpaGaWaULWLCxADEBFjpH:
                    mIukiuhoraRJbJqUHAAajFLUQHiHGDrW = 'ahqwxRkYpiHZjcDVRMiLzbtEEkZdJrHz'
                    hDLngIngVAXTRhagMnEVUDNAGRSQcYuP = 'mbuqYLpOUeFDKKhNxObmqOPNClWAToWd'
                    hDLngIngVAXTRhagMnEVUDNAGRSQcYuP = mIukiuhoraRJbJqUHAAajFLUQHiHGDrW
                pbar.update(1)
                if re.match(blockDirs, output):
                    continue
                else:
                    with fileinput.input(output, inplace=True) as inputFile:
                        for eachLine in inputFile:
                            print(eachLine)
                            if eachLine == "\n":
                                continue
                            else:
                                if codeArg == "python":
                                    spaces                  = len(eachLine) - len(eachLine.lstrip())
                                    noAddScript             = r"(^[\#]+.*)|(\@|\s+\@)|(\s+return)|(\s+#\s{1,10}\w+)"
                                    addIndentScript         = r".*\:{1}\s"
                                    checkAddIndentScript    = r".*\:{1}\s\w+"
                                    listCheckEndLine = []
                                    for i in eachLine:
                                        listCheckEndLine.append(i)
                                    if "," in listCheckEndLine[-2] or "\\" in listCheckEndLine[-2]:
                                        continue
                                    if '\"\"\"' in QZbkYCTSvuvrZrEXUdYvKQsUNnhhUJjy or "\'\'\'" in QZbkYCTSvuvrZrEXUdYvKQsUNnhhUJjy:
                                        qIboDIaeXmsAJnrNOntlzHVyNJHCNvLK += 1
                                    if checkPassing == 1:
                                        continue
                                    else:
                                        checkPassing = 0
                                if re.match(noAddScript, eachLine) is not None:
                                    continue
                                elif re.match(addIndentScript, eachLine) is not None:
                                    if re.match(checkAddIndentScript, eachLine) is not None:
                                        continue
                                    else:
                                        if spaces == 0:
                                            print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg),"    "))
                                            countScriptsAdded += 1
                                        elif spaces == 4:
                                            print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "        "))
                                            countScriptsAdded += 1
                                        elif spaces == 8:
                                            print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "            "))
                                            countScriptsAdded += 1
                                        elif spaces == 12:
                                            print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "                "))
                                            countScriptsAdded += 1
                                        else:
                                            continue
                                else:
                                    if spaces == 0:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg),""))
                                        countScriptsAdded += 1
                                    elif spaces == 4:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "    "))
                                        countScriptsAdded += 1
                                    elif spaces == 8:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "        "))
                                        countScriptsAdded += 1
                                    elif spaces == 12:
                                        print(textwrap.indent(Padding.ScriptsGenerator(self, codeArg, mixerLevelArg), "            "))
                                        countScriptsAdded += 1
                                    else:
                                        continue
        xTnKdUPtLeNnglyVTgMJisieHtshzoaE = 'HVkYQJnJrOuvOFoujebdIemryqDkcoKe'
        OQmZMRCCqGzJybUOHjpCsGpCDXTdGCaj = 'vHEsOQrAgNSxKYVbXDMnYANNTZAxCwlD'
        rLmzKRQxiouRqtePANcuMEZabSEFgxmP = 'tjxZCblKtIhUguQqpPlJdglxnWqkdZcQ'
        CYclmUVWkhOrXykQwZttNVQiQyQfZYTq = 'jewuGxEIrBWmuPaIJbeGxnbrpcJlvXZy'
        qYCUiSxufzCTItsKzSBYWlRyjqqZHjRJ = 'GfRBnbGFpWZInzeXFHGLUNsDQUswRmpe'
        klTlNbRNGzuZiJlgOdZcRlYQTrnonQma = 'KWxEMeHKPIoBIgyLTNgstNyEzCSaIUuj'
        if rLmzKRQxiouRqtePANcuMEZabSEFgxmP == CYclmUVWkhOrXykQwZttNVQiQyQfZYTq:
            for klTlNbRNGzuZiJlgOdZcRlYQTrnonQma in qYCUiSxufzCTItsKzSBYWlRyjqqZHjRJ:
                if klTlNbRNGzuZiJlgOdZcRlYQTrnonQma == CYclmUVWkhOrXykQwZttNVQiQyQfZYTq:
                    qYCUiSxufzCTItsKzSBYWlRyjqqZHjRJ = xTnKdUPtLeNnglyVTgMJisieHtshzoaE
                else:
                    CYclmUVWkhOrXykQwZttNVQiQyQfZYTq = OQmZMRCCqGzJybUOHjpCsGpCDXTdGCaj
        for output in recursFiles:
            CgPePBZMLaUONHedMmIrrXacMGHHUAbS = 'DbZpgdMdbNnjkznFTqpMwwQDBbFtlJre'
            kZtAXPJFhFTDSJmuYcSyYjcZWMoDANZi = 'ykUyZDKrqxJOuJydrwDzEkJGRXqdCNIl'
            RmhAJPsqXnQACKKsLddcPgIEBkbItLjh = 'cKXNkukDZnFJlWhEeJKNEutvsjJRklNT'
            JxCSKxagWPPjfGGZYjMTwSQBTssallLw = 'dvdBtZcyCraUUQXsJdvkklrwhqhxxusy'
            NhaWGiFmCPdODKXgujzDzWtMWQAGvwPX = 'nlQkBxpvSVIppNoFItuOhkyMWBUFrpnj'
            if CgPePBZMLaUONHedMmIrrXacMGHHUAbS in kZtAXPJFhFTDSJmuYcSyYjcZWMoDANZi:
                CgPePBZMLaUONHedMmIrrXacMGHHUAbS = NhaWGiFmCPdODKXgujzDzWtMWQAGvwPX
                if kZtAXPJFhFTDSJmuYcSyYjcZWMoDANZi in RmhAJPsqXnQACKKsLddcPgIEBkbItLjh:
                    kZtAXPJFhFTDSJmuYcSyYjcZWMoDANZi = JxCSKxagWPPjfGGZYjMTwSQBTssallLw
            elif kZtAXPJFhFTDSJmuYcSyYjcZWMoDANZi in CgPePBZMLaUONHedMmIrrXacMGHHUAbS:
                RmhAJPsqXnQACKKsLddcPgIEBkbItLjh = kZtAXPJFhFTDSJmuYcSyYjcZWMoDANZi
                if RmhAJPsqXnQACKKsLddcPgIEBkbItLjh in kZtAXPJFhFTDSJmuYcSyYjcZWMoDANZi:
                    kZtAXPJFhFTDSJmuYcSyYjcZWMoDANZi = NhaWGiFmCPdODKXgujzDzWtMWQAGvwPX
            if re.match(blockDirs, output):
                MDUFPmzLlvvmguyqekMLwWFhyERMUZoA = 'YPdPOCDyKGxzQhLNGyUnMljhiEFjGaaO'
                duEGNyPcszumtWaQZiuGckTMwtJpoINe = 'KpiParOsAqClbYDQYAPitZZUpCArkzRi'
                zZUoAMFAYzlYaJsuESOOLuLfLrdWammH = 'LfTMlYKUnHMdYrgGodUiPptiAoRkaetJ'
                BhvniZZIHJwEuwBrehQaqHVErxXAYSlZ = 'zwHDemxaxNjHyxSRTEvtMAjcdIVgJMhd'
                kwMRzSQwjBQdIxqeVtYqZlIeJnStXKAl = 'WjQWsoUwVbYbfeLIelGGfscUEWrpTdop'
                FeohhGPEiFKypBlvaLZneIMXELWamYdr = 'pTurkGOROJxPbfHpIgsJNyCnrZgACwKM'
                if MDUFPmzLlvvmguyqekMLwWFhyERMUZoA != BhvniZZIHJwEuwBrehQaqHVErxXAYSlZ:
                    duEGNyPcszumtWaQZiuGckTMwtJpoINe = zZUoAMFAYzlYaJsuESOOLuLfLrdWammH
                    for FeohhGPEiFKypBlvaLZneIMXELWamYdr in BhvniZZIHJwEuwBrehQaqHVErxXAYSlZ:
                        if FeohhGPEiFKypBlvaLZneIMXELWamYdr != zZUoAMFAYzlYaJsuESOOLuLfLrdWammH:
                            duEGNyPcszumtWaQZiuGckTMwtJpoINe = duEGNyPcszumtWaQZiuGckTMwtJpoINe
                        else:
                            kwMRzSQwjBQdIxqeVtYqZlIeJnStXKAl = MDUFPmzLlvvmguyqekMLwWFhyERMUZoA
                else:
                    zZUoAMFAYzlYaJsuESOOLuLfLrdWammH = MDUFPmzLlvvmguyqekMLwWFhyERMUZoA
                    MDUFPmzLlvvmguyqekMLwWFhyERMUZoA = kwMRzSQwjBQdIxqeVtYqZlIeJnStXKAl
                    if zZUoAMFAYzlYaJsuESOOLuLfLrdWammH == MDUFPmzLlvvmguyqekMLwWFhyERMUZoA:
                        for FeohhGPEiFKypBlvaLZneIMXELWamYdr in MDUFPmzLlvvmguyqekMLwWFhyERMUZoA:
                            if FeohhGPEiFKypBlvaLZneIMXELWamYdr == zZUoAMFAYzlYaJsuESOOLuLfLrdWammH:
                                zZUoAMFAYzlYaJsuESOOLuLfLrdWammH = MDUFPmzLlvvmguyqekMLwWFhyERMUZoA
                            else:
                                zZUoAMFAYzlYaJsuESOOLuLfLrdWammH = kwMRzSQwjBQdIxqeVtYqZlIeJnStXKAl
                continue
            else:
                ojfxXeNTucojxFHDMyGLWDJjiyTENZgK = 'YJRETikkmtZXImePsseMAlJmufkwpQju'
                JNyGZpaGsdpNocgcxwiMfhBfrDXebfpX = 'nTxtSeWTfrHaiiUaZlIsPAQdttxFzPKz'
                naTgwoijwRlRbElkSySdiqHjjpeyNuop = 'oFbuFnDYTbtssDjdFJfqwLNacmaRJhPS'
                if ojfxXeNTucojxFHDMyGLWDJjiyTENZgK == JNyGZpaGsdpNocgcxwiMfhBfrDXebfpX:
                    SpSLqvVdzZYFzPSfpTWTpOKyOYYJfvAR = 'MeErBfINViCZoYZJDcpeJmcHMAgfoCVl'
                    SpSLqvVdzZYFzPSfpTWTpOKyOYYJfvAR = ojfxXeNTucojxFHDMyGLWDJjiyTENZgK
                else:
                    SpSLqvVdzZYFzPSfpTWTpOKyOYYJfvAR = 'MeErBfINViCZoYZJDcpeJmcHMAgfoCVl'
                    SpSLqvVdzZYFzPSfpTWTpOKyOYYJfvAR = naTgwoijwRlRbElkSySdiqHjjpeyNuop
                with open(output , "r") as readFile:
                    readF = readFile.readlines()
                    for eachLine in readF:
                        if not eachLine:
                            continue
                        checkLine += 1
        countLineAdded = checkLine - countLine
        nbeMycRwUvGTgriCIVCRTzefdLfOpYTV = 'zSCAVuCGFHHqIyapYRGwrruhihOPKHmg'
        KwrxCHlLQlpegCNTzGgrOZrMLRMXItkl = 'urZVAOvkTKKeywFHSPuLVqHlWrMBlEPb'
        sMsuVjNCUMbjgJGTLFHXYFEGpAnZfcit = 'UXQEGzupbQfvMmWahmUJhYLTscWPkIQm'
        HBOCpUemePAExEhpkoUitmiVKAdXdKHg = 'HkDlABYmpgYKhIgFbpYvwSCgYYYrnGFo'
        dBZnzXDdVhmkalGIWPpukFKUoAuOcpJw = 'ZATxXEbjiTrzanKYZkStgYeCrzEtBDYO'
        OuIxlbDcCTDeWwgeWcFGRSlpRUfufydp = 'RWWwHDDqzngVfcGwQBxwznHGYVrZwOER'
        if sMsuVjNCUMbjgJGTLFHXYFEGpAnZfcit == HBOCpUemePAExEhpkoUitmiVKAdXdKHg:
            for OuIxlbDcCTDeWwgeWcFGRSlpRUfufydp in dBZnzXDdVhmkalGIWPpukFKUoAuOcpJw:
                if OuIxlbDcCTDeWwgeWcFGRSlpRUfufydp == HBOCpUemePAExEhpkoUitmiVKAdXdKHg:
                    dBZnzXDdVhmkalGIWPpukFKUoAuOcpJw = nbeMycRwUvGTgriCIVCRTzefdLfOpYTV
                else:
                    HBOCpUemePAExEhpkoUitmiVKAdXdKHg = KwrxCHlLQlpegCNTzGgrOZrMLRMXItkl
        if checkLine > countLine:
            AsFvfTAPSRWadihSdmEHTLPkJceVActi = 'WDPfBbjTJjZNeKqFAlnLlxuQRqhzCkQu'
            jbHFwGVbtOitwYYLWdNTiMGbfTVAKNpr = 'DHLVpzyqBtrhKNvMAokmWCqZYmEfjeWU'
            if AsFvfTAPSRWadihSdmEHTLPkJceVActi != jbHFwGVbtOitwYYLWdNTiMGbfTVAKNpr:
                BbKtaXgjirilajsfdMPKyAqryGtKAWbE = 'hSeRrZHOSCYKmJXNuAsEdRmHGBszqtSB'
                jIZeARaRvyvEEvMzKNHewZFrWDPFgJon = 'vnkdSFZgFwmztwNcgGLLHPwAgopCrsIN'
                jIZeARaRvyvEEvMzKNHewZFrWDPFgJon = BbKtaXgjirilajsfdMPKyAqryGtKAWbE
            print("\n-> {0} scripts added in {1} file(s)\n".format(countScriptsAdded, countRecursFiles))
            NvSAhqwVsFKQJfIOHbXDPzJmkroJeWCd = 'izOzTKFBxqHRKHPpHHgslVdxTqpwXsMR'
            EUwiXOWSUaPBeFMtwQdwOEnQhiPBITCF = 'CXaHVfalrinESqDaWUplKeJDxnGIDaTV'
            hlBBPhazMcZVDkbsbCDOacdBmvVjWFwF = 'uYhQXkYNykFbMnTmtYBNjtGpfgFORIVj'
            CWCmKzTlSSXzBsYwFBLrEWTEJCKpUJRe = 'rLEwMJRWOJUhBQKcmReeRdSqfVYmvnVO'
            RZNRsFRUtgBlbVfjetUKLdNXtQpvzZYo = 'ZOVMMrqTawGASpOmhdjcxIiKTstDpipn'
            bGUYNYreVlmoDYxzXdMbTddxGoXYWxmU = 'WZmsRKQcLcjlpTxXoDgsbdCufuTlSCbs'
            if hlBBPhazMcZVDkbsbCDOacdBmvVjWFwF == CWCmKzTlSSXzBsYwFBLrEWTEJCKpUJRe:
                for bGUYNYreVlmoDYxzXdMbTddxGoXYWxmU in RZNRsFRUtgBlbVfjetUKLdNXtQpvzZYo:
                    if bGUYNYreVlmoDYxzXdMbTddxGoXYWxmU == CWCmKzTlSSXzBsYwFBLrEWTEJCKpUJRe:
                        RZNRsFRUtgBlbVfjetUKLdNXtQpvzZYo = NvSAhqwVsFKQJfIOHbXDPzJmkroJeWCd
                    else:
                        CWCmKzTlSSXzBsYwFBLrEWTEJCKpUJRe = EUwiXOWSUaPBeFMtwQdwOEnQhiPBITCF
            print("-> {0} lines added in {1} file(s)\n".format(countLineAdded, countRecursFiles))
            BthxIyfDSMiBTfLdDjccnerGYYAuIPXV = 'tUutEmzOBtzSPMVBBXcEzNuleBfIiGwm'
            PAUJnpwlgxVXicfmuhYGyBlFttOdPtRw = 'uErghUZTyrUuzFuwFumPvnrHwKTHNJIP'
            pRbRZDVhhGoIKjPtFspehTBGsOEYiMfl = 'oLSUHnwXdPEeNYxZnqbpYzVCRemXimsv'
            JKsOlVHUxvpSZUCgrDVdKymaGEptRvov = 'pQqtTaxVeQLXxLhbiophdxGHwdtdLlUT'
            mJieFQMttskBigiSrsLLzXKplnzaSkaF = 'dhnEDlgiLXgAUvJPjlmimMNFVGvfisoS'
            RQcGpiPjTZFQseHatjBEMMhYOKPTeSvC = 'KYHWLIelaJsbQZrhosedZXKRJGhhekzD'
            if BthxIyfDSMiBTfLdDjccnerGYYAuIPXV != JKsOlVHUxvpSZUCgrDVdKymaGEptRvov:
                PAUJnpwlgxVXicfmuhYGyBlFttOdPtRw = pRbRZDVhhGoIKjPtFspehTBGsOEYiMfl
                for RQcGpiPjTZFQseHatjBEMMhYOKPTeSvC in JKsOlVHUxvpSZUCgrDVdKymaGEptRvov:
                    if RQcGpiPjTZFQseHatjBEMMhYOKPTeSvC != pRbRZDVhhGoIKjPtFspehTBGsOEYiMfl:
                        PAUJnpwlgxVXicfmuhYGyBlFttOdPtRw = PAUJnpwlgxVXicfmuhYGyBlFttOdPtRw
                    else:
                        mJieFQMttskBigiSrsLLzXKplnzaSkaF = BthxIyfDSMiBTfLdDjccnerGYYAuIPXV
            else:
                pRbRZDVhhGoIKjPtFspehTBGsOEYiMfl = BthxIyfDSMiBTfLdDjccnerGYYAuIPXV
                BthxIyfDSMiBTfLdDjccnerGYYAuIPXV = mJieFQMttskBigiSrsLLzXKplnzaSkaF
                if pRbRZDVhhGoIKjPtFspehTBGsOEYiMfl == BthxIyfDSMiBTfLdDjccnerGYYAuIPXV:
                    for RQcGpiPjTZFQseHatjBEMMhYOKPTeSvC in BthxIyfDSMiBTfLdDjccnerGYYAuIPXV:
                        if RQcGpiPjTZFQseHatjBEMMhYOKPTeSvC == pRbRZDVhhGoIKjPtFspehTBGsOEYiMfl:
                            pRbRZDVhhGoIKjPtFspehTBGsOEYiMfl = BthxIyfDSMiBTfLdDjccnerGYYAuIPXV
                        else:
                            pRbRZDVhhGoIKjPtFspehTBGsOEYiMfl = mJieFQMttskBigiSrsLLzXKplnzaSkaF
            if (self.remove.LineBreaks(codeArg, outputArg) == 0):
                hpOSXFfuVzZJowCFHmSfNMULqVxEcrEC = 'nuVvwylHkyHGvYHLwkNwnhKYwKsiOdEV'
                iKfGCpxjidRjBhYwLnWFAPFymmrDbAwz = 'OeMROFUreTBgJoWidsbHezmsvwloAvWu'
                if hpOSXFfuVzZJowCFHmSfNMULqVxEcrEC != iKfGCpxjidRjBhYwLnWFAPFymmrDbAwz:
                    gqGYFVokVJBDdBNzaCKYmStFZKOFehcR = 'MjEBskhxtORNjXgtTmgaqNCHalgMGtSb'
                    jNlnMjeLrRwlHhPWDeiYJqduRCsWeeIz = 'JObypwzufQNkHVXVOiIqcVxrfXdsyOZL'
                    jNlnMjeLrRwlHhPWDeiYJqduRCsWeeIz = gqGYFVokVJBDdBNzaCKYmStFZKOFehcR
                return EXIT_SUCCESS
            else:
                hxkQqUvLtgrtGHPXcyUgnoVIrSjzfYhx = 'BcbijqjFfjDboCpmprOMdpwhkoYTrcNc'
                uEdlpNpoVFRWJgGhARgHasNOappUvgDU = 'eofmVlFKvBcBIieScfmhVclXSlFKmnQO'
                iYbJZVMfLIcVGggsPrHnUgdIwElrluqm = 'MBYkEVYdUmmPlxGXVQxRsHXhoLgaZVut'
                sUjpcSDlTJCDCJRlcxoItydgyFKsMWKi = 'gwVDnnHqUSyciwqcdhXCtoOoNjxLOvus'
                nPPupWkgnHEjwPIpovJNRyhdXXYrDCNV = 'YFUnFcIyfHsySSoTPYXUqvFWTFmgoYjY'
                if hxkQqUvLtgrtGHPXcyUgnoVIrSjzfYhx in uEdlpNpoVFRWJgGhARgHasNOappUvgDU:
                    hxkQqUvLtgrtGHPXcyUgnoVIrSjzfYhx = nPPupWkgnHEjwPIpovJNRyhdXXYrDCNV
                    if uEdlpNpoVFRWJgGhARgHasNOappUvgDU in iYbJZVMfLIcVGggsPrHnUgdIwElrluqm:
                        uEdlpNpoVFRWJgGhARgHasNOappUvgDU = sUjpcSDlTJCDCJRlcxoItydgyFKsMWKi
                elif uEdlpNpoVFRWJgGhARgHasNOappUvgDU in hxkQqUvLtgrtGHPXcyUgnoVIrSjzfYhx:
                    iYbJZVMfLIcVGggsPrHnUgdIwElrluqm = uEdlpNpoVFRWJgGhARgHasNOappUvgDU
                    if iYbJZVMfLIcVGggsPrHnUgdIwElrluqm in uEdlpNpoVFRWJgGhARgHasNOappUvgDU:
                        uEdlpNpoVFRWJgGhARgHasNOappUvgDU = nPPupWkgnHEjwPIpovJNRyhdXXYrDCNV
                return EXIT_FAILURE
        else:
            xZryJxaNEanCdgJZzdtGLgLmVugjcGyv = 'qzqYKlNoiaZbwkDTFWzAdGhLuGJWqElf'
            CCmUpGhbhQnyRemMNnHgUfepebfrCQZp = 'lBRtKMBiruPbBxFMmnOPAmOBzHjlidZI'
            if xZryJxaNEanCdgJZzdtGLgLmVugjcGyv != CCmUpGhbhQnyRemMNnHgUfepebfrCQZp:
                jWhmTqxMXlKCsxjrTTyTaFVDwhpzEXjg = 'boyhWPxUkZfWPuRaucokIuNzYxqYbekP'
                aCwdMRnxkBINzrllFUPiQVnTxpNVTbUw = 'KbxLrgABLpItEHLcsaEeRqmykJRAqhLJ'
                aCwdMRnxkBINzrllFUPiQVnTxpNVTbUw = jWhmTqxMXlKCsxjrTTyTaFVDwhpzEXjg
            return EXIT_FAILURE
