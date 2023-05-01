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

def strStr_28_v2(haystack, needle):
    """
    Time: O(n + m)
    Space: O(m), m being size of the prefix table

    This is a classic problem that uses the KMP algorithm.
    """

def repeatedSubstringPattern_459(s):
    """
    Given a string s, check if it can be constructed by
    taking a substring of it and appending multiple copies
    of the substring together.

    Time: O()
    Space: O()
    """
    return