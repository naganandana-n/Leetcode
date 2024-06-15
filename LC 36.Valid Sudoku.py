'''
36. Valid Sudoku

https://leetcode.com/problems/valid-sudoku/description/

'''

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Create a defaultdict where each value is a set
        # defaultdict(<class 'set'>, {1: {1}, 2: {4}, 3: {9}, 4: {16}, 5: {25}})
        row = defaultdict(set)
        col = defaultdict(set)
        sqr = defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".": #do this so that its not added to the set
                    continue
                if board[r][c] in row[r] or board[r][c] in col[c] or board[r][c] in sqr[(r//3, c//3)]: # r//3 gives lower value of r/3 (floor division)
                    return False
                
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                sqr[(r//3, c//3)].add(board[r][c])

        return True