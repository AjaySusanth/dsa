class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


def conver_to_ll(arr):
    head = Node(arr[0])
    temp = head
    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next

    return head


def deleteHead(head):
    if head is None:
        return None
    head = head.next
    return head

def deleteTail(head):
    if head is None or head.next is None:
        return None
    
    temp = head

    while temp.next.next is not None:
        temp =temp.next

    temp.next = None

    return head

def deleteNode(head,node):
    if head.data == node:
        head = head.next
        return head
    prev = Node(None)
    temp = head
    while temp is not None:
        if temp.data == node:
            prev.next = temp.next
            break
        prev = temp
        temp = temp.next

    return head

def print_ll(head):
    temp = head
    while temp:
        print(temp.data,end= "->")
        temp = temp.next

    print("Null")

arr = [4,5,1,9]
node = 5

head = conver_to_ll(arr)
head = deleteNode(head,4)
print_ll(head)

