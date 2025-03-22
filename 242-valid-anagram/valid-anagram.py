class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        HM = {}
        if n != m:
            return False
        for char in s:
            HM[char] = HM.get(char, 0) + 1
        for char in t:
            if char not in HM or HM[char] == 0:
                return False
            HM[char] -= 1
        return True