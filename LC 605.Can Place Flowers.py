'''
You have a long flowerbed in which some of the plots are planted, 
and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, 
where 0 means empty and 1 means not empty, and an integer n, 
return true if n new flowers can be planted in the flowerbed 
without violating the no-adjacent-flowers rule and false otherwise.

 
Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 10^4
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length

'''

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        f = [0] + flowerbed + [0] # CREATE A NEW LIST WITH 0 ON BOTH ENDS

        for i in range(1, len(f) - 1): # ITERATE THROUGH THE NEW LIST ONLY CHECKING THROUGH INDEXES 1 TO LEN - 1 (CAUSE THAT'S THE GIVEN LIST)
            if f[i - 1] == 0 and f[i] == 0 and f[i + 1] == 0: # IF ADJACENTS ARE 0 AND INDEX I ALSO IS 0 THEN YOU CAN PLANT A FLOWER, AND CHANGE VALUE OF I TO 1, AND DECREMENT N
                f[i] = 1
                n -= 1
        return n <= 0 # IF N = 0 OR N < 0 THAT MEANS ALL N PLANTS ARE PLANTED AND FALSE IS IF THEY ARE NOT PLANTED