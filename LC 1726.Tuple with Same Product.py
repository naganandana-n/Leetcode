'''
1726. Tuple with Same Product
'''

'''
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        
        # so the solution i saw for this used collections.Counter()
        # but im going to first do it with hashmaps (dict)

        products = {}
        
        for i, j in enumerate(nums):
            for k in range(i):
                prod = j * nums[k]
                if prod in products:
                    products[prod] += 1
                else:
                    products[prod] = 1
        
        answer = 0

        for i in products:
            if products[i] > 1:
                answer += (products[i] * (products[i] - 1)) * 4
        
        return answer
'''

# im going to implement the same solution using collections.Counter()

# how is collections.Counter() different from dict?
# - counter is optimized for counting occurances of elements
# - is the key isn't defined before, it maps it to 0
# - 

# ill implement this tomorrow mornign to see how much i remember

# morning implementaion
class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        products = collections.Counter()

        for i, j in enumerate(nums):
            for k in range(i):
                prod = nums[k] * j
                products[prod] += 1
        
        answer = 0

        for i in products:
            if products[i] > 1:
                answer += products[i] * (products[i] - 1) * 4
        
        return answer
