class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #high = 0
        #for i in piles:
        #    high = max(high, i)
        
        high = max(piles) # Directly findes maximum element in array

        def totalHours(piles, hourly):
            total_hour = 0
            n = len(piles)
            for i in range(n):
                total_hour += math.ceil(piles[i] / hourly)
            return total_hour

        left, right = 1, high
        while left <= right:
            mid = (left + right) // 2
            total_hour = totalHours(piles, mid)
            if total_hour <= h:
                right = mid - 1
            else:
                left = mid + 1
        return left