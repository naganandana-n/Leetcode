'''
128. Longest Consecutive Sequence

https://leetcode.com/problems/longest-consecutive-sequence/description/

'''

# ORIGINAL SOLUTION - ISSUE IS THAT 'TIME LIMIT EXCEEDED'

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        for i in nums:
            if i - 1 not in nums:
                length = 0
                while i + length in nums:
                    length += 1
                if length > longest:
                    longest = length
        return longest
    
# FIX THE ERROR BY USING SETS

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numset = set(nums)
        longest = 0

        for i in numset:
            if i - 1 not in numset:
                length = 0
                while i + length in numset:
                    length += 1
                longest = max(length, longest)

        return longest