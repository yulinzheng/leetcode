import string_problems as code

def test_reverseString_344():
    s = ["h","e","l","l","o"]
    code.reverseString_344(s)
    assert s == ["o","l","l","e","h"]
    s = ["H","a","n","n","a","h"]
    code.reverseString_344(s)
    assert s == ["h","a","n","n","a","H"]

def test_reverseStr_541():
    result = code.reverseStr_541("a", 2)
    assert result == "a"
    result = code.reverseStr_541("abcd", 4)
    assert result == "dcba"
    result = code.reverseStr_541("abcdefg", 2)
    assert result == "bacdfeg"
    result = code.reverseStr_541("abcd", 2)
    assert result == "bacd"
    result = code.reverseStr_541("abcdefg", 8)
    assert result == "gfedcba"

def test_reverseWords_15():
    result = code.reverseWords_151("the sky is blue")
    assert result == "blue is sky the"
    result = code.reverseWords_151(" a good   example")
    assert result == "example good a"

def test_strStr_28():
    result = code.strStr_28_v1("sadbutsad", "sad")
    assert result == 0
    result = code.strStr_28_v1("leetcode", "leeto")
    assert result == -1
    result = code.strStr_28_v2("sadbutsad", "sad")
    assert result == 0
    result = code.strStr_28_v2("leetcode", "leeto")
    assert result == -1

def test_repeatedSubstringPattern_45():
    result = code.repeatedSubstringPattern_459_v1("abab")
    assert result == True
    result = code.repeatedSubstringPattern_459_v1("aabaab")
    assert result == True
    result = code.repeatedSubstringPattern_459_v1("abcabc")
    assert result == True
    result = code.repeatedSubstringPattern_459_v1("ababca")
    assert result == False
    result = code.repeatedSubstringPattern_459_v2("abab")
    assert result == True
    result = code.repeatedSubstringPattern_459_v2("aabaab")
    assert result == True
    result = code.repeatedSubstringPattern_459_v2("abcabc")
    assert result == True
    result = code.repeatedSubstringPattern_459_v2("ababca")
    assert result == False
