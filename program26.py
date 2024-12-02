# Get user input
input_string = input("Enter a comma-separated string: ")

# Step 1: Find all letters in the string and convert them to uppercase
letters = list(filter(lambda x: x.isalpha(), input_string))  # Filter letters
uppercase_letters = list(map(lambda x: x.upper(), letters))  # Convert to uppercase

# Step 2: Find all digits in the string and compute their squares
digits = list(filter(lambda x: x.isdigit(), input_string))  # Filter digits
squared_digits = list(map(lambda x: int(x)**2, digits))  # Square the digits

# Print the outputs
print(f"Uppercase Letters: {uppercase_letters}")
print(f"Squared Digits: {squared_digits}")