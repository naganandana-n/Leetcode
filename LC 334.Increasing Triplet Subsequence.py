'''
334. Increasing Triplet Subsequence
'''

class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        # Could you implement a solution that runs in O(n) time complexity and O(1) space complexity?

        # here the constraints are from 2^(-31) to 2^(31)
        # so how do you code that in?
        # you can use placeholders for +ve infinity and -ve infinity
        first = float('inf')
        second = float('inf')
        # -ve infinity : float('-inf')

        for i in nums:
            if i <= first:
                first = i
            elif i <= second:
                second = i
            else:
                return True
        return False