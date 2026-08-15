class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        size = len(heights)
        maxArea = 0
        stack = []

        for i in range(size + 1):
            while stack and (i == size or heights[stack[-1]] >= heights[i]):
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea

