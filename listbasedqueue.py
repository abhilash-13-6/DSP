class Queue:
    def __init__(self):
        self.queue = []  # Initialize an empty list to represent the queue

    # Enqueue: Add an item to the rear of the queue
    def enqueue(self, item):
        self.queue.append(item)

    # Dequeue: Remove an item from the front of the queue
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)  # Remove and return the front element
        else:
            print("Queue is empty!")
            return None

    # Peek: View the front item without removing it
    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        else:
            print("Queue is empty!")
            return None

    # Check if the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Get the size of the queue
    def size(self):
        return len(self.queue)

# Function to display the menu and perform actions
def display_menu():
    print("\nQueue Operations Menu:")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Peek")
    print("4. Check Size")
    print("5. Exit")

# Main program loop
def main():
    queue = Queue()

    while True:
        display_menu()  # Display options to the user
        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            item = input("Enter the item to enqueue: ")
            queue.enqueue(item)
            print(f"Enqueued: {item}")

        elif choice == "2":
            dequeued_item = queue.dequeue()
            if dequeued_item:
                print(f"Dequeued: {dequeued_item}")

        elif choice == "3":
            front_item = queue.peek()
            if front_item:
                print(f"Front item: {front_item}")

        elif choice == "4":
            print(f"Queue size: {queue.size()}")

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice, please try again.")

# Run the main program
if __name__ == "__main__":
    main()
