class Solution:
    def reverse(self, x: int) -> int:
        rev = 0
        temp = abs(x)
        while temp:
            rev = (rev * 10) + temp % 10
            temp //= 10

        if -2 ** 31 > rev  or rev > 2 ** 31 - 1:
            return 0
        
        if x < 0:
            return -rev
        else:
            return rev