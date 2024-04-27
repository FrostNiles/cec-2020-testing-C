import subprocess
import sys
import os

func_num = sys.argv[1]
dimension = sys.argv[2]
# Check if dimension is valid
if dimension not in ['2', '5', '10', '15', '20', '30', '50', '100']:
    print("Invalid dimension. Please choose from 2, 5, 10, 15, 20, 30, 50, 100.")
    sys.exit(1)

# Set the dimension as a command line argument for the C++ program
args = ["./main", func_num, dimension]

# Run the compiled file with the specified arguments
subprocess.run(args, check=True)