from ctypes import *

libc = CDLL("libc.dylib")
# linux
#﻿libc = CDLL("libc.so.6")
message_string = "Hello world!\n"
libc.printf("Testing: %s", message_string)