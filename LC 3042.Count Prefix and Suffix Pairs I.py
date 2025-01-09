'''
3042. Count Prefix and Suffix Pairs I

COMPLETED
'''

'''
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        sortedWords = sorted(words, key = len)
        answer = 0
        for i, j in enumerate(words):
            for k in range(i+1, len(words)):
                # print(j + " " + words[k][-1: (-1 * len(j) - 1)])
                # this is wrong
                # the correct way to do this:
                # words[k][(-1 * len(j) - 1) : -1]
                # print(j + " " + words[k][0:len(j)]+ " " + words[k][(-1 * len(j) - 1) : ])
                if j == sortedWords[k][0:len(j)] and j == sortedWords[k][len(sortedWords[k]) - len(j) : ]:
                    if words.index(j) < words.index(sortedWords[k]):
                        answer += 1
                    elif j == words[k]:
                        answer += 1
                    # print(j + " " + words[k][0:len(j)]+ " " +words[k][(-1 * len(j) - 1) : -1])
        return answer
'''

# redoing it the next day
class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        answer = 0
        for i, j in enumerate(words):
            if j == len(words) - 1:
                return answer
            for k in range(i+1, len(words)):
                if j == words[k][0:len(j)]:
                    revJ = j[::-1] # reversing a string
                    revK = words[k][::-1]
                    if revJ == revK[0:len(j)]:
                        answer += 1
        return answer
