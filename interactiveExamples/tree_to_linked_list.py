# Given the root `Node` of a tree, convert the tree into a double linked list.
# We don't particularly care about the order, but the linked list should contain
# all the nodes inside the tree.

class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return self.val

def solution(root):
    if root is None:
        return root
    if root.left is None and root.right is None:
        return root

    stack = []
    stack.append(root)

    head = root
    tail = None

    while len(stack) > 0:
        curr = stack.pop()

        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)

        if tail is None:
            tail = curr
            tail.left = None
        else:
            tail.right = curr
            curr.left = tail
            tail = curr
            tail.right = None
    return head
