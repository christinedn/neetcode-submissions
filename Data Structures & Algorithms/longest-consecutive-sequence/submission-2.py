class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        for n in nums:
            s.add(n)
        
        res = 0
        # find leftmost number
        for n in nums:
            currRes = 1
            leftNei = n - 1
            if leftNei not in s: # found the number that starts the sequence
                nextNum = n + 1
                while nextNum in s:
                    currRes += 1
                    nextNum += 1
            res = max(res, currRes)

        return res