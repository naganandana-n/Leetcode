'''
19. Remove Nth Node From End of List
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # this is how to traverse a linked list
        '''
        l = []
        while head:
            l.append(head.val)
            head = head.next
        '''

        res = ListNode(0, head)
        dummy = res

        # solving this using two pointers:
        for _ in range(n):
            head = head.next # to get the second pointer to the end
        
        # get both the pointers moving till head reaches the end
        while head:
            head = head.next 
            dummy = dummy.next
        
        dummy.next = dummy.next.next # oh you can change vals togehter

        return res.next # res starts at 0, so when we cahnge the res list using dummy and return it - done using res.next


        
        
        