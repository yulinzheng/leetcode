class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree_226_recur(root):
    """
    Given the root of a binary tree, invert the tree,
    and return its root.

    Time: O(n)
          Runtime for a recursive function is equivalent to
          the number of recursive function calls.
          Here, each node in the tree is visited once.
    """
    if not root:
        return
    invertTree_226_recur(root.left)
    invertTree_226_recur(root.right)
    root.left, root.right = root.right, root.left
    return root

def invertTree_226_iter(root):
    pass

def isSymmetric_101(root):
    """
    Given the root of a binary tree, check whether it is
    a mirror of itself.
    """
    def compare(left, right):
        if not left and not right:
            return True
        if not left or not right:
            return False
        if left.val != right.val:
            return False
        return compare(left.left, right.right) and compare(left.right, right.left)
    return compare(root.left, root.right)

def maxDepth_104(root):
    """
    Given the root of a binary tree, return its maximum depth.
    """
    # note: what we're really calculating here is height, not depth
    if not root:
        return 0
    left = maxDepth_104(root.left)
    right = maxDepth_104(root.right)
    return max(left + 1, right + 1)

def minDepth_111(root):
    """
    Given a binary tree, find its minimum depth.
    """
    # note: what we're really calculating here is height, not depth
    if not root:
        return 0
    if not root.left and root.right:
        return 1 + minDepth_111(root.right)
    if not root.right and root.left:
        return 1 + minDepth_111(root.left)
    return 1 + min(minDepth_111(root.left), minDepth_111(root.right))

def countNodes_222(root):
    """
    Given the root of a complete binary tree,
    return the number of the nodes in the tree.
    """
    if not root:
        return 0
    if not root.left and root.right:
        return 1 + countNodes_222(root.right)
    if not root.right and root.left:
        return 1 + countNodes_222(root.left)
    return 1 + countNodes_222(root.left) + countNodes_222(root.right)

def isBalanced_110(root):
    """
    Given a binary tree, determine if it is height-balanced,
    meaning for every node, the following is true:
        abs( height(node.left) - height(node.right) ) <= 1
    """
    def get_height(node):
        if not node:
            return 0
        left_height = get_height(node.left)
        if left_height < 0:
            return -1
        right_height = get_height(node.right)
        if right_height < 0:
            return -1
        if abs(left_height - right_height) > 1:
            return -1
        return max(left_height + 1, right_height + 1)
    return get_height(root) >= 0

def binaryTreePaths_257(root):
    """
    Given the root of a binary tree, return all
    root-to-leaf paths in any order.
    """
    def traverse(curr, path, result):
        path.append(curr.val)
        if not curr.left and not curr.right:
            str_path = "->".join(map(str, path))
            result.append(str_path)
            return
        if curr.left:
            traverse(curr.left, path, result)
            path.pop()
        if curr.right:
            traverse(curr.right, path, result)
            path.pop()

    if not root:
        return []
    else:
        result = []
        traverse(root, [], result)
        return result
