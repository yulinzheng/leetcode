class MyQueue232(object):
    """
    queue = [1, 2, 3, 4...]
    stack_in = [4]
    stack_out = [3, 2, 1]

    push to stack_in, pop from stack_out
    """
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack_in.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if self.stack_out:
            return self.stack_out.pop()
        else:
            while self.stack_in:
                item = self.stack_in.pop()
                self.stack_out.append(item)
            return self.stack_out.pop()

    def peek(self):
        """
        :rtype: int
        """
        item = self.pop()
        self.stack_out.append(item)
        return item

    def empty(self):
        """
        :rtype: bool
        """
        if self.stack_in or self.stack_out:
            return False
        return True


class MyStack225(object):
    """
    stack: [1, 2, 3, 4...]
    queue_in: [4, 3, 2, 1]
    queue_out: []

    queue_out is used as temp storage for queue_in
    """
    def __init__(self):
        self.queue_in = []
        self.queue_out = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """


    def pop(self):
        """
        :rtype: int
        """

    def top(self):
        """
        :rtype: int
        """


    def empty(self):
        """
        :rtype: bool
        """
