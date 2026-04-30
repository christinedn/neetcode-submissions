class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        count_t, window = defaultdict(int), defaultdict(int)
        for c in t:
            count_t[c] += 1
        
        # both dicts have key = char, value = num of chars. 
        need, have = len(count_t), 0
        l = 0
        res, len_res = [-1, -1], float("inf")
        for r in range(len(s)):
            window[s[r]] += 1
            if window[s[r]] == count_t[s[r]]:
                have += 1
            # found window containing all characters 
            while need == have: 
                if (r - l + 1) < len_res:
                    res = [l,r]
                    len_res = r - l + 1
                # save substring
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l:r+1]



        

        