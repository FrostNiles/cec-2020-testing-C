import re
import sys

argNum = sys.argv[1]

# Open the file and read its contents
with open(f'test_data/shift_data_{argNum}_upper.txt', 'r') as file:
    upper = file.read()

# open the latest backup file and read its contents
with open(f'test_data/shift_data_{argNum}_lower.txt', 'r') as file:
    lower = file.read()

with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
    original = file.read()

#backup the data to the step backup

lower_numbers = [float(i) for i in lower.split()]
upper_numbers = [float(i) for i in upper.split()]
original_numbers = [float(i) for i in original.split()]



# now I want to bisecting the interval between the two numbers on the same position in each file
# I want to get the number in the middle between the two numbers with bisecting the interval

number_of_element = int(sys.argv[3]) - 1

middle_number = [(lower_numbers[number_of_element] + upper_numbers[number_of_element]) / 2]

original_numbers[number_of_element] = middle_number[0]

# now I want to write the middle numbers to the original file just the number and with a space behind the number
with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
    for number in original_numbers:
        file.write(f"{number} ")


