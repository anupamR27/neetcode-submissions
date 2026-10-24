class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        left = 0
        right = 1
        answer = 0
        while right < len(prices):
            if prices[right] < prices[left]:
                left = right
                
            else:
                profit = prices[right] - prices[left]
                answer = max(answer, profit)
                
            right += 1
            

        return answer