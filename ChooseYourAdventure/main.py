name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == 'left':
    answer = input("You come to a river, you can walk around it or swim accross. Type 'swim' to swim accross or 'walk' to walk around it: ")
    
    if answer == 'swim':
       print("You swam accross and were eaten by an alligator.") 
    elif answer == 'walk':
        print("You walked for many miles, ran out of water and died.")
    else:
        print('Not a valid option. You lose.')
    
elif answer == 'right':
    answer = input("You come to a bridge, it looks wobbly, do you want to cross it or go back? (Cross/Back): ").lower()
    if answer == 'back':
           print("You are back and thus lose.") 
    elif answer == 'cross':
        answer = input("You cross the bridge and meet a stranger. Do you talk to them? (yes/no): ").lower()
        if answer == 'yes':
           print("You talk to the stranger and they give you Gold. You win.") 
        elif answer == 'no':
            print("You ignore the stranger and they feel disrespected and kill you.")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')
else:
    print('Not a valid option. You lose.')
    
print("Thank you for trying", name)