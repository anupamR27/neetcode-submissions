class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_1 = {}

        for word in s:
            if word in dict_1:
                dict_1[word] += 1
            else:
                dict_1[word] = 1

        print(dict_1)

        dict_2 = {}

        for letter in t:
            if letter in dict_2:
                dict_2[letter] += 1
            else:
                dict_2[letter] = 1
        # print(dict_2)
        return (dict_1 == dict_2)