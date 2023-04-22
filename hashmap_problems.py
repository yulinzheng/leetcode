def isAnagram_242(s, t):
    """
    Given two strings s and t,
    return true if t is an anagram of s, false otherwise.
    What if the inputs contain Unicode characters?
    How would you adapt your solution to such a case?

    Time: O(m + n)
    Space: O(1)

    Space can be less if we reuse the same hashmap.
        Simply decrement each occurrence by 1,
        and check if all values are 0 in the end.

    Space can be less if we use an array with 26 slots.
        See problem 1002.
    """
    hashmap_s = {}
    for letter in s:
        if letter not in hashmap_s:
            hashmap_s[letter] = 1
        else:
            hashmap_s[letter] += 1

    hashmap_t = {}
    for letter in t:
        if letter not in hashmap_t:
            hashmap_t[letter] = 1
        else:
            hashmap_t[letter] += 1

    return hashmap_s == hashmap_t

def commonChars_1002(words):
    """
    Given a string array words,
    return an array of all characters that
    show up in all strings within the words
    (including duplicates).
    You may return the answer in any order.

    Time: O(n)
    Space: O(n)

    Use a 26 x (num words) matrix,
        take the min of each letter's occurrences.
    """
    matrix = [[0] * len(words) for i in range(26)]
    # build the matrix
    for i in range(len(words)):
        word = words[i]
        for letter in word:
            matrix[ord(letter) - ord('a')][i] += 1
    # find the min of each row and add to result list
    # e.g. min of 'a' is 2, then append ['a', 'a']
    result = []
    for i in range(26):
        min_count = min(matrix[i])
        result += [chr(i + ord('a'))] * min_count
    return result

def intersection_349(nums1, nums2):
    """
    Given two integer arrays nums1 and nums2,
    return an array of their intersection.
    Each element in the result must be unique,
    you may return the result in any order.

    Time: O(m + n)
    Space: O(n)
    """
    count = {}
    for num in nums1:
        if num not in count:
            count[num] = 1
    result = []
    for num in nums2:
        if num in count and count[num] == 1:
            result.append(num)
            count[num] = 0
    return result

def isHappy_202(n):
    """
    Write an algorithm to determine if a n is happy.
    A happy number is a number defined by:

        - Start with a positive integer.
        - Replace it by the sum of squares of its digits.
        - Repeat until it equals 1,
            or loops in a cycle which does not include 1.
    Numbers for which this process ends in 1 are happy.

    Time: O(logn)
    Space: O(logn)
    """
    seen = set()
    while n != 1:
        sum_digits = 0
        while n > 0:
            digit = n % 10
            n = n // 10
            sum_digits += digit * digit
        # update n
        n = sum_digits
        # check for loop
        if n in seen:
            return False
        else:
            seen.add(n)
    return True

def twoSum_1(nums, target):
    """
    Given an array of integers nums and an int target,
    return indices of the two numbers such that
    they add up to target.

    Time: O(n)
    Space: O(n)
    """
    hashmap = {}
    for i, num in enumerate(nums):
        other = target - num
        if other in hashmap:
            return [i, hashmap[other]]
        else:
            hashmap[num] = i
    return []

def fourSumCount_454(nums1, nums2, nums3, nums4):
    """
    Given four integer arrays nums1, nums2, nums3, nums4
    all of length n, return the number of tuples (i, j, k, l)
    such that:
        0 <= i, j, k, l < n
        nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0

    Time: O(n^2)
    Space: O(n^2)
    """
    # map all unique sums of nums1 & nums2
    # to their number of occurrences
    sum_1 = {}
    for num_1 in nums1:
        for num_2 in nums2:
            sum_num = num_1 + num_2
            if sum_num not in sum_1:
                sum_1[sum_num] = 1
            else:
                sum_1[sum_num] += 1
    # map all unique sums of nums3 & nums4
    # to their number of occurrences
    sum_2 = {}
    for num_3 in nums3:
        for num_4 in nums4:
            sum_num = num_3 + num_4
            if sum_num not in sum_2:
                sum_2[sum_num] = 1
            else:
                sum_2[sum_num] += 1
    # calculate # of possible sums
    count = 0
    for sum_num in sum_1:
        other = 0 - sum_num
        if other in sum_2:
            count += sum_1[sum_num] * sum_2[other]
    return count

def canConstruct_383(ransomNote, magazine):
    """
    Given two strings ransomNote and magazine,
    return true if ransomNote can be constructed
    by using the letters from magazine, false otherwise.

    Each letter in magazine can only be used once.

    Time: O(n)
    Space: O(1)

    Space can be less if we use an array with 26 slots.
        See problem 1002.
    """
    # map each letter to its number of occurrences
    dict_mag = {}
    for letter in magazine:
        if letter not in dict_mag:
            dict_mag[letter] = 1
        else:
            dict_mag[letter] += 1
    # reduce each letter's number of occurrences by 1
    for letter in ransomNote:
        if letter not in dict_mag:
            return False
        if dict_mag[letter] == 0:
            return False
        dict_mag[letter] -= 1
    return True

def threeSum_15_v1(nums):
    """
    Given an integer array nums, return all the triplets
    [nums[i], nums[j], nums[k]] such that i != j, i != k, j != k,
    and nums[i] + nums[j] + nums[k] == 0.

    Solution set must not contain duplicate triplets.

    Time: O(n^2)
    Space: O(n)

    Using two sets.
    """
    nums.sort()
    end = len(nums)
    result = set()

    for i in range(end-2):
        target = 0 - nums[i]
        seen = set()
        for j in range(i+1, end):
            third = target - nums[j]
            if third not in seen:
                seen.add(nums[j])
            else:
                result.add((nums[i], nums[j], third))
    return [list(triplet) for triplet in result]

def threeSum_15_v2(nums):
    """
    Time: O()
    Space: O()

    Using two pointers.
    """

def fourSum_18(nums, target):
    """

    """
    return