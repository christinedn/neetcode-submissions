class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = [[] for _ in range(len(nums)+1)]
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        for num, freq in d.items():
            arr[freq].append(num)
        
        res = []
        for i in range(len(arr)-1, -1, -1):
            for n in arr[i]:
                res.append(n)
                if len(res) == k:
                    return res
