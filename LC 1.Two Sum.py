'''
1. Two Sum

https://leetcode.com/problems/two-sum/description/
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        previousMap = {} # value:index
        for i in range(0, len(nums)):
            diff = target - nums[i]
            if diff in previousMap:
                return [previousMap[diff], i]
            previousMap[nums[i]] = i
    
        