#https://leetcode.com/problems/remove-nth-node-from-end-of-list/

'''
Brute - Find the length of ll and remove go to length-n node and update its links by skipping the nth node
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        length = 1
        temp = head
        while temp.next:
            temp = temp.next
            length +=1
        if n == length:
            temp = head
            head = head.next
            temp.next = None
            return head
        temp = head
        count = 0

        while temp:
            count+=1
            if count == length - n:
                break
            temp = temp.next
        node = temp.next
        temp.next = temp.next.next

        node.next  = None
        return head
    

'''
Optimal - fast and slow pointer

Move the fast pointer n positions n positions initialy
After that till fast reaches last, move fast and slow one node each
When fast reaches last, slow points to n-1 th node from back, update its link to skip the nth node
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: Optional[ListNode]
        :type n: int
        :rtype: Optional[ListNode]
        """
        if head is None or head.next is None:
            return None
        slow = fast = head

        for _ in range(n):
            fast = fast.next

        if fast is None:
            return head.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        node = slow.next

        slow.next = slow.next.next
        node.next = None
        return head
        