class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # return min(nums)
        '''
        min_Nums = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                min_Nums = nums[i]
                return min_Nums
                
        return min_Nums
        '''

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        
        return nums[left]
        