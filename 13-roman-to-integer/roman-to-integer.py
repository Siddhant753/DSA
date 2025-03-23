class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value = {
            "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000
        }
        result = 0
        n = len(s)
        for i in range(n):
            if i < n-1 and roman_value[s[i]] < roman_value[s[i+1]]:
                result -= roman_value[s[i]]
            else:
                result += roman_value[s[i]]
        return result