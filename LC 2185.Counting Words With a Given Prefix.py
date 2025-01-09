'''
2185. Counting Words With a Given Prefix
'''

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        '''
        words = ["a", "b"]
        print(words[0][0:10])
        '''
        l = len(pref)
        answer = 0
        for i, j in enumerate(words):
            if pref == j[0:l]:
                answer += 1
        return answer