class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total = 1
        total2 = 1
        zeros = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                total = total * nums[i]
                total2 = total2 * nums[i]
            else:
                zeros = zeros + 1
                total2 = total2 * nums[i]
        
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i] = total2 // nums[i]
            elif nums[i] == 0:
                nums[i] = total
            if zeros >= 2:
                nums[i] = 0
            
            
        
        return nums
        
            
        
        