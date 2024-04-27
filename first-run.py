import re
import sys

argNum = sys.argv[1]
# Open the file and read its contents
with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
    data = file.read()

# open the latest backup file and read its contents
with open(f'test_data/shift_data_{argNum}_backup.txt', 'r') as file:
    backup_latest_data = file.read()

#set the backup as uppper border
with open(f'test_data/shift_data_{argNum}_lower.txt', 'w') as file:
    file.write(backup_latest_data)

#set the data as lower border
with open(f'test_data/shift_data_{argNum}_upper.txt', 'w') as file:
    file.write(data)

# Split the data into individual numbers - the one number is written like this (for example) in the file -5.527639849e+01

data_numbers = re.findall(r'[-+]?\d*\.\d+e[-+]?\d+|\d+', data)
backup_numbers = re.findall(r'[-+]?\d*\.\d+e[-+]?\d+|\d+', backup_latest_data)

data_numbers = [float(num) for num in data_numbers]
backup_numbers = [float(num) for num in backup_numbers]



# now I want to bisecting the interval between the two numbers on the same position in each file
# I want to get the number in the middle between the two numbers with bisecting the interval

number_of_element = int(sys.argv[3]) - 1

middle_number = [(data_numbers[number_of_element] + backup_numbers[number_of_element]) / 2]

data_numbers[number_of_element] = middle_number[0]


# now I want to write the middle numbers to the original file just the number and with a space behind the number
with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
    for number in data_numbers:
        file.write(f"{number} ")