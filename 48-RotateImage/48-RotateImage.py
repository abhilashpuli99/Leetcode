# Last updated: 9/2/2025, 1:43:53 PM
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix[0])):
            for j in range(len(matrix[0])):
                if i<j:
                   matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
            matrix[i]=matrix[i][::-1]
        return matrix 
        