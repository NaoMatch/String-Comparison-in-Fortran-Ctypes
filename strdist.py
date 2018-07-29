
import py_common_subseq
import hashlib
import numpy as np
from ctypes import *
import datetime
from difflib import SequenceMatcher


def lcs(a, b):
    lengths = [[0 for j in range(len(b)+1)] for i in range(len(a)+1)]
    # row 0 and column 0 are initialized to 0 already
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            if x == y:
                lengths[i+1][j+1] = lengths[i][j] + 1
            else:
                lengths[i+1][j+1] = max(lengths[i+1][j], lengths[i][j+1])
    # read the substring out from the matrix
    result = ""
    x, y = len(a), len(b)
    while x != 0 and y != 0:
        if lengths[x][y] == lengths[x-1][y]:
            x -= 1
        elif lengths[x][y] == lengths[x][y-1]:
            y -= 1
        else:
            assert a[x-1] == b[y-1], "ERROR"
            result = a[x-1] + result
            x -= 1
            y -= 1
    return result

def longestSubstring(str1,str2):
    # initialize SequenceMatcher object with
    # input string
    seqMatch = SequenceMatcher(None,str1,str2)

    # find match of longest sub-string
    # output will be like Match(a=0, b=0, size=5)
    match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))

    # print longest substring
    if (match.size!=0):
        # print (str1[match.a: match.a + match.size])
        return str1[match.a: match.a + match.size]
    else:
        # print ('No longest common sub-string found')
        return None

def longestSubstring_length(str1,str2):
    # initialize SequenceMatcher object with
    # input string
    seqMatch = SequenceMatcher(None,str1,str2)

    # find match of longest sub-string
    # output will be like Match(a=0, b=0, size=5)
    match = seqMatch.find_longest_match(0, len(str1), 0, len(str2))

    # print longest substring
    if (match.size!=0):
        # print (str1[match.a: match.a + match.size])
        return len(str2[match.b: match.b + match.size])
    else:
        # print ('No longest common sub-string found')
        return 0

def timeChecker(func, str1, str2, lang, n):
    strstr1 = str1
    strstr2 = str2
    st1 = datetime.datetime.now()
    for i in range(n):
        x = func(strstr1, strstr2)
    ed1 = datetime.datetime.now()
    diff1 = ed1-st1
    print("\n {} [sec]".format(diff1))
    print(" Result {} : {}".format(lang, x))
    return diff1

def compare2Functions(func1, func2, str1, str2, discription, n):
    print("\n\n ----- {} -----".format(discription))
    diff1 = timeChecker(func1, str1, str2, "Python ", n)
    diff2 = timeChecker(func2, str1, str2, "Fortran", n)
    print("\n Ratio {}".format(diff1/diff2))
