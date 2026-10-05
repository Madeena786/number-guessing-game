# **Number Guessing Game**

#### **Project Description**



The Number Guessing Game is a simple Python game.



In this game, the computer generates a random number between 1 and 100. The user has to guess the number.



After every guess, the program tells the user whether the guessed number is too high or too low.



The game continues until the user guesses the correct number.



The program also counts the total number of attempts made by the user.







#### **Objective**



###### The objectives of this project are:



* To understand Python loops
* To understand conditional statements
* To use the random module
* To generate random numbers
* To take input from the user
* To use an attempt counter
* To understand basic game logic





#### **Technologies Used**



* Python
* Random Module
* GitHub







#### **Features**



* Generates a random number between 1 and 100
* Takes the user's guess as input
* Checks whether the guess is high or low
* Gives a hint to the user
* Counts the number of attempts
* Stops the game when the correct number is guessed
* Displays the total number of attempts



#### **Python Program**

import random

randomn=random.randint(1,100)

a=0

print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")

print("       NUMBER GUESSING GAME")

print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")

print("I have selected a number between 1 and 100.")

print("Try to guess the number!")

while True:

&#x20;   guess=int(input("\\nEnter your guess: "))

&#x20;   a+=1

&#x20;   if guess<randomn:

&#x20;       print("Too low! Try a higher number.")

&#x20;   elif guess>randomn:

&#x20;       print("Too high! Try a lower number.")

&#x20;   else:

&#x20;       print("\\nCongratulations! You guessed the correct number.")

&#x20;       print("The number was:",randomn)

&#x20;       print("Number of attempts:",a)

&#x20;       print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")

&#x20;       print("          GAME OVER")

&#x20;       print("\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*")

&#x20;       break



#### **How the Program Works:**

**Step 1:** Import Random Module

The random module is imported to generate a random number.

import random



**Step 2:** Generate Random Number

The computer generates a number between 1 and 100.

random\_number = random.randint(1, 100)



**Step 3:** Get User Input

The user enters a number.

guess = int(input("Enter your guess: "))



**Step 4:** Check the Guess

The program compares the user's guess with the random number.

If the guess is smaller:

Too low! Try a higher number.

If the guess is larger:

Too high! Try a lower number.

If the guess is correct:

Congratulations! You guessed the correct number.



**Step 5:** Count Attempts

Every time the user makes a guess, the attempt counter increases.

attempts += 1



**Step 6:** Stop the Game

When the user guesses the correct number, the break statement stops the loop.

break

#### 

#### **Sample Output:**

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

&#x20;      NUMBER GUESSING GAME

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

I have selected a number between 1 and 100.

Try to guess the number!



Enter your guess: 63

Too high! Try a lower number.



Enter your guess: 50

Too high! Try a lower number.



Enter your guess: 40

Too high! Try a lower number.



Enter your guess: 30

Too high! Try a lower number.



Enter your guess: 20

Too low! Try a higher number.



Enter your guess: 25

Too high! Try a lower number.



Enter your guess: 23

Too high! Try a lower number.



Enter your guess: 22

Too high! Try a lower number.



Enter your guess: 21



Congratulations! You guessed the correct number.

The number was: 21

Number of attempts: 9

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*

&#x20;         GAME OVER

\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*



#### **TODAY I LEARNED:**

This project helped me understand:



* Python variables
* User input
* Conditional statements
* While loops
* Break statement
* Random number generation
* Attempt counters
* Basic game development logic



