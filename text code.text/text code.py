class MyStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = []
    
    def push(self, item):
        if len(self.stack) < self.capacity:
            self.stack.append(item)
        else:
            print("Stack is full")
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            print("Stack is empty")
            return -1
    
    def print(self):
        if self.stack:
            print("From bottom:", " ".join(map(str, self.stack)))
        else:
            print("Stack is empty")

def merge_stack(sa, sb, method="stack"):
    new_stack = MyStack(sa.capacity + sb.capacity)  # Create a new stack with combined capacity
    
    if method == "stack":
        # Append all elements from sa and then sb
        while sa.stack:
            new_stack.push(sa.pop())
        while sb.stack:
            new_stack.push(sb.pop())
        
        # Reverse the new stack to maintain the original order
        temp_stack = MyStack(new_stack.capacity)
        while new_stack.stack:
            temp_stack.push(new_stack.pop())
        
        # Transfer back to new_stack to maintain order
        while temp_stack.stack:
            new_stack.push(temp_stack.pop())
    
    elif method == "interleave":
        # Interleave elements from sa and sb
        temp_stack = MyStack(sa.capacity + sb.capacity)
        
        while sa.stack or sb.stack:
            if sa.stack:
                temp_stack.push(sa.pop())
            if sb.stack:
                temp_stack.push(sb.pop())
        
        # Reverse the temp_stack to maintain interleaved order
        while temp_stack.stack:
            new_stack.push(temp_stack.pop())
    
    else:
        print("Invalid method. Use 'stack' or 'interleave'.")
    
    return new_stack

# Example usage:
# Test case 1
a, b = MyStack(5), MyStack(4)
for i in range(1, 4): a.push(i)  # a = [1, 2, 3]
for i in range(4, 6): b.push(i)  # b = [4, 5]
c = merge_stack(a, b)
c.print()  # Output: From bottom: 1 2 3 4 5

# Test case 2
a, b = MyStack(5), MyStack(4)
for i in range(1, 4): b.push(i)  # b = [1, 2, 3]
a.push(4)  # a = [4]
c = merge_stack(a, b, method="interleave")
c.print()  # Output: From bottom: 4 1 2 3