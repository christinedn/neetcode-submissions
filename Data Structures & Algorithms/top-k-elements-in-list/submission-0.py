class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for n in nums:
            d[n] += 1
        freq_pairs = list(d.items())
        freq_pairs.sort(key = lambda x: x[1], reverse = True)

        res = []
        for i in range(k):
            res.append(freq_pairs[i][0])

        return res


