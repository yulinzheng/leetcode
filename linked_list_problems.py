"""
See also:
    my_linked_list_707.py
"""

class ListNode(object):
    # singly-linked list
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements_203(head, val):
    """
    Given the head of a linked list and an integer val,
    remove all the nodes of the linked list that has Node.val == val,
    and return the new head.

    O(n):
    1. Need to keep track of new head: create a dummy head
    2. Need to keep track of prev node: start with dummy head
    """
    dummy_head = ListNode(next=head)
    prev = dummy_head
    while prev.next != None:
        curr = prev.next
        if curr.val == val:
            # delete curr node
            prev.next = curr.next
        else:
            # move on
            prev = prev.next
    return dummy_head.next

def reverseList_206_iterative(head):
    """
    O(n) time
    O(1) space
    """
    # two pointers prev and curr
    curr = head
    prev = None
    while curr:
        temp = curr.next
        # reverse direction of pointer
        curr.next = prev
        # increment prev and curr
        prev = curr
        curr = temp
    return prev

def reverseList_206_recursive(head):
    """
    Given the head of a singly linked list, reverse the list,
    and return the reversed list.

    O(n) time
    O(n) space
    """
    if head == None:
        return
    if head.next == None:
        return head
    # head of reversed rest
    reversed_rest = reverseList_206_recursive(head.next)
    # reverse direction of pointer between head and head.next
    # head.next is the original one before the recursive call
    head.next.next = head
    head.next = None
    return reversed_rest

def swapPairs_24_iterative(head):
    """
    Given a linked list, swap every two adjacent nodes and return its head.
    You must solve the problem without modifying the values in the list's nodes,
    only nodes themselves may be changed.

    O(n) time
    O(1) space
    """
    dummy_head = ListNode(next=head)
    prev = dummy_head

    while prev.next and prev.next.next:
        curr = prev.next
        post = curr.next

        prev.next = post
        curr.next = post.next
        post.next = curr

        prev = prev.next.next

    return dummy_head.next

def swapPairs_24_recursive(head):
    """
    O(n) time
    O(n) space
    """
    if head == None or head.next == None:
        return head

    newhead = head.next
    swapped = swapPairs_24_iterative(head.next.next)

    newhead.next = head
    head.next = swapped

    return newhead

def removeNthFromEnd_19_v1(head, n):
    """
    Given the head of a linked list,
    remove the nth node from the end of the list and return its head.

    O(2n) two passes:
            1st pass count size of linked list
            2nd pass delete node at (size - n)
    """
    size = 0
    curr = head
    while curr:
        curr = curr.next
        size += 1

    idx = size - n
    dummy_head = ListNode(next=head)
    prev = dummy_head

    while idx:
        prev = prev.next
        idx -= 1

    prev.next = prev.next.next
    return dummy_head.next

def removeNthFromEnd_19_v2(head, n):
    """
    O(n) one pass:
            Fast pointer advance by n,
            slow pointer then advance together.
            When fast pointer reaches None,
            slow pointer reaches (size - n)
    """
    fast = head
    dummy_head = ListNode(next=head)
    slow = dummy_head

    while n:
        fast = fast.next
        n -= 1

    while fast:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return dummy_head.next

def getIntersectionNode_160(headA, headB):
    """
    Given the heads of two singly linked-lists headA and headB,
    return the node at which the two lists intersect.
    If the two linked lists have no intersection at all, return null.

    O(m + n):
        Say, the number of nodes after intersection is n, then
            sizeA = A + n
            sizeB = B + n
        Note, sizeA - sizeB = A - B, which means
            we can find the intersection by having
            two pointers offset by (sizeA - sizeB)
    """
    def get_size(head):
        size = 0
        curr = head
        while curr:
            curr = curr.next
            size += 1
        return size

    size_a = get_size(headA)
    size_b = get_size(headB)
    offset = abs(size_a - size_b)

    curr_a = headA
    curr_b = headB

    # offset pointer of the longer list
    if size_a > size_b:
        count = offset
        while count:
            curr_a = curr_a.next
            count -= 1
    else:
        count = offset
        while count:
            curr_b = curr_b.next
            count -= 1

    while curr_a:
        if curr_a != curr_b:
            curr_a = curr_a.next
            curr_b = curr_b.next
        else:
            return curr_a
    return None

def detectCycle_142(head):
    """
    Given the head of a linked list, return the node where the cycle begins.
    If there is no cycle, return null.

    O(n):
        Easy problem if adding a "self.seen" attribute to ListNode is allowed.
        Otherwise, use two pointers as follows.

            fast advance by two nodes,
            slow adcance by one node.

        fast and slow eventually will meet inside the cycle,
        but how to find where the cycle begins?

            Say, distance from head to intersection is x
            distance from head to where two pointers meet up is y
            distance from meetup back to intersection is z

            Then, when two pointers meet up:
                slow = x + y
                fast = x + y + n * (y + z)
                n = number of cycles fast went thru
            Because fast is x2 faster than slow:
                2 * (x + y) = x + y + n * (y + z)
                x = (n - 1) * (y + z) + z
            Bascially, x = z
    """
    # find index of meetup node
    fast = head
    slow = head
    idx = 0

    while True:
        try:
            fast = fast.next.next
            slow = slow.next
            idx += 1
            if fast == slow:
                break
        except AttributeError:
            return None

    # reset one of the pointers
    slow = head
    # find index of intersection
    while True:
        if fast == slow:
            return fast
        fast = fast.next
        slow = slow.next
