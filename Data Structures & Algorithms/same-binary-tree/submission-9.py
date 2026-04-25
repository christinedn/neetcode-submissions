# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        pQueue, qQueue = deque([p]), deque([q])
        while pQueue and qQueue:
            for i in range(len(pQueue)):
                pNode, qNode = pQueue.popleft(), qQueue.popleft()
                if not pNode and not qNode:
                    continue
                if not pNode or not qNode:
                    return False
                if pNode.val != qNode.val:
                    return False
                pQueue.append(pNode.left)
                pQueue.append(pNode.right)
                qQueue.append(qNode.left)
                qQueue.append(qNode.right)
        return True

