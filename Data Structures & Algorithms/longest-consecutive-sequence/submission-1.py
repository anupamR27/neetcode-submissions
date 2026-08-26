class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        new_count = 0
        for num in hash_set:
            if (num-1) not in hash_set:
                count = 1

                while(num+1) in hash_set:
                    count+=1
                    num+=1
                new_count = max(new_count, count)

        return new_count
        # print(count)
        # return count