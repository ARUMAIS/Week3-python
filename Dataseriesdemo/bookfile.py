"""
# ---------------------------
# File           : bookfile.py
# Created        : 05-10-2021 14:21
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# ---------------------------
"""
books=[]

for i in range(0,4):
 books.append(input("Enter the book name:"))
for i in range(0,4):
 print("{} has a value of {}".format(i,books[i]))




