class Node(object):
    def __init__(self, val=0):
        self.val = val
        self.next = None
        # doubly linked list only
        # do not use for singly
        self.prev = None

"""
Why use a dummy head: no need to check if head is null
"""

class MySinglyLinkedList(object):
    """
    """
    def __init__(self):
        # dummy head
        self.head = Node()
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list.
        If the index is invalid, return -1.

        O(n)
        """
        if index > self.size - 1:
            return -1

        curr = self.head.next
        while index > 0:
            curr = curr.next
            index -= 1
        return curr.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list.
        After the insertion, the new node will be the first node of the linked list.

        O(1)
        """
        # or call self.addAtIndex(0, val)
        new_head = Node(val)
        old_head = self.head.next
        new_head.next = old_head
        self.head.next = new_head
        self.size += 1

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None

        O(n)
        """
        # or call self.addAtIndex(self.size, val)
        n = self.size
        prev = self.head
        while n > 0:
            prev = prev.next
            n -= 1

        tail = Node(val)
        prev.next = tail
        self.size += 1

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None

        O(n)
        """
        # add before the index-th node
        n = self.size
        if index > n:
            return

        prev = self.head
        while index > 0:
            prev = prev.next
            index -= 1

        node = Node(val)
        node.next = prev.next
        prev.next = node
        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None

        O(n)
        """
        n = self.size
        if index > n - 1:
            return

        prev = self.head
        while index > 0:
            prev = prev.next
            index -= 1
        prev.next = prev.next.next
        self.size -= 1



class MyDoublyLinkedList(object):
    """
    >>> node_a, node_b, node_c = Node(1), Node(2), Node(3)
    >>> doubly = MyDoublyLinkedList()
    >>> doubly.addAtHead(1)
    >>> doubly.addAtTail(3)
    >>> doubly.addAtIndex(1, 2)
    >>> doubly.list_values()
    0 -> 1 -> 2 -> 3 -> 0 -> 
    >>> doubly.get(0)
    1
    >>> doubly.get(1)
    2
    """
    def __init__(self, val=0):
        # dummy head
        self.head = Node()
        # dummy tail
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def list_values(self):
        curr = self.head
        output = ''
        while curr:
            output += str(curr.val) + ' -> '
            curr = curr.next
        print(output)

    def get_node(self, index):
        # O(n/2)
        if index < self.size // 2:
            curr = self.head.next
            while index > 0:
                curr = curr.next
                index -= 1
        else:
            curr = self.tail.prev
            while index < self.size - 1:
                curr = curr.prev
                index += 1
        return curr

    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index < 0 or index > self.size - 1:
            return -1
        return self.get_node(index).val

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        return self.addAtIndex(0, val)

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        return self.addAtIndex(self.size, val)

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        # for both addAtIndex and deleteAtIndex
        # it's better to find the prev instead of curr
        if index < 0 or index > self.size:
            return

        prev = self.head
        while index > 0:
            prev = prev.next
            index -= 1

        node = Node(val)
        node.next = prev.next
        node.next.prev = node
        prev.next = node
        node.prev = prev

        self.size += 1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        # for both addAtIndex and deleteAtIndex
        # it's better to find the prev instead of curr
        if index < 0 or index > self.size - 1:
            return

        prev = self.head
        while index > 0:
            prev = prev.next
            index -= 1

        prev.next = prev.next.next
        prev.next.prev = prev
        self.size -= 1
