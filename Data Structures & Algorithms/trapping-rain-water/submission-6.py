class Solution:
    def trap(self, height: List[int]) -> int:
        
        # Blind code writing 
        '''
        first = 0
        index = 0
        total = 0
        count = 0
        subtract = 0

        for i in range(len(height)-1):
            temp = height[i]
            if temp >= first:
                first = temp
            else:
                index = i
                break

            

        for i in range(len(height)):
            if height[i] < first and index <= i:
                subtract += height[i]
                count += 1

            if height[i] >= first and index <= i:
                total += min(height[i], first) * count - subtract
                first = height[i]
                index = i
                count = 0
                subtract = 0
        
        return total
        '''
        
        left, right = 0, len(height) - 1
        leftMax, rightMax = 0, 0
        total = 0

        while left < right:
            if height[left] < height[right]:
                leftMax = max(leftMax, height[left])
                total += leftMax - height[left]
                left += 1
            else:
                rightMax = max(rightMax, height[right])
                total += rightMax - height[right]
                right -= 1

        return total

    
            
        