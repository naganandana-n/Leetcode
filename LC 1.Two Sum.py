'''
1. Two Sum

https://leetcode.com/problems/two-sum/description/
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # DONT DO THE BRUTE FORCE SOLUTION -> O(N^2)

        # FIRST CREATE A DICT 
        hashmap = {}
        for i in range(len(nums)):
            # IF TARGET - ARRAY NUM IS IN DICT
            if target - nums[i] in hashmap:
                return hashmap[target - nums[i]], i
            else:
                # ELSE ADD ARRAY NUM TO DICT
                hashmap[nums[i]] = i
        