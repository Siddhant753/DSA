class Solution:
    def check(self, nums: List[int]) -> bool:
        n = len(nums)
        x = 0
        for i in range(n):
            if nums[i] > nums[(i+1) % n]:
                x += 1
                if x > 1:
                    return False
        return True