class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        if len(s) == 1:
            return 1     
        
        char_read = set()
        l, r = 0, 1
        char_read.add(s[l])
        longest = 0
        while r < len(s):
            while s[r] in char_read:
                char_read.remove(s[l])
                l += 1
            longest = max(longest, r-l+1)
            char_read.add(s[r])
            r += 1
        return longest
        