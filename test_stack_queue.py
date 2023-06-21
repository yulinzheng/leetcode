import stack_queue_problems as code

def test_myqueue_232():
    que = code.MyQueue232()
    que.push(1)
    que.push(2)
    que.push(3)
    assert que.pop() == 1
    assert que.peek() == 2
    assert que.pop() == 2
    assert que.empty() == False

def test_mystack_225():
    stack = code.MyStack225()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.top() == 2
    assert stack.pop() == 2
    assert stack.empty() == False
