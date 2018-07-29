
from ctypes import *

gpm = CDLL("./GestaltPatternMatching.dll")

gpm.gestaltpatternmatching_.argtypes = [POINTER(c_int), c_char_p, c_char_p, c_long, c_long]
gpm.gestaltpatternmatching_.restype  = None

def gpmscore(str1, str2):
    try:
        char1 = str1.encode(); char2 = str2.encode()
    except:
        char1=str1; char2=str2
    score = c_int(0)
    lenc1 = len(char1)
    lenc2 = len(char2)
    gpm.gestaltpatternmatching_(byref(score), char1, char2, lenc1, lenc2)
    return score.value / (len(str1)+len(str2))

#
