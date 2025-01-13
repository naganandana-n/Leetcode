'''
3223. Minimum Length of String After Operations

shitty solution - check the optimal one
my solution rn beats 5 % of the solutions lol
'''

'''
class Solution:
    def minimumLength(self, s: str) -> int:
        s = list(s)
        exists = True
        count = len(s)

        while exists:
            # so im doing this to ensure that i've not missed out any letters - but this doesn't seem to be the best way to do it, as I'm getting TLE error
            for i, j in enumerate(s):
                if i == 0 or i == len(s) - 1:
                    pass
                elif j in s[0:i] and j in s[i+1:]:
                    s.remove(j)
                    s.reverse()
                    s.remove(j)
                    s.reverse()
                    # done to remove the character from front and back
                    # hence the 2 reverse
                    # there prolly exists a better way to do this
                    # print(s)
            if count != len(s):
                count = len(s)
            else:
                exists = False
    
        
        return len(s)
'''

# so i used a bit of pattern recognition
# what i'm seeing is - if there are an odd number of letters, you can remove 2 from them and keep doing that
# ik that order here matters, but I think cause its odd number letters, i can afford to not pay attention to that (atleast now)

class Solution:
    def minimumLength(self, s: str) -> int:
        s = list(s)
        s.sort()
        d = {}
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        print(d)
        answer = 0
        for i in d:
            while d[i] > 3:
                d[i] -= 2
            if d[i] == 3:
                d[i] -= 2
            # print(d[i])
            answer += d[i]
        return answer



        