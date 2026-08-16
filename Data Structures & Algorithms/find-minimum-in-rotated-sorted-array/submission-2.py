class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        # return min(nums)

        min_Num = nums[0] 
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i-1]:
                min_Num = nums[i]
        
        return min_Num
        