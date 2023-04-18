def isAnagram_242(s, t):
    """
    Given two strings s and t,
    return true if t is an anagram of s, false otherwise.
    What if the inputs contain Unicode characters?
    How would you adapt your solution to such a case?

    Time: O(m + n)
    Space: O(m + n)

    Space can be O(m) if we reuse the same hashmap.
        Simply decrement each occurrence by 1,
        and check if all values are 0 in the end.

    Space can be O(1) if we use an array with 26 slots.
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
    Space: O(m)
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

    Time: O()
    Space: O()
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
    return

def fourSumCount(nums1, nums2, nums3, nums4):
    return