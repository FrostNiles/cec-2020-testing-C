import sys
import os

argNum = sys.argv[1]

with open(f'input_data/shift_data_{argNum}.txt', 'r') as file:
    original_data = file.read()

# Read the new numbers
#if exists read the new numbers
if os.path.exists(f'test_data/shift_data_{argNum}.txt'):
    with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
        new_data = file.read()
else:
    print("The data are not there. We are going to write them.")
    with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
        file.write(original_data)

if original_data == new_data:
    print("The data are original.")
else:
    print("The data are not original we are going to rewrite them.")
    with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
        file.write(original_data)
