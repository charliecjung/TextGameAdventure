print("Hello, World")
print("Get ready for adventure!")

location = "Siebel Center"
blah = 10
number_of_lives = 3

name = input("What is your name?\n")
print("Hello, " + name + "!")
print("You are trying to survive the zombie apocalypse.")
response = input("Do you run or hide?")
if response == "run":
    print("You get tired and the zombies get you.")
    print("Game Over")
elif response == "hide":
    print("You find refuge but you have no supplies")
    weapons_or_foods = input("Do you search for weapons or foods?")
    if weapons_or_foods == "weapons":
        print("You find a baseball bat")
        refuge_or_continue = input("Do you want to take refuge or keep searching?")
        if refuge_or_continue == "refuge":
            #story continues
        elif refuge_or_continue == "keep searching":
            #story continues
    elif weapons_or_food == "food":
        print("You go to the kitche nand find a person.")
        work_together = input("Do you want to work together?")
        #story continues
else:
    print("That was not a valid response")

