 # -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import sys

from core.utils.intensio_error import ERROR_BAD_ENVIRONMENT

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

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
