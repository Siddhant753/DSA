class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def possible_weight(weights, days, capacity):
            total = 0
            day = 1
            for weight in weights:
                if weight > capacity:
                    return False
                if total + weight > capacity:
                    day += 1
                    total = 0
                total += weight
            return day <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if possible_weight(weights, days, mid):
                right = mid
            else:
                left = mid + 1
        return left