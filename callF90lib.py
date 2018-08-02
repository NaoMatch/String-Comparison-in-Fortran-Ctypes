import sys
import textdistance
import py_common_subseq
import hashlib
import numpy as np
from ctypes import *
import datetime
from difflib import SequenceMatcher
import difflib

sys.path.append("./")
from strdist import *
from hamming import *
from levenshtein import *
from lcsubstr import *
from lcsubseq import *
from gestaltpatternmatching import *
from jaro_winkler import *

now = str(datetime.datetime.now()).encode()
hash1 = hashlib.sha512(now).hexdigest()
hash2 = hashlib.sha512(hash1.encode()).hexdigest()
hash3 = hashlib.sha512(hash2.encode()).hexdigest()

def callDiffLib(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).ratio()

# print(hash1)
# print(hash2)
# print(hash3)

# hash1="e8a829675f39fb5b94ca7b6fae2295482d1a1519ffe994fdbe30036aa4ce33eb1b47238113356a0194164282de6313c4889bbfa21ed05b7cfa56bdcd545f7a84"
# hash2="fa1e1c8199ca2b80f04d6f6ec3a6a06b0784d7567e8b295f9d0172f8aa43503b911bcad3be535be7fa9c089fb4f27c257da1e6d742cf4b1b6129d47de9c79001"
# hash1 = hash1[0:50]
# hash2 = hash2[0:50]
print("="*100)
print(hash1)
print(hash2)

compare2Functions(textdistance.jaro.distance, jarodistance, hash1, hash2,
                  "Jaro Distance : Python vs Fortran", 1000)

compare2Functions(textdistance.jaro.similarity, jarosimilarity, hash1, hash2,
                  "Jaro Similarity : Python vs Fortran", 1000)

compare2Functions(textdistance.jaro.normalized_distance, jarodistance, hash1, hash2,
                  "Jaro Distance (Normalized) : Python vs Fortran", 1000)

compare2Functions(textdistance.jaro.normalized_similarity, jarosimilarity, hash1, hash2,
                  "Jaro Similarity (Normalized) : Python vs Fortran", 1000)

compare2Functions(callDiffLib, gpmscore, hash1, hash2,
                  "Gestalt Pattern Matching : Python vs Fortran", 1000)

compare2Functions(lcs, LCSubSeq_character, hash1, hash2,
                  "Longest Common Subsequence : Python vs Fortran", 100)

compare2Functions(longestSubstring, LCSubStr_character, hash1, hash2,
                  "Longest Common Substring : Python(difflib) vs Fortran", 100)

compare2Functions(longestSubstring_length, LCSubStr_length, hash1, hash2,
                  "Longest Common Substring Distance : Python(difflib) vs Fortran", 1000)

compare2Functions(textdistance.lcsstr, LCSubStr_character, hash1, hash2,
                  "Longest Common Substring : Python(textdistance) vs Fortran", 100)

compare2Functions(textdistance.lcsstr.distance, LCSubStr_distance, hash1, hash2,
                  "Longest Common Substring Distance : Python(textdistance) vs Fortran", 1000)

compare2Functions(textdistance.lcsstr.similarity, LCSubStr_length, hash1, hash2,
                  "Longest Common Substring Similarity : Python(textdistance) vs Fortran", 1000)

compare2Functions(textdistance.lcsstr.normalized_distance, LCSubStr_distance_norm, hash1, hash2,
                  "Longest Common Substring Distance (Normalized) : Python(textdistance) vs Fortran", 1000)

compare2Functions(textdistance.lcsstr.normalized_similarity, LCSubStr_length_norm, hash1, hash2,
                  "Longest Common Substring Similarity (Normalized) : Python(textdistance) vs Fortran", 1000)

compare2Functions(textdistance.hamming.distance, hammingdistance, hash1, hash2,
                  "Hamming Distance : Python vs Fortran", 1000)

compare2Functions(textdistance.hamming.normalized_distance, hammingdistance_norm, hash1, hash2,
                  "Hamming Distance (Normalized) : Python vs Fortran", 1000)

compare2Functions(textdistance.hamming.similarity, hammingsimilarity, hash1, hash2,
                  "Hamming similarity : Python vs Fortran", 1000)

compare2Functions(textdistance.hamming.normalized_similarity, hammingsimilarity_norm, hash1, hash2,
                  "Hamming similarity (Normalized) : Python vs Fortran", 1000)

compare2Functions(textdistance.levenshtein.distance, levenshteindistance, hash1, hash2,
                  "Levenshtein Distance : Python vs Fortran", 20)

compare2Functions(textdistance.levenshtein.normalized_distance, levenshteindistance_norm, hash1, hash2,
                  "Levenshtein Distance (Normalized) : Python vs Fortran", 20)

compare2Functions(textdistance.levenshtein.similarity, levenshteinsimilarity, hash1, hash2,
                  "Levenshtein similarity : Python vs Fortran", 20)

compare2Functions(textdistance.levenshtein.normalized_similarity, levenshteinsimilarity_norm, hash1, hash2,
                  "Levenshtein similarity (Normalized) : Python vs Fortran", 20)
