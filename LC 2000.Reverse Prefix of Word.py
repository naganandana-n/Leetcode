'''
2000. Reverse Prefix of Word

CHECK FOR BETTER SOLUTION
'''

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
       ind = word.find(ch)
       rev = word[0:ind+1]
       return str(rev[::-1]) + str(word[ind+1:])
