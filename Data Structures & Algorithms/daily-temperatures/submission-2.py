class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0] * len(temperatures)

        stack = []

        for i, t in enumerate(temperatures):
            if not stack:
                stack.append((t, i))
            else:
                while stack and stack[-1][0] < t:
                    s_t, s_i = stack.pop()
                    output[s_i] = i - s_i
                stack.append((t, i))
                
        return output

            