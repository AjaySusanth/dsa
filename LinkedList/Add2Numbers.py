'''
https://leetcode.com/problems/add-two-numbers/description/
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

def add(head1,head2):
    temp1,temp2 = head1,head2
    carry=0
    dummyNode = Node(-1)
    curr = dummyNode
    while temp1 is not None or temp2 is not None:
        summ = carry
        if temp1:
            summ+=temp1.val
            temp1 = temp1.next
        if temp2:
            summ += temp2.val
            temp2 = temp2.next

        carry = summ//10
        newNode = Node(summ%10)
        curr.next = newNode
        curr = newNode

    if carry:
        newNode = Node(carry)
        curr.next = newNode
        curr = newNode
    
    return dummyNode.next
        
l1 = [2,4,3]
l2 = [5,6,4]

head1 = conver_to_ll(l1)
head2 = conver_to_ll(l2)
head  = add(head1,head2)
print_ll(head)