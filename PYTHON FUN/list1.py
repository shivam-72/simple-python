import random
names = (input("enter the names as a string"))
lst = names.split(",")
access = random.randint(0, len(lst)-1)

print(f"{lst[access]}is going to buy the meal today")
