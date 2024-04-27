file_path = "input_data/shift_data_22.txt"
count = 0

with open(file_path, "r") as file:
    for line in file:
        numbers = line.split()
        count += len(numbers)

print("Number of numbers:", count)