import numbers


class Stack:
    
    def __init__(self, size):
        self.buffer = [0 for _ in range(size)]
        self.stackpointer = -1
        
    def push(self, token):
        self.stackpointer += 1
        self.buffer[self.stackpointer] = token
    
    def pop(self):
        token = self.buffer[self.stackpointer]
        self.stackpointer -= 1
        return token
    
    def top(self):
        return self.buffer[self.stackpointer]