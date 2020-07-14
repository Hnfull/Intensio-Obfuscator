# -*- coding: utf-8 -*-
def sDbdGVTmnYPISKJkENqYvrbalANhLchN(bytes):
    tPRbiMBffyIeZvPPYViVoXWUMGNaAsOJ = 0
    while bytes:
        tPRbiMBffyIeZvPPYViVoXWUMGNaAsOJ = tPRbiMBffyIeZvPPYViVoXWUMGNaAsOJ << 8
        tPRbiMBffyIeZvPPYViVoXWUMGNaAsOJ += ord(bytes[-1])
        bytes = bytes[:-1]
    return tPRbiMBffyIeZvPPYViVoXWUMGNaAsOJ
def DKoAKXcLBxaCwnVTbPAvLSNDpZiNHsFA(tPRbiMBffyIeZvPPYViVoXWUMGNaAsOJ):
    IcVzPJDfYVsFBnElsTyTCEBzgOsgSIrM = ''
    while tPRbiMBffyIeZvPPYViVoXWUMGNaAsOJ:
        IcVzPJDfYVsFBnElsTyTCEBzgOsgSIrM += chr(tPRbiMBffyIeZvPPYViVoXWUMGNaAsOJ & 0xff)
        tPRbiMBffyIeZvPPYViVoXWUMGNaAsOJ = tPRbiMBffyIeZvPPYViVoXWUMGNaAsOJ >> 8
    return IcVzPJDfYVsFBnElsTyTCEBzgOsgSIrM
