class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        HM1, HM2 = {}, {}
        n, m = len(s), len(t)
        if n != m:
            return False
        for i, j in zip(s, t):
            HM1[i] = HM1.get(i, 0) + 1
            HM2[j] = HM2.get(j, 0) + 1
        if HM1 == HM2:
            return True
        else:
            return False