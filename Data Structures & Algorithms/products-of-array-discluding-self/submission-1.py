class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # l_output = [1, 1, 2, 6]
        # r_output = [48, 24, 6, 1]
        n = len(nums)
        output = n*[1]

        # nums = [1, 2, 3, 4]
        left = 1
        for i in range(n):
            output[i]*=left
            left = left*nums[i]
        # print(output)
        
        # r_output = [48, 24, 6, 1]
        right = 1
        for i in range(n-1, -1, -1):
            output[i] *= right
            right *= nums[i]
        # print(output)
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
