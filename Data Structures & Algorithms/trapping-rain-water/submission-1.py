class Solution:
    def trap(self, height: List[int]) -> int:

        left = 0
        right = len(height) - 1

        left_max = 0
        right_max = 0

        water = 0
        while left<right:

            if height[left] < height[right]:
                left_max = max(left_max, height[left])
                water += (left_max - height[left])
                left+=1
            
            else:
                right_max = max(right_max, height[right])
                water += (right_max - height[right])
                right-=1

        return water





















        # max_left = []
        # max_right = []
        # min_array = []

        # max_current_left = 0
        # for h in height:
        #     max_left.append(max_current_left)
        #     max_current_left = max(max_current_left, h)
            
        # # print(max_left)
        
        # max_current_right = 0
        # for h in height[::-1]:
        #     max_right.append(max_current_right)
        #     max_current_right = max(max_current_right, h)

        # max_right = max_right[::-1]

        # water_area = 0
        # for i in range(len(height)):
        #     if (min(max_left[i], max_right[i]) - height[i] >= 0):
        #         water_area += (min(max_left[i], max_right[i]) - height[i])
        
        # return water_area