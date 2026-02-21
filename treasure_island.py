print("Welcome to Treasure Island.")
print("your mission is to find the Treasure")
choice1 = input('you\'re at a crossroad, where do you want to go? type "left" or "right"... ').lower()
if choice1 == "left":
  choice2 = input('you\'ve come to a lake, there is an island in the middle of the lake. \n type "wait" to wait for a boat. type "swim" to swim across...').lower()
  if choice2 == "wait":
    choice3 = input('you\'ve arrived at the island unharmed. there is a house with 3 doors. \n one red , one yellow and one blue. which colour do you choose? ...').lower()
    if choice3 == "red":
      print(" Game Over ")
    elif choice3 == "yellow":
      print(" You Found the Treasure! ")
    elif choice3 == "blue":
      print(" Game Over ")
    else:
      print(" Game Over ")
  else:
      print(" Game Over ")
else:
  print(" Game Over ")
