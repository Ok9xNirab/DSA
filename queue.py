class queue():
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Dequeue from an empty queue")
    
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("Peek from an empty queue")
    
    def size(self):
        return len(self.items)

if __name__ == "__main__":
    queue_instance = queue()
    queue_instance.enqueue(1)
    queue_instance.enqueue(2)
    print(queue_instance.dequeue())  # Output: 1
    print(queue_instance.peek())     # Output: 2
    print(queue_instance.size())     # Output: 1