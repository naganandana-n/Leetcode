'''
27. Remove Element

TWO POINTERS
'''

'''
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        
        # stupid soln - NOPE, its just me thats stupid:
        # THIS IS A VALID SOLUTION!!!
        p = 0
        while p < len(nums):
            if nums[p] == val:
                nums.remove(val)
                p = 0
            else:
                p += 1
        return len(nums)
'''

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        # snehas SMART SOLUTION

        k = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                count += 1 # k is same as count - so no need to maintain sepearate count, just return k
        return count
