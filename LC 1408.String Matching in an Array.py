'''
1408. String Matching in an Array
'''

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        '''
        words = sorted(words)
        words.sort() - not working
        ok no, it works - but its sorting based on first letter, whereas i want it to sort based on length of word

        my solution here doesn't sort the list at all - so no optimization - i just check for solutions that are greater in len than the OG word (j)
        '''
        
        answer = []
        for i, j in enumerate(words):
            for k in range(len(words)):
                if len(words[k]) >= len(j) and j in words[k] and j != words[k]:
                    answer.append(j)
                    break

        return answer
