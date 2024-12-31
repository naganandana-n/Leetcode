'''
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/description/
'''

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # stack to keep track
        for i in s:
            if i in "([{":
                stack.append(i)
            elif i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        return True
        
'''
This first implementation misses out on this edge case:
if s = [, then it gives True -> which is wrong!
'''

# WORKING SOLUTION:

class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # stack to keep track
        for i in s:
            if len(stack) == 0: # DID THIS TO DEAL WITH AN EDGE CASE, WHERE IF YOU GIVE: S = }, THE PROGRAM FAILS OTHERWISE
                stack.append(i) 
            elif i in "([{":
                stack.append(i)
            elif i == ")" and stack[-1] == "(":
                stack.pop()
            elif i == "]" and stack[-1] == "[":
                stack.pop()
            elif i == "}" and stack[-1] == "{":
                stack.pop()
            else:
                return False
        if len(stack) == 0:
            return True
        else:
            return False # IMP OTHERWISE IT RETURNS NULL
        
# LEARN THE HASHMAP SOLUTION FOR THIS!
