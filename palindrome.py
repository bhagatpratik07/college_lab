# Function to check if a number is a palindrome
def is_palindrome(number):
    # Convert the number to a string for easy comparison
    num_str = str(number)
    
    # Check if the string is equal to its reverse
    return num_str == num_str[::-1]

# Input: Number to check for palindrome
num_to_check = int(input("Enter a number to check for palindrome: "))

# Output: Displaying the result
if is_palindrome(num_to_check):
    print(f"{num_to_check} is a palindrome.")
else:
    print(f"{num_to_check} is not a palindrome.")

## Enter a number to check for palindrome: 121
## 121 is a palindrome.
