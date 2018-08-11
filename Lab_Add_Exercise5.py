# Exercise 5: Write a Python function that takes two lists and returns true if they have at least one common element.


# The basic idea of this function is to sort both lists, then take the first element of list1 and compare to all
# the elements in list 2. If it hits an identical element, the loop stops and returns true, else it will move to the
# next element in list 1 and again compare to all the elements in list 2. If no identical elements are identified, a
# false statement is returned.

def one_element(list1,list2):
    list1.sort()
    list2.sort()
    for x in list1:
        for y in list2:
            if x!=y:
                continue # If element comparison is not equal, continue onto next iteration of loop.
            else:
                print('These lists have at least 1 identical element')
                return  # Else, if there is a comparison (first true), then finish function and return True statement
    return print('These lists have zero identical element') # If no equal elements, return False statement

one_element([1,2,3,4,5],[9,8,7,6,5]) # These list have 1 identical element and should return true statement
one_element([1,2,3,4,5,6],[9,0,7,8]) # These lists have zero identical elements, and should return false statement
one_element([11,12,13,14],[87,65,5,65,12]) # These list have 1 identical element and should return true statement