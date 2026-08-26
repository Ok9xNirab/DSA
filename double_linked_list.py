from typing import Optional

class double_linked_list():
    class Node():
        def __init__(self, data):
            self.data = data
            self.next: Optional["double_linked_list.Node"] = None
            self.prev: Optional["double_linked_list.Node"] = None

    def __init__(self):
        self.head: Optional["double_linked_list.Node"] = None

    def append(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        new_node.prev = last_node

    def prepend(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node

    def insert(self, prev_node_data, data):
        if not self.head:
            return
        current_node = self.head
        while current_node:
            if current_node.data == prev_node_data:
                new_node = self.Node(data)
                new_node.next = current_node.next
                new_node.prev = current_node
                if current_node.next:
                    current_node.next.prev = new_node
                current_node.next = new_node
                return
            current_node = current_node.next

    def remove(self, data):
        if not self.head:
            return
        if self.head.data == data:
            if self.head.next:
                self.head.next.prev = None
            self.head = self.head.next
            return
        current_node = self.head
        while current_node:
            if current_node.data == data:
                if current_node.prev:
                    current_node.prev.next = current_node.next
                if current_node.next:
                    current_node.next.prev = current_node.prev
                return
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")

double_linked_list_instance = double_linked_list()
double_linked_list_instance.append(1)
double_linked_list_instance.append(2)
double_linked_list_instance.prepend(0)
double_linked_list_instance.display()  # Output: 0 <-> 1 <-> 2 <-> None
double_linked_list_instance.insert(1, 1.5)
double_linked_list_instance.display()  # Output: 0 <-> 1 <-> 1.5 <-> 2 <-> None
double_linked_list_instance.remove(1.5)
double_linked_list_instance.display()  # Output: 0 <-> 1 <-> 2 <-> None