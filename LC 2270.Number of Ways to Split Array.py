'''
2270. Number of Ways to Split Array
'''

# this is my first solution, accepted
# very slow - beats only 6.68%
# this is because im using list reversal and other things
# i have to study how time complexity works for these problems

'''
LOGIC OF THIS PROGRAM:

eg) [10, 4, -8, 7]

so what i do first is calc a prefix and suffix array:
prefixList = [0, 10, 14, 6, 13]
suffixList = [0, 7, -1, 3, 13]

reverse the suffix list:
prefixList = [0, 10, 14, 6, 13]
suffixList = [13, 3, -1, 7, 0]
indexes:      0   1   2  3  4

look at indexes 1, 2 (they fit the conditions of the question)

the logic to solve the question:
if prefixList[i] >= suffixList[i]:
    answerCount += 1
return answerCount
'''

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixList = [0,]
        suffixList = [0,]
        prefixCount = 0
        suffixCount = 0

        for i in nums:
            prefixCount += i
            prefixList.append(prefixCount)
        for i in range(-1, (len(nums)*-1)-1, -1):
            suffixCount += nums[i]
            suffixList.append(suffixCount)
        suffixList.reverse()
        
        answer = 0
        for i in range(len(prefixList)):
            if i != 0 and i != len(prefixList)-1:
                if prefixList[i] >= suffixList[i]:
                    answer += 1
        
        return answer
    
# make a better solution tomorrow
# understand how time complexity works - start reading about it and seeing its applications everyday
    