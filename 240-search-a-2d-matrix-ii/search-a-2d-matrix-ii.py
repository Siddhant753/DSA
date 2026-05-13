class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row = 0
        while row < m:
            left, right = 0, n-1
            while left <= right:
                mid = (left + right) // 2
                val = matrix[row][mid]
                if val == target:
                    return True
                elif val < target:
                    left = mid + 1
                else:
                    right = mid - 1
            row += 1
        return False