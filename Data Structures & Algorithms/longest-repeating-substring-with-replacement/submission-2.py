class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        l = 0
        d[s[l]] += 1
        res = 0
        for r in range(1, len(s), 1):
            d[s[r]] += 1
            while sum(d.values()) - max(d.values()) > k:
                d[s[l]] -= 1
                l += 1
            res = max(r-l+1, res)
        return res