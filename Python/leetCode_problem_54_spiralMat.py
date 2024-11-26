from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        spiral_mat = []

        m = len(matrix)     # rows
        n = len(matrix[0])  # cols

        x, y = 0, 0
        dx, dy = 1, 0

        for _ in range(m * n):
            spiral_mat.append(matrix[y][x])
            matrix[y][x] = "."

            if (not 0 <= x + dx < n or
                not 0 <= y + dy < m or 
                matrix[y+dy][x+dx] == "."):
                dx, dy = -dy, dx
                    
            x += dx
            y += dy

        return spiral_mat
                

matrix = [[1,2,3],[4,5,6],[7,8,9]]

sol = Solution()

print(sol.spiralOrder(matrix))

"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
