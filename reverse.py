import re
import sys

argNum = sys.argv[1]
# Open the file and read its contents
with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
    data = file.read()

#open the backup file and read its contents
with open(f'test_data/shift_data_{argNum}_backup.txt', 'r') as file:
    backup_data = file.read()

# backup the latest data
with open(f'test_data/shift_data_{argNum}_backup_latest.txt', 'w') as file:
    file.write(data)

# copy the backup data to the original file
with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
    file.write(backup_data)

