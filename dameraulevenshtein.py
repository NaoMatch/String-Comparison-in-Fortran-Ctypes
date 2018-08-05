from ctypes import *
# https://thetaiko.wordpress.com/2011/01/21/damerau-levenshtein-distance-in-python/
dameraulevenshtein = CDLL("./Damerau_Levenshtein.dll")

dameraulevenshtein.dameraulevenshteindistance_.argtypes = [POINTER(c_int), c_char_p, c_char_p, c_long, c_long]
dameraulevenshtein.dameraulevenshteindistance_.restype  = None

def dameraulevenshteindistance(str1, str2):
    if (str1==str2): return 0
    try:
        char1 = str1.encode(); char2 = str2.encode()
    except:
        char1=str1; char2=str2
    distance = c_int(0)
    lenc1 = len(char1)
    lenc2 = len(char2)
    dameraulevenshtein.dameraulevenshteindistance_(byref(distance), char1, char2, lenc1, lenc2)
    return distance.value

def dameraulevenshteinsimilarity(str1, str2):
    max_len = max([len(str1), len(str2)])
    distance = dameraulevenshteindistance(str1, str2)
    return max_len - distance

def dameraulevenshteindistance_norm(str1, str2):
    max_len = max([len(str1), len(str2)])
    distance = dameraulevenshteindistance(str1, str2)
    return distance / float(max_len)

def dameraulevenshteinsimilarity_norm(str1, str2):
    max_len = max([len(str1), len(str2)])
    similarity = dameraulevenshteinsimilarity(str1, str2)
    return similarity / float(max_len)
    
