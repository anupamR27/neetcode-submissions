class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        answer = 0
        charSet = set()

        for right in range(len(s)):
            if(s[right] not in charSet):
                charSet.add(s[right])
                answer = max(answer, len(charSet))
            else:
                while (s[right] in charSet):
                    charSet.remove(s[left])
                    left = left + 1
                charSet.add(s[right])

        return answer