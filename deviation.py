import sys

argNum = sys.argv[1]

# Read the original numbers
with open(f'input_data/shift_data_{argNum}.txt', 'r') as file:
    original_data = file.read()

# Read the new numbers
with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
    new_data = file.read()

# Split the data into individual numbers
original_numbers = [float(i) for i in original_data.split()]
new_numbers = [float(i) for i in new_data.split()]

# Get n from command line arguments
n = int(sys.argv[2])
#get number of element in the list from command line
numberOfElement = int(sys.argv[3]) - 1
# Calculate the deviation
deviation = abs(original_numbers[numberOfElement] - new_numbers[numberOfElement])
#count deviation in the exact position

with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'w') as file:
    file.write(f"{deviation:.5e}")