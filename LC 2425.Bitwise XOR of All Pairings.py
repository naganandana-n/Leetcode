'''
2425. Bitwise XOR of All Pairings

MEMORY LIMIT EXCEEDED ERROR!
'''

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        total = []
        answer = 0
        for i in nums1:
            for j in nums2:
                total.append(i ^ j)

        for i, j in enumerate(total):
            if i == 0:
                answer = j
            else:
                answer = j ^ answer
        
        return answer