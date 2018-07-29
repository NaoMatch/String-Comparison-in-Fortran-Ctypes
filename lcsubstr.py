
from ctypes import *
import numpy as np

lcsubstrF90 = CDLL("./LCSubStr.dll")

lcsubstrF90.lcsubstr_len_.argtypes = [POINTER(c_int), c_char_p, c_char_p, c_long, c_long]
lcsubstrF90.lcsubstr_len_.restype  = None

lcsubstrF90.lcsubstr_pos_.argtypes = [np.ctypeslib.ndpointer(dtype = np.int32), c_char_p, c_char_p, c_long, c_long]
lcsubstrF90.lcsubstr_pos_.restype  = None

def LCSubStr_length(str1, str2):
    try:
        char1 = str1.encode(); char2 = str2.encode()
    except:
        char1=str1; char2=str2
    length = c_int(0)
    lenc1 = len(char1)
    lenc2 = len(char2)
    lcsubstrF90.lcsubstr_len_(byref(length), char1, char2, lenc1, lenc2)
    return length.value

def LCSubStr_length_norm(str1, str2):
    return LCSubStr_length(str1, str2) / max([len(str1), len(str2)])

def LCSubStr_distance(str1, str2):
    return max([len(str1), len(str2)]) - LCSubStr_length(str1, str2)

def LCSubStr_distance_norm(str1, str2):
    return 1-LCSubStr_length(str1, str2) / max([len(str1), len(str2)])

def LCSubStr_position(str1, str2):
    try:
        char1 = str1.encode(); char2 = str2.encode()
    except:
        char1=str1; char2=str2
    lcs_pos = np.zeros(3, dtype = np.int32)
    lenc1 = len(char1)
    lenc2 = len(char2)
    lcsubstrF90.lcsubstr_pos_(lcs_pos, char1, char2, lenc1, lenc2)
    return [lcs_pos[-1]-lcs_pos[0], lcs_pos[-1]]

def LCSubStr_character(str2, str1):
    try:
        char1 = str1.encode(); char2 = str2.encode()
    except:
        char1=str1; char2=str2
    lcs_pos = np.zeros(3, dtype = np.int32)
    lenc1 = len(char1)
    lenc2 = len(char2)
    lcsubstrF90.lcsubstr_pos_(lcs_pos, char1, char2, lenc1, lenc2)
    ini, fin = lcs_pos[-1]-lcs_pos[0], lcs_pos[-1]
    return str1[ini:fin]
