class Solution:
    def maxDepth(self, s: str) -> int:
        max_depth = 0
        balance = 0
        for char in s:
            if char == "(":
                balance += 1
            elif char == ")":
                balance -= 1
            max_depth = max(max_depth, balance)
        return max_depth