'''
724. Find Pivot Index
'''


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_array = [nums[0]]
        # i gives index, j gives value
        for i, j in enumerate(nums):
            if i == 0:
                pass
            else:
                prefix_array.append(prefix_array[i-1] + j)
        print(prefix_array)
        # print done to debug and understand logic

        for i, j in enumerate(prefix_array):
            if i == 0:
                if (prefix_array[-1] - j == 0):
                    return i
            elif i == (len(prefix_array) - 1):
                if (prefix_array[i-1] == 0):
                    return i
            else:
                if ((prefix_array[-1] - j) == prefix_array[i-1]):
                    return i

        return -1