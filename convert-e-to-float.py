import re
import sys

argNum = sys.argv[1]
# Open the file and read its contents
with open(f'test_data/shift_data_{argNum}_upper.txt', 'r') as file:
    upper = file.read()

# open the latest backup file and read its contents
with open(f'test_data/shift_data_{argNum}_lower.txt', 'r') as file:
    lower = file.read()

#backup the data to the step backup


# Split the data into individual numbers - the one number is written like this (for example) in the file -5.527639849e+01

#data_numbers = re.findall(r'[-+]?\d*\.\d+|\d+', data)
#backup_numbers = re.findall(r'[-+]?\d*\.\d+|\d+', backup_latest_data)

# split all the data numbers from upper with "e" 

upper_numbers = re.findall(r'[-+]?\d*\.\d+e[-+]?\d+|\d+', upper)
lower_numbers = re.findall(r'[-+]?\d*\.\d+e[-+]?\d+|\d+', lower)

convert_upper_numbers = [float(num) for num in upper_numbers]
convert_lower_numbers = [float(num) for num in lower_numbers]

with open(f'test_data/shift_data_{argNum}_upper.txt', 'w') as file:
    for number in convert_upper_numbers:
        file.write(f"{number} ")

with open(f'test_data/shift_data_{argNum}_lower.txt', 'w') as file:
    for number in convert_lower_numbers:
        file.write(f"{number} ")
