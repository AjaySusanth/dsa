# https://leetcode.com/problems/linked-list-cycle/description/

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

def brute(head):
    if head is None or head.next is None:
        return False

    temp = head
    hashmap = set()
    while temp:
        if temp in hashmap:
            return True
        hashmap.add(temp)
        temp = temp.next

    return False

def optimal(head):
    if head is None or head.next is None:
        return False
    
    slow,fast = head,head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False
