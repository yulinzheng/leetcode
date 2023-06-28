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
    if not root:
        return 0
    left = maxDepth_104(root.left)
    right = maxDepth_104(root.right)
    return max(left + 1, right + 1)

def minDepth_111(root):
    """
    Given a binary tree, find its minimum depth.
    """
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

def isBalanced(root):
    """
    Given a binary tree, determine if it is height-balanced.
    """
