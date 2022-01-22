# The dungeon games:
print("Welcome to the dungeon Games")
print('''                                    \  /
                                    (())
                                    ,~L_
                                   2~~ <|
                                   )>-\y(
 ___________________________________)v_\__________________________________
(_// / / / (////////3__________((_/      _((__________E////////) \ \ \ / /_)
  (_/ / / / (////////////////////(c  (c /|\///////////////////) \ \ \ \_)
    "(_/ / / /(/(/(/(/(/(/(/(/(/(/\_    /\)\)\)\)\)\)\)\)\)\)\ \ \ \_)"
       "(_/ / / / / / / / / / / / /|___/\ \ \ \ \ \ \ \ \ \ \ \ \_)"
         "(_(_(_(_(_(_(_(_(_(_(_(_[_]_|_)_)_)_)_)_)_)_)_)_)_)_)"
                                   |    |
                                  /      |
                                 / /    /___
                                /           "~~~~~__
                                \_\_______________\_"_?''')
input("Press any key to enter the dungeon: ")
key = input("There are three keys: Gold, Red or Voilet. Choose one.\n")
if key.casefold() == "gold":
    print("You have entered Greater Ghost Domain")
    item = input("The War God bestows upon you a white dagger and a black pearl. Ahead there is a ghost king. Choose one. \n")
    if item.casefold() == "white dagger":
        print("The white dagger is unable to kill the ghost king.")
        print("You die and become an offering to the War God.")
    elif item.casefold() == "black pearl":
        print("The black pearl emits a black powder and the ghost king dies. ||||Level 1 cleared|||")
        print("Now two paths open up. The left one has thick corpse qi and the right one has chilly yin qi.")
        path = input("Choose a path: left or right\n")
        if path.casefold() == "left":
            print("The thick corpse qi corrodes your body.")
            print("You die and become an offering to the War God.")
        elif path.casefold() == "right":
            print("The black pearl protects you from the chilly yin qi.")
            print("There is a treasure box ahead.")
            input("Press enter to unlock the treasure box with the gold key.\n")
            print("You have recieved the war god's blessings and given a void shattering spear. ||| Dungeon Cleared |||")
elif key.casefold() == "red":
    print("You have entered the lair of the celestial dragon. The war god bestows you two swords to choose from.")
    print("One is the fire sword and the other is a ice sword")
    sword = input("Your sword of choice: \n")
    if sword.casefold() == "fire sword":
        print("The fire sword is unable to subdue the celestial dragon.")
        print("You die and become an offering to the War God.")
    elif sword.casefold() == "ice sword":
        print("The ice sword subdues the celestial dragon. Now he thinks of you as his master. ||| Level 1 Cleared |||")
        input("Press enter to sit on the dragon.\n")
        print("The dragon fies out of his lair. Ahead there is a rugged mountain range on the left and a dense forest on the right.")
        choice = input("Choose one: left or right \n")
        if choice.casefold() == "left":
            print("You discover a treasure chest hidden in the mountain range.")
            input("Press enter to unlock the treasure chest with the red key.\n")
            print("You have recieved the war god's blessings and given the true god fire.")
            print("This allows your dragon to evolve into a deity dragon. ||| Dungeon cleared |||")
        elif choice.casefold() == "right":
            print("The Ice phoenix in the forest kills you and your dragon.")
            print("You become an offering to the War God.")
elif key.casefold() =="voilet":
    print("You have entered the Corpse World. Ahead is the Grim Reaper.")
    print("The War God bestows upon you a yellow and a black talisman to fight him.")
    talisman = input("Choose a talisman: yellow or black\n")
    if talisman.casefold() == "yellow":
        print("The talisman is unable to protect you from the Grim Reaper.")
        print("You become an offering to the War God.")
    elif talisman.casefold() == "black":
        print("The Grim Reaper is unable to do anything to you due to the black talisman. ||| Level 1 Cleared |||")
        print("There are two paths ahead. The left one is a sea of fire and the right one has thick corpse qi.")
        choice = input("Choose a path: left or right\n")
        if choice.casefold() == "left":
            print("The sea of fire has very high temperature and burns you to a crisp.")
            print("You become an offering to the War God.")
        elif choice.casefold() == "right":
            print("The black talisman protects you from the thick corpse qi.")
            input("Ahead is a door. Press enter to unlock it with the voilet key.\n")
            print("You have exited the dungeon alive.")