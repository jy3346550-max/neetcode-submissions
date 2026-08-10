class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Brute Force
        '''
        result = set()
        nums.sort()

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):

                    if nums[i] + nums[j] + nums[k] == 0:
                        truple = [nums[i], nums[j], nums[k]]
                        result.add(tuple(truple))

        return [list(i) for i in result]
        '''

        result = []
        nums.sort()

        for i, a in enumerate(nums):
            if a > 0:
                break
            
            if i > 0 and a == nums[i - 1]:
                continue
            
            l, r = i + 1, len(nums) -1

            while l < r:
                s = a + nums[l] + nums[r]
                if s > 0:
                    r -= 1
                elif s < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    r -= 1
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return result