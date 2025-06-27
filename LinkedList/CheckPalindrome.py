# https://leetcode.com/problems/palindrome-linked-list/description/
class Node:
    def __init__(self,val,next1=None):
        self.val= val
        self.next = next1
    


def conver_to_ll(arr):
    head = Node(arr[0])
    temp = head
    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next

    return head

def print_ll(head):
    temp = head
    while temp:
        print(temp.val,end= "->")
        temp = temp.next

    print("Null")

def reverse_iterative(head):
    if head is None or head.next is None:
        return head
    
    temp =head
    prev = None

    while temp:
        front = temp.next
        temp.next = prev
        prev = temp
        temp = front

    return prev

def check_palindrome(head):
    if head.next is None:
        return True
    
    slow,fast = head
    temp = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    reverseHead = reverse_iterative(slow.next)

    while reverseHead:
        if temp.value != reverseHead.value:
            reverse_iterative(slow.next)
            return False
        
        temp = temp.next
        reverseHead = reverseHead.next

    return True

