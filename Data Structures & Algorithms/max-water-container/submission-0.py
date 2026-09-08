class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        for i in range(n):
            left = i
            right = len(height) - 1
            while left<right:
                h = min(height[left], height[right])
                width = right - left
                calculate = h*width
                area = max(area, calculate)
                right -= 1

        return area
