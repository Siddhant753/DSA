class Solution:
    def romanToInt(self, s: str) -> int:
        roman_value = {
            "I" : 1, "V" : 5, "X" : 10, "L" : 50, "C" : 100, "D" : 500, "M" : 1000
        }
        result = 0
        pre_val = 0
        for char in reversed(s):
            value = roman_value[char]
            if value < pre_val:
                result -= value
            else:
                result += value
            pre_val = value
        return result