# to create random no.
# to create integer
import random
# random_integer = random.randint(1, 100)
# print(random_integer)
# # to create float
# random_float = random.random()  # number between(0.00-0.99)
# print(random_float)
# so if you want 0 to 5 so we have to multiply with 5
toss_guess = int(
    input("what you want to select  0 and 1 for'head' and 'tail' "))
tossed = random.randint(0, 1)
# print(tossed)
if tossed == 1:
    print("head")
else:
    print("tail")
if toss_guess == tossed:
    print("you win the toss")
else:
    print("you lost the toss")
