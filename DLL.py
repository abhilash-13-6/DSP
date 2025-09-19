class node:
    def __init__(self,data):
       self.data=data
       self.next=None
       self.prev=None
class DLL:
    def __init__(self):
        self.head=None
    def insert(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
        else:
           new_node.next=self.head
           self.head.prev=new_node
           self.head=new_node
    def insert_at_end(self,data):
        new_node=node(data)
        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next:
            temp=temp.next
        temp.next=new_node
        new_node.prev=temp
    def insert_at_pos(self,data,pos):
        new_node=node(data)
        if pos<=0:
            print("Position Should be >=1")
            return
        if pos==1:
            self.insert(data)
            return
        temp=self.head
        count=1
        while temp and count<pos-1:
            temp=temp.next
            count+=1
        if temp is None:
            print("Position out of Range")
            return
        new_node.next=temp.next
        new_node.prev=temp
        if temp.next:
            temp.next.prev=new_node
        temp.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="<->")
            temp=temp.next
        print("None")
dll=DLL()
dll.insert(10)
dll.display()
dll.insert(20)
dll.display()
dll.insert(30)
dll.display()
dll.insert(40)
dll.display()
dll.insert(50)
dll.display()
dll.insert_at_end(60)
dll.display()
dll.insert_at_pos(70,4)
dll.display()
