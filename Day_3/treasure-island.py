print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_______/
*******************************************************************************
''')
print('''Welcome to Treasure Island.
Your mission is to find the treasure.
You\'re at the cross road. Where do you want to go?''')

user_choice = input('\tType "left" or "right"\n')

if user_choice == 'left':
    print('You\'ve come to a lake. There is an island in the middle of a lake.')
    user_choice = input('\tType "wait" to wait for a boat. Type "swim" to swim across the lake.\n')

elif user_choice == 'right':
    print('Game over.')

else:
    print('Game over.')

if user_choice =='wait':
    print('''You arrive at the island unharmed. There is a house with 3 doors.''')
    user_choice = input(' One red, one yellow and one blue. Which color do you choose?\n')

    if user_choice == 'yellow':
        print('You found the treasure! You Win!')

    elif user_choice == 'red':
        print('Burned by fire. Game over.')   

    elif user_choice == 'blue':
        print('Eaten by beasts. Game over.')
        
    else:
        print('Game Over.')

elif user_choice == 'swim':
    print('Attacked by trout. Game over')

else:
    print('Game Over.')
