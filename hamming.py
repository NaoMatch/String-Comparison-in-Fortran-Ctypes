import sys
from ctypes import *

hammingdist = CDLL("./HammingDistance.dll")

hammingdist.hammingdistance_.argtypes = [POINTER(c_int), c_char_p, c_char_p, c_long, c_long]
hammingdist.hammingdistance_.restype  = None

hammingdist.hammingsimilarity_.argtypes = [POINTER(c_int), c_char_p, c_char_p, c_long, c_long]
hammingdist.hammingsimilarity_.restype  = None

"""
Hamming :
  - Hamming Distance
  - Hamming Normlized Distance
  - Hamming Similarity
  - Hamming Normlized Similarity
"""
def hammingdistance(str1, str2):
    if (len(str1) != len(str2)): sys.exit("Error : Length Minmatch! {} / {}".format(len(str1), len(str2)))
    try:
        char1 = str1.encode(); char2 = str2.encode()
    except:
        char1=str1; char2=str2
    distance = c_int(0)
    lenc1 = len(char1)
    lenc2 = len(char2)
    hammingdist.hammingdistance_(byref(distance), char1, char2, lenc1, lenc2)
    return distance.value

def hammingdistance_norm(str1, str2):
    if (len(str1) != len(str2)): sys.exit("Error : Length Minmatch! {} / {}".format(len(str1), len(str2)))
    dist = hammingdistance(str1, str2)
    return dist / float(len(str1))

def hammingsimilarity(str1, str2):
    if (len(str1) != len(str2)): sys.exit("Error : Length Minmatch! {} / {}".format(len(str1), len(str2)))
    try:
        char1 = str1.encode(); char2 = str2.encode()
    except:
        char1=str1; char2=str2
    similarity = c_int(0)
    lenc1 = len(char1)
    lenc2 = len(char2)
    hammingdist.hammingsimilarity_(byref(similarity), char1, char2, lenc1, lenc2)
    return similarity.value

def hammingsimilarity_norm(str1, str2):
    if (len(str1) != len(str2)): sys.exit("Error : Length Minmatch! {} / {}".format(len(str1), len(str2)))
    dist = hammingsimilarity(str1, str2)
    return dist / float(len(str1))
