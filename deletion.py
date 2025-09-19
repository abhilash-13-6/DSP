lass Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
         self.head=new_node
         return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
        
    def del_beginning(self):
        if self.head is None:
            print("List Is Empty")
            return 
        print("Deleted:",self.head.data)
        self.head=self.head.next
        
    def del_end(self):
        if self.head is None:
            print("List is Empty")
            return
        if self.head.next is None:
            print("Deleted:",self.head.data)
            self.head=None
            return 
        prev= self.head
        current=self.head.next
        while current.next:
            prev=current
            current=current.next
        print("Deleted:",current.data)
        prev.next=None
        
    def del_at_pos(self,pos):
        if self.head is None:
            print("List is Empty")
            return
        if pos==1:
            print("deleted:",self.head.data)
            self.head=self.head.next
            return
        current=self.head
        prev=None
        count=1
        while current and count<pos:
            prev=current
            current=current.next
            count+=1
        if current is None:
            print("Invalid Position")
            return
        print("deleted:",current.data)
        prev.next=current.next    
        
    def display(self):
        if self.head is None:
            print("List is Empty")
            return
        current=self.head
        while current:
            print(current.data,end=' ->')
            current=current.next
        print("None")
ll=sll()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)
ll.display()
ll.del_beginning()
ll.display()
ll.del_end()
ll.display()
ll.del_at_pos(3)
ll.display()
