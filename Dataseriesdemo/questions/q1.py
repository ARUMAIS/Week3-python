"""
# ---------------------------
# File           : q1.py
# Created        : 08-10-2021 00:23
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
if __name__ == "__main__":
    '''

    Main method of application
    List out the student modules and grades.

    Linear programming only presented here wrt demo of lists
    
    Parameters:
     Returns:
'''

Studentid = ("L12345", "L54321")

modulesubject = ["Java_programming", "Python_Scripting"]
module1 = {"L12345":40, "L54321":70}
module2 = {"L12345":69, "L54321":58}

s_id = input("Enter the studentid_number:")
index = Studentid.index(s_id)

print("Student ID - {} | Subject - {} | Module 1 Grade - {} | Module 2 Grade - {}".
      format(s_id, modulesubject[index], module1.get(s_id), module2.get(s_id)))
