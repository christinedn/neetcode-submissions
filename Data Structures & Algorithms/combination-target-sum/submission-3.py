class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = [[] for _ in range(target+1)]
        res[0] = [[]]
        for n in nums:
            for i in range(n, len(res)):
                for comb in res[i-n]:
                    res[i].append(comb + [n])
        return res[target]

        
        


        

        
        
        
       


        