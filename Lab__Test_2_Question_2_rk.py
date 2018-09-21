# Lab Test 2 - Question 2
# Use of replace_all function, with reading and writing to files.

def replace_all(string,list1,list2):
    str_list = string.split() # First, turn the input string into a list
    x = 0 # Initialise counters x and y
    y = 0
    for x in range (0, len(str_list)): # For each element in the list (our string)...
        for y in range (0, len(list1)): # For each element in the replacement lists (any number of elements)
            if str_list[x] == list1[y]: # If the element in the list(string) is equal to the word to be replaced
                str_list[x] = list2[y] # Then replace that list(string) element with the replacement word, otherwise no action
    return (" ".join(str_list)) # Then, join the list back up into a string


x = ["a"] # List of words to be replaced
y = ["the"] # List of words to be replaced with
output_file = open("gettysburg_output.txt", "w") # Create and open a new file to write to

with open('gettysburg.txt', 'r') as file_obj:
    for line in file_obj: # For each file in the line
        print(replace_all(line,x,y), file = output_file) # Run the function and write the result to the new output file
output_file.close() # Close output file. the input file (in this case gettysburg.txt) closes automatically when you use 'with'