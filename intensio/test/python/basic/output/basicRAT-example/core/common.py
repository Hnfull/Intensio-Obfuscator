# -*- coding: utf-8 -*-
def NHnBfNVCKBbNASdmdnEOSpKkCrHhLIhR(bytes):
    LzGXqmNenirBzPlhVchwrEvaQRzIMgwH = 0
    while bytes:
        LzGXqmNenirBzPlhVchwrEvaQRzIMgwH = LzGXqmNenirBzPlhVchwrEvaQRzIMgwH << 8
        LzGXqmNenirBzPlhVchwrEvaQRzIMgwH += ord(bytes[-1])
        bytes = bytes[:-1]
    return LzGXqmNenirBzPlhVchwrEvaQRzIMgwH
def UCMpkcMOquIpwsHsVjcrIugfBZPLljiQ(LzGXqmNenirBzPlhVchwrEvaQRzIMgwH):
    WycdYteTqLUqOIGEmlOhTYcRnuTSdjYj = ''
    while LzGXqmNenirBzPlhVchwrEvaQRzIMgwH:
        WycdYteTqLUqOIGEmlOhTYcRnuTSdjYj += chr(LzGXqmNenirBzPlhVchwrEvaQRzIMgwH & 0xff)
        LzGXqmNenirBzPlhVchwrEvaQRzIMgwH = LzGXqmNenirBzPlhVchwrEvaQRzIMgwH >> 8
    return WycdYteTqLUqOIGEmlOhTYcRnuTSdjYj
