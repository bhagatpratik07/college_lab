# Function to generate Fibonacci series up to n terms
def generate_fibonacci(n):
    fib_series = []
    
    # Initializing the first two terms of the series
    a, b = 0, 1
    
    # Generating Fibonacci series up to n terms
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b  # Update next terms
        
    return fib_series

# Input: Number of terms in the Fibonacci series
num_terms = int(input("Enter the number of terms in the Fibonacci series: "))

# Output: Displaying the Fibonacci series
fibonacci_series = generate_fibonacci(num_terms)
print(f"Fibonacci series up to {num_terms} terms: {fibonacci_series}")


## SAMPLE INPUT: 8
## OUTPUT: Fibonacci series up to 8 terms: [0, 1, 1, 2, 3, 5, 8, 13]
