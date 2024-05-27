'''
2259. Remove Digit From Number to Maximize Result

https://leetcode.com/problems/remove-digit-from-number-to-maximize-result/description/

String Greedy
'''

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:

        # MAKE A LIST OF POTENTIAL ANSWERS
        potentialAns = [] 

        for i in range(0, len(number)):
            if digit == number[i]:
                potentialAns.append(number[0:i] + number[i+1:]) # PUT ALL THE ANSWERS IN THAT LIST

        # SORT THAT LIST IN REVERSE TO GET THE HIGHEST VALUE
        # "resulting string in decimal form is maximized"
        potentialAns.sort(reverse = True)
        return potentialAns[0]