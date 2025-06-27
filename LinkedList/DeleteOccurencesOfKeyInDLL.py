class Node:
    def __init__(self,data,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev


def arr_to_dll(arr):
    if len(arr) == 0:
        return None
    head = Node(arr[0])
    prev = head

    for i in range(1,len(arr)):
        temp = Node(arr[i],None,prev)
        prev.next = temp
        prev = temp

    return head

def print_ll(head):
    temp = head
    while temp:
        print(temp.data,end= "->")
        temp = temp.next

    print("Null")

def delete_key(head,key):
    if head is None or (head.data == key and head.next is None):
        return None
    
    if head.data == key:
        nextNode = head.next
        nextNode.prev = None
        head.next  = None
        head = nextNode
    temp = head
    while temp:
        if temp.data == key:
            prevNode = temp.prev
            nextNode = temp.next
            if nextNode:
                nextNode.prev = prevNode
            prevNode.next = nextNode
            temp.next = None
            temp.prev = None
            temp = nextNode
        else:
            temp = temp.next
    return head

arr = [0]
head = arr_to_dll(arr)
head = delete_key(head,10)
print_ll(head)