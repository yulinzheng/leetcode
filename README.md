### Naming Convention:
```
[function name]_[leetcode problem number](_[solution version])
```
For example: `isAnagram_242`, `reverseList_206_iterative`, `removeElement_27_v1`

### Testing:
Test all problems:
```
$ pytest -v test_[suite].py
```
Test one function:
```
$ pytest -v test_[suite].py::function_name
```
