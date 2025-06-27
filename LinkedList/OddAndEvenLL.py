'''
https://leetcode.com/problems/odd-even-linked-list/description/
'''

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
        return head
    arr= []
    temp = head

    while temp and temp.next:
        arr.append(temp.val)
        temp = temp.next.next

    temp = head.next

    while temp and temp.next:
        arr.append(temp.val)
        temp = temp.next.next

    temp = head
    i=0
    while i < len(arr):
        temp.val = arr[i]
        temp = temp.next
        i+=1

    return head


def optimal(head):
    if head is None or head.next is None:
        return head
    
    odd,even = head,head.next
    evenHead = head.next

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next

    odd.next = evenHead

    return head

arr = [1,2,3,4,5]
head = conver_to_ll(arr)
head  = brute(head)
print_ll(head)