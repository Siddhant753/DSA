class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        operations = 0
        n = len(nums)
        while True:
            non_zeros = [x for x in nums if x > 0]

            if not non_zeros:
                return operations
            
            min_val = min(non_zeros)

            for i in range(n):
                if nums[i] > 0:
                    nums[i] -= min_val
            operations += 1