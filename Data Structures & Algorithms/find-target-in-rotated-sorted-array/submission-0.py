class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        index = -1
        for i in range(len(nums)):
            if nums[i] == target:
                index = nums.index(nums[i])
        return index
        