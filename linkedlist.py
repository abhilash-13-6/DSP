class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class sll:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=Node(data)
        new_node=self.head
        self.head=new_node
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
         self.head=new_node
         return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    def traverse(self,data):
        if self.head is None:
          print("Linked List Is Empty")
          return
        current=self.head
        while current:
            print(current.data,end="->")
            current=current.next
        print("None")
ll=sll()
ll.append(10)
ll.append(20)
ll.append(int(input("Enter A element:")))
print("After Appending At End:")
ll.traverse()
ll.insert(5)
