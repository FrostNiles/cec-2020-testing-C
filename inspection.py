import sys

argNum = sys.argv[1]
# Read the original numbers
with open(f'input_data/shift_data_{argNum}.txt', 'r') as file:
    original_data = file.read()

# Read the new numbers

# Split the data into individual numbers
original_numbers = [float(i) for i in original_data.split()]

with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'r') as file:
    deviation = float(file.read())
print("Final deviation: ", deviation)

number_of_element = int(sys.argv[3]) - 1
# Add the median deviation to the original numbers
original_numbers[number_of_element] = original_numbers[number_of_element] - deviation

# Write the adjusted numbers to a new file

with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
    for number in original_numbers:
        file.write(f"{number} ")