'''
238. Product of Array Except Self
'''

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # the solution i see:
        # i will have to go through the array twice - O(2n) - O(n)

        total = 1
        # NOTE: List comprehesnions are used to make new lists,
        # not perform in place assignments
        # total = [total *= i for i in nums]
        # WRONG - not working

        for i in nums:
            total *= i
        ans = []
        for i in nums:
            if i == 0: # edge case where i == 0
                ans.append(total)
            else:
                ans.append(total // i)
        return ans
        # BUT, the question says we cant use division

'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        # ok so here's the solution that does it in O(n)
        # while also mainting O(n) space also

        pre = [1]
        suf = [1] 

        for i in range(0, len(nums)-1):
            pre.append(pre[i] * nums[i])
        
        for i in range(len(nums) - 1, 0, -1):
            suf.append(nums[i] * suf[len(nums) - i - 1])
        suf.reverse()
        
        ans = []
        for i in range(len(pre)):
            ans.append(pre[i] * suf[i])
        
        return ans

        # this solution handles even the cases:
        # - if theres 1 zero, then you should return the remaining total in the place of the zero
        # - if theres more than 1 zero, the you should return 0's for all the elements of the array

        