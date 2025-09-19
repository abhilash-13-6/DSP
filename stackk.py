class Stack:
    def _init__(self):
       self.stack=[]
    def push(self,item):
        self.stack.append(item)
        print(f"Pushed:{item}")
    def pop(self):
        if self.is_empty():
            return"Stack Is Empty!"
        return f"Popped:{self.stack.pop()}"
    def peek(self):
        if self.is_empty():
            return"Stack Is Empty!"
        return f"Top:{self.stack[-1]}"
    def is_empty(self):
        return len(self.stack)==0
    def size(self):
         return len(self.stack)
    def display(self):
        return f"Stack(Top -> Bottom):{self.stack[::-1]}"
s=Stack()
s.push(int(input()))
s.push(50)
s.pop()
s.peek()
s.is_empty()
s.size()
s.display()
