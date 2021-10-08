"""
# ---------------------------
# File           : copy_deepcopy.py
# Created        : 06-10-2021 00:01
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
from copy import deepcopy
if __name__ == "__main__":
    student1_details = [20, "Michael Brennan", 77.5]
    student2_details = [33, "Maired Gallagher", 65]

    # copy type 3: deepcopy
    student4_details = deepcopy(student1_details)
    print("student4details:{}".format(student4_details))

    print("\n")
    student4_details[0] = 66
    print("student1_details: {}".format(student1_details))
    print("student4_details: {}".format(student4_details))


