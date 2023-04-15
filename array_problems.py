def search_704(nums, target):
    """
    Given an array of integers nums which is sorted in ascending order,
    and an integer target, write a function to search target in nums.
    If target exists, then return its index. Otherwise, return -1.

    O(logn):
        1. left = half + 1 because we already know nums[half] is not target, 
            vice versa for right = half - 1
        2. meaning left could equal to right, therefore left <= right,
            not left < right
    """
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] < target:
            left = mid + 1
        elif nums[mid] > target:
            right = mid - 1
        else:
            return mid
    return -1

def removeElement_27_v1(nums, val):
    """
    Given an integer array nums and an integer val,
    remove all occurrences of val in nums in-place.
    Return k after placing the final result in the first k slots of nums.

    O(n^2): when val occurs, shift entire list left by 1 
    """
    i = 0
    k = len(nums)

    while i < k:
        if nums[i] == val:
            for j in range(i+1, len(nums)):
                nums[j-1] = nums[j]
            # length of final list has decremented by 1
            k -= 1
        else:
            i += 1
    return k

def removeElement_27_v2(nums, val):
    """
    O(n): j finds element equal to val, i finds replacement
          j: fast pointer, i: slow pointer
    """
    j = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[j] = nums[i]
            j += 1
    return j

def sortedSquares_977_v1(nums):
    """
    Given an integer array nums sorted in non-decreasing order,
    return an array of the squares of each number sorted in non-decreasing order.

    O(nlogn): square nums then sort
    """
    for i in range(len(nums)):
        squared = nums[i] ** 2
        nums[i] = squared
        i += 1
    nums.sort()
    return nums

def sortedSquares_977_v2(nums):
    """
    O(n): have two pointers at the start and end of nums,
          add the bigger squared number to the front a new list.
    """
    result = []
    i, j = 0, len(nums) - 1
    while i <= j:
        squared_i = nums[i] ** 2
        squared_j = nums[j] ** 2
        if squared_i >= squared_j:
            result = [squared_i] + result
            i += 1
        else:
            result = [squared_j] + result
            j -= 1
    return result

def minSubArrayLen_209_v1(target, nums):
    """
    Given an array of positive integers nums and a positive integer target,
    return the minimal length of a subarray whose sum >= target.
    If there is no such subarray, return 0 instead.

    O(n^2): find the sum and len of all possible subarrays
    """
    min_len = 10**5 + 1

    for i in range(len(nums)):
        sub_sum = 0
        sub_len = 0
        # subarray starting at i
        j = i
        while sub_sum < target and j < len(nums):
            sub_sum += nums[j]
            sub_len += 1
            j += 1
        # update min_sum if sum > target
        if sub_sum >= target:
            min_len = min(min_len, sub_len)

    if min_len == 10**5 + 1:
        return 0
    else:
        return min_len

def minSubArrayLen_209_v2(target, nums):
    """
    O(n^2): same logic, better style
    """
    min_len = 10**5 + 1

    for i in range(len(nums)):
        sub_sum = 0
        sub_len = 0
        # subarray starting at i
        for j in range(i, len(nums)):
            sub_sum += nums[j]
            if sub_sum < target:
                sub_len += 1
            else:
                min_len = sub_len + 1

    return 0 if min_len == 10**5 + 1 else min_len

def minSubArrayLen_209_v3(target, nums):
    """
    O(n): sliding window
          two pointers left and right, increment right till sum >= target
          then shrink window by incrementing left if sum >= target
    """
    min_len = 10**5 + 1
    window_sum = 0
    window_len = 0
    left= 0

    for right in range(len(nums)):
        window_sum += nums[right]
        window_len += 1
        while window_sum >= target:
            min_len = min(min_len, window_len)
            # shrink window
            window_sum -= nums[left]
            window_len -= 1
            left += 1

    return 0 if min_len == 10**5 + 1 else min_len

def generateMatrix_59(n):
    """
    Given a positive integer n, generate an n x n matrix
    filled with elements from 1 to n2 in spiral order.

    O(n^2): 4 directions as one loop
            index out of range is fine because range() is empty
    """
    result = [ [ 0 for i in range(n) ] for j in range(n) ]
    loop = 0
    num = 1
    while num <= n * n:
        # right
        for k in range(loop, n - loop):
            result[loop][k] = num
            num += 1
        # down
        for k in range(loop + 1, n - loop):
            result[k][n - 1 - loop] = num
            num += 1
        # left
        for k in list(reversed(range(loop, n - loop - 1))):
            result[n - 1 - loop][k] = num
            num += 1
        # up
        for k in list(reversed(range(loop + 1, n - loop - 1))):
            result[k][loop] = num
            num += 1
        # increment loop
        loop += 1
    return result
