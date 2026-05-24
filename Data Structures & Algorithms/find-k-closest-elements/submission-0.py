class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l, r = 0, len(arr)-1
        index = None
        res = []
        while l <= r:
            m = (l+r)//2
            if arr[m] == x:
                index = m
                break
            elif arr[m] > x:
                r = m - 1
            else:
                l = m + 1
        if index is None:
            left_index = l-1
            right_index = l
        else:
            res.append(arr[index])
            left_index = index-1
            right_index = index+1

        while len(res) != k:
            if left_index < 0:
                res.append(arr[right_index])
                right_index = right_index+1
            elif right_index >= len(arr): # but i do have that check here see, i just append left_index
                res.append(arr[left_index])
                left_index = left_index-1
            else:
                right_dis = abs(arr[right_index]-x)
                left_dis = abs(arr[left_index]-x)
                if left_dis <= right_dis:
                    res.append(arr[left_index])
                    left_index = left_index-1
                else: 
                    res.append(arr[right_index])
                    right_index = right_index+1
        res.sort()
        return res




