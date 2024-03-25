class GeneralQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)
    
    def priority_dequeue(self, item):
        return self.items.remove(item)
    
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return self.items == []