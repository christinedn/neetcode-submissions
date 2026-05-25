class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s[0]) == 0: return 0
        dp = [0] * (len(s) + 1)
        dp[0], dp[1] = 1, 1
        for i in range(2, len(dp), 1):
            newElem = 0
            if 0 < int(s[i-1]) <= 9:
                newElem += dp[i-1]
            print("newElem", newElem)
            print("currentInt", int(s[i-2] + s[i-1]))
            if 10 <= int(s[i-2] + s[i-1]) <= 26:
                newElem += dp[i-2]
            print("newElem2", newElem)
            dp[i] = newElem
        print(dp)
        return dp[len(dp)-1]

        


        