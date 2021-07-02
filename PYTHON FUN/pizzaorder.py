print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_s = 2
pepperoni_m_l = 3
extra_chees = 1
total = 0
if size == "S":
    total += small_pizza
    if add_pepperoni == "Y":
        total += pepperoni_s
    elif add_pepperoni == "N":
        total += 0
    if extra_cheese == "Y":
        total += extra_chees
    elif extra_cheese == "N":
        total += 0
elif size == "M":
    total += medium_pizza
    if add_pepperoni == "Y":
        total += pepperoni_m_l
    elif add_pepperoni == "N":
        total += 0
    if extra_cheese == "Y":
        total += extra_chees
    elif extra_cheese == "N":
        total += 0
elif size == "L":
    total += large_pizza
    if add_pepperoni == "Y":
        total += pepperoni_m_l
    elif add_pepperoni == "N":
        total += 0
    if extra_cheese == "Y":
        total += extra_chees
    elif extra_cheese == "N":
        total += 0

print(f'your final bill is: {total} ')
