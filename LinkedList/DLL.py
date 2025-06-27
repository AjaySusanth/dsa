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


def deleteHead(head):
    temp = head
    head = head.next
    head.prev = None
    temp.prev = temp.next = None
    return head


def deleteTail(head):
    if head is None or head.next is None:
        return None

    tail = head

    while tail.next is not None:
        tail = tail.next

    prev = tail.prev

    prev.next =None
    tail.prev = None
    return head


def deleteK(head,k):
    if head is None:
        return None
    if k == 1:
        return deleteHead(head)
    
    temp = head
    count = 0

    while temp is not None:
        count +=1
        if count == k:
            break
        temp = temp.next

    prev = temp.prev
    next = temp.next

    if next is None:
        return deleteTail(head)

    prev.next = next
    next.prev = prev
    temp.next = temp.prev = None

    return head


def insertBeforeHead(head,data):
    newNode = Node(data,head)
    head.prev = newNode
    head = newNode
    return head


def insertAfterTail(head,data):
    if head is None:
        return Node(data)
    
    tail = head
    while tail.next is not None:
        tail = tail.next
    
    newNode = Node(data,None,tail)
    tail.next  =newNode
    return head


def insertBeforeK(head,data,k):
    if head is None:
        return Node(data)
    
    if k == 1:
        return insertBeforeHead(head,data)
    
    temp = head
    count =0

    while temp is not None:
        count +=1
        if count == k:
            break
        temp = temp.next

    prev = temp.prev
    newNode = Node(data,temp,prev)
    temp.prev = newNode
    prev.next  = newNode

    return head





arr = [10,20,30,40]
head = arr_to_dll(arr)
head = insertBeforeK(head,3,2)
print_ll(head)

