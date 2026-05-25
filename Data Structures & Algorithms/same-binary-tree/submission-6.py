# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq, qq = deque(), deque()
        pq.append(p)
        qq.append(q)
        while pq and qq:
            pqlen = len(pq)
            qqlen = len(qq)
            for i in range(pqlen):
                pNode = pq.popleft()
                qNode = qq.popleft()
                if not pNode and not qNode:
                    continue
                if (not pNode or not qNode) or (pNode.val != qNode.val):
                    return False
                if pNode and qNode and pNode.val == qNode.val:
                    pq.append(pNode.left)
                    pq.append(pNode.right)
                    qq.append(qNode.left)
                    qq.append(qNode.right)
        return True


        