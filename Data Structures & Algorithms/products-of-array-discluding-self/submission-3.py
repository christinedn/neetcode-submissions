class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pre, post = [], [0] * len(nums)
        currPre, currPost = 1, 1
        # calculate prefix array
        for n in nums:
            pre.append(currPre)
            currPre *= n
        # iterate backwards, calculate postfix array
        for i in range(len(nums) - 1, -1, -1):
            post[i] = currPost
            currPost *= nums[i]
        res = []
        for i in range(len(nums)):
            res.append(pre[i] * post[i])
        return res