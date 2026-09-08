class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        area = 0
        left = 0
        right = len(height) - 1

        while left<right:
            h = min(height[left], height[right])
            width = right - left
            calculate = h*width

            area = max(area, calculate)

            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return area
