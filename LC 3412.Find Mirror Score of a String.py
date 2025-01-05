'''
3412. Find Mirror Score of a String

problem part of the weekely leetcode contest today.
'''

# i think the solution is correct, but gives "Time Limit Exceeded"

class Solution:
    def calculateScore(self, s: str) -> int:
        s = list(s)
        mirror = {"a":"z", "b":"y", "c":"x", "d":"w", "e":"v", "f":"u", "g":"t", "h":"s", "i":"r", "j":"q", "k":"p", "l":"o", "m":"n", "n":"m", "o":"l", "p":"k", "q":"j", "r":"i", "s":"h", "t":"g", "u":"f","v": "e", "w":"d", "x":"c", "y":"b", "z":"a"}
        answer = 0
        marked = []
        for i, j in enumerate(s):
            semi = s[0:i]
            semi.reverse()
            if i == 0:
                continue
            try:
                if mirror[j] in semi:
                    if len(semi) - 1 - semi.index(mirror[j], 0, i) not in marked:
                        answer += i - (len(semi) - 1 - semi.index(mirror[j], 0, i))
                        marked.append(len(semi) - 1 - semi.index(mirror[j], 0, i))
                        marked.append(i)
                        s[len(semi) - 1 - semi.index(mirror[j], 0, i)] = ""
                        s[i] = ""
            except:
                None
        return answer