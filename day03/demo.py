#宝探しゲーム

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
course = input("You are at a cross road. "
               "The sun-drenched path awaits your choice. "
               "Where dop you want to go?\n   Type 'left' or 'right'\n").lower()
# The sun-drenchedに黄色という意味が込められている
if course == "left":
    print("You've come to a lake. A hammer is sunk in the dust. "
          "There is an island in the middle of the lake.")
    course2 = input("type 'wait' to wait for a boat. "
                    "Type 'swim' to swim across.\n").lower()
    if course2 == "wait":
        print("After barely making it across, you see three doors.")
        course3 = input("Which door would you choose? "
                        "'red', 'yellow', or 'blue'?\n").lower()
        if course3 == "yellow":
            print("You Win! Happiness will come to you.")
        else:
            print("Game Over. A hint is concealed!")
    else:
        print("Game Over. That's your loss.")
else:
    print("Game Over. You lose.")
