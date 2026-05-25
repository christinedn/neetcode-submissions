# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # have two stacks, read through tree, push onto stack, as you pop, compare elements
        pStk, qStk = [p], [q]
        while pStk and qStk:
            pNode, qNode = pStk.pop(), qStk.pop()
            if not pNode and not qNode:
                continue
            if not pNode or not qNode or pNode.val != qNode.val:
                return False
            pStk.append(pNode.left)
            pStk.append(pNode.right)
            qStk.append(qNode.left)
            qStk.append(qNode.right)
        return True

        