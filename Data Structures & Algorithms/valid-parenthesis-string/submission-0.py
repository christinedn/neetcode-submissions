class Solution:
    def checkValidString(self, s: str) -> bool:
        memo = [[None] * (len(s) + 1) for _ in range(len(s) + 1)]

        def dfs(i, open):
            if open < 0:
                return False
            if i == len(s):
                return open == 0
            if memo[i][open] is not None:
                return memo[i][open]
            if s[i] == '(':
                result = dfs(i + 1, open + 1)

            elif s[i] == ')':
                result = dfs(i + 1, open - 1)

            elif s[i] == '*':
                result = (
                    dfs(i + 1, open - 1) or
                    dfs(i + 1, open + 1) or
                    dfs(i + 1, open)
                )

            memo[i][open] = result

            return result

        return dfs(0, 0)