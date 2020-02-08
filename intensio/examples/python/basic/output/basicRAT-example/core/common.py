# -*- coding: utf-8 -*-
def ckAjUaLEXnferbefRGpQeOZRysoqlffQ(bytes):
    kWFtuPcTzhXQsxkZcspaKNvhNllUXCxh = 0
    while bytes:
        kWFtuPcTzhXQsxkZcspaKNvhNllUXCxh = kWFtuPcTzhXQsxkZcspaKNvhNllUXCxh << 8
        kWFtuPcTzhXQsxkZcspaKNvhNllUXCxh += ord(bytes[-1])
        bytes = bytes[:-1]
    return kWFtuPcTzhXQsxkZcspaKNvhNllUXCxh
def xJiPZbUzlGCIdemowYnQNONypdeudgmd(kWFtuPcTzhXQsxkZcspaKNvhNllUXCxh):
    FRIUnJhVUpQceKKKwrGdGufEFeSRdAAs = ''
    while kWFtuPcTzhXQsxkZcspaKNvhNllUXCxh:
        FRIUnJhVUpQceKKKwrGdGufEFeSRdAAs += chr(kWFtuPcTzhXQsxkZcspaKNvhNllUXCxh & 0xff)
        kWFtuPcTzhXQsxkZcspaKNvhNllUXCxh = kWFtuPcTzhXQsxkZcspaKNvhNllUXCxh >> 8
    return FRIUnJhVUpQceKKKwrGdGufEFeSRdAAs
