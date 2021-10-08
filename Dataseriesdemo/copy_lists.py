"""
# ---------------------------
# File           : copy_lists.py
# Created        : 06-10-2021 00:10
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
if __name__ == "__main__":
    student1_details = [20, "Michael Brennan", 77.5]
    student2_details = [33, "Maired Gallagher", 65]

    #copy type1:
    student3_details= student1_details
    print("student3_details: {}".format(student3_details))

    student3_details[0]=55
    print("student1_details: {}".format(student1_details))
    print("student3_details: {}".format(student3_details))

    #using id() function to show that they point the same object
    print("\n")
    print("student1_details: {} with an id: {}".format(student1_details,id(student1_details)))
    print("student3_details: {} with an id: {}".format(student3_details,id(student3_details)))

    #Copy type 2:
    student3_details=student1_details[:]
    print("student3_details: {}".format(student3_details))
    student3_details[0] = 88
    print("student1_details: {}".format(student1_details))
    print("student3_details: {}".format(student3_details))

