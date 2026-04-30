class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(temp_list):
            if len(temp_list) == len(nums):
                res.append(list(temp_list))
                return
            for n in nums:
                if n in temp_list:
                    continue
                temp_list.append(n)
                # go back and try to add other element
                backtrack(temp_list)

                temp_list.pop()
        
        backtrack([])
        return res