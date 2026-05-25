# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def has_sum(node, curr_sum):
            if not node:
                return False
            curr_sum += node.val
            if curr_sum == targetSum and node.left is None and node.right is None:
                return True
            return has_sum(node.left, curr_sum) or has_sum(node.right, curr_sum)
        return has_sum(root, 0)
            