# A Python program to encrypt a string

input_str = str(input("Enter some text to encrypt: "))

#Initialise variables
x = 0
s1 = 0
output_str = 0
count = len(input_str) # Count is the length of the sting (from 1 to...)

# Step 1: Shift character 2 positions to the left, by using concatenation to create the interim string, s1
s1 = input_str[2:count] + input_str[0:2]

# Step 2: Shift ASCII by -1
while x <= count - 1: # Count from 0 to length of string -1. This count is the length of the sting - to correspond to indices of the input
    utf8_int = ord(s1[x])-1 # Change each index of the string from Step 1, s1, to UTF-8 integer value and shift by -1, and store in an interim variable, utf8_int
    output_str = chr(utf8_int) # Change UTF-8 integer and returns the UTF-8 character
    print(output_str, end='') # Print result
    x=x+1 # Increment counter
