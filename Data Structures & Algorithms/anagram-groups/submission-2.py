class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}

        for str in strs:

            str_sorted = "".join(sorted(str))

            if str_sorted not in my_dict:
                my_dict[str_sorted] = [str]
            else:
                my_dict[str_sorted].append(str)

        return (list(my_dict.values()))

        # print(my_dict.values())
        # return ([my_dict.values()])

        # empty_list = []
        # for value in my_dict.values():
        #     empty_list.append(value)
        # return empty_list

        # print(empty_list)


