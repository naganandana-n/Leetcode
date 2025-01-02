'''
2559. Count Vowel Strings in Ranges
https://leetcode.com/problems/count-vowel-strings-in-ranges/description
'''
# this solution gives 'Time limit exceeded'

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        answer = []
        for i in queries:
            count = 0
            for j in range(i[0], i[1] + 1):
                if words[j][0] in "aeiou" and words[j][-1] in "aeiou":
                    count += 1
            answer.append(count)
                    
        return answer
    
# after reading the editorial i found out about the idea called PREFIX SUM:

# so basically, I wrote this program as my v2:

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        hashmap = {}
        for i in range(len(words)):
            if words[i][0] in "aeiou" and words[i][-1] in "aeiou":
                hashmap[i] = 1
            else:
                hashmap[i] = 0
        answer = []
        for i in queries:
            count = 0
            for j in range(i[0], i[-1] + 1):
                count += hashmap[j]
            answer.append(count)
        return answer
    
# so what I'm doing here is that I'm using a dictionary to keep track of all words that have a vowel at the start and the end
# this appraoch is right, but what i can do to make my life easier is, 
# maintain a list, where each time there is a word with a vowel in it, the count of that list goes up
# lets take a simple eg:
# l = [a, b, c, e, i, o]
# prefixsum = [1, 1, 1, 2, 3, 4]
# now if i have to find according to query, i will just have to do right most minus left most
# atleast, that's what i think, let me implement and see

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        prefixSum = [0,] # already keep one element in list as 0
        sumCount = 0
        for i in words:
            if i[0] in "aeiou" and i[-1] in "aeiou":
                sumCount += 1
            prefixSum.append(sumCount)
        
        answer = []
        for j in queries:
            answer.append(prefixSum[j[-1] + 1] - prefixSum[j[0]]) # no edge cases here - bcz we did that zero thing at the prefixSum list
        return answer