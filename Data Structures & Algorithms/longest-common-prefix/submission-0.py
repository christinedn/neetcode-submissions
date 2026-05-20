class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        def check_longest(s1, s2):
            i = 0
            while i < len(s1) and i < len(s2):
                if s1[i] == s2[i]:
                    i += 1
                else:
                    break
            return i
            

        
        if len(strs) == 0:
            return ""
        
        if len(strs) == 1:
            return strs[0]

        longest = check_longest(strs[0], strs[1])    

        for i in range(2, len(strs)):
            longest = min(longest, check_longest(strs[i-1], strs[i]))
        
        return strs[0][0:longest]
            

