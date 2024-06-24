'''
125. Valid Palindrome

https://leetcode.com/problems/valid-palindrome/description/
'''

# MY ORIGINAL SOLUTION

class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = ""
        for i in s:
            if i.isalnum():
                newString += i
        newString = newString.lower()
        
        print(newString)
        return newString == newString[::-1]
    
# THE ABOVE SOLUTION, USES EXTRA MEMORY: TO STORE THE NEW STRING, AND TO REVERSE IT

# SOLUTION WHICH HAS O(1) MEMORY (IE, NO EXTRA MEMORY USED):
# TWO POINTERS

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def alphaNum(c): # HERE WE CODE OUT OUR OWN ALPHANUMERIC CHECKER
            if (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9')):
                return True
            else:
                return False
        
        l, r = 0, len(s) - 1

        while l < r: # WHILE THE 2 POINTERS NOT PASSED EACH OTHER
            while not alphaNum(s[l]) and l < r:
                l += 1
            while not alphaNum(s[r]) and r > l: # WE DO THE AND R > L TO ENSURE THAT THE POINTERS HAVEN'T PASSED EACH OTHER, CAUSE NO NEED TO CHECK YEAH IF THEY HAVE (WE'VE ALREADY CHECKED BEFORE)
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l, r = l + 1, r - 1
        return True