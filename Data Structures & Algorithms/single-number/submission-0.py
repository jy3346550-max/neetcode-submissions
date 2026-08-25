class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        single = set()

        for i in range(len(nums)):
            if nums[i] not in single:
                single.add(nums[i])
            else:
                seen.add(nums[i])
        
        ans = single - seen
        return ans.pop()

        