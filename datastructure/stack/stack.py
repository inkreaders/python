## LIFO -> Last in first out 

class Stack(object):
    def __init__(self):
        self.stack = []

    def isEmpty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)
    
    def pop(self):
        data = self.stack[-1]
        del self.stack[-1]
        return data

    def peek(self):
        return self.stack[-1]
    
    def sizeOfStack(self):
        return len(self.stack)

stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print("{} {}".format("Size of stack: ", stack.sizeOfStack()))
print("{} {}".format("Pop top of stack: ", stack.pop()))
print("{} {}".format("Peek top of stack: ", stack.peek()))
print("{} {}".format("Size of stack: ", stack.sizeOfStack()))
