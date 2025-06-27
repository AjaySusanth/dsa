# Creating a node
class Node:
    def __init__(self,data1,next1=None):
        self.data= data1
        self.next = next1
    
y = Node(2)
print(y.data)


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

#Delete a node




arr = [10, 20, 30, 40]
head = conver_to_ll(arr)
print_ll(head)










