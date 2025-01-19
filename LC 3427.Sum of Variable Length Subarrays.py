'''
3427. Sum of Variable Length Subarrays
'''

class Solution:
    def subarraySum(self, nums: List[int]) -> int:

        total = 0
        
        for i, j in enumerate(nums):
            for k in range(max(i - j, 0), i+1):
                # print(nums[k])
                total += nums[k]

        return total