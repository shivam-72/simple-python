print("    Welcome to the world of dream      ")
print("""
  \ \_\ .----------. /    \   (| |    | |  )   / ..
|\  \   ~- | |= == = | |-~_  // /
| | | | | // / ((()))
 \|  |    | |= == = | | ~ / \\\// /
     |__ | | | | | `|''
     | |\ | |= == = | | __ |  _ | _
     | | \`'    `'/| |= O=| | | _ ` / | | ~
     | | | |\____ | | | _
 _ | | | | ____ | | | _]
| |  | | |l/: : : : |  | |
| /   | | |:: : : : : \  | |
     | | /:: : : : : : \ | |
     |_|/: : : : : : : : : \| _|
  /|/|:.:.:.:.:.:.:.:|
 | / |.:.:.:.:.:.:.:.|
 |/| /...............\ |\
   |/.................\ \|
   /. . . . . . . . . .\
  /. . . . . . . . . . .\


""")
print("Your misssion is to find the gate to come out from the maze")
print("your game starts")
start = input(
    "you are at a danger road where you want to go Type 'left' or 'right'\n")


if start == "left":
    middle = input(
        "you are at trench of maze.you want to use rope Type 'yes' otherwise type wait  \n")
    if middle == "wait":
        next = input(
            """you arrived at a door of maze. there are 4 door 'red' or 'blue' or 'green' or 'brown' which  colour you want to choose\n""")

        if next == "blue":
            print("Wohoo! you arrived your destination.")
        else:
            print("Oh! NO you arrived at monsters room:  GAME OVER")

    elif middle == "yes":
        print("you fall down from the trench :  GAME OVER")
    else:
        print("Invalid input start again")


elif start == "right":
    print("TRY FOR THE NEXT TIME: GAME OVER")
else:
    print("Invalid input start again")
