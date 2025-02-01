'''
3438. Find Valid Pair of Adjacent Digits in String
'''

'''
class Solution:
    def findValidPair(self, s: str) -> str:
        # they have to be fucking adjacent also
        s = list(s)
        answer = ""
        for i in s:
            if s.count(i) == int(i) and i not in answer:
                answer += str(i)
        if len(answer) >= 2:
            return answer[:2]
        else:
            return ""
'''

class Solution:
    def findValidPair(self, s: str) -> str:

        s = list(s)
        for i, j in enumerate(s):
            if i < len(s) - 1:
                if s.count(j) == int(j) and s.count(s[i+1]) == int(s[i+1]) and j != s[i+1]:
                    return str(j) + str(s[i+1])
        return ""