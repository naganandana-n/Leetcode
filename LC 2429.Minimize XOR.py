'''
2429. Minimize XOR

NOT DONE!!
'''

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # print(bin(3)) # printing a int as binary
        # print(bin(2)[2:]) # int to binary without '0b' in it

        # what i understand about xor: a xor b = c
        # if i know c and b, then: c xor b = a
        # so i can apply that here

        # ok so what i've understood after a few wrong testcases
        # is that I dont understand the problem here
        # I've designed my current solution only seeing the problem
        # statement without understanding the logic

        setbits = str(bin(num2)).count('1')
        minicount = -1
        answer = 0
        for i in range(max(num1, num2)+1):
            bini = int(bin(i)[2:])
            if str(bini).count('1') == setbits:
                if minicount == -1 or i ^ num1 <= minicount:
                    answer = i
                    minicount = i ^ num1
        
        return answer
        

