# https://leetcode.com/problems/intersection-of-two-linked-lists/

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


def brute(head1,head2):
    if head1 is None or head2 is None:
        return None
    temp1,temp2 = head1,head2
    hashmp = set()
    while temp1:
        hashmp.add(temp1)
        temp1 = temp1.next

    while temp2:
        if temp2 in hashmp:
            return temp2
        temp2 = temp2.next

    return None

def intersection(temp1,temp2,diff):
    print(diff)
    while diff > 0:
        temp1 = temp1.next
        diff -=1

    while temp1 and temp2:
        if temp1 == temp2:
            return temp1
        temp1 = temp1.next
        temp2 = temp2.next
    return None
def better(head1,head2):
    if head1 is None or head2 is None:
        return None
    temp1,temp2 = head1,head2

    l1,l2 =0,0

    while temp1:
        l1+=1
        temp1 = temp1.next
    while temp2:
        l2+=1
        temp2 = temp2.next
    if l1 > l2:
        return intersection(head1,head2,l1-l2)
    else:
         return intersection(head2,head1,l2-l1)
    
def optimal(head1,head2):
    if head1 is None or head2 is None:
        return None
    temp1,temp2 = head1,head2

    while temp1 != temp2:
        temp1 = head2 if temp1 is None else temp1.next
        temp2 = head1 if temp2 is None else temp2.next

    return temp1

listA = [4,1,8,4,5]
listB = [5,6,1,8,4,5]    

head1 = conver_to_ll(listA)
head2 = conver_to_ll(listB)
head = optimal(head1,head2)
print_ll(head)