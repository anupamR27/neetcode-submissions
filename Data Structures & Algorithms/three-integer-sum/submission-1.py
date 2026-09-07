class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        new_sorted = sorted(nums)
        s_set = set()
        left = 1
        right = len(nums) - 1

        for i in range(len(new_sorted)):
            left = i+1
            num = new_sorted[i]

            while left<right:
                current_sum = num + new_sorted[left] + new_sorted[right]

                if current_sum == 0:
                    s_set.add((num, new_sorted[left], new_sorted[right]))
                    left+=1
                    right-=1
                elif current_sum > 0:
                    right-=1
                elif current_sum<0:
                    left+=1

        return list(s_set)
