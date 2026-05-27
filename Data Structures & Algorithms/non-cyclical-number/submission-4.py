class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        cs = n
        curr_sum = 0
        while curr_sum != 1:
            curr_sum = 0
            for digit in str(cs):
                curr_sum += int(digit) * int(digit)
            if curr_sum not in s:
                s.add(curr_sum)
            else:
                return False
            cs = curr_sum
            print(curr_sum)
        return True
