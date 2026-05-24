class Solution:
    def trap(self, height: List[int]) -> int:
        left_max = [0 for _ in range(len(height))]
        right_max = [0 for _ in range(len(height))]
        curr_left_max = 0
        for i in range(1, len(left_max)):
            if height[i-1] > curr_left_max:
                curr_left_max = height[i-1]
            left_max[i] = curr_left_max
            
        curr_right_max = 0
        for i in range(len(right_max)-2, -1, -1):
            if height[i+1] > curr_right_max:
                curr_right_max = height[i+1]
            right_max[i] = curr_right_max

        res = 0
        for i in range(len(height)):
            if min(left_max[i], right_max[i]) - height[i] > 0:
                res += min(left_max[i], right_max[i]) - height[i]
        return res
        
