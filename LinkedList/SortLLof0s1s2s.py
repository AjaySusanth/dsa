# https://www.geeksforgeeks.org/problems/given-a-linked-list-of-0s-1s-and-2s-sort-it/1

# Creating a node
class Node:
    def __init__(self,data1,next1=None):
        self.data= data1
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
        print(temp.data,end= "->")
        temp = temp.next

    print("Null")


def brute(head):
    if head is None or head.next is None:
        return head
    
    temp = head
    count0,count1,count2=0,0,0

    while temp:
        if temp.data == 0:
            count0+=1

        if temp.data == 1:
            count1+=1

        if temp.data == 2:
            count2+=1
        temp = temp.next

    temp = head

    while temp:
        if count0 > 0:
            temp.data = 0
            count0-=1
        elif count1 > 0:
            temp.data = 1
            count1-=1
        else:
            temp.data = 2
            count2-=1
        temp = temp.next

    return head

def optimal(head):
    if head is None or head.next is None:
        return head
    
    zeroHead,oneHead,twoHead = Node(-1),Node(-1),Node(-1)
    zero,one,two=zeroHead,oneHead,twoHead

    temp = head

    while temp:
        if temp.data == 0:
            zero.next = temp
            zero = zero.next

        if temp.data == 1:
            one.next = temp
            one = one.next

        if temp.data == 2:
            two.next = temp
            two = two.next
        temp = temp.next

    zero.next = (oneHead.next) if oneHead.next else twoHead.next
    one.next = twoHead.next
    two.next = None

    newHead = zeroHead.next

    return newHead

arr = [1,2,0,1,0,0,2,1,0,2] 

head = conver_to_ll(arr)

head = brute(head)
print_ll(head)