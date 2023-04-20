import hashmap_problems as code

def test_isAnagram_242():
    assert code.isAnagram_242('anagram', 'nagaram') == True
    assert code.isAnagram_242('rat', 'car') == False

def test_commonChars_1002():
    result = code.commonChars_1002(["bella","label","roller"])
    assert set(result) == set(["e","l","l"])
    result = code.commonChars_1002(["cool","lock","cook"])
    assert set(result)== set(["c","o"])

def test_intersection_349():
    result = code.intersection_349([1, 2, 2, 1], [2, 2])
    assert set(result) == set([2])
    result = code.intersection_349([4,9,5], [9,4,9,8,4])
    assert set(result) == set([9, 4])

def test_isHappy_202():
    assert code.isHappy_202(19) == True
    assert code.isHappy_202(2) == False

def test_twoSum_1():
    result = code.twoSum_1([2,7,11,15], 9)
    assert set(result) == set([0, 1])
    result = code.twoSum_1([3,2,4], 6)
    assert set(result) == set([1, 2])

def test_fourSumCount_454():
    result = code.fourSumCount_454([1,2], [-2,-1], [-1,2], [0,2])
    assert result == 2
    result = code.fourSumCount_454([-1,-1], [-1,1], [-1,1], [1,-1])
    assert result == 6