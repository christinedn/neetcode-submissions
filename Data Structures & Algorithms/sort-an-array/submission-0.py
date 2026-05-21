class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, L, m, r):
            left, right = arr[L:m+1], arr[m+1:r+1]
            i, j, k = L, 0, 0
            while j < len(left) and k < len(right):
                if left[j] <= right[k]:
                    arr[i] = left[j]
                    j += 1
                else:
                    arr[i] = right[k]
                    k += 1
                i += 1

            while j < len(left):
                arr[i] = left[j]
                j += 1
                i += 1

            while k < len(right):
                arr[i] = right[k]
                k += 1
                i += 1

        def merge(arr, l, r):
            if l >= r:
                return
            m = (l + r)//2
            merge(arr, l, m)
            merge(arr, m+1, r)
            mergeSort(arr, l, m, r)
        merge(nums, 0, len(nums)-1)
        return nums