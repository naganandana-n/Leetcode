'''
DO AGAIN!!!

For two strings s and t, we say "t divides s" if and only if 
s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 
Example 1:

Input: str1 = "ABCABC", str2 = "ABC"
Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"

Example 3:

Input: str1 = "LEET", str2 = "CODE"
Output: ""
 

Constraints:

1 <= str1.length, str2.length <= 1000
str1 and str2 consist of English uppercase letters.

'''

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        l1, l2 = len(str1), len(str2)

        def isDivisor(i):
            if l1 % i or l2 % i: # BOTH STR1 AND STR2 SHOULD BE A MULTIPLE OF i
                return False
            f1, f2 = l1 // i, l2 // i
            return str1[:i] * f1 == str1 and str1[:i] * f2 == str2 # MULTIPLYING LENGTH WITH STR1[:i]
                                                                   #  SHOULD GIVE THE OG STRING BACK

        for i in range(min(l1, l2), 0, -1): # YOU ITERATE IN REVERSE SO WHICHEVER SUBSTRING YOU
            if isDivisor(i):                # GET FIRST WILL AUTOMATICALLY BE THE LONGEST SUBSTRING.
                return str1[:i]
        
        return ""


'''
MY ORIGINAL SOLUTION:

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        ans = []

        for i in range(len(str1)):
            if str1[0:i] in str2:
                ans.append(str1[0:i])
        
        ans.sort(reverse=True)
        return ans[0];

Here the problem was that i didn't read into the question correctly, 
missing this part of the question:

we say "t divides s" if and only if s = t + t + t + ... + t + t 
(i.e., t is concatenated with itself one or more times).

My solution FAILS HERE:

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"
Output: "AB"
MY OUTPUT: "ABAB"

'''