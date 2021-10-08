"""
# ---------------------------
# File           : list_plus_debug.py
# Created        : 05-10-2021 14:07
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
if __name__ == "__main__":
    empty_list = []
    empty_list.append(10)
    ages = [19, 21, 20]

    student1_details = [20, "Michael Brennan", 77.5]
    student2_details = [33, "Maired Gallagher", 65]
    class_of_students = [student1_details,student2_details,"Module name",[2,3,4]]
    group_of_students = student1_details + student2_details

    group_of_students = class_of_students[0:2]
    print(group_of_students)
    print("1st student,2nd datum is:{0}".format((group_of_students[0])[1]))

    second_group_of_students = student1_details+student2_details
    third_group_of_students =[]
    third_group_of_students += second_group_of_students

    print("Is michael in list? {}".format("Michael" in group_of_students[0][1]))
    print("Is michael in list? {}".format("Michael" in group_of_students[0]))

    print("\n{}".format(group_of_students[0][1]))
    print("{}".format(group_of_students[0]))
    print("Third group of students {}".format(third_group_of_students))