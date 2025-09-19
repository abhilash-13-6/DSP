class node:
    def __init__(self,data):
       self.data=data
       self.next=None
       self.prev=None
class CLL:
    def __init__(self):
        self.head=None
        self.prev=self.head
    def insert(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
           new_node.next=self.head
           self.head.prev=new_node
           self.head=new_node
    def delete_at_end(self):
        if self.head is None:
            print("Empty List")
            return
        print(f"Deleted:{self.head.data}")
        self.head=self.head.next
        if self.head:
            self.head.prev=None    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
    
cll=CLL()
cll.insert(10)
cll.insert(20)
cll.insert(30)
cll.insert(40)
cll.insert(50)
cll.display()
cll.delete_at_end()
cll.display()
