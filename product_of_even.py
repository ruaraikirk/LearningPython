# A Python program that will ask the user for a number, and print the product of all EVEN numbers from 1
# to the number the enter inclusive. The program will also print how many numbers were multiplied.

# Ask for input
input_int = int(input('Please enter an integer number: '))

# Initialise Variables
count = 0
x = 0
y = 1

# Check if input is less than 2 and if so return error message.
if input_int < 2:
    print('ERROR! Number is less than 2!')
else:
# In range 2 (first even number) to the number given by the user (inclusive), multiply each even number (iterate by 2 from 2).
    for x in range (2, input_int+1, 2):
        y = y*x
        count += 1 # Increment counter
# Print result
    print('The multiples of all the even numbers from 1 to', input_int, 'is', y,', and there were', count, 'numbers multiplied.')
