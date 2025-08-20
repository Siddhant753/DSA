class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        temp = n
        product = 1
        num_sum = 0
        while temp:
            product = product * (temp % 10)
            num_sum = num_sum + temp % 10
            temp //= 10
        result = product - num_sum
        return result