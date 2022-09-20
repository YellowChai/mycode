#!/usr/bin/env python3

wordbank= ["indentation", "spaces"] 
tlgstudents= ["Aaron", "Andy", "Asif", "Brent", "Cedric", "Chris", "Cory", "Ebrima", "Franco", "Greg", "Hoon", "Joey", "Jordan", "JC", "LB", "Mabel", "Shon", "Pat", "Zach"]

# append  int 4 to the list wordbank

print(wordbank)

wordbank.append(4)
print(wordbank)

# get the input value from 1 -18

num = input("please select the number between 1-8: ")
print(num)

# convert str num into int

num = int(num)
print(num)

# slice one of the elements from the tlgstudents list using the num variable 

student_name = tlgstudents[num]


# Challenge - if the user input it not a number, print the input as a student name
'''if int(num):
    num = int(num)
    student_name = tlgstudents[num]
    print(student_name)
else:
    
    student_name = tlgstudents[num]
    print(student_name)'''

# print statement using user input and lists
print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent. ")


#randomize student pick 
student  = tlgstudents.pop(num)
tlgstudents.append(student)
student_name = tlgstudents[num]
print(f"{student_name} always uses {wordbank[2]} {wordbank[1]} to indent.")

 



