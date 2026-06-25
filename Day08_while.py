#while loop
#number guessing game
import random
secret = random.randint(1, 100)
attempts =0
while True:
    guess =int(input("Guess the number(1-100): "))
    attempts+=1
    if guess<secret:
        print("Low ! guess higher")
    elif guess>secret:
        print("High! guess lower")
    else:
        print(f"Correct! you guessed in {attempts} attempts")
        break
