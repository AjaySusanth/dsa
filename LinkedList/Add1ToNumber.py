
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

def reverse(head):
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

def iterative(head):
    reverseHead = reverse(head)
    carry=1
    temp = reverseHead
    while temp:
        temp.val +=carry
        if temp.val < 10:
            carry = 0
            break
        else:
            temp.val = 0
            carry =1
        temp = temp.next

    if carry == 1:
        head = reverse(reverseHead)
        newNode = Node(carry)
        newNode.next = head
        return newNode
    return reverse(reverseHead)

def helper(temp):
    if temp is None:
        return 1
    carry = helper(temp.next)
    temp.val +=carry
    if temp.val <10:
        return 0
    temp.val = 0
    return 1

def recursive(head):
    carry = helper(head)
    if carry == 1:
        newNode = Node(carry)
        newNode.next = head
        return newNode
    return head

arr=[9,8]
head = conver_to_ll(arr)
head = recursive(head)
print_ll(head)