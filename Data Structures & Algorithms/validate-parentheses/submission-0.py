class Solution:
    def isValid(self, s: str) -> bool:
        ans = []
        array = ['(', ')', '[', ']', '{', '}']
        for x in s:
            if x in array:
                ans.append(x)

        left = 0
        right = len(ans) - 1

        while left<right:
            if ans[left] == '(' and ans[right] != ')':
                return False
            if ans[left] == '[' and ans[right] != ']':
                return False
            if ans[left] == '{' and ans[right] != '}':
                return False

            left+=1
            right-=1


        return True












        # print(ans)
        # Open = ['(', '[', '{']
        # close = [')', ']', '}']

        # (, ), [, ], {, }
        # for bracket in ans:
        #     if bracket == '(' and ')' in ans:
        #         ans.remove(bracket)
        #         ans.remove(')')

        #     elif bracket == '[' and ']' in ans:
        #         ans.remove(bracket)
        #         ans.remove(']')

        #     elif bracket == '{' and '}' in ans:
        #         ans.remove(bracket)
        #         ans.remove('}')

        # if not ans:
        #     return True
        
        # return False

