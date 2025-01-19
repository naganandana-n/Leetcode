'''
3423. Maximum Difference Between Adjacent Elements in a Circular Array
'''

class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        answer = 0
        for i, j in enumerate(nums):
            diff = 0
            if i == len(nums) - 1:
                diff = abs(nums[i] - nums[0])
            else:
                diff = abs(j - nums[i - 1])
            if diff >= answer:
                answer = diff

        # ok so they asked max diff
        # so that meant: i and i - 1 AND ALSO i and i + 1 DIFFERENCES!!
        nums.reverse()
        for i, j in enumerate(nums):
            diff = 0
            if i == len(nums) - 1:
                diff = abs(nums[i] - nums[0])
            else:
                diff = abs(j - nums[i - 1])
            if diff >= answer:
                answer = diff

        return answer