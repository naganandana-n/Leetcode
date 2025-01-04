'''
3407. Substring Matching Pattern
'''

# easy question part of the biweekly contest today
# my method for solving this was a lot of trial and error, rather than thinking about the problem
# that is NOT GOOD!

class Solution:
    def hasMatch(self, s: str, p: str) -> bool:
        # the word can have letters before and after *, or either one 
        plist = p.split("*")
        print(plist)
        if len(plist) > 1 and '' not in plist:
            if plist[0] in s:
                pos = s.find(plist[0])
                nextword = s[pos+len(plist[0]):]
                print(nextword)
                if plist[1] in nextword:
                    return True
            return False
        else:
            while '' in plist:
                plist.remove('')
            if len(plist) == 0:
                return True
            elif plist[0] in s:
                return True
            else:
                return False