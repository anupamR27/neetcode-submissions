class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        if n in [0, 1] or s.isspace():
            return True

        new_str = ""
        for c in s:
            if c.isalnum():
                new_str+=c.lower()

        left=0
        right = len(new_str) - 1

        while left<right:
            if (new_str[left] == new_str[right]):
                left+=1
                right-=1
            else:
                return False
        return True
        