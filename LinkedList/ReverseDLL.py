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


def reverse(head):
    if head is None or head.next is None:
        return head
    curr = head
    last = None

    while curr is not None:
        last = curr.prev
        curr.prev = curr.next
        curr.next = last
        curr = curr.prev

    newHead = last.prev

    return newHead

arr = [10,20,30,40]
head = arr_to_dll(arr)
head = reverse(head)
print_ll(head)
