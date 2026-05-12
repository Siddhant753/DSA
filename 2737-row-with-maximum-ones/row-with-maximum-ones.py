class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        index, ones = 0, 0
        n = len(mat)
        for i in range(n):
            count = sum(mat[i])
            if count > ones:
                ones = count
                index = i
        return [index, ones]