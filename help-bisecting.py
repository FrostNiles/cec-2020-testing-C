
# ok I want to set the upper or lower bound to the current data based on the result of the ran-main.py

import re
import sys

argNum = sys.argv[1]

#Open upper and lower bound

with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
    current = file.read()

#open the result file
with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
    result = file.read()


with open(f'test_data/shift_data_{argNum}_upper.txt', 'r') as file:
    upper = file.read()

with open(f'test_data/shift_data_{argNum}_lower.txt', 'r') as file:
    lower = file.read()




#upper border is upper higher number in the current as it should be in original

""" with open(f'test_data/shift_data_{argNum}_upper.txt', 'w') as file:
    file.write(current) """



 
#result is like this f1(x[1]) = 100.0000000395, and I want to take just 100.0000000395
result = re.findall(r'\d+\.\d+', result)
result = float(result[0])

result = str(result)
result = result.split('.')
#before the floating point
before = result[0]
#after the floating point
after = result[1]

# Now I want to get the first 8 digits from after
eightDigits = after[:8]
lastTwoDigits = after[-2:]



if int(eightDigits) > 0:
    with open(f'test_data/shift_data_{argNum}_upper.txt', 'w') as file:
        file.write(current)
else:
    if int(lastTwoDigits) < 96:
        with open(f'test_data/shift_data_{argNum}_lower.txt', 'w') as file:
            file.write(current)
    else:
        exit(0)
