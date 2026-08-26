class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            n=str(len(i))
            res = res + n + '#' + i
        return res

    def decode(self, s: str) -> List[str]:
        list_final = []
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            
            n=int(s[i:j])
            word = s[j+1 : j+1+n]
            list_final.append(word)
            i=j+1+n
        return list_final

              


# solution = Solution()

# result = solution.encode(["hello", "world"])

# print(result)