class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        opened, closed = 0, 0
        n = len(s)
        for i in range(n):
            if s[i] == '(':
                opened += 1
            else:
                if opened > 0:
                    opened -= 1
                else:
                    closed += 1
        return opened + closed