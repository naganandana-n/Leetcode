'''
4. Median of Two Sorted Arrays

I HAVE TO UNDERSTAND WHY MY SOLUTION WORKS! 
- THE TIME COMPLEXITY AND ALL THAT!
'''

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # so median is the value that lies at the midpoint
        # [1, 2, 3]
        # median = 2
        # but its not the value
        # eg: [1, 2, 3, 4] -> median = 2.5
        # ig even no. of elements

        nums = nums1 + nums2
        # print(nums) -> adding 2 lists together
        nums.sort()
        if len(nums) % 2 != 0:
            return nums[(len(nums) - 1) // 2]
        else:
            # print(nums[(len(nums) - 1) // 2])
            # print(nums[((len(nums) -1) // 2) + 1])
            return ((nums[(len(nums) - 1) // 2] + nums[((len(nums) -1) // 2) + 1]) / 2)

