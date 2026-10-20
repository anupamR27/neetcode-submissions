class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        def next_small(arr):
            n = len(arr)
            nse = [n] * n
            stack = []

            for i in range(n):
                while stack and arr[stack[-1]] > arr[i]:
                    idx = stack.pop()
                    nse[idx] = i
                stack.append(i)
            return nse

        def prev_small(arr):
            n = len(arr)
            pse = [-1] * n
            stack = []
            
            for i in range(n):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                
                if stack:
                    pse[i] = stack[-1]
                
                stack.append(i)
            return pse

        nse = next_small(heights)
        pse = prev_small(heights)
        maxi = 0

        for i in range(len(heights)):
            width = nse[i] - pse[i] - 1
            area = heights[i] * width
            maxi = max(area, maxi)
        
        return maxi
