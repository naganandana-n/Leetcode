'''
3417. Zigzag Grid Traversal With Skip
'''

class Solution:
    def zigzagTraversal(self, grid: List[List[int]]) -> List[int]:
        answer = []
        turn = True
        for i, j in enumerate(grid):
            if i % 2 != 0:
                j = j.reverse()
        # print(grid)
        for i in grid:
            for j in i:
                if turn:
                    answer.append(j)
                    turn = False
                else:
                    turn = True

        return answer