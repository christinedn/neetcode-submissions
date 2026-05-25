class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        minProd, maxProd, result = nums[0], nums[0], nums[0]
        for n in nums[1:]:
            tempMax = maxProd
            maxProd = max(n, maxProd * n, minProd * n)
            minProd = min(n, tempMax * n, minProd * n)
            result = max(result, maxProd)
        return result

        