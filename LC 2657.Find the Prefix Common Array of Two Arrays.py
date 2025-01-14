'''
2657. Find the Prefix Common Array of Two Arrays

BEATS ONLY 5 % - VERY POOR / BASIC SOLUTION!
'''

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        answer = []

        for i in range(len(A)):
            if i == 0 and A[i] == B[i]:
                answer.append(1)
            elif i == 0 and A[i] != B[i]:
                answer.append(0)
            else:
                count = 0
                for j in range(0, i+1):
                    if A[j] in B[0:i+1]:
                        count += 1
                answer.append(count)
            
        return answer