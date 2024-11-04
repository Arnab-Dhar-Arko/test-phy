class QueueList:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
    
    def enqueue(self, item):
        if len(self.queue) < self.capacity:
            self.queue.append(item)
        else:
            print("Queue is full")
    
    def dequeue(self):
        if self.queue:
            return self.queue.pop(0)
        else:
            print("Queue is empty")
            return -1
    
    def drop(self):
        if self.queue:
            return self.queue.pop()  
        else:
            return -1  
    
    def print(self):
        if self.queue:
            print(" ".join(map(str, self.queue)))
        else:
            print("Queue is empty")


a = QueueList(5)
for i in range(6):
    a.enqueue(i)  

a.dequeue()  
a.drop()     
a.print()    # This will print: "1 2 3 4"