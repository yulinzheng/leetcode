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

def test_isValid_20():
    assert code.isValid_20("()") == True
    assert code.isValid_20("(]") == False
    assert code.isValid_20("()[]{}") == True
    assert code.isValid_20("([]") == False
    assert code.isValid_20("]]") == False

def test_removeDuplicates_1047():
    assert code.removeDuplicates_1047("abbaca") == "ca"
    assert code.removeDuplicates_1047("azxxzy") == "ay"

def test_evalRPN_150():
    assert code.evalRPN_150(["2","1","+","3","*"]) == 9
    assert code.evalRPN_150(["4","13","5","/","+"]) == 6
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    assert code.evalRPN_150(tokens) == 22

def test_maxSlidingWindow_239():
    assert code.maxSlidingWindow_239_v1([1], 1) == [1]
    result = code.maxSlidingWindow_239_v1([1,3,-1,-3,5,3,6,7], 3)
    assert result == [3,3,5,5,6,7]
    assert code.maxSlidingWindow_239_v2([1], 1) == [1]
    result = code.maxSlidingWindow_239_v2([1,3,-1,-3,5,3,6,7], 3)
    assert result == [3,3,5,5,6,7]

def test_topKFrequent_347():
    assert code.topKFrequent_347_v1([1,1,1,2,2,3], 2) == [2,1]
    assert code.topKFrequent_347_v1([1], 1) == [1]
    assert code.topKFrequent_347_v1([4,1,-1,2,-1,2,3], 2) == [-1, 2]
    assert code.topKFrequent_347_v2([1,1,1,2,2,3], 2) == [2,1]
    assert code.topKFrequent_347_v2([1], 1) == [1]
    assert code.topKFrequent_347_v2([4,1,-1,2,-1,2,3], 2) == [-1, 2]