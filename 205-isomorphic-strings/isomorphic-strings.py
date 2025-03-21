class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        HM1, HM2 = {}, {}
        n = len(s)
        for i in range(n):
            char1, char2 = s[i], t[i]
            if (char1 in HM1 and HM1[char1] != char2) or (char2 in HM2 and HM2[char2] != char1):
                return False

            HM1[char1] = char2
            HM2[char2] = char1

        return True