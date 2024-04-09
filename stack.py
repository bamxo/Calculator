# author: Landon Nguyen
# date: March 3, 2023
# file: stack.py a Python file that defines a Stack
# input: data types are stored in a list
# output: stored data types can only be added, removed, and peeked at from the top of the stack

class Stack:
    
    def __init__(self):
        self.items = [] 

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()
    
    def peek(self):
        if self.items != []:
            return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

# a driver program for class Stack

if __name__ == '__main__':
    
    data_in = ['hello', 'how', 'are', 'you']
    s = Stack()
    for i in data_in:
        s.push(i)
           
    assert s.size() == len(data_in)
    assert s.peek() == data_in[-1]

    data_out = []
    while not s.isEmpty():
        data_out.append(s.pop())

    assert data_out == data_in[::-1]
    assert s.size() == 0
    assert s.peek() == None
