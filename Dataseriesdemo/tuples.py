"""
# ---------------------------
# File           : tuples.py
# Created        : 07-10-2021 23:04
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
if __name__ == "__main__":
    '''...'''

    empty_tuple = ()
    ages = (19,21,20)

    student1_details = (20, "Michael Brennan", 77.5)
    student2_details = (33, "Maired Gallagher", 65)

    class_of_students = (student1_details,student2_details,"Module name",[2,3,4],("a","b"))
    group_of_students = student1_details + student2_details

    '''Printing list examples'''
    print("{}".format(ages[1]))
    print("{0} \t\t{1} \t{2} ".format(student1_details[0],student1_details[1],student1_details[2]))
    print("{}".format(student1_details))
    print("{}".format(class_of_students))
    print("{}".format(class_of_students[0][1]))

    grades = (1,2,3)
    nu_grades = (grades) * 2
    print(nu_grades)
    # grades[0][0] = 6 (we cant assign or change the values for tuples)
    # print(nu_grades)

