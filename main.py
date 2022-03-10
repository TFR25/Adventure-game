# COM203
#Parsons, J. J. (2018). New perspectives on computer concepts 2018, comprehensive (20th ed.). Cengage.
# Adventure Game
print("Last night, you went to sleep in your own home.")
print("Now, you wake up in a locked room.")
print("Could there be a key hidden somewhere?")
print("In the room, you can see: ")


# The menu function
def menu(list, question):
    for item in list:
        print(1 + list.index(item), item)
    return int(input(question))


# This is a list of the items in the room
items = ["backpack", "painting", "vase", "bowl", "door"]
# Generate random number for key location
import random

keylocation = random.randint(1, 4)
# Initializing the variables
# Key is not found:
keyfound = "No"
loop = 1
# Display menu until key is found
while loop == 1:
    choice = menu(items, "What do you want to inspect? ")
    print("")
    if choice < 5:
        if choice == keylocation:
            print(
                "You found a small key in the", items[choice - 1]
            )  #index starts at 0, -1 starts the variable choice at the correct index.
            keyfound = "Yes"
        else:
            print("You found nothing in the", items[choice - 1])
    elif choice == 5:
        if keyfound == "Yes":
            loop = 0
            print("You insert the key in the keyhole and turn it.")
        else:
          print("The door is locked. You need to find a key.")
    else:
      print("Choose a number less than 6.")
print("You open the door to your freedom.") 
