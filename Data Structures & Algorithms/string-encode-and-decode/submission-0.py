class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            count = len(s)
            res += str(count) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            # j is used to find the count len
            j = i
            while s[j] != '#':
                j += 1
            # at this point, we know that the length of the string is stored in j[0:2]
            length = int(s[i:j])

            res.append(s[j+1:j+1+length])

            i = j + 1 + length
        return res
            
            
