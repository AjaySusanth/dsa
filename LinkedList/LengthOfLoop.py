# https://www.geeksforgeeks.org/problems/find-length-of-loop/1


class ListNode:
    def __init__(self,val,next1=None):
        self.val= val
        self.next = next1

def brute(head):
    if head is None or head.next is None:
        return 0

    temp = head

    hashamp =dict()
    count = 1

    while temp:
        if temp in hashamp:
            return count - hashamp[temp]
        hashamp[temp] = count
        temp = temp.next
        count +=1
    return 0

def optimal(head):
    if head is None or head.next is None:
        return 0
    slow,fast = head,head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            count =1
            slow = slow.next
            while slow!=fast:
                count+=1
                slow = slow.next

            return count
    return 0

head = ListNode(1)
second = ListNode(2)
third = ListNode(3)
fourth = ListNode(4)
fifth = ListNode(5)

    # Linking nodes
head.next = second
second.next = third
third.next = fourth
fourth.next = fifth
fifth.next = third


print(brute (head))