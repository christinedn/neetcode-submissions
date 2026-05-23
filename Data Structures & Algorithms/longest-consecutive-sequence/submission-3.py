class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
        
        res = 0
        for n in nums:
            temp_res = 1
            curr_n = n
            while curr_n + 1 in s:
                temp_res +=1
                curr_n = curr_n + 1
            res = max(res, temp_res)

        return res
