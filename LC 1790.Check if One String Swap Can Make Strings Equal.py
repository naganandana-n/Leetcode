'''
1790. Check if One String Swap Can Make Strings Equal
'''

# this is not the best solution!!!

class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        # edge case - since they said atmost one swap (max one):
        if s1 == s2:
            return True

        nots1 = []
        nots2 = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                nots1.append(s1[i])
                nots2.append(s2[i])
        nots1.sort()
        nots2.sort()
        if nots1 == nots2 and len(nots1) == len(nots2) == 2:
            return True
        else:
            return False