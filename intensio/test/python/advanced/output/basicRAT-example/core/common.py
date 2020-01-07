# -*- coding: utf-8 -*-
def fWgMvsZQGaiamgQMhvvIAoPAldfTADmA(bytes):
    fcUvUWvdMWjQzCEAElsAtioTqFjArjjm = 0
    while bytes:
        fcUvUWvdMWjQzCEAElsAtioTqFjArjjm = fcUvUWvdMWjQzCEAElsAtioTqFjArjjm << 8
        fcUvUWvdMWjQzCEAElsAtioTqFjArjjm += ord(bytes[-1])
        bytes = bytes[:-1]
    return fcUvUWvdMWjQzCEAElsAtioTqFjArjjm
def UoWPRTiVwehQrDkyyalyWSqZMdquoskF(fcUvUWvdMWjQzCEAElsAtioTqFjArjjm):
    IrPPeZdcKqphLopsuAyyrHCbtKkfKlbK = ''
    while fcUvUWvdMWjQzCEAElsAtioTqFjArjjm:
        IrPPeZdcKqphLopsuAyyrHCbtKkfKlbK += chr(fcUvUWvdMWjQzCEAElsAtioTqFjArjjm & 0xff)
        fcUvUWvdMWjQzCEAElsAtioTqFjArjjm = fcUvUWvdMWjQzCEAElsAtioTqFjArjjm >> 8
    return IrPPeZdcKqphLopsuAyyrHCbtKkfKlbK
