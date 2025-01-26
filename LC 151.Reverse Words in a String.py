'''
151. Reverse Words in a String

check the better solution!
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        # i think i can do this with python functions
        s = s.split() # you can't just write s.split without the equal to
        s.reverse()
        print(s)
        ans = ""
        for i, j in enumerate(s): # tried doing list comphrehension - look into it! 
            if i == len(s) - 1:
                ans += j
            else:
                ans += j + " "
        return ans