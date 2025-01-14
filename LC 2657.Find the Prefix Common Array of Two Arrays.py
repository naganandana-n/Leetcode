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
    
# better solution: [beats 49 %]


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # the solution i see here, is to have a common array
        # since both the lists are permutations of each other (ie),
        # they both have the same elements and that also only 1 of
        # each. Append every element into the common array, if the
        # element occurs twice, add it to the count answer array

        common = []
        answer = []
        acount = 0
        for i in range(len(A)):
            if A[i] in common:
                # print(A[i])
                acount += 1
            common.append(A[i])
            if B[i] in common:
                # print(B[i])
                acount += 1
            common.append(B[i])
            answer.append(acount)

        return answer

