"""
# ---------------------------
# File           : q2.py
# Created        : 09-10-2021 11:31
# Author         : Aishwarya
# Version        : v1.0.0
# Licensing      : (c) 2021 Aishwarya,LYIT
#                  Available under GNU Public License (GPL)
# Description    
# Create the lotto player list for 2weeks
# find the intersection
# unique member in 2 weeks
# most common lotto numbers
# member who pick the same number on multipke occasions
"""
from random import randrange
week_1_lotto_players = ["Joe", "John", "Jane", "Mick", "Mary", "Ann", "Rick", "John", "Aine", "Brenda"]
numberslist_1 = []
for i in range(10):
    #number_1= (randrange(20))
    numberslist_1.append(randrange(20))
print(week_1_lotto_players)
print(numberslist_1)
lotto_players_1 = dict(zip(week_1_lotto_players, numberslist_1))
print(lotto_players_1)
print("\n")
week_2_lotto_players = ["Jack", "Mary", "Phil", "John", "Pat", "Joe", "Luke", "Bill", "Ben", "Nathan"]
numberslist_2 = []
for i in range(10):
    #number_2= (randrange(20))
    numberslist_2.append(randrange(20))
print(week_2_lotto_players)
print(numberslist_2)
lotto_players_2 = dict(zip(week_2_lotto_players, numberslist_2))
print(lotto_players_2)
print("\n")

intersection = lotto_players_1.keys() & lotto_players_2.keys()
print("{} who bought the tickets on both weeks".format(intersection))

unique_names = [intersection]
print("unique names:{}".format(unique_names))

n_list= numberslist_1+numberslist_2
print(n_list)


def most_frequent(n_list):
    return max(set(n_list), key=n_list.count)
print("{} is the most common lotto number.".format(most_frequent(n_list)))

is_multiple_ocssaions = False
for member in intersection:
    if lotto_players_1.get(member) == lotto_players_2.get(member):
        print("Player {} got same {} on multiple occasions".format(member, lotto_players_1.get(member)))
        is_multiple_ocssaions = True

if not is_multiple_ocssaions:
    print("No player got same number on multiple ocassions")


# intersection_1 = lotto_players_1.values() & lotto_players_2.values()
# print("{} who bought the tickets on both weeks".format(intersection_1 ))



