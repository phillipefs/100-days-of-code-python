import random

names_string = input("Give me everybody's name, seperated by a comma. ")

names = names_string.split(", ")

#Get the total number of items in list
len_list = len(names)

#Choose element aleatory in the list
choose_name = names[random.randint(0,len_list-1)]

#Using Function Choice Module Random
person_who_will_pay =  random.choice(names)


print(person_who_will_pay + " is going to buy the meal today!")