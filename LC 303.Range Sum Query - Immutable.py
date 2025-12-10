'''
303. Range Sum Query - Immutable

from neetcode list for prefix sum
'''


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums    
        l = self.nums # can't be asked to write self.nums so many times
        prefix_array = [] 
        # i see the irony of having to write prefix_array so many times now
        for i, j in enumerate(l):
            if i == 0:
                prefix_array.append(j)
            else:
                prefix_array.append(prefix_array[i-1] + j)
        self.prefix_array = prefix_array
            
    def sumRange(self, left: int, right: int) -> int:
        # edge case - cause left <= right (just think about it a little bit)
        if left == right:
            return self.nums[left]
        if left != 0:
            return self.prefix_array[right] - self.prefix_array[left-1]
        else:
            return self.prefix_array[right]

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)