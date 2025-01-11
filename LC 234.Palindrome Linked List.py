'''
234. Palindrome Linked List
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        l = []

        # method of putting the linkedlist into a regular list
        while head is not None:
            l.append(head.val)
            head = head.next
        
        if l == l[::-1]:
            return True
        else:
            return False