def reverseString_344(s):
    """
    Write a function that reverses a string.
    You must do this in-place with O(1) extra memory.

    Time: O(n)
    Space: O(1)
    """
    half = len(s) // 2
    for i in range(half):
        s[i], s[len(s)-1 - i] = s[len(s)-1 - i], s[i]

def reverseStr_541(s, k):
    """
    Given a string s and an integer k,
    reverse the first k characters for every 2k characters
    counting from the start of the string.

    If there are fewer than k characters left,
    reverse all of them.
    If there are < 2k but >= k characters,
    reverse the first k characters.

    Time: O(n)
    Space: O(n)
    """
    def reverse_sublst(s):
        left = 0
        right = len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        return s
    # convert string to list
    lst = [char for char in s]
    # reverse each sublist
    for i in range(0, len(lst), 2*k):
        lst[i: i+k] = reverse_sublst(lst[i: i+k])
    # convert list back to str
    return "".join(lst)

def reverseWords_151(s):
    """
    Given an input string s, reverse the order of words.

    Time: O(n)
    Space: O(n)
    """
    words = s.split()
    result = []
    for word in words:
        result = [word] + result
    return " ".join(result)

def strStr_28_v1(haystack, needle):
    """
    Given two strings needle and haystack, return the
    index of the first occurrence of needle in haystack,
    or -1 if needle is not part of haystack.

    Using the default index function, just for fun.
    """
    try:
        return haystack.index(needle)
    except ValueError:
        return -1

"""
KMP algorithm:
    The basic idea is whenever we detect a mismatch,
    we already know some of the characters in the text of the next window.
    We take advantage of this information to avoid matching the characters
    that we know will anyway match.

    txt: text string
    pat: pattern str
    lps[i]: longest prefix that is also a suffix for pat[0..i]

    For example,
        lps[] for pattern "AAAA" is [0, 1, 2, 3]
        lps[] for pattern "AAABAAA" is [0, 1, 2, 0, 1, 2, 3]
"""

def strStr_28_v2(text, pattern):
    """
    Time: O(n + m)
    Space: O(m), m being size of the prefix table
    """
    # longest matching prefix suffix
    lps = [0] * len(pattern)
    j = 0 # points to end of current longest prefix
    i = 1 # points to end of current longest suffix

    while i < len(pattern):
        if pattern[j] == pattern[i]:
            # char matched
            lps[i] = j + 1
            j += 1
            i += 1
        else:
            if j != 0:
                # j moves to end of longest prefix for pattern[0: j-1]
                j = lps[j-1]
            else:
                # i at unseen char, no match found
                lps[i] = 0
                i += 1

    t = 0 # ptr for text
    p = 0 # ptr for pattern
    while t < len(text):
        if text[t] == pattern[p]:
            t += 1
            p += 1
        else:
            if p != 0:
                p = lps[p-1]
            else:
                t += 1
        # pattern has been found
        if p == len(pattern):
            return t - len(pattern)
    # pattern not found
    return -1

def repeatedSubstringPattern_459_v1(s):
    """
    Given a string s, check if it can be constructed
    by taking a substring of it and appending multiple
    copies of the substring together.

    Time: O(n^2)
    Space: O(1)

    Using brute force: 2 loops
    """
    half = len(s)//2 + 1

    # first loop
    for i in range(1, half):
        substring = s[:i]

        if len(s) % len(substring) == 0:
            num_copies = len(s) // len(substring)
            # second loop
            if s == substring * num_copies:
                return True

    return False

def repeatedSubstringPattern_459_v2(s):
    """
    Time: O(n)
    Space: O(n)

    Using KMP:
                For a true return value, s must have
                the same longest prefix and suffix,
                and they're offset by len(substring).
                And len(s) must be divisible by offset.
    For example:
                s:          abababab
                l_prefix:   ababab
                l_suffix:     ababab
    """
