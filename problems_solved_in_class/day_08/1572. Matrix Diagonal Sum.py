'''Given a square matrix mat, return the sum of the matrix diagonals.

Only include the sum of all the elements on the primary diagonal and all the elements on the secondary diagonal that are not part of the primary diagonal.

 '''

class Solution(object):
    def diagonalSum(self, mat):
        n = len(mat)
        total = 0
        j=n-1
        for i in range(n):
            total += mat[i][i]
            total += mat[i][j - i]

        if n % 2 == 1:
            total -= mat[n // 2][n // 2]

        return total 