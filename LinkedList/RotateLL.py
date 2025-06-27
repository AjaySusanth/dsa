
#https://leetcode.com/problems/rotate-list/

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


def rotate(head,k):
    if head is None or head.next is None:
        return head
    
    length = 0
    tail = head

    while tail.next:
        length +=1
        tail = tail.next
    length+=1
    k = k % length

    if k == 0:
        return head

    count = 0

    temp = head
    while temp:
        count +=1
        if count == length - k:
            break
        temp = temp.next
    tail.next = head
    newHead = temp.next
    temp.next = None

    return newHead


arr = [1,2,3,4,5]
k = 2

head = conver_to_ll(arr)
head = rotate(head,k)
print_ll(head)

    
