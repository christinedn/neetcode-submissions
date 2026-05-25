class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for _ in range(32):
            res = res << 1
            lsb = n & 1
            res = res | lsb # can you do this or do you have to use the or operation?
            n = n >> 1
        return res
