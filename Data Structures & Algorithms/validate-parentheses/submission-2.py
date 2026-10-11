class Solution:
    def isValid(self, s: str) -> bool:
        # closeToOpen = {')':'(', '}': '{', ']': '['}
        # stack = []
        # for c in s:
        #     if c in ['(', '[', '{']:
        #         stack.append(c)
        #     else:
        #         if not stack or stack[-1] != closeToOpen[c]:
        #             return False
        #         stack.pop()
                
        # return (len(stack) == 0)
        
        stack = []
        closeToOpen = {')':'(', '}': '{', ']': '['}

        for bracket in s:
            if bracket in ['(', '{', '['] :
                stack.append(bracket)

            else:
                if not stack or stack[-1] != closeToOpen[bracket]:
                    return False
                stack.pop()
                
        if not stack:
            return True            



