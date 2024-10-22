print('''
888                                                          
888                                                          
888                                                          
888888888d888 .d88b.  8888b. .d8888b 888  888888d888 .d88b.  
888   888P"  d8P  Y8b    "88b88K     888  888888P"  d8P  Y8b 
888   888    88888888.d888888"Y8888b.888  888888    88888888 
Y88b. 888    Y8b.    888  888     X88Y88b 888888    Y8b.     
 "Y888888     "Y8888 "Y888888 88888P' "Y88888888     "Y8888                                                             
''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("Where do you want to go? \n Left or right ").lower()
if direction == 'left':
    print("Going left, there is a lake in front")
    ride = input("Do you wanna wait for the boat or swim across \n Wait or Swim ").lower()
    if ride == 'wait':
        print("Boat is in the way")
        colour = input("which colour would you like to choose? \n Red or Yellow or Blue ").lower()
        if colour == 'Yellow':
            print("Hurrah!! You found the treasure")
        else:
            print("Sorry You chose wrong colour! Game Over!")
    else:
        print("Oops... There are alligators! Game Over!")
else:
    print("Sorry you fell in a hole! Game Over!")