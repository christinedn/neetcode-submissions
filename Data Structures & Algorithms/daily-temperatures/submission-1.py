class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] 

        for i in range(len(temperatures)):
            # after each iteration, peek at the top of the stack (and retrieve the temprature) 
            # to keep it in decreasing order
            while stack:
                topStackIndex = stack[-1]
                if temperatures[i] > temperatures[topStackIndex]:
                    # currTemperature is greater than top of stack, pop from stack
                    res[topStackIndex] = i - topStackIndex
                    stack.pop()
                else:
                    break
            stack.append(i)
        return res



            