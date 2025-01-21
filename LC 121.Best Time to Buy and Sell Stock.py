'''
121. Best Time to Buy and Sell Stock
'''

'''
# in this first version of my soln:
# i'm only able to check if it satisifies the condition once
# i also make use of sort, have to make sure its better than that

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # sprices = prices.sort()
        sprices = sorted(prices)
        print(sprices)
        print(prices)
        buy = sprices[0]
        sell = sprices[-1]

        if prices.index(buy) > prices.index(sell):
            return sell - buy
        else:
            return 0 
'''

# I DONT FULLY UNDERSTAND 2 POINTERS

class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # ok so this uses 2 POINTERS
        left = 0 # buy
        right = 1 # sell
        maxprofit = 0

        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                maxprofit = max(maxprofit, profit)
            else:
                left = right # remember the neetcode video diagram
            
            right += 1
        
        return maxprofit
