class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while (mask&b) > 0:
            a, b = a^b, (a&b) << 1
            print(bin(a), a, bin(b), b, bin(mask&b), mask&b)
        print(bin(mask&a), mask&a, bin(b), b, bin(mask&b), mask&b)
        return (mask&a) if b > 0 else a