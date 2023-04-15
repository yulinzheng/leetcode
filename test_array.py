import array_problems as code

def test_search_704():
    assert code.search_704([], 9) == -1
    assert code.search_704([-1, 10], 9) == -1
    assert code.search_704([-1, 0, 1, 3, 5, 9, 15], 9) == 5
    assert code.search_704([9, 12, 15, 20], 9) == 0
    assert code.search_704([0, 9, 10], 9) == 1
    assert code.search_704([1, 9, 10, 11], 9) == 1
    assert code.search_704([1, 9], 1) == 0
    assert code.search_704([1, 9], 9) == 1

def test_removeElement_27():
    lst_a = [3, 2, 2, 3]
    end = code.removeElement_27_v1(lst_a, 3)
    assert lst_a[:end] == [2, 2]
    lst_b = [0, 1, 2, 2, 3, 0, 4, 2]
    end = code.removeElement_27_v1(lst_b, 2)
    assert lst_b[:end] == [0, 1, 3, 0, 4]
    lst_c = [4, 5]
    end = code.removeElement_27_v1(lst_c, 4)
    assert lst_c[:end] == [5]

    lst_a = [3, 2, 2, 3]
    end = code.removeElement_27_v2(lst_a, 3)
    assert lst_a[:end] == [2, 2]
    lst_b = [0, 1, 2, 2, 3, 0, 4, 2]
    end = code.removeElement_27_v2(lst_b, 2)
    assert lst_b[:end] == [0, 1, 3, 0, 4]
    lst_c = [4, 5]
    end = code.removeElement_27_v2(lst_c, 4)
    assert lst_c[:end] == [5]

def test_sortedSquares_977():
    assert code.sortedSquares_977_v1([-4,-1,0,3,10]) == [0, 1, 9, 16, 100]
    assert code.sortedSquares_977_v1([-7,-3,2,3,11]) == [4, 9, 9, 49, 121]
    assert code.sortedSquares_977_v2([-4,-1,0,3,10]) == [0, 1, 9, 16, 100]
    assert code.sortedSquares_977_v2([-7,-3,2,3,11]) == [4, 9, 9, 49, 121]

def test_minSubArrayLen_209():
    assert code.minSubArrayLen_209_v1(7, [2,3,1,2,4,3]) == 2
    assert code.minSubArrayLen_209_v1(4, [1,4,4]) == 1
    assert code.minSubArrayLen_209_v2(7, [2,3,1,2,4,3]) == 2
    assert code.minSubArrayLen_209_v2(4, [1,4,4]) == 1
    assert code.minSubArrayLen_209_v3(7, [2,3,1,2,4,3]) == 2
    assert code.minSubArrayLen_209_v3(4, [1,4,4]) == 1

def test_generateMatrix_59():
    assert code.generateMatrix_59(3) == [[1,2,3], [8,9,4],[7,6,5]]
    assert code.generateMatrix_59(1) == [[1]]