import sys
from ctypes import *

jarowinkler = CDLL("./Jaro_Winkler.dll")

jarowinkler.jarodistance_.argtypes = [POINTER(c_double), c_char_p, c_char_p, c_long, c_long]
jarowinkler.jarodistance_.restype  = None

def jarodistance(str2, str1):
    try:
        char1 = str1.encode(); char2 = str2.encode()
    except:
        char1 = str1; char2 = str2
    distance = 0.0
    distance = c_double(distance)
    lenc1 = len(char1)
    lenc2 = len(char2)
    jarowinkler.jarodistance_(byref(distance), char1, char2, lenc1, lenc2)
    return distance.value

def jarosimilarity(str1, str2):
    return 1.0 - jarodistance(str1, str2)

def jarodistance_norm(str1, str2):
    return jarodistance(str1, str2)

def jarosimilarity_norm(str1, str2):
    return jarosimilarity(str1, str2)
