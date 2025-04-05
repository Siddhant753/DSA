class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if m * k > n:
            return -1

        def possible(bloomDay, day, m, k):
            bouquets = 0
            flowers = 0
            for bloom in bloomDay:
                if bloom <= day:
                    flowers += 1
                    if flowers == k:
                        bouquets += 1
                        flowers = 0
                else:
                    flowers = 0
            return bouquets >= m

        left, right = min(bloomDay), max(bloomDay)
        result = -1
        while left <= right:
            mid = (left + right) // 2
            if possible(bloomDay, mid, m, k):
                result = mid
                right = mid - 1
            else:
                left = mid + 1
            
        return result