
from ctypes import *
import numpy as np

lcsubseqF90 = CDLL("./LCSubSeq.dll")

lcsubseqF90.lcsubseq_len_.argtypes = [POINTER(c_int), c_char_p, c_char_p, c_long, c_long]
lcsubseqF90.lcsubseq_len_.restype  = None

lcsubseqF90.lcsubseq_pos_.argtypes = [np.ctypeslib.ndpointer(dtype = np.int32), c_char_p, c_char_p, c_long, c_long]
lcsubseqF90.lcsubseq_pos_.restype  = None

def LCSubSeq_length(str1, str2):
    try:
        char1 = str1.encode(); char2 = str2.encode()
    except:
        char1=str1; char2=str2
    lcs_len = c_int(0)
    lenc1 = len(char1)
    lenc2 = len(char2)
    lcsubseqF90.lcsubseq_len_(byref(lcs_len), char1, char2, lenc1, lenc2)
    return lcs_len.value

def LCSubSeq_character(str1, str2):
    try:
        char1 = str1.encode(); char2 = str2.encode()
    except:
        char1=str1; char2=str2
    lenc1 = len(char1)
    lenc2 = len(char2)
    min_len = min([lenc1, lenc2])
    lcs_pos = np.zeros(min_len*2, dtype = np.int32)
    lcsubseqF90.lcsubseq_pos_(lcs_pos, char1, char2, lenc1, lenc2)
    positions = lcs_pos[0:min_len*2:2]
    lcsubseq = ""
    for position in positions:
        if (position-1 == -1): break
        lcsubseq = str1[position-1] + lcsubseq
    return lcsubseq

def LCSubSeq_position(str1, str2):
    try:
        char1 = str1.encode(); char2 = str2.encode()
    except:
        char1=str1; char2=str2
    lenc1 = len(char1)
    lenc2 = len(char2)
    min_len = min([lenc1, lenc2])
    lcs_pos = np.zeros(min_len*2, dtype = np.int32)
    lcsubseqF90.lcsubseq_pos_(lcs_pos, char1, char2, lenc1, lenc2)
    positions = lcs_pos[0:min_len*2:2]
    return positions
