# -*- coding: utf-8 -*-

# https://github.com/Hnfull/Intensio-Obfuscator

#--------------------------------------------------------- [Global] ---------------------------------------------------------#

# -- !! Only for verbosity of code !! -- #
                        
# -- Name from winerror.h -- #
EXIT_SUCCESS            = 0

EXIT_FAILURE            = 1
ERROR_FILE_NOT_FOUND    = 1
ERROR_PATH_NOT_FOUND    = 1
ERROR_INVALID_PARAMETER = 1
ERROR_BAD_ARGUMENTS     = 1
ERROR_CANNOT_COPY       = 1
ERROR_INVALID_FUNCTION  = 1
                            
# -- Name generated manually -- #
ERROR_CAN_NOT_REMOVE    = 1
ERROR_CAN_NOT_COPY      = 1                                                                             
ERROR_FILE_EMPTY        = 1                 
ERROR_DIR_NOT_FOUND     = 1
ERROR_DIR_EMPTY         = 1

#------------------------------------------------- [Function(s)/Class(es)] --------------------------------------------------#

# -- Not raised an error, only for breaking a loop -- #
class BreakLoop (Exception):
    pass
