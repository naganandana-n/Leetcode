'''
347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/description/

SEE NEETCODE EXPLANATION
'''

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)] # MAKE A LIST OF LISTS: [[], [], []] OF LENGTH NUMS LEN + 1

        for num in nums: # PUT THE COUNTS IN A DICT
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        
        for num, c in count.items():
            freq[c].append(num)

        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res