"""
# ---------------------------
# File           : q1.py
# Created        : 08-10-2021 00:23
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# Read in using studentid number and print the results
# Each student module & grades
# used tuples,list & Dictionaries
"""
if __name__ == "__main__":
    '''

    Main method of application
    List out the student modules and grades.

    Linear programming only presented here wrt demo of lists
    
    Parameters:
     Returns:
'''

student_id = ("L12345", "L54321")
module_subject = ["Java_programming", "Python_Scripting"]
module_1 = {"L12345": 40, "L54321": 70}
module_2 = {"L12345": 69, "L54321": 58}

while 1:
 s_id = input("Enter the student id number  or Do you wanna quit, Enter Q :")
 if s_id.lower() == "q":
   break
 elif s_id in student_id:
     print("Student ID - {} | Subject - {} | Module 1 Grade - {} | Subject - {} |Module 2 Grade - {}".
           format(s_id, module_subject[0], module_1.get(s_id), module_subject[1], module_2.get(s_id)))
 else:
     print("Please enter a valid student id")
