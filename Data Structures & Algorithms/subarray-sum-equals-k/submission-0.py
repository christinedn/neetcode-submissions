class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int) # key = old_prefix, value = count
        freq[0] = 1 # 1 way to make 0 prefix
        current_sum = 0
        res = 0
        for n in nums:
            current_sum += n
            if current_sum - k in freq:
                res += freq[current_sum - k]
            freq[current_sum] += 1
        return res 