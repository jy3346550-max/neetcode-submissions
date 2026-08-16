class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # return min(nums)
        min_Nums = nums[0]

        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                min_Nums = nums[i]
                return min_Nums
                
        return min_Nums
        