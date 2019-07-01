# -*- coding: utf-8 -*-
import socket
import struct
from crypto import TKQFCDOUTVgFyFAJmsSOIosLeXgEyzvM
from crypto import ofRSbfGSJUJdJOMAHnOdMFDQhCuQDoiv
def FEDRkrcFQWVmxhAcLZqwmJisXuseuPOa(sock, wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj, key):
    with open(wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj, 'wb') as f:
        tEnVGsZIBBmcmLdTAEGCopYaxQyxsWvQ = struct.unpack("!I", sock.recv(4))[0]
        while tEnVGsZIBBmcmLdTAEGCopYaxQyxsWvQ:
            OIzAkJwmuKlGwKClDnCXURAvUCgRYiKV = sock.recv(tEnVGsZIBBmcmLdTAEGCopYaxQyxsWvQ)
            f.write(ofRSbfGSJUJdJOMAHnOdMFDQhCuQDoiv(OIzAkJwmuKlGwKClDnCXURAvUCgRYiKV, key))
            tEnVGsZIBBmcmLdTAEGCopYaxQyxsWvQ = struct.unpack("!I", sock.recv(4))[0]
def thflmVfaWGOyjCvyeYkEruExtxkCUNyb(sock, wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj, key):
    with open(wLLVWYAkHYMhQoGtlhOPdEoZRyLXNWmj, 'rb') as f:
        OIzAkJwmuKlGwKClDnCXURAvUCgRYiKV = f.read(4096)
        while len(OIzAkJwmuKlGwKClDnCXURAvUCgRYiKV):
            yIbmFXUqarkHrHIsiTIcgTzFECyImlqk = TKQFCDOUTVgFyFAJmsSOIosLeXgEyzvM(OIzAkJwmuKlGwKClDnCXURAvUCgRYiKV, key)
            sock.send(struct.pack("!I", len(yIbmFXUqarkHrHIsiTIcgTzFECyImlqk)))
            sock.send(yIbmFXUqarkHrHIsiTIcgTzFECyImlqk)
            OIzAkJwmuKlGwKClDnCXURAvUCgRYiKV = f.read(4096)
        sock.send('\x00\x00\x00\x00')
