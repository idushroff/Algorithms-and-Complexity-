# Licensing Information: You are free to use or extend this file for
# educational purposes provided that (1) you retain this notice, and
# (2) you provide clear attribution to the University of Melbourne,
# including a link to https://cis.unimelb.edu.au.
#
# This file was created as part of teaching material for COMP90038
# January, 2020

ALPHA_SIZE = 256


def FindShifts(P):
    m = len(P)
    Shift = [m] * ALPHA_SIZE
    for j in range(m - 1):
        Shift[ord(P[j])] = m - j - 1
    return Shift


def Horspool(P, T):
    m = len(P)
    n = len(T)
    Shift = FindShifts(P)
    i = m - 1
    while i < n:
        k = 0
        while k < m and P[m - 1 - k] == T[i - k]:
            k = k + 1
        if k == m:
            return i - m + 1
        else:
            i = i + Shift[ord(T[i])]
    return -1


def test():
    print(Horspool("ABCD", "ACBBBIPABCDD"))
    print(Horspool("ABCD", "ACBBBIPABCCDD"))


if __name__ == "__main__":
    test()


"""alternative code i found online"""


import collections

def strStr_horspool(needle, haystack):
    m, n = len(haystack), len(needle)
    if m < n:
        return -1
    bad_char_jump = collections.defaultdict(lambda: n)
    for i in range(n - 1):
        bad_char_jump[needle[i]] = n - i - 1
    pos = 0
    while pos <= m - n:
        j = n - 1
        while j >= 0 and needle[j] == haystack[pos + j]:
            j -= 1
        if j == -1:
            return pos
        else:
            pos += bad_char_jump[haystack[pos + n - 1]]
    return -1

print(strStr_horspool("LOOKS", "The_WEATHER_LOOKS_FANTASTIC_TODAY"))
print(strStr_horspool("ABCD", "ACBBBIPABCDD"))
print(strStr_horspool("ABCD", "ACBBBIPABCCDD"))