class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        l = 1
        r = 0
        while l < len(s):
            if s[l] == " ":
                temp = l - 1
                while r < temp:
                    s[r], s[temp] = s[temp], s[r]
                    r += 1
                    temp -= 1
                r = l + 1
                l = r + 1
                continue
            l += 1

        # once l is at the end we have to reverse the last word 
        temp = l - 1
        while r < temp:
            s[r], s[temp] = s[temp], s[r]
            r += 1
            temp -= 1
        r = l + 1
        l = r + 1
        print(s)
        


    #       0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  
    #     ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    #     ["e","u","l","b"," ","s","i"," ","y","k","s"," ","e","h","t"]    

    #     ["e","u","l","b"," ","s"," ","y","k","s"," ","e","h","t"]
    # l = 8
    # r = 9
    # l+1:r+1
