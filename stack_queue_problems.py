class MyQueue232(object):
    """
    Implement a first in first out (FIFO) queue using only two stacks.

    queue = [1, 2, 3, 4...]
    stack_in = []
    stack_out = []

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

        Time: O(n)
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

        Time: O(n)
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


from collections import deque
"""
Here we use deque instead of list because
    list.pop(0) takes O(n)
    deque.popleft(0) take O(1)
"""
class MyStack225(object):
    """
    Implement a last-in-first-out (LIFO) stack using only two queues.

    stack: [1, 2, 3, 4...]
    que: [4, 3, 2, 1]
    tmp: []

    tmp is used as temp storage for que
    """
    def __init__(self):
        self.que = deque()
        self.tmp = deque()

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.tmp.append(x)
        for i in range(len(self.que)):
            self.tmp.append(self.que.popleft())
        self.tmp, self.que = self.que, self.tmp

    def pop(self):
        """
        :rtype: int
        """
        return self.que.popleft()

    def top(self):
        """
        :rtype: int

        newest element of the stack
        """
        return self.que[0]

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.que) == 0

def isValid_20(s):
    """
    Given a string s containing only ( ) { } [ ]
    determine if the input string is valid.

        An input string is valid if:

            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
            Every close bracket has a corresponding open bracket of the same type.
    """
    stack = []
    for bracket in s:
        if bracket in ['(', '{', '[']:
            stack.append(bracket)
        else:
            # no open bracket in stack
            if not stack:
                return False
            # check for matches
            open_bracket = stack.pop()
            if bracket == ')' and open_bracket != '(':
                return False
            elif bracket == '}' and open_bracket != '{':
                return False
            elif bracket == ']' and open_bracket != '[':
                return False
            else:
                continue
    # stack should be empty
    if stack == []:
        return True
    return False

def removeDuplicates_1047(s):
    """
    s consists of lowercase English letters.
    Keep removing adjacent and equal letters until we no longer can.
    """
    stack = []
    for letter in s:
        if not stack:
            stack.append(letter)
        else:
            prev = stack.pop()
            if prev != letter:
                stack.append(prev)
                stack.append(letter)
    return "".join(stack)

def evalRPN_150(tokens):
    """
    You are given an array of string tokens that represents
    an arithmetic expression in a Reverse Polish Notation.
    Return an integer that represents the value of the expression.
    """
    stack = []
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            second = stack.pop()
            first = stack.pop()
            if token == '+':
                stack.append(first + second)
            elif token == '-':
                stack.append(first - second)
            elif token == '*':
                stack.append(first * second)
            else:
                # division always truncates toward 0
                stack.append(int(first / second))
        else:
            stack.append(int(token))
    return stack.pop()
