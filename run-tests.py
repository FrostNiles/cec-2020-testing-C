import runpy
import re
import sys

arg1 = sys.argv[1]
arg2 = sys.argv[2]
arg3 = sys.argv[3]

# Run the first Python script
argNum = arg1
dimension = arg2

sys.argv = ['run-tests.py', arg1, arg2, arg3]
#import the original data

runpy.run_path('./import-original.py')
runpy.run_path('./run-main.py')

# Open the dimension file and func_num file and read its contents

with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
    result = file.read()

# Find the number in the string
result = re.findall(r'\d+\.\d+', result)

# Keep the number as a string to preserve trailing zeroes
number_string = result[0]

# Convert to float when you need to do a numerical operation

result = str(result)
result = result.split('.')
#before the floating point
before = result[0]
#after the floating point
after = result[1]

# Now I want to get the first 8 digits from after
eightDigits = after[:8]
lastTwoDigits = after[-2:]

while int(eightDigits) == 0:
    runpy.run_path('./delete-floating-point.py')
    runpy.run_path('./run-main.py')
    with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
        result = file.read()

    result = re.findall(r'\d+\.\d+', result)

    result = float(result[0])
    

    result = str(result)
    result = result.split('.')
    #before the floating point
    before = result[0]
    #after the floating point
    after = result[1]

    eightDigits = after[:8]
    lastTwoDigits = after[-2:]
    

with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
    data = file.read()

with open(f'test_data/shift_data_{argNum}_backup.txt', 'r') as file:
    backup = file.read()

# lets write both data and backup to the file separete them with enter
with open(f'test_data/shift_data_{argNum}_final.txt', 'w') as file:
    file.write(backup)
    file.write("\n")
    file.write(data)


number_of_element = int(arg3) - 1
data_number = re.findall(r'\d+\.\d+e[+-]\d+', data)[number_of_element]
backup_number = re.findall(r'\d+\.\d+e[+-]\d+', backup)[number_of_element]

#write only one of the data to the file
with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'w') as file:
    file.write(f"Dimension: {dimension}")
    file.write("\n")
    file.write(data_number)
    file.write("\n")
    file.write(backup_number)
    file.write("\n")
with open(f'test_data/shift_data_{argNum}.txt', 'w') as file:
    file.write(data)

with open(f'test_data/shift_data_{argNum}_backup.txt', 'w') as file:
    file.write(backup)

#stop here for now
#sys.exit()

runpy.run_path('./first-run.py')

runpy.run_path('./convert-e-to-float.py')

runpy.run_path('./run-main.py')





#open the result file
with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
    result = file.read()

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



while int(eightDigits) > 0 or int(lastTwoDigits) < 96:
    
    runpy.run_path('./help-bisecting.py')
    
    runpy.run_path('./half.py')
    
    runpy.run_path('./run-main.py')
    with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
        result = file.read()

    result = re.findall(r'\d+\.\d+', result)
    result = float(result[0])

    result = str(result)
    result = result.split('.')
    #before the floating point
    before = result[0]
    #after the floating point
    after = result[1]

    eightDigits = after[:8]
    lastTwoDigits = after[-2:]


#open the shift_data_1.txt and read the data
with open(f'test_data/shift_data_{argNum}.txt', 'r') as file:
    data = file.read()
#write these results to the file shift_data_1final_bisection.txt
with open(f'test_data/shift_data_{argNum}_final_bisection.txt', 'w') as file:
    file.write(data)


runpy.run_path('./deviation.py')
runpy.run_path('./inspection.py')
runpy.run_path('./run-main.py')

with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
    result = file.read()

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
tenDigits = after[:10]

if int(eightDigits) > 0:

    while int(eightDigits) != 0:
        #load median deviation
        with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'r') as file:
            median_deviation = file.read()
        #change the median deviation
        #check the first two digits after the floating point
        median_deviation = str(median_deviation)
        median_deviation = median_deviation.split('.')
        #before the floating point
        before = median_deviation[0]
        

        if len(before) > 1:
            if before[1] == 'e':
                backup = before.split('e')
                if before[0] == '0':
                    before = '9'
                    backup[1] = int(backup[1]) - 1
                    backup[1] = str(backup[1])
                    median_deviation = before + "." + "" + "e" + backup[1]
                else:
                    
                    before = before.split('e')
                    before[0] = int(before[0]) - 1
                    before = str(before[0]) 
                    median_deviation = before + "." + "99" + "e" + backup[1]
            else:
                
                #after the floating point
                after = median_deviation[1]
                # Now I want to get the first 2 digits from after
                twoDigits = after[:2]
                if twoDigits[1] == 'e':
                    
                    if twoDigits[0] == '1':
                        twoDigits = '0' + '9'
                        twoDigits = int(twoDigits) -1
                    else:
                        twoDigits = twoDigits[0] + '0'
                        twoDigits = int(twoDigits) - 1
                else:
                    twoDigits = int(twoDigits) - 1
                    
                #and also I want to get e-01 or whatever is there after "e" and after is like this: 5056482283171135e-08
                exponent = after.split('e')[1]
                twoDigits = f"{twoDigits:02d}"
                #substract 1 from the first two digits
                
                #concatenate the before and the two digits
                median_deviation = before + "." + twoDigits + "e" + exponent
                
        else:
            if (int(eightDigits) > 3):
                before = int(before) - 1
                before = str(before)
            #after the floating point
            after = median_deviation[1]
            # Now I want to get the first 2 digits from after
            twoDigits = after[:2]
            if twoDigits[1] == 'e':
                if twoDigits[0] == '1':
                    twoDigits = '0' + '9'
                    twoDigits = int(twoDigits) -1
                else:
                    twoDigits = twoDigits[0] + '0'
                    twoDigits = int(twoDigits) - 1
            elif twoDigits == '00':
                twoDigits = '99'
                twoDigits = int(twoDigits)
                before = int(before) - 1
                before = str(before)
            else:
                twoDigits = int(twoDigits) - 1
                
            #and also I want to get e-01 or whatever is there after "e" and after is like this: 5056482283171135e-08
            exponent = after.split('e')[1]
            twoDigits = f"{twoDigits:02d}"
            #substract 1 from the first two digits
            
            #concatenate the before and the two digits
            median_deviation = before + "." + twoDigits + "e" + exponent
                
        #write the new median deviation to the file
        with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'w') as file:
            file.write(median_deviation)
        
        runpy.run_path('./inspection.py')
        runpy.run_path('./run-main.py')

        with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
            result = file.read()

        result = re.findall(r'\d+\.\d+', result)
        result = float(result[0])

        result = str(result)
        result = result.split('.')
        #before the floating point
        before = result[0]
        #after the floating point
        after = result[1]
        eightDigits = after[:8]
        lastTwoDigits = after[-2:]
        tenDigits = after[:10]
    

    

else:
    if int(lastTwoDigits) < 96:
        while int(lastTwoDigits) < 96:

            #load median deviation
            with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'r') as file:
                median_deviation = file.read()
            #change the median deviation
            #check the first two digits after the floating point
            median_deviation = str(median_deviation)
            median_deviation = median_deviation.split('.')
            #before the floating point
            before = median_deviation[0]

            if len(before) > 1:
                if before[1] == 'e':
                    backup = before.split('e')
                    before = before.split('e')
                    before[0] = int(before[0])
                    before = str(before[0]) 
                    median_deviation = before + "." + "01" + "e" + backup[1]
        
            else:
                if (int(tenDigits) < 40):
                    digitCount = len(str(int(tenDigits)))
                    
                    if digitCount == 2:  
                        before = int(before) + 1
                        before = str(before)
                #after the floating point
                after = median_deviation[1]
                # Now I want to get the first 2 digits from after
                twoDigits = after[:2]
                #and also I want to get e-01 or whatever is there after "e" and after is like this: 5056482283171135e-08
                
                exponent = after.split('e')[1]
                
            
                if twoDigits == '99':

                    if (before == '9'):
                        exponent = int(exponent) + 1
                        exponent = str(exponent)
                        before = '1'
                    else:
                        before = int(before) + 1
                        before = str(before)
                    twoDigits = '00'
                    median_deviation = before + "." + twoDigits + "e" + exponent
                else:
                    if twoDigits[1] == 'e':
                        twoDigits = twoDigits[0] + '0'
                        #concatenate the before and the two digits
                        median_deviation = before + "." + twoDigits + "e" + exponent
                    if twoDigits[0] == '0':
                        if twoDigits[1] == '9':

                            twoDigits = "10"
                            #concatenate the before and the two digits
                            median_deviation = before + "." + twoDigits + "e" + exponent
                        else:
                            twoDigits = int(twoDigits) + 1
                            #convert the two digits to string
                            twoDigits = str(twoDigits)
                            twoDigits = '0' + twoDigits
                            #concatenate the before and the two digits
                            median_deviation = before + "." + twoDigits + "e" + exponent
                    else:
                        twoDigits = int(twoDigits) + 1
                        #convert the two digits to string
                        twoDigits = str(twoDigits)
                        #concatenate the before and the two digits
                        median_deviation = before + "." + twoDigits + "e" + exponent
            #write the new median deviation to the file
            with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'w') as file:
                file.write(median_deviation)
            
            runpy.run_path('./inspection.py')
            runpy.run_path('./run-main.py')

            with open(f'test_data/current_result_{argNum}.txt', 'r') as file:
                result = file.read()

            result = re.findall(r'\d+\.\d+', result)
            result = float(result[0])

            result = str(result)
            result = result.split('.')
            #before the floating point
            before = result[0]
            #after the floating point
            after = result[1]
            eightDigits = after[:8]
            lastTwoDigits = after[-2:]
            tenDigits = after[:10]
# Add more lines as needed to run more scripts

with open(f'test_data/shift_data_{argNum}_deviation_final.txt', 'r') as file:
                deviation = file.read()

with open(f'test_data/result/result_data_{argNum}_dim_{dimension}_number_of_element_{number_of_element+1}.txt', 'w') as file:
    file.write("deviation:")
    file.write(deviation)
    