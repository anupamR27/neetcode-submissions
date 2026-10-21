class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        low = 1
        high = max(piles)
        ans = high
        while(low<=high):
            hours = 0
            mid = (low+high)//2

            for p in piles:
                hours = hours + ceil(p/mid)
            
            if (hours<=h):
                ans = min(ans,mid)
                high = mid - 1

            elif(hours>h):
                low = mid + 1

        return ans
