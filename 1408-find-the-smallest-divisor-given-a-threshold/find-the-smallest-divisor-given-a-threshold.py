class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def possible_sum(nums, threshold, divisor):
            Total_sum = 0
            for num in nums:
                Total_sum += math.ceil(num / divisor)
            return Total_sum <= threshold

        left, right = 1, max(nums)
        while left < right:
            mid = (left + right) // 2
            if possible_sum(nums, threshold, mid):
                right = mid
            else:
                left = mid + 1
        return left