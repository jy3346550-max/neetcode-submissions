class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        combined = []

        for i in range(len(nums1)):
            combined.append(nums1[i])
        for i in range(len(nums2)):
            combined.append(nums2[i])
        
        combined.sort()

        if len(combined) % 2 == 0:
            mid1 = len(combined) // 2 - 1
            mid2 = len(combined) // 2
            return (combined[mid1] + combined[mid2]) / 2
        else:
            mid = len(combined) // 2
            return combined[mid]

        