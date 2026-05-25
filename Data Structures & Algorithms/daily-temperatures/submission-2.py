class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stck = []
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures)): 
            while stck and temperatures[i] > temperatures[stck[-1]]:
                index = stck.pop()
                res[index] = i - index
            stck.append(i)
        
        return res