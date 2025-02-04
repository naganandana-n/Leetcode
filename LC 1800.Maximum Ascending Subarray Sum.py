'''
1800. Maximum Ascending Subarray Sum
'''

class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        # this looks like a 2 pointers thing to me:

        l = 0
        r = 0
        answer = 0
        localans = 0
        while r < len(nums):
            if r == 0:
                localans += nums[r]
            elif nums[r] > nums[r-1]:
                localans += nums[r]
            else:
                answer = max(answer, localans)
                l = r
                localans = nums[l]
            r += 1
            # print(localans)
        return max(localans, answer) # cause the max could be in the last iteration - and we're not considering it

'''
TWO POINTERS EXPLAINED HERE:

- so lets look at the first eg, using which ill show the approach.

[10, 20, 30, 5, 10, 50]

- first you use 2 trackers (pointers) - l and r
- initalize them to 0 (both of them)

[10, 20, 30, 5, 10, 50]
 l,r

- also, maintain a sum, that your calculating. So initally sum = 0
- now if r == 0, then add the nums[r] to sum
- sum += nums[r]
- then you incrememnt r -> so r == 1 now

[10, 20, 30, 5, 10, 50]
 l   r

- now, check if nums[r] > nums[r-1]:
- it is, yeah? so then sum += nums[r]
- r += 1

[10, 20, 30, 5, 10, 50]
 l       r

- is nums[r] > nums[r-1] -> sum += nums[r], r += 1

[10, 20, 30, 5, 10, 50]
 l           r

- now see what happens
- nums[r] > nums[r-1] -> NO!!!
- so what we do here is
- your sum that you calc so far
- add it to a new array -> that will contain all the sums -> out of this array in the end we'll pick a max one
- and here's what you do with the pointers

[10, 20, 30, 5, 10, 50]
             l  r

- you bring your left pointer to where the fuck up happend
- and increment your right pointer
- and set your sum variable to nums[l] -> so that you can add to it
- repeat again
- once you get to the end, there also append the sum to the sum array -> THIS IS IMP, PPL TEND TO FORGET THIS!! (def not talking about myself, i... I would never)

- in the end you're sum array will look like this:

[60, 65]

- sort the array in reverse using your inbuilt sort function

[65, 60]

- return the first element of the array
- ta da!
'''