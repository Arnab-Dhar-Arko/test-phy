def find_all_sum(arr, N):
    # Base case: if N is 0, print the current combination
    if N == 0:
        print(arr)
        return
    
    # Start from 1 and go up to N
    for i in range(1, N + 1):
        # Include the current number in the combination
        arr.append(i)
        # Recur with reduced N
        find_all_sum(arr, N - i)
        # Backtrack: remove the last element to try the next number
        arr.pop()

# Example usage:
find_all_sum([], 5)