class Solution:
    def trap(self, height: List[int]) -> int:
        max_left = []
        max_right = []
        min_array = []

        max_current_left = 0
        for h in height:
            max_left.append(max_current_left)
            max_current_left = max(max_current_left, h)
            

        # print(max_left)
        
        max_current_right = 0
        for h in height[::-1]:
            max_right.append(max_current_right)
            max_current_right = max(max_current_right, h)

        max_right = max_right[::-1]

        water_area = 0
        for i in range(len(height)):
            if (min(max_left[i], max_right[i]) - height[i] >= 0):
                water_area += (min(max_left[i], max_right[i]) - height[i])
        
        return water_area