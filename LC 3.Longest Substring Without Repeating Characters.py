'''
3. Longest Substring Without Repeating Characters

not complete!!
'''

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # i think we can do this using two pointers
        # oh it said not repeating characters
        # i rembered some other solution and applied it without thinking

        l = 0
        r = 0
        longest = 0
        count = 1

        while r < len(s):
            if s[l] != s[r]:
                print(s[l])
                print(s[r])
                count += 1
            elif count > longest:
                longest = count
                count = 1
                l = r
            r += 1
        
        return longest


# this is another solution that i implemented, without fully 
# understanding the problem at hand

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        substring = ""
        # print("" == " ") # they not the same
        if len(s) == 0 or len(s) == 1:
            return len(s) # the edge case
        for i, j in enumerate(s):
            print(substring)
            if j in substring:
                print(len(substring))
                if len(substring) > longest:
                    longest = len(substring)
                    substring = j
            else:
                substring += j
        
        if len(substring) > longest:
            return len(substring)
        else:
            return longest
'''

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        longest = 0
        count = 0
        while r < len(s):
            if s[r] in s[l:r]:
                l += 1
                r += 1
                longest = count
            else:
                r += 1
                count += 1
        return longest