from typing import Optional

class linked_list:
    def __init__(self):
        self.head: Optional["linked_list.Node"] = None

    class Node:
        def __init__(self, data):
            self.data = data
            self.next: Optional["linked_list.Node"] = None

    def append(self, data):
        new_node = self.Node(data)
        if not self.head:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = self.Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert(self, prev_node_data, data):
        if not self.head:
            return
        current_node = self.head
        while current_node:
            if current_node.data == prev_node_data:
                new_node = self.Node(data)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def remove(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" -> ")
            current_node = current_node.next
        print("None")

linked_list_instance = linked_list()
linked_list_instance.append(1)
linked_list_instance.append(2)
linked_list_instance.display()  # Output: 1 -> 2 -> None
linked_list_instance.prepend(0)
linked_list_instance.display()  # Output: 0 -> 1 -> 2 -> None
linked_list_instance.insert(1, 1.5)
linked_list_instance.display()  # Output: 0 -> 1 -> 1.5 -> 2 -> None
linked_list_instance.remove(1.5)
linked_list_instance.display()  # Output: 0 -> 1 -> 2 -> None