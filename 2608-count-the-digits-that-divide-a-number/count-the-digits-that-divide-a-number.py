class Solution:
    def countDigits(self, num: int) -> int:
        count = 0
        temp = num
        while temp != 0:
            val = temp % 10
            temp = temp // 10
            if val != 0 and num % val == 0:
                count += 1
        return count