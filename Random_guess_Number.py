import random

cnumber = random.randrange(1,101)
userInput = int(input('enter your number'))
while True:
    if( userInput > cnumber):
        print('Computer Number:', cnumber)
        print('Ypur guess Number is high')
    elif(userInput < cnumber):
        print('Computer Number:', cnumber)
        print('Your guess Number is low')
    elif(userInput==cnumber):
            print('Computer Number:', cnumber)
            print('Your guess number equal to computer value')
    else:
         break;
    userInput = int(input('enter your number'))
    continue_game = input("Do you want to continue playing? (yes/no): ").strip().lower()
    if continue_game != "yes":
            print("Thanks for playing!")
            break
