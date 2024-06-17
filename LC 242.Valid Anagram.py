'''
242. Valid Anagram

https://leetcode.com/problems/valid-anagram/description/

MULTIPLE SOLUTIONS
'''

# 1. HASHMAP SOLUTION

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #HASH MAP SOLUTION
        if len(s) != len(t):
            return False
        countS, countT = {}, {}

        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0) # what .get does is if s[i] is a valid key, it just return that to get incremented, and if the key doesn't exist, IT INITALIZES IT WITH A VALUE OF 0 (SO THAT ITS ADDED WITH 1)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for c in countS:
            if countS[c] != countT.get(c, 0): # imagine the key doesn't exist in the opposite hashmap of T, then you initalize 0 to not get error
                return False
        return True
    
# 2. PYTHON INBUILT HASHMAP BUILDER SOLUTION

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    

# O(1) SOLUTION
# 3. YOU CAN ALSO PUT ALL LETTERS IN A LIST, AND SORT AND CHECK IF BOTH LISTS ARE SAME

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)