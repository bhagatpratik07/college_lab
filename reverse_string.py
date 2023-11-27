# Function to reverse a string
def reverse_string(input_string):
    return input_string[::-1]

# Input: String to reverse
input_str = input("Enter a string to reverse: ")

# Output: Displaying the reversed string
reversed_str = reverse_string(input_str)
print(f"Reversed String: {reversed_str}")
