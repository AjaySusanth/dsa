#Approach 1
stack=[]
def push(item):
    if len(stack)==0:
        return;
    mini = min(item,mini)
    stack.append((item,min(item,stack[-1][1])))

def pop():
    return stack.pop()

def top():
    return stack[-1][0]

def getMin():
    return stack[-1][1]

#TC - O(1) SC - O(2N)

#Optimising the extra space

class MinStack(object):

    def __init__(self):
        self.stack=[]
        self.min = float('inf')        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """

        if not self.stack:
            self.min = val
            self.stack.append(val)
        elif val > self.min:
            self.stack.append(val)
        else:
            new_val = 2*val-self.min
            self.min = val
            self.stack.append(new_val)
        

    def pop(self):
        """
        :rtype: None
        """

        top = self.stack.pop()
        if top < self.min:
            self.min = 2*self.min-top
    
    def top(self):
        """
        :rtype: int
        """
        item = self.stack[-1]
        if (item >= self.min):
            return item
        else:
            return self.min
        

    def getMin(self):
        """
        :rtype: int
        """
        return self.min
        
# SC - O(N)