'''
167. Two Sum II - Input Array Is Sorted

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

'''

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1

        while l < r:
            currentSum = numbers[l] + numbers[r]

            if currentSum > target: # IF THE CURRENT SUM IS GREATER THAN THE TARGET, YOU MOVE THE RIGHT POINTER TO LOWER
                                    # WE ARE ONLY ABLE TO DO THIS POINTER TRICK, CAUSE THE ARRAY IS ALREADY SORTED!!!
                r -= 1
            elif currentSum < target:
                l += 1
            else:
                return l + 1, r + 1

# TIME COMPLEXITY : O(N) -> WORST CASE
# MEMORY COMPLEXITY: O(1) -> SAID IN QUESTION: "Your solution must use only constant extra space."