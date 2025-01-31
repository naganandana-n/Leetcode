'''
392. Is Subsequence

meme solution
'''

'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        # here's the first solution that came to my head: its a weird one:

        # already see the problem in this tho:
        # if there are mutiple same letters, then my solution fails
        # ill implement it anyway - for the memes
        # or maybe not - i might have found a way
        position = []
        s = list(s)
        for i, j in enumerate(s):
            if j in t:
                if len(position) == 0:
                    position.append(t.index(j))
                elif position[-1] == len(t) - 1 and i != len(s) - 1:
                    # edge case
                    return False
                elif position[-1] < t[position[-1]:].index(j):
                    # print statements for debugging
                    # print(position[-1])
                    # print(t[position[-1]:].index(j))
                    position.append(t.index(j))
                else:
                    # print("came here")
                    return False
            else:
                return False
        
        return True

'''

# new day, new solution
# first i want to try and understand why my exisitng solution works for the test cases but gives me 'ValueError: substring not found' for the other cases
# what if i use try except?

# i have no idea whats going on in this test case here:
# t = "abzba"
# t.find('a') and t.index('a') -> both returning None
# omg im such an idiot -> it was returning None cause i was pritnting the operation of appedning it onto a list

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        position = []
        s = list(s)
        t = list(t)
        print(s)
        for i, j in enumerate(s):
            if j in t:
                if len(position) == 0:
                    position.append(t.index(j))
                elif position[-1] == len(t) - 1 and i != len(s) - 1:
                    # edge case
                    return False
                else:
                    try:
                        print("i did go here tho")
                        print(j)
                        print(t[position[-1]:].index(j))
                        t[position[-1]:].index(j)
# ohh i realise a big flaw that i overlooked here:
# when i do t[position[-1]:], the indexing starts with position[-1] as 0
# accounting for that
                        if position[-1] < t[position[-1]:].index(j)+position[-1]:
                            position.append(t.index(j))
                        else:
                            return False
                    except ValueError:
                        print("heere")
                        return False
                # else:
                #     print("no, here")
                #     return False
            else:
                return False
        
        return True

# still getting wrong answer -> im going to think and refine this stupid solution - for the memes.