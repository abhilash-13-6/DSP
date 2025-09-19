from colorama import Fore, Style

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            last = self.head.prev
            new_node.next = self.head
            new_node.prev = last
            self.head.prev = new_node
            last.next = new_node
            self.head = new_node
        print(Fore.GREEN + "Node inserted at the beginning" + Style.RESET_ALL)

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node.prev = new_node
            self.head = new_node
        else:
            last = self.head.prev
            last.next = new_node
            new_node.prev = last
            new_node.next = self.head
            self.head.prev = new_node
        print(Fore.GREEN + "Node inserted at the end" + Style.RESET_ALL)

    def insert_at_position(self, data, position):
        if position <= 0:
            print(Fore.RED + "Position should be >= 1" + Style.RESET_ALL)
            return

        if position == 1:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        temp = self.head
        count = 1

        while count < position - 1 and temp.next != self.head:
            temp = temp.next
            count += 1

        if count != position - 1:
            print(Fore.RED + "Position out of range" + Style.RESET_ALL)
            return

        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

        print(Fore.GREEN + f"Node inserted at position {position}" + Style.RESET_ALL)

    def display_forward(self):
        if self.head is None:
            print(Fore.BLUE + "List is empty" + Style.RESET_ALL)
            return
        temp = self.head
        while True:
            print(Fore.BLUE + str(temp.data) + Style.RESET_ALL, end=" <-> ")
            temp = temp.next
            if temp == self.head:
                break
        print(Fore.BLUE + "HEAD" + Style.RESET_ALL)

    def display_backward(self):
        if self.head is None:
            print(Fore.MAGENTA + "List is empty" + Style.RESET_ALL)
            return
        last = self.head.prev
        temp = last
        while True:
            print(Fore.MAGENTA + str(temp.data) + Style.RESET_ALL, end=" <-> ")
            temp = temp.prev
            if temp == last:
                break
        print(Fore.MAGENTA + "HEAD" + Style.RESET_ALL)


# ---------- Test ----------
cdll = CircularDoublyLinkedList()
cdll.insert_at_end(10)
cdll.insert_at_beginning(20)
cdll.insert_at_position(30, 2)
cdll.display_forward()
cdll.display_backward()
