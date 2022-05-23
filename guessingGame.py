import random
print("Number Guessing Game")
number=random.randint(1,9)
chances=0
print("Guess a number(between 1-9) :")
while chances<5 :
    guess=int(input("Enter your guess :"))
    if guess==number :
        print("You won!!")
        break
    elif guess<number :
        print("Your guess was low : Guess a number higher than ",guess )  

    else:
        print("Your guess was high : Guess a number lower than ",guess )    

    chances+=1

if not chances<5 :
    print("You lost. The number is ",number)
