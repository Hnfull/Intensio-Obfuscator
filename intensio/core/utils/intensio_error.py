 # -*- coding: utf-8 -*-

#---------------------------------------------------------- [Lib] -----------------------------------------------------------#

import sys

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

# -- !! Only for verbosity of code !! -- #

# -- Name generated from winerror.h -- #
EXIT_SUCCESS            = 0

EXIT_FAILURE            = 1
ERROR_FILE_NOT_FOUND    = 1
ERROR_PATH_NOT_FOUND    = 1
ERROR_BAD_ENVIRONMENT   = 1
ERROR_INVALID_DATA      = 1
ERROR_BAD_COMMAND       = 1
ERROR_BAD_LENGTH        = 1
ERROR_INVALID_PARAMETER = 1
ERROR_BAD_ARGUMENTS     = 1
ERROR_BAD_FILE_TYPE     = 1
ERROR_CANNOT_COPY       = 1
ERROR_NOT_EMPTY         = 1
ERROR_INVALID_FUNCTION  = 1

# -- Name generated manually -- #
ERROR_CANNOT_REMOVE = 1
ERROR_FILE_EMPTY    = 1
ERROR_DIR_EMPTY     = 1
ERROR_NOT_DIR       = 1
ERROR_NOT_FILE      = 1
ERROR_DIR_EMPTY     = 1

#--------------------------------------------------- [Function(s)/Class] ----------------------------------------------------#

# -- Not raised an error, only for breaking a loop -- #
class BreakLoop (Exception):
    pass
