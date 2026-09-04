class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for index, num in enumerate(nums):
            compliment = target - num

            if compliment in my_dict:
                return [my_dict[compliment], index]
            
            my_dict[num] = index
        