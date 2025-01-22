'''
3194. Minimum Average of Smallest and Largest Elements

NOT COMPLETE!!
'''

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        # ok i know this a 2 pointers soln
        # cause of the tag
        # however, I'm gonna do my brute force first

        avg = 0
        nums.sort()
        for i in range(len(nums)//2):
            s = nums.pop(0)
            l = nums.pop(-1)
            if i == 0 or avg > (s + l) / 2:
                avg = (s + l) / 2
        return avg

