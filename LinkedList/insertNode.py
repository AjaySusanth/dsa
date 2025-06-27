class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


def conver_to_ll(arr):
    head = Node(arr[0])
    temp = head
    for i in range(1,len(arr)):
        temp.next = Node(arr[i])
        temp = temp.next

    return head


def insertHead(head,data):
    if head is None:
        head = Node(data)
        return head
    temp = Node(data)
    temp.next = head
    return temp


def insertK(head,k,data):
    if head is None:
        if k==1:
            head = Node(data)
            return head
        else:
            return ValueError
    
    if k ==1:
        temp = Node(data,head)
        return temp
    
    temp = head
    count =0
    while temp is not None:
        count+=1
        if count == k-1:
            newNode = Node(data)
            newNode.next = temp.next
            temp.next = newNode
            break
        temp = temp.next
    return head

def print_ll(head):
    temp = head
    while temp:
        print(temp.data,end= "->")
        temp = temp.next

    print("Null")

arr = [4,5,1,9]
head = conver_to_ll(arr)
head = insertK(head,2,10)
print_ll(head)