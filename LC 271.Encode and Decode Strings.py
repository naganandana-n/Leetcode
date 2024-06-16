'''
271. Encode and Decode Strings

https://neetcode.io/problems/string-encode-and-decode

input = ["naga", "nandana"]
output = 4#naga7#nandana

vice versa for decode
'''

class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for i in strs:
            result += str(len(i)) + "#" + i
        return result
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i : j])
            result.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return result