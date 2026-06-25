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

#countdown
count =10
while count>=0:
    print(f"countdown:{count}")
    count-=1
print("Blast off! 🚀")

#sum until user enters 0
total=0
while True:
    num=int(input("Enter number you want to add: "))
    if num==0:
        print("You entered 0")
        break
    total+=num
print(f"Total: {total}")
