"""
# ---------------------------
# File           : dictionary.py
# Created        : 07-10-2021 23:15
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
if __name__ == "__main__":
    campus={}
    contacts={"Ruth.Lennon": 6355, "Thomas": 6384, "Info": 6000}
    contact_addr={"Ruth.Lennon":"port Road","Thomas":"Port Road","Info":"Port Road"}
    print(contacts)
    print(contact_addr)

    print(contacts["Ruth.Lennon"])
    contacts["Gemma.Lynch"]=1234

    print(len(contacts))
    del contact_addr["Info"]

    print("Ruth.Lennon" in contacts)
    contact_name,contact_campus = contact_addr.popitem()
    print("pop item is {} and {} ".format(contact_name,contact_campus))
    print("\n")
    print("Dictionary now contact contains {}". format(contacts))
    print("Dictionary now contact address contains {}".format(contact_addr))

    print("\n")
    class_group_1 = {"Muhammed": 123455 , "Priyank": 455667}
    class_group_2 = {"Priyank": 756767 ,"Daniel": 675683}
    #group = class_group_1+class_group_2
    group_1= class_group_1 | class_group_2
   # print(group)
    print(group_1)