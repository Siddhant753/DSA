class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        def totalHours(k):
            return sum((bananas + k - 1) // k for bananas in piles)

        while left < right:
            mid = (left + right) // 2
            if totalHours(mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left