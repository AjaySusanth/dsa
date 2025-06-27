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


def find_pairs(head,summ):
    if head is None or head.next is None:
        return None

    pairs=[]

    tail = head
    while tail.next:
        tail= tail.next
    temp = head

    while temp.data < tail.data:
        if temp.data + tail.data == summ:
            pairs.append((temp.data,tail.data))
            temp = temp.next
            tail = tail.prev
        elif temp.data + tail.data > summ:
            tail = tail.prev
        else:
            temp =temp.next
    
    return pairs

arr = [1,2,4,6,7,8,9,12]
head = arr_to_dll(arr)
pairs = find_pairs(head,10)
print(pairs)