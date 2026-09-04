class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for num in nums:
            if num not in my_dict:
                my_dict[num] = 1
            else:
                my_dict[num] += 1
        sorted_dict = dict(sorted(my_dict.items(), key=lambda item:item[1], reverse=True))
        my_list = []
        for i, n in enumerate(sorted_dict):
            if i<k:
                my_list.append(n)
        
        return (my_list)
        