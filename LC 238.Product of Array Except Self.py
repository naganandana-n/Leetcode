'''
238. Product of Array Except Self

https://leetcode.com/problems/product-of-array-except-self/description/
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums) # CREATING A RESULT ARRAY HERE IS IMPORTANT (OTHERWISE FUCKS UP)
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix # MULTIPLY YOUR RESULT WITH THE POSTFIX, THEN 
            postfix *= nums[i]   # UPDATE THE POSTFIX BY MULTIPLYING WITH ORIGINAL ARRAY

        return result