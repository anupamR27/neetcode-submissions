class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        hash_set = set()
        for num in nums:
            hash_set.add(num)

        longest = 1
        for num in nums:
            count = 1
            if (num - 1) not in hash_set:
                num_1 = num + 1
                while(num_1) in hash_set:
                    count += 1
                    num_1 += 1
                    longest = max(longest, count)

        return longest
