class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Ensure that nums1 is the shorter array to reduce the number of iterations
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        start, end = 0, m
        half_len = (m + n + 1) // 2

        while start <= end:
            partition1 = (start + end) // 2
            partition2 = half_len - partition1

            max_left1 = float('-inf') if partition1 == 0 else nums1[partition1 - 1]
            min_right1 = float('inf') if partition1 == m else nums1[partition1]

            max_left2 = float('-inf') if partition2 == 0 else nums2[partition2 - 1]
            min_right2 = float('inf') if partition2 == n else nums2[partition2]

            if max_left1 <= min_right2 and max_left2 <= min_right1:
                if (m + n) % 2 == 0:
                    return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2.0
                else:
                    return max(max_left1, max_left2)
            elif max_left1 > min_right2:
                end = partition1 - 1
            else:
                start = partition1 + 1
