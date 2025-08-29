class Node:
    def __init__(self, data):
        self.data = data  
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None  

 
    def insert(self, data):
        new_node = Node(data)
        if not self.head: 
            self.head = new_node
        else:
            temp = self.head
            while temp.next:  
                temp = temp.next
            temp.next = new_node

    
    def delete(self, value):
        temp = self.head
        if temp and temp.data == value:  
            self.head = temp.next
            temp = None
            return

     
        prev = None
        while temp and temp.data != value:
            prev = temp
            temp = temp.next

        if not temp:
            print("Value not found!")
            return
        
        prev.next = temp.next  
        temp = None 

    def update(self, old_value, new_value):
        temp = self.head
        while temp:
            if temp.data == old_value:
                temp.data = new_value
                return
            temp = temp.next
        print("Value not found to update!")


    def display(self):
        temp = self.head
        if not temp:
            print("List is empty.")
            return
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")


def menu():
    print("\n--- DSP Single Linked List Operations ---")
    print("1. Insert Sample")
    print("2. Delete Sample")
    print("3. Update Sample")
    print("4. Display List")
    print("5. Exit")

def main():
    linked_list = LinkedList()

    while True:
        menu()
        choice = input("Enter your choice: ")
        
        if choice == '1':
            try:
                sample = float(input("Enter sample value to insert: "))
                linked_list.insert(sample)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '2':
            try:
                sample = float(input("Enter sample value to delete: "))
                linked_list.delete(sample)
            except ValueError:
                print("Please enter a valid number.")
        
        elif choice == '3':
            try:
                old_sample = float(input("Enter sample value to update: "))
                new_sample = float(input("Enter new sample value: "))
                linked_list.update(old_sample, new_sample)
            except ValueError:
                print("Please enter valid numbers.")
        
        elif choice == '4':
            linked_list.display()
        
        elif choice == '5':
            print("Exiting program.")
            break
        
        else:
            print("Invalid choice! Please enter a valid option.")

if __name__ == "__main__":
    main()
