class Solution:
    def beautySum(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(n):
            HM = {}
            for j in range(i, n):
                char = s[j]
                HM[char] = HM.get(char, 0) + 1
                
                max_freq = max(HM.values())
                min_freq = min(HM.values())

                result += (max_freq - min_freq)
        return result