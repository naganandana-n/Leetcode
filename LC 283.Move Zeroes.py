'''
283. Move Zeroes
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # very bad solution, prolly cause i did it using python functions
        count = nums.count(0)
        for i in nums:
            if count > 0: # edge case that there are no zeroes
                nums.remove(0)
                nums.append(0)