'''
3408. Design Task Manager
'''

import heapq
class TaskManager:

    def __init__(self, tasks: List[List[int]]):
        # we're using a priority heap and a dict to get rid of extra operations
        # so the gist of what's happening is this:
        # when we make an edits to the tasks, or even remove the task
        # the task gets marked as "None" (ie, removed) in the dict
        # but it will still continue to exist in the heap
        # when we do execTop (to remove the topmost element)
        # we first check the dict value of that element - if according to the dict it still exists, only then do we execute it
        # otherwise, we recursively call the function again
        self.pheap = []
        self.tmap = {}

        for i in tasks:
            uid, tid, p = tuple(i)
            self.add(uid, tid, p)

    def add(self, userId: int, taskId: int, priority: int) -> None:
        heapq.heappush(self.pheap, (-priority, -taskId, userId))
        self.tmap[taskId] = (priority, userId)

    def edit(self, taskId: int, newPriority: int) -> None:
        oldPriority, uid = self.tmap[taskId]
        self.tmap[taskId] = None
        self.add(uid, taskId, newPriority)        

    def rmv(self, taskId: int) -> None:
        self.tmap[taskId] = None

    def execTop(self) -> int:
        if not self.pheap:
            # checking is heap is empty, and return -1 if it is
            return -1
        
        p, t, u = heapq.heappop(self.pheap)
        if self.tmap[-t] and self.tmap[-t][0] == -p and self.tmap[-t][1] == u:
            self.tmap[-t] = None
            return u
        
        # If the popped task is invalid (removed or edited), recursively call execTop to process the next valid task.
        return self.execTop()


# Your TaskManager object will be instantiated and called as such:
# obj = TaskManager(tasks)
# obj.add(userId,taskId,priority)
# obj.edit(taskId,newPriority)
# obj.rmv(taskId)
# param_4 = obj.execTop()