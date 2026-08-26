class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_dict = {}
        count=1
        for index, num in enumerate(nums):
            if num in my_dict:
                return True

            my_dict[num] = 1

        return False










        # list_final = []
        # for num in nums:
        #     if num in list_final:
        #         return True
        #     list_final.append(num)
        
        # return False
