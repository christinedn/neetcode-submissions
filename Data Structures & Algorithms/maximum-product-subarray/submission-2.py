class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res, maxProd, minProd = nums[0], nums[0], nums[0]
        for n in nums[1:]:
            tempMax = maxProd # used for minProd calcuation. stores prev maxProd
            maxProd = max(n, maxProd*n, minProd*n)
            minProd = min(n, tempMax*n, minProd*n) # used in maxProd in case negatives are encountered
            res = max(res, maxProd)
        return res
