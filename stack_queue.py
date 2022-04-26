class Queue:
    def __init__(self):
        self.q = []
    
    def enqueue(self, value):
        self.q.append(value)

    def dequeue(self):
        if (len(self.q) == 0):
            return ("ERROR: cannot dequeue from empty queue")
        
        item = self.q[0]
        self.q.remove(item)
        return item
    
    def first(self):
        if (len(self.q) == 0):
            return ("ERROR: cannot dequeue from empty queue")
        
        return self.q[0]
    
    def is_empty(self):
        if(len(self.q) == 0):
            return True
        return False
    
    def __str__(self):
        return str(self.q)

# Implementation of a Stack using a Queue
class Stack:
    def __init__(self):
       self.s = Queue()
    
    def is_empty(self):
        self.s.is_empty()

    def push(self, value):
        self.s.enqueue(value)

    def pop(self):
        hold = self.s.dequeue()

        if self.s.is_empty():
            return hold
        
        r = self.pop() 
        self.s.enqueue(hold)
        return r
            
    
    def top(self):
        if (self.s.is_empty()):
            return "ERROR: Stack is empty"
        hold = self.s.dequeue()

        if self.s.is_empty():
            return hold
        
        r = self.top() 
        self.s.enqueue(hold)
        return r
    
    def size(self):
        return len(self.s)

    def __str__(self):
        return str(self.s)
        

    

if __name__ == "__main__":
    test_stack = Stack()
    

    #TEST CASE 1:
    print("TEST STACK")

    print("Stack:", test_stack)
    print("Stack empty:", test_stack.is_empty())

    # Checking for Errors
    print("Stack pop:", test_stack.pop())
    print("Stack top:", test_stack.top())

    # Testing push
    test_stack.push("O")
    print("Stack after push:", test_stack)
    test_stack.push("L")
    print("Stack after push:", test_stack)
    test_stack.push("L")
    print("Stack after push:", test_stack)
    test_stack.push("E")
    print("Stack after push:", test_stack)
    test_stack.push("H")
    print("Stack after push:", test_stack)

    print("Stack empty:", test_stack.is_empty())

    # Testing top
    print("Stack top:", test_stack.top())
    print("Stack after top:", test_stack) # Make sure stack is not mofidied after top

    # Testing pop
    print("Stack pop:", test_stack.pop())
    print("Stack after pop:", test_stack)
    print("Stack pop:", test_stack.pop())
    print("Stack after pop:", test_stack)
    print("Stack pop:", test_stack.pop())
    print("Stack after pop:", test_stack)
    print("Stack pop:", test_stack.pop())
    print("Stack after pop:", test_stack)
    print("Stack pop:", test_stack.pop())
    print("Stack after pop:", test_stack)

    # Checking for Error again
    print("Stack pop:", test_stack.pop())