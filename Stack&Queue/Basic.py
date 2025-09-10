# Basic Stack and Queue functions in Python
from collections import deque
class Stack():
    def __init__(self):
        self.items = []

    def push(self,item):
        self.items.append(item)
    def pop(self):
        if not self.items:
            raise IndexError("Pop from empty stack")
        return self.items.pop()
    def peek(self):
        if not self.items:
            raise IndexError("Pop from empty stack")
        return self.items[-1]
    def size(self):
        return len(self.items)
    def print(self):
        print(self.items)


class Queue():
    def __init__(self):
        self.items = deque()
    def enqueue(self,item):
        self.items.append(item)
    def dequeue(self):
        if not self.items:
            raise IndexError("Dequeue from empty queue")
        return self.items.popleft()
    def print(self):
        print(list(self.items))
# Stack using Arrays

class ArrayStack():
    def __init__(self,size):
        self.size = size
        self.arr = [None] * size
        self.top = -1
    
    def push(self,item):
        if self.top > self.size - 1:
            raise OverflowError("Stack Overflow")
        self.top+=1
        self.arr[self.top] = item

    def pop(self):
        if self.top == -1:
            raise IndexError("Stack underflow")
        item = self.arr[self.top]
        self.top -=1
        return item
    
    def peek(self):
        if self.top == -1:
            raise IndexError("Stack underflow")
        return self.arr[self.top]
    def print(self):
        print(self.arr[:self.top+1])
# Queue using arrays

class ArrayQueue():
    def __init__(self,size):
        self.size = size
        self.arr = [None] * size
        self.front = 0
        self.rear = -1
        self.count = 0

    def enqueue(self,item):
        if self.count > self.size:
            raise OverflowError("Queue overflow")
        self.rear = (self.rear + 1) % self.size
        self.arr[self.rear] = item
        self.count +=1
    
    def dequeue(self):
        if self.count == 0:
            raise IndexError("Queue underflow")
        item = self.arr[self.front]
        self.front = (self.front + 1)% self.size
        self.count -=1
        return item
    
    def print(self):
        items = []
        i = self.front
        for _ in range(self.count):
            items.append(self.arr[i])
            i = (i + 1) % self.size
        print(items)


class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class StackLL:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self.size +=1
    
    def pop(self):
        if self.top is None:
            raise IndexError("Stack underflow")
        item = self.top.data
        self.top = self.top.next
        self.size -=1
        return item
    def peek(self):
        if self.top is None:
            raise IndexError("Stack empty")
        return self.top.data
    
class QueueLL:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def enqueue(self,item):
        new_node = Node(item)
        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.size+=1

    def dequeue(self):
        if self.front is None:
            raise IndexError("Queue empty")
        temp = self.front
        self.front = self.front.next
        self.size -=1
        if self.front is None:
            self.rear = None
        return temp.data
    
#Stack using queue

class StackQueue:
    def __init__(self):
        self.q = deque()

    def push(self,item):
        self.q.append(item)
        for _ in range(len(self.q)-1):
            self.q.append(self.q.popleft())

    def pop(self):
        if not self.q:
            raise IndexError("Pop from empty stack")
        return self.q.popleft()
