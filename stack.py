class Stack:
    def __init__(self):
       self.stack1=[]
    def push(self, item):
        self.stack1.append(item)
        print(f"Pushed:{item}")
    def pop(self):
        if self.is_empty():
            return"Stack Is Empty!"
        return f"Popped:{self.stack1.pop()}"
    def peek(self):
        if self.is_empty():
            return"Stack Is Empty!"
        return f"Top:{self.stack1[-1]}"
    def is_empty(self):
        return len(self.stack1)==0
    def size(self):
         return len(self.stack1)
    def display(self):
        return f"Stack(Top -> Bottom):{self.stack1[::-1]}"
    def even(self):
        for i in self.stack1:
            if i%2==0:
                print("Even Number:",i)
    def odd(self):
        for j in self.stack1:
            if j%2!=0:
                print("Odd Number:",j)
s=Stack()
s.push(int(input()))
s.push(int(input()))
s.push(int(input()))
s.push(int(input()))
s.push(int(input()))
s.even()
s.odd()
