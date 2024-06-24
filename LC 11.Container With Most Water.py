'''
11. Container With Most Water

https://leetcode.com/problems/container-with-most-water/description/
'''

# BRUTE FORCE - TWO POINTER APPROACH:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        # checking every single combination, O(n^2)
        # still using concepts from 2 pointer
        # GIVES TIME LIMIT EXCEEDED ERROR!!!

        maxArea = 0

        for l in range(len(height)):
            for r in range(l+1, len(height)):
                area = min(height[l], height[r]) * (r - l)
                maxArea = max(maxArea, area)
        
        return maxArea
    
# OPTIMAL SOLUTION:

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # linear time solution -> O(n)
        # MOVE the pointer that has THE LEAST HEIGHT!

        maxArea = 0
        l, r = 0, len(height) - 1
        
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            maxArea = max(maxArea, area)

            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                r -= 1 # you can either do r or l here
        
        return maxArea

