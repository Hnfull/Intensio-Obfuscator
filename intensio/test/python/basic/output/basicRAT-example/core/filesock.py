# -*- coding: utf-8 -*-
import socket
import struct
from crypto import FPmaenntgMXUySRHYnxonMrLjGvQbFhl
from crypto import FAkNnUdNDaFZorQoeriEgCCFHcblhqBR
def eRrqpYUchKPoYbYxOYQeDwzVUJNcqUZT(sock, paCQjENnuYPVmljLLYILWWljITjDzepC, key):
    with open(paCQjENnuYPVmljLLYILWWljITjDzepC, 'wb') as f:
        xvAUUAzNvthWXDrEIQMfFHXTBoGLpnek = struct.unpack("!I", sock.recv(4))[0]
        while xvAUUAzNvthWXDrEIQMfFHXTBoGLpnek:
            gWxMpOditfUtXVGfAAMvZXbMLCEdJbOd = sock.recv(xvAUUAzNvthWXDrEIQMfFHXTBoGLpnek)
            f.write(FAkNnUdNDaFZorQoeriEgCCFHcblhqBR(gWxMpOditfUtXVGfAAMvZXbMLCEdJbOd, key))
            xvAUUAzNvthWXDrEIQMfFHXTBoGLpnek = struct.unpack("!I", sock.recv(4))[0]
def JKkiTRuroBtXTQaWSmtYrgeAxgzygIAE(sock, paCQjENnuYPVmljLLYILWWljITjDzepC, key):
    with open(paCQjENnuYPVmljLLYILWWljITjDzepC, 'rb') as f:
        gWxMpOditfUtXVGfAAMvZXbMLCEdJbOd = f.read(4096)
        while len(gWxMpOditfUtXVGfAAMvZXbMLCEdJbOd):
            JqzFjOyDgRqmMmnmPktCeCpuhOEASOBx = FPmaenntgMXUySRHYnxonMrLjGvQbFhl(gWxMpOditfUtXVGfAAMvZXbMLCEdJbOd, key)
            sock.send(struct.pack("!I", len(JqzFjOyDgRqmMmnmPktCeCpuhOEASOBx)))
            sock.send(JqzFjOyDgRqmMmnmPktCeCpuhOEASOBx)
            gWxMpOditfUtXVGfAAMvZXbMLCEdJbOd = f.read(4096)
        sock.send('\x00\x00\x00\x00')
