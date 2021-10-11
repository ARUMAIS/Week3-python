"""
# ---------------------------
# File           : q3.py
# Created        : 10-10-2021 00:21
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# create the vm machine
# with  the minimum specifications required for OS
# collect the user data and show in tidy manner
"""

vm_min_requirements = {"Windows": {"processor_core": 4, "ram_in_gb": 8, "storage_in_gb": 40},
                       "Linux": {"processor_core": 4, "ram_in_gb": 8, "storage_in_gb": 40}}

requestor_name = input("Please enter your name")
time_duration_in_days = int(input("Please enter how long you need the VM (in days). Enter only number"))
vm_needed_date = input("Enter VM start date in MM-DD-YYYY format")


vm_os_num = int(input("Select VM OS. Enter 1 for Windows, 2 for Linux"))
if vm_os_num == 1:
    vm_os = "Windows"
elif vm_os_num == 2:
    vm_os = "Linux"


while 1:
    vm_processor = int(input("Enter no. of processor core required (in numbers)"))
    min_processor_core = vm_min_requirements[vm_os]["processor_core"]
    if vm_processor < min_processor_core:
        print("Minimum processor core allowed is 4. Please select again")
    else:
        break
while 1:
    vm_ram = int(input("Enter no. of gb ram required (in numbers)"))
    min_ram = vm_min_requirements[vm_os]["ram_in_gb"]
    if vm_ram < min_ram:
        print("Minimum ram gb allowed is 4. Please select again")
    else:
        break
while 1:
    vm_storage = int(input("Enter no. of gb storage required (in numbers)"))
    min_storage = vm_min_requirements[vm_os]["storage_in_gb"]
    if vm_storage < min_storage:
        print("Minimum gb storage allowed is 4. Please select again")
    else:
        break

requestor_details = {"operationg_sys":vm_os,"processor_core": vm_processor, "ram_in_gb": vm_ram, "storage_in_gb": vm_storage}

print("*"*10)
print("Requestor Name: {}".format(requestor_name))
print("Duration: {}".format(time_duration_in_days))
print("VM Needed date: {}".format(vm_needed_date))
print("VM Operating System: {}".format(vm_os))
print("Processor core: {}".format(vm_processor))
print("*"*10)
print(requestor_details)