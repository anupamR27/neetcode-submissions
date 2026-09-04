class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # my_dict = {}
        # count=1
        # for index, num in enumerate(nums):
        #     if num in my_dict:
        #         return True

        #     my_dict[num] = 1

        # return False

        seen = set()

        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        return False
