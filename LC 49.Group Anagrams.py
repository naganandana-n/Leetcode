'''
49. Group Anagrams

https://leetcode.com/problems/group-anagrams/description/

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # using hashmap(dict)
        # what im doing is, the key will be letters in the word
        # and the value is the list of words that match that

        # IMPORTANT FUNCTION:
        # ORD( ) -> gets ascii value of letter

        result = defaultdict(list)

        for s in strs:
            count = [0] * 26 # a...z
            for c in s:
                count[ord(c) - ord("a")] += 1
            
            result[tuple(count)].append(s) # dicts can't take lists as key
        
        answer = []
        for key, value in result.items():
            local = []
            for i in value:
                local.append(i)
            answer.append(local)
        return answer
        
# Better solution (ONLY LAST PART OF SHOWING RESULT IS DIFFERENT - ONE LINE)

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) #mapping character count to list of Anagrams

        for s in strs:
            count = [0] * 26

            for c in s:
                count[ord(c) - ord("a")] += 1
            
            res[tuple(count)].append(s)

        return res.values()

        # O(m * n) m -> no. of strings, n -> avg length of a string
