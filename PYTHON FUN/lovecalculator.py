print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
name1.lower()
name2.lower()
name3 = name1+name2
T = name3.count("t")
R = name3.count("r")
U = name3.count("u")
E = name3.count("e")
total = str(T+R+U+E)
L = name3.count("l")
O = name3.count("o")
V = name3.count("v")
E = name3.count("e")
total2 = str(L+O+V+E)
total3 = total+total2
value = int(total3)
if value >= 0 and value <= 25:
    print(f'your score is {total3}, you are decent couple')
elif value > 25 and value <= 50:
    print(f'your score is {total3}, you are alright together')
elif value > 50 and value <= 75:
    print(f'youour score is {total3}, you love is unconditional')
else:
    print(f' your score is {total3}, purest form of love')
