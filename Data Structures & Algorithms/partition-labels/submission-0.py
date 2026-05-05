class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        d = defaultdict(int)
        res = []
        for i in range(len(s)-1,-1,-1):
            if s[i] not in d:
                d[s[i]] = i
        start = 0
        end = d[0]
        for i, c in enumerate(s):
            if d[c] > end:
                end = d[c]
            if i == end:
                res.append(end - start + 1)
                if i + 1 < len(s):
                    start = i + 1
                    end = d[s[i+1]]
        return res
