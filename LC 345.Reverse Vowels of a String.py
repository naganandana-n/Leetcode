'''
345. Reverse Vowels of a String

ONLY BRUTE FORCE SOLN!!
'''

class Solution:
    def reverseVowels(self, s: str) -> str:
        v = "aeiouAEIOU"
        l = []
        s = list(s)
        for j, i in enumerate(s):
            if i in v:
                l.append(i)
        # print(s)
        # print(l)
        pos = len(l) - 1
        answer = ""
        for i in s:
            if i in v:
                answer += l[pos]
                pos -= 1
            else:
                answer += i
        return answer
