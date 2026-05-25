class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # create a dict
        d = defaultdict(int)
        # store all values of nums in dict, with key = value, value = count
        for n in nums:
            d[n] += 1
        # convert the items of dict to a list 
        freq_pairs = list(d.items())
        # sort that list by comparing the count in reverse order
        freq_pairs.sort(key = lambda x: x[1], reverse = True)
        # append to result
        res = []
        for i in range(k):
            res.append(freq_pairs[i][0])
        return res


