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
    
    def merge(self, other, method="append"):
        if method == "append":
            for item in other.queue:
                self.enqueue(item)
        elif method == "interleave":
            new_queue = []
            len_self = len(self.queue)
            len_other = len(other.queue)
            min_length = min(len_self, len_other)
            
            # Interleave elements
            for i in range(min_length):
                new_queue.append(self.queue[i])
                new_queue.append(other.queue[i])
            
           
            if len_self > len_other:
                new_queue.extend(self.queue[min_length:])
            else:
                new_queue.extend(other.queue[min_length:])
            
          
            self.queue = new_queue
        else:
            print("Invalid method. Use 'append' or 'interleave'.")

# Exampl
q1 = QueueList(5)
q2 = QueueList(5)

# q1
q1.enqueue(1)
q1.enqueue(2)

#  q2
q2.enqueue(3)
q2.enqueue(4)
q2.enqueue(5)

# Merge using append
q1.merge(q2, method="append")
q1.print()  # Output: 1 2 3 4 5

# Reset q1 £ q2 for leave example
q1 = QueueList(5)
q2 = QueueList(5)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q2.enqueue(4)
q2.enqueue(5)

# Merge using interleave
q1.merge(q2, method="interleave")
q1.print()  

# Further test with different lengths
q1 = QueueList(5)
q2 = QueueList(5)
q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q2.enqueue(4)
q2.enqueue(5)
q2.enqueue(6)


q1.merge(q2, method="interleave")
q1.print()  # Output: 1 4 2 3 5 6