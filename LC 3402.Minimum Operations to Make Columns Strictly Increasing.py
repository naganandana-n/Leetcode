'''
3402. Minimum Operations to Make Columns Strictly Increasing
https://leetcode.com/problems/minimum-operations-to-make-columns-strictly-increasing/description/
'''

class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        operations = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if i == 0:
                    pass
                elif grid[i-1][j] >= grid[i][j]:
                    oldgrid = grid[i][j]
                    grid[i][j] = grid[i-1][j] + 1
                    operations += grid[i][j] - oldgrid

        return operations
                
                