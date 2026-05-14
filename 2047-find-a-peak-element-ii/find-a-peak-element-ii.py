class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                up = mat[i-1][j] if i > 0 else -1
                down = mat[i+1][j] if i < m-1 else -1
                left = mat[i][j-1] if j > 0 else -1
                right = mat[i][j+1] if j < n-1 else -1

                if mat[i][j] > up and mat[i][j] > down and mat[i][j] > left and mat[i][j] > right:
                    return [i, j]