'''
15. 3Sum

https://leetcode.com/problems/3sum/description/

'''

# SO THE TRICK IN THIS QUESTION IS THAT YOU:
# 1. SORT THE ARRAY
# 2. PICK THE FIRST NUMBER
# 3. AND THEN USE THE 'TWO SUM - 2' METHOD TO FIND THE SECOND AND THIRD NUMBER  

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort() 

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]: # SO IF THE PREVIOUS NUMBER IS THE SAME AS THE CURRENT ONE, SKIP. THIS IS DONE TO FIT THE CONSTRAINTS OF THE QUESTION (NO DUPLICATES)
                continue
            l, r = i + 1, len(nums) - 1 # i + 1, NOT JUST 1 CAUSE WE ARE IN A LOOP 
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r: # THIS PART IM A LIL CONFUSED ABOUT FROM THE NEETCODE EXPLANATION, SEE YOUTUBE FOR MORE EXPLANATIONS
                        l += 1
        return result

