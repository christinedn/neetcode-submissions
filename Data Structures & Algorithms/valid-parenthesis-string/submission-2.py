class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0
        for i, c in enumerate(s):
            if c == '(':
                left_max += 1
                left_min += 1
            elif c == ')':
                left_max -= 1
                left_min -= 1
            else: # *
                left_max += 1
                left_min -= 1

            if left_max < 0:
                return False # can never recover
                
            if left_min < 0:
                left_min = 0
        
        return left_min == 0 or left_max == 0
