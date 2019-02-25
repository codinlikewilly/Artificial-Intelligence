#Guessing Game
import random
play = True


while play:
    
    tries = 0

    print("welcome to the guessing game!")
    print("------------------------------------")
    print("You only get three tries to guess a number between 1 and 100")
    print("------------------------------------")

    number = random.randint(1,100)
    #print("guess a number between 1 and 100: ")


    while tries < 3:
        tries = tries + 1
        
        
        #print("Guess number "+str(tries+1)+" :")
        guess = input("Guess number " +str(tries)+" :")
        guess = int(guess)

       # tries = tries + 1
        
    
        if guess < number:
            print("That was low....")
            print("***********************")
            print("***********************")
        

        if guess > number:
            print("That was high! ")
            print("***********************")
            print("***********************")
        

        if guess == number:
            print("you got it!!!")
            break
    
    print("---------------------------")
    print("The number was: " + str(number))
    print("---------------------------")

    print("=================================")
    again = str(input("Play again? (y/n):"))
    if again == "n":
        play = False
    else:
        play = True
    print("=================================")




        
    
    

print(number)
print(guess)
