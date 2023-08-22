# write a python program for fibonnaci numbers.
def fibonacci(n):
    fib_list = [0, 1]  # List to store Fibonacci numbers
    
    # Generate Fibonacci numbers until nth term
    while len(fib_list) < n:
        next_num = fib_list[-1] + fib_list[-2]  # Calculate next Fibonacci number
        fib_list.append(next_num)  # Add the number to the list
    
    return fib_list

# Get user input for the number of terms
num_terms = int(input("Enter the number of Fibonacci terms: "))

# Call the fibonacci function and print the result
fibonacci_sequence = fibonacci(num_terms)
print("Fibonacci sequence:", fibonacci_sequence)

# Enter the number of Fibonacci terms: 13
# Fibonacci sequence: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144]