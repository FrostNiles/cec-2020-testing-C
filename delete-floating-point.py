import re
import sys

argNum = sys.argv[1]
numberOfDelete = sys.argv[3]

numberOfDelete = int(numberOfDelete) - 1

# Open the file and read its contents
with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
    data = file.read()

#write original content to backup file
with open(f'test_data/shift_data_{argNum}_backup.txt', 'w') as file:
    file.write(data)

# Use a regular expression to replace numbers before "e" with an empty string
# just delete one number before "e"
# in the end I want to get the whole number just without the digit before "e"
# but I want to delete only from one number and its position I will tell in the argument
# so I will delete the number before "e" from the number which is in the position 1


# Extract the second number from the modified data
numbers = re.findall(r'(-?\d+\.\d+e[+-]\d+)', data)
if len(numbers) >= numberOfDelete:
    numeroToDelete = numbers[numberOfDelete]
else:
    print("The number of the position to delete is greater than the number of numbers in the file")
    sys.exit()

#delete the number before "e" from the number in variable numeroToDelete
modified_number = re.sub(r'(\d)(e)', r'\2', numeroToDelete)

# Replace the first number with the modified number
modified_data = data.replace(numeroToDelete, modified_number)


# Write the modified contents to the original file
with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
    file.write(modified_data)