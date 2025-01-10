'''
916. Word Subsets

Time Limit Exceeded
'''

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:

        wordsone = []
        wordstwo = []
        answer = []
        tracker = {}

        for j, i in enumerate(words1):
            tracker[j] = True
            letter = [0] * 26
            for j in i:
                letter[ord(j) - 97] += 1
            wordsone.append(letter)

        for i in words2:
            letter = [0] * 26
            for j in i:
                letter[ord(j) - 97] += 1
            wordstwo.append(letter)

        for i in wordstwo:
            for j, l in enumerate(wordsone):
                for k, m in enumerate(i):
                    if m > wordsone[j][k]:
                        tracker[j] = False

        for i in tracker:
            if tracker[i] == True:
                answer.append(words1[i])
        return answer 



