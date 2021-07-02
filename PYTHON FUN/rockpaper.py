import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
you = int(input("type 0 for rock 1for paper and 2 for scizzor"))
gamelst = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''', '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']

comp = random.randint(0, 2)
print("computers choice :")
print(gamelst[comp])
print("your choice :")
if comp == you:
    print(f"{gamelst[you]}\ngame is drawn")
else:
    if comp == 0 and you == 1:
        print(f"{gamelst[you]}\nyou win")
    elif comp == 1 and you == 0:
        print(f"{gamelst[you]}\nyou lost")
    if comp == 1 and you == 2:
        print(f"{gamelst[you]}\nyou win")
    elif comp == 2 and you == 1:
        print(f"{gamelst[you]}\nyou lost")
    if comp == 2 and you == 0:
        print(f"{gamelst[you]}\nyou win")
    elif comp == 0 and you == 2:
        print(f"{gamelst[you]}\nyou lost")
