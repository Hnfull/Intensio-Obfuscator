# -*- coding: utf-8 -*-
def eCYwFUxuSOdzxlFJDXYkjfnEbtTZqEYg(bytes):
    kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs = 0
    while bytes:
        kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs = kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs << 8
        kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs += ord(bytes[-1])
        bytes = bytes[:-1]
    return kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs
def SNYDucfxYRhXDMuRJTDBCRnAkWNYSZBi(kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs):
    uhKbXIobsxIiifCMGPRzFNBHQAeJupJM = ''
    while kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs:
        uhKbXIobsxIiifCMGPRzFNBHQAeJupJM += chr(kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs & 0xff)
        kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs = kJsMTlOenjgnlvKLOJTqQqAwyESQpoCs >> 8
    return uhKbXIobsxIiifCMGPRzFNBHQAeJupJM
