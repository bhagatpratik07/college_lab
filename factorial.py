# Function to calculate the factorial of a number
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculate_factorial(n - 1)

# Input: Number to calculate the factorial
num = int(input("Enter a number to calculate its factorial: "))

# Output: Displaying the result
result = calculate_factorial(num)
print(f"The factorial of {num} is {result}")

## INPUT: 5
## OUTPUT: The factorial of 5 is 120
