'''
217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate/description/

array
'''

# INITIAL SOLUTION: PROBLEM - TIME LIMIT EXCEEDED
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        newList = []
        answer = False
        for i in nums:
            if i not in newList:
                newList.append(i)
            else:
                answer = True
                return answer
                break
        return answer
    
# THE IDEA ABOVE IS CORRECT, BUT BY IMPLEMENTING IT USING HASHSET, RATHER THAN LIST, TIME IS SAVED

# HASHSET SOLUTION
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for i in nums:
            if i in hashset:
                return True
            hashset.add(i) # .add not .append
        return False