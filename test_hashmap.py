import hashmap_problems as code

def test_isAnagram_242():
    assert code.isAnagram_242('anagram', 'nagaram') == True
    assert code.isAnagram_242('rat', 'car') == False

def test_commonChars_1002():
    assert code.commonChars_1002(["bella","label","roller"]) == ["e","l","l"]
    assert code.commonChars_1002(["cool","lock","cook"]) == ["c","o"]

def test_intersection_349():
    assert code.intersection_349([1, 2, 2, 1], [2, 2]) == [2]
    assert code.intersection_349([4,9,5], [9,4,9,8,4]) == [9, 4]

def test_isHappy_202():
    assert code.isHappy_202(19) == True
    assert code.isHappy_202(2) == False
