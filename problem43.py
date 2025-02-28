'''
Implement a stack that has the following methods:

push(val), which pushes an element onto the stack
pop(), which pops off and returns the topmost element of the stack. If there are no elements in the stack, then it should throw an error or return null.
max(), which returns the maximum value in the stack currently. If there are no elements in the stack, then it should throw an error or return null.
Each method should run in constant time.
'''

class Stack:
    def __init__(self, val=None):
        self.stack = []
        self.max = val

    def push(self, val):
        if self.max == None:
            self.max = val
        elif val > self.max:
            self.max = val
        self.stack.append(val)
    
    def max(self):
        return self.max
    

'''
methods do not depend on size of stack so run in O(c) time
'''

if __name__ == '__main__':
    stack = Stack()
    print(stack.max)
    stack.push(3)
    print(stack.max)
    stack.push(2)
    print(stack.max)