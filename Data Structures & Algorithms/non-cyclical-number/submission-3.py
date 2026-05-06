class Solution:
    def isHappy(self, n: int) -> bool:
        my_sum = n
        s = set()        
        while my_sum != 1:
            if my_sum in s:
                return False
            s.add(my_sum)
            n = 0
            for digit in str(my_sum):
                n += int(digit) ** 2
            my_sum = n
        return True
        

