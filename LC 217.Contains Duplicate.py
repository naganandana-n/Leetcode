'''
217. Contains Duplicate

https://leetcode.com/problems/contains-duplicate/description/
'''

# LIST SOLUTION (SELF CODED): [GIVES TIME LIMIT EXCEEDED] [O(N^2)]

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # my LIST solution:

        l = []
        for i in nums:
            if i in l:
                return True
            else:
                l.append(i)
        return False
    
# HASH SET SOLUTION

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # USING HASHSET INSTEAD OF LIST - CAUSE ITS BETTER TIME WISE
        # O(n) -> Time complexity
        # O(n) -> MEMORY complexity (BCZ OF HASHSET)

        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False
        