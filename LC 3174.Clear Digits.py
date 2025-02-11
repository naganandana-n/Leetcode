'''
3174. Clear Digits
'''

'''
class Solution:
    def clearDigits(self, s: str) -> str:
        # two pointers:
        l = 0
        r = 0
        d = list(s)
        print(d)
        ans = ""
        while r < len(s):
            print(str(l) + " " + str(r))
            if s[r].isdigit == True:
                print(l + " " + r)
                l -= 1
            r += 1
        for i in d:
            ans += i
        return ans
'''

# fuck this im doing a brute force

class Solution:
    def clearDigits(self, s: str) -> str:

        found = []
        for i, j in enumerate(s):
            if j.isdigit() == True:
                found.append(i)
                for k in range(i-1, -1, -1):
                    if k not in found:
                        found.append(k)
                        break

        ans = ""
        for i, j in enumerate(s):
            if i not in found:
                ans += j
        return ans          

        # just had to convert it from value based to index based to beat this test case:   s = "c5c"
        # lmao this the slowest sloution 