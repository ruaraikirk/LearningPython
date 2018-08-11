# Exercise 5: Write a class Student. Every student should have a name, student number and a list of marks
# (implemented as a python list) Include any appropriate methods, and a method to calculate the average mark.

class Student:
    def __init__(self, name, studentID, marks):
        self.name = name
        self.studentID = studentID
        self.marks = marks
    def __str__(self):
        return "Name: {}, Student ID: {}, Marks: {}".format(self.name, self.studentID, self.marks)

    def average(self):
        if type(self.marks) is list:  # If input is a list the proceed
            x = 0  # Initialise Variable
            for el in self.marks:  # Add each numeric element to the last
                x = x + el
            return x / len(self.marks)
        else:  # Else we aren't working with a list, error!
            x = 'ERROR! Input is not a numeric list!'
            return x

s1 = Student("Jack", 12345, [1, 2, 3, 4, 5])

print(s1)
print(s1.average())