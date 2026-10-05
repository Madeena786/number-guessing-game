import random
randomn=random.randint(1,100)
a=0
print("************************************")
print("       NUMBER GUESSING GAME")
print("************************************")
print("I have selected a number between 1 and 100.")
print("Try to guess the number!")
while True:
    guess=int(input("\nEnter your guess: "))
    a+=1
    if guess<randomn:
        print("Too low! Try a higher number.")
    elif guess>randomn:
        print("Too high! Try a lower number.")
    else:
        print("\nCongratulations! You guessed the correct number.")
        print("The number was:",randomn)
        print("Number of attempts:",a)
        print("************************************")
        print("          GAME OVER")
        print("************************************")
        break
