filename = 'shift_data_1.txt'

# Open the file in read mode
with open(filename, 'r') as file:
    # Read the contents of the file
    contents = file.read()

# Split the contents into a list of numbers
numbers = contents.split()

# Iterate over each number
for number in numbers:
    # Check if the number contains a floating point
    if '.' in number:
        # Count the number of digits after the floating point
        digits_after_decimal = len(number.split('.')[1])
        print(f"Number: {number}, Digits after decimal: {digits_after_decimal}")
    else:
        print(f"Number: {number}, No floating point")