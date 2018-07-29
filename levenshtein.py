
from ctypes import *

levenshtein = CDLL("./Levenshtein.dll")

levenshtein.levenshteindistance_.argtypes = [POINTER(c_int), c_char_p, c_char_p, c_long, c_long]
levenshtein.levenshteindistance_.restype  = None

def levenshteindistance(str1, str2):
    if (str1==str2): return 0
    try:
        char1 = str1.encode(); char2 = str2.encode()
    except:
        char1=str1; char2=str2
    distance = c_int(0)
    lenc1 = len(char1)
    lenc2 = len(char2)
    levenshtein.levenshteindistance_(byref(distance), char1, char2, lenc1, lenc2)
    return distance.value

def levenshteindistance_norm(str1, str2):
    dist = levenshteindistance(str1, str2)
    dist = dist/float(max([len(str1), len(str2)]))
    return dist

def levenshteinsimilarity(str1, str2):
    dist = levenshteindistance(str1, str2)
    dist = max([len(str1), len(str2)]) - dist
    return dist

def levenshteinsimilarity_norm(str1, str2):
    return 1.0 - levenshteindistance_norm(str1, str2)

def levenshtein_python(s1, s2):
    """
    >>> levenshtein('kitten', 'sitting')
    3
    >>> levenshtein('あいうえお', 'あいうえお')
    0
    >>> levenshtein('あいうえお', 'かきくけこ')
    5
    """
    n, m = len(s1), len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    print(np.array(dp).shape)
    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            cost = 0 if s1[i - 1] == s2[j - 1] else 1
            dp[i][j] = min(dp[i - 1][j] + 1,         # insertion
                           dp[i][j - 1] + 1,         # deletion
                           dp[i - 1][j - 1] + cost)  # replacement
    return dp[n][m]
