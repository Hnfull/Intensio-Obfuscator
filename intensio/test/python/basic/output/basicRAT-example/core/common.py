# -*- coding: utf-8 -*-
def GutZpRlAsBCAvPyzhYlxoAGyimkaOLTR(bytes):
    JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr = 0
    while bytes:
        JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr = JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr << 8
        JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr += ord(bytes[-1])
        bytes = bytes[:-1]
    return JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr
def OwBGcBlzySYfaqOsrGimMtFLwhqqzoHn(JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr):
    kGYTWSfvuDprKpGLiqehVAXxBnCjSGTy = ''
    while JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr:
        kGYTWSfvuDprKpGLiqehVAXxBnCjSGTy += chr(JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr & 0xff)
        JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr = JYxOQoHxrWVlWZGFRgpIWcoGVeKxUiXr >> 8
    return kGYTWSfvuDprKpGLiqehVAXxBnCjSGTy
