class StackQueue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, item):
        self.stack_in.append(item)

    def dequeue(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            return "Queue is empty"
        return self.stack_out.pop()

    def peek(self):
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        if not self.stack_out:
            return "Queue is empty"
        return self.stack_out[-1]

    def is_empty(self):
        return not self.stack_in and not self.stack_out

    def display(self):
        if not self.stack_out:
            temp = self.stack_in
        else:
            temp = self.stack_out[::-1] + self.stack_in
        return temp if temp else "Queue is empty"


def menu():
    q = StackQueue()
    while True:
        print("\n----- Stack-Based Queue Menu -----")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Check if Empty")
        print("5. Display Queue")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            item = input("Enter value to enqueue: ")
            q.enqueue(item)
            print(f"{item} enqueued.")
        elif choice == '2':
            print("Dequeued:", q.dequeue())
        elif choice == '3':
            print("Front item:", q.peek())
        elif choice == '4':
            print("Queue is empty?" , q.is_empty())
        elif choice == '5':
            print("Queue contents:", q.display())
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

# Run the menu
menu()
