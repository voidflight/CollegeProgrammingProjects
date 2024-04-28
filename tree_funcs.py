"""
Provides various functions for operating on binary trees.
Trees should be composed out of some sort of
Node class, where each Node has the fields:
    
Node.right
Node.left
Node.val

(see example at bottom of this file)

The val field should be an integer for compatibility with the tree_sum function
Some of the functions are specifically for binary search trees.
"""

def tree_count(root):
    """
    This function counts the number of nodes in a tree.
    Argument: root is the root node of a tree.
    Return value: an integer.
    """
    if root is None:
        return 0
    return tree_count(root.left)+tree_count(root.right)+1  # add one per node

def tree_count_1_child(root):
    """
    This function counts the number of nodes with exactly one child node
    in a tree.
    Argument: root is the root node of a tree.
    Return value: an integer.
    """
    if root is None:
        return 0
    count=tree_count_1_child(root.left)+tree_count_1_child(root.right)
    if root.left is None and root.right is not None:  # add one if 1 child
        count+=1
    elif root.left is not None and root.right is None:  # add one if 1 child
        count+=1
    return count

def tree_sum(root):
    """
    This function calculates the sum of all the values of the nodes in
    a tree.
    Argument: root is the root node of a tree.
    Return value: an integer.
    """
    if root is None:
        return 0
    return tree_sum(root.left)+tree_sum(root.right)+root.val  # add 1 per node

def tree_print(root):
    """
    This function prints the values of all the nodes in a tree.
    Argument: root is the root node of a tree.
    """
    if root is None:
        return
    print(root.val)
    tree_print(root.left)
    tree_print(root.right)
    
def tree_print_leaves(root):
    """
    This function prints the values of all the leaf nodes in a tree.
    Argument: root is the root node of a tree.
    """
    if root is None:
        return
    elif root.left is None and root.right is None:  # node is a leaf
        print(root.val)
    tree_print_leaves(root.left)
    tree_print_leaves(root.right)

def bst_search_loop(root, val):
    """
    This function searches for a value in a binary search
    tree and returns the node containing it if it exists.
    Arguments: root is the root node of a tree.
    val is an integer.
    Return value: either a tree node or None.
    """
    while root is not None and root.val!=val:  # will exit if either is False
        if val<=root.val:  # values are sorted
            root=root.left
        else:
            root=root.right
    return root  # will return either a node or None

def tree_search(root, val):
    """
    This function searches for a value in a tree and returns the node
    containing it if it exists.
    Arguments: root is the root node of a tree.
    val is an integer.
    Return value: either a tree node or None.
    """
    if root is None or root.val==val:
        return root  # will return either a node or None
    left=tree_search(root.left, val)
    right=tree_search(root.right, val)
    if left is not None:  # only one branch will pass up the value
        return left
    elif right is not None:
        return right
    else:  # if neither branch has the value, return None
        return None

def bst_max_loop(root):
    """
    This function finds the maximum value in a binary search tree.
    Argument: root is the root node of a tree.
    Return value: an integer.
    """
    while root.right is not None:  # bigger value is always to the right
        root=root.right
    return root.val

def tree_max(root):
    """
    This function finds the maximum value in a tree.
    Argument: root is the root node of a tree.
    Return value: an integer.
    """
    if root.left is None and root.right is None:  # leaf node
        return root.val
    elif root.left is None:  # left is None but right is not None
        return max(root.val, tree_max(root.right))
    elif root.right is None:  # right is None but left is not None
        return max(root.val, tree_max(root.left))
    return max(max(tree_max(root.left), tree_max(root.right)), root.val)

class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.val = val