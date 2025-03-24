class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        i, sign, result = 0, 1, 0
        INT_MAX, INT_MIN = 2**31 - 1, -2**31
        while i < n and s[i] == " ":
            i += 1
        
        if i < n and s[i] in ("+", "-"):
            sign = -1 if s[i] == "-" else 1
            i += 1

        while i < n and "0" <= s[i] <= "9":
            digit = ord(s[i]) - ord("0")

            if result > (INT_MAX - digit) // 10:
                return INT_MAX if sign == 1 else INT_MIN

            result = result * 10 + digit
            i += 1

        return sign * result