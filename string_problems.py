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
        lst[i : i+k] = reverse_sublst(lst[i: i+k])
    # convert list back to str
    return "".join(lst)
