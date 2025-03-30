class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            # Ensure mid is even for pairing
            if mid % 2 == 1:
                mid -= 1 # Move mid to left if its odd

            if nums[mid] == nums[mid+1]: # Single element is in right half
                left = mid + 2
            else: # Single element is in left half
                right = mid
        
        return nums[left]