# https://leetcode.com/problems/reverse-linked-list/description/

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


def reverse_recursive(head):

    if head is None or head.next is None:
        return head
    
    newHead = reverse_recursive(head.next)
    front = head.next
    front.next = head
    head.next = None

    return newHead
    
    

arr=[1,2,3,4,5]
head = conver_to_ll(arr)
head = reverse_recursive(head)
print_ll(head)