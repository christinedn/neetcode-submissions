class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        templist = []
        res = []
        def backtrack(templist):
            if len(templist) == len(nums):
                res.append(templist.copy())
            for n in nums:
                if n in templist:
                    continue
                templist.append(n)
                backtrack(templist)
                templist.pop()
        backtrack([])
        return res

