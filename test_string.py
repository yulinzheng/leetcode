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