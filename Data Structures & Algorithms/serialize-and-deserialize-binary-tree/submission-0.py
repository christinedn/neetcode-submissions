# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        # create res list
        res = []
        # perform dfs on the root
        def dfs(root):
            # if root not null, append N (account for null cases)
            if not root:
                res.append("N")
                return
            # append regular nodes with value
            res.append(str(root.val))
            # perform dfs on left and right
            dfs(root.left)
            dfs(root.right)
        # call the dfs function
        dfs(root)
        # use the join function to separate each element in res string.join(iterable)
        return ",".join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = data.split(",")
        self.i = 0
        # split your data
        # define i globally. how do you do that?
        # why don't you need to pass anything into dfs function?
        def dfs():
            # base case?
            if vals[self.i] == "N":
                self.i += 1
                return None
            
            # create tree node
            node = TreeNode(int(vals[self.i]))
            # increment i
            self.i += 1
            # go left
            node.left = dfs()
            # go right
            node.right = dfs()
            # return that node
            return node
        # return the function call 
        return dfs()



