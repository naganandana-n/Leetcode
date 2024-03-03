'''
You are given two strings word1 and word2. 
Merge the strings by adding letters in alternating order, 
starting with word1. If a string is longer than the other, 
append the additional letters onto the end of the merged string.

Return the merged string.


Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r


Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s


Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
 

Constraints:

1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.

'''

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0 # pointers to word1 and word2

        res = [] # list res, used to store the final word to be returned.

        while i < len(word1) and j < len(word2):
            res.append(word1[i])
            res.append(word2[j])
            i += 1
            j += 1
        res.append(word1[i:]) # if word1 is empty, ie i has reached the end of word1, it appends nothing
        res.append(word2[j:]) # similar scenario with word2

        return "".join(res) # in python, its inefficent to append characters to strings,
                            # rather, just store the entire string in the form of a list
                            # and in the end return "".join(res) which adds all the strings
                            # in the list res into one string and returns it.