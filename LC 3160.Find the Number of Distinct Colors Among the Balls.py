'''
3160. Find the Number of Distinct Colors Among the Balls
'''

'''
# THIS SOLUTION GOT MEMORY LIMIT EXCEEDED!

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        l = [0] * (limit + 1)
        ans = []

        for i in queries:
            l[i[0]] = i[1]
            prev = []
            localans = 0
            for j in l:
                if j != 0  and j not in prev:
                    localans += 1
                    prev.append(j)
            ans.append(localans)
        
        return ans

'''

class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:

        