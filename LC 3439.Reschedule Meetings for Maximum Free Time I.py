'''
3439. Reschedule Meetings for Maximum Free Time I

UPSOLVED AFTER CONTEST
'''

'''

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        # so i can make the diagram into a list
        # time = [1, 0, 1, 1, 0, 0, .. , 1]
        # 1 represents meetings, and 0 is free time
        # im only allowed k moves
        # how do i maximise the longest set of 0's within k moves
        # thats the question - without all the fluff
        # ok lets first get the problem looking like that

        time = [0] * eventTime
        for i in range(len(startTime)):
            for j in range(startTime[i], endTime[i]):
                time[j] = 1
        print(time)

        # ok now that is handled
        # solution i see:
        # first find the existing longest set of 0's
        # and then try to expand it
        # move the 1's one its edges elsewhere

        # so how do you find the longest set of 0's?
        # use two pointers
        longest = 0
        longstart = 0
        longend = 0
        l = 0
        r = 0
        while r < len(time):
            if time[r] != 0:
                if (r - l) > longest:
                    longstart = l
                    longend = r
                    longest = r - l
                r += 1
                l = r
            else:
                r += 1
        print(longest)

        # ok so im able to find out the longest interval currently
        # im fguring out something
        # so for k moves, max each move she can get one free hour into the continous slot
        # so, we just have to - yeah i have no idea



# crazy idea - YOU ONLY FUCKING HAVE K MOVES IDIOT!!
class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        for i in range(len(startTime)):
            for j in range(startTime[i], endTime[i]):
                eventTime -= 1
        return eventTime
        # WRONG ANSWER!!

'''

# solving this after the contest [UPSOLVING - MY FIRST ONE!]

# so the solution says that since we mvoing k meetings, 
# we technically trying to put togehter k + 1 freetimes (b/w the meetings)
# imagining this makes it better (3 meetings - 2 spaces between them - move 1 meeting, it joins 2 spaces)

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:

        # 1. calc all the gaps:

        gaps = [0] * (len(startTime) + 1) # no. of meetings + 1, each meeting -> gap before it AND the final end time gap

        # 2. calc gap of start and end:

        gaps[0] = startTime[0] - 0
        gaps[len(startTime)] = eventTime - endTime[len(endTime) - 1]

        # 3. add all the gaps of meetings in between:

        for i in range(1, len(startTime)):
            gaps[i] = startTime[i] - endTime[i-1]
        
        # 4. calc the prefix array of gaps:
        # we do this so that the sliding window of k + 1, captures the greatest gaps, that we get after shifting k meetings

        pre = [0] * (len(gaps) + 1) 

        for i in range(1, len(pre)):
            pre[i] = pre[i-1] + gaps[i-1]
        
        # 5. now use a k + 1 sliding window to go over these:

        answer = 0
        for i in range(k + 1, len(pre)):
            if pre[i] - pre[i-(k+1)] > answer:
                answer = pre[i] - pre[i-(k+1)] # brackets matter idiot ! -> basic algebra, BODMAS
        
        return answer