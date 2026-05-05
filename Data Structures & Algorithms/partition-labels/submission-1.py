class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(int)
        res = []
        for i in range(len(s)-1,-1,-1):
            if s[i] not in d:
                d[s[i]] = i
        size = end = 0
        for i, c in enumerate(s):
            size += 1
            end = max(end, d[c])
            if d[c] > end:
                end = d[c]
            if i == end:
                res.append(size)
                size = 0
        return res
