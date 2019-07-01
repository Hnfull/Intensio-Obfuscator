# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import sys

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

class Utils:

    def __init__(self):
        self.platform = sys.platform

    def Platform(self):
        if self.platform == "win32":
            return "\\"
        else:
            return "/"

    def DictMerge(self, dict1, dict2):
    	merge = {**dict1, **dict2}
    	return merge
