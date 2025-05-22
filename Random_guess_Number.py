import random

while True:

    for i in range(3):
        userInput =int (input('enter num:'))

        cnumber = random.randint(1,100)


 
        if( userInput > cnumber):
            print('Computer Number:', cnumber)
            print('Your guess Number is high')
        elif(userInput < cnumber):
            print('Computer Number:', cnumber)
            print('Your guess Number is low')
    
        else:
             print('Your guess Number is equal to Computer')
    else:    
        continue_game = input("Do you want to continue playing? (yes/no): ").strip().lower()
        if continue_game != "yes":
                print("Thanks for playing!")
                break
