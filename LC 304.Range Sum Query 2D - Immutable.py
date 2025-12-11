'''
304. Range Sum Query 2D - Immutable

neetcode prefix sum
'''


class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        prefix_matrix = []
        for i in matrix:
            temp = []
            for j, k in enumerate(i):
                if j == 0:
                    temp.append(k)
                else:
                    temp.append(k + temp[j - 1])
            prefix_matrix.append(temp)

        self.prefix_matrix = prefix_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # print to debug and see if i got it right
        # print(self.prefix_matrix)

        sum = 0
        for i in range(row1, row2 + 1):
            # edge cases
            if col1 == 0:
                sum += self.prefix_matrix[i][col2]
            else:
                sum += (self.prefix_matrix[i][col2] - self.prefix_matrix[i][col1 - 1])
        
        return sum


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)


# better solution i came up with
# that uses 2D prefix array:
# faster runtime

# my solution for 2D prefix array
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        prefix_matrix = []
        for l, i in enumerate(matrix):
            temp = []
            for j, k in enumerate(i):
                if l == 0:
                    if j == 0:
                        temp.append(k)
                    else:
                        temp.append(k + temp[j - 1])
                else:
                    if j == 0:
                        temp.append(k + prefix_matrix[l - 1][j])
                    else:
                        temp.append(k + temp[j - 1] + prefix_matrix[l - 1][j] - prefix_matrix[l-1][j - 1])
            prefix_matrix.append(temp)
        
        self.prefix_matrix = prefix_matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        if row1 != 0 and col1 != 0:
            return self.prefix_matrix[row2][col2] + self.prefix_matrix[row1-1][col1-1] - self.prefix_matrix[row1-1][col2] - self.prefix_matrix[row2][col1-1]
        
        elif row1 !=0:
            return self.prefix_matrix[row2][col2] - self.prefix_matrix[row1-1][col2]
        elif col1 != 0:
            return self.prefix_matrix[row2][col2] - self.prefix_matrix[row2][col1-1]
        else:
            return self.prefix_matrix[row2][col2]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)