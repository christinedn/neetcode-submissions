class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return 1
        l, r = 0, 1
        d = defaultdict(int)
        d[s[l]] += 1
        longest = 0
        while r < len(s):
            d[s[r]] += 1
            while (sum(d.values()) - max(d.values()) > k):
                d[s[l]] -= 1
                l += 1
            longest = max(longest, r-l+1)
            r += 1
        return longest

         