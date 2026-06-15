class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1 # search on smaller array. if search on larger array, index may go out of bounds for smaller array
        total = len(nums1) + len(nums2)
        half = total // 2

        left, right = 0, len(nums1) # not - 1 because searching paritition positions as opposed to indexes

        while True:
            partition1 = (left + right)//2
            partition2 = half - partition1

            l1 = nums1[partition1-1] if partition1 > 0 else float("-inf")
            r1 = nums1[partition1] if partition1 < len(nums1) else float("inf")
            l2 = nums2[partition2-1] if partition2 > 0 else float("-inf")
            r2 = nums2[partition2] if partition2 < len(nums2) else float("inf")

            if l1 <= r2 and l2 <= r1:
                return min(r1,r2) if total % 2 == 1 else (max(l1,l2) + min(r1, r2))/2

            elif l1 > r2:
                right = partition1 - 1
            else:
                left = partition1 + 1
            

